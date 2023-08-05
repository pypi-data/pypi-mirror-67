import random
from datetime import date, datetime
import dateutil.parser
from ast import literal_eval

from typing import Callable, Any, Optional, Union, List, Tuple

from faker import Faker

from .data_gen_exceptions import DataGenError

import snowfakery.data_generator_runtime  # noqa

RuntimeContext = "snowfakery.data_generator_runtime.RuntimeContext"
FieldDefinition = "snowfakery.data_generator_runtime_dom.FieldDefinition"
ObjectRow = "snowfakery.data_generator_runtime.ObjectRow"

fake = Faker()

# It might make more sense to use context vars for context handling when
# Python 3.6 is out of the support matrix.


def lazy(func: Any) -> Callable:
    """A lazy function is one that expects its arguments to be unparsed"""
    func.lazy = True
    return func


def random_number(context: RuntimeContext, min: int, max: int) -> int:
    """Pick a random number between min and max like Python's randint."""
    return random.randint(min, max)


def parse_weight_str(context: RuntimeContext, weight_value) -> int:
    """For constructs like:

    - choice:
        probability: 60%
        pick: Closed Won

    Render and convert the 60% to just 60.
    """
    weight_str = weight_value.render(context)
    if isinstance(weight_str, str):
        weight_str = weight_str.rstrip("%")
    return int(weight_str)


def weighted_choice(choices: List[Tuple[int, object]]):
    """Selects from choices based on their weights"""
    weights = [weight for weight, value in choices]
    options = [value for weight, value in choices]
    return random.choices(options, weights, k=1)[0]


@lazy
def random_choice(context: RuntimeContext, *choices):
    """Template helper for random choices.

    Supports structures like this:

    random_choice:
        - a
        - b
        - <<c>>

    Or like this:

    random_choice:
        - choice:
            pick: A
            probability: 50%
        - choice:
            pick: A
            probability: 50%

    Probabilities are really just weights and don't need to
    add up to 100.

    Pick-items can have arbitrary internal complexity.

    Pick-items are lazily evaluated.
    """
    if not choices:
        raise ValueError("No choices supplied!")

    if getattr(choices[0], "function_name", None) == "choice":
        choices = [choice.render(context) for choice in choices]
        rc = weighted_choice(choices)
    else:
        rc = random.choice(choices)
    if hasattr(rc, "render"):
        rc = rc.render(context)
    return rc


@lazy
def choice_wrapper(
    context: RuntimeContext,
    pick,
    probability: FieldDefinition = None,
    when: FieldDefinition = None,
):
    """Supports the choice: sub-items used in `random_choice` or `if`"""
    if probability:
        probability = parse_weight_str(context, probability)
    return probability or when, pick


def parse_date(d: Union[str, datetime, date]) -> Optional[Union[datetime, date]]:
    if isinstance(d, (datetime, date)):
        return d
    try:
        return dateutil.parser.parse(d)
    except dateutil.parser.ParserError:
        pass


def date_(
    context: RuntimeContext,
    *,
    year: Union[str, int],
    month: Union[str, int],
    day: Union[str, int],
):
    """A YAML-embeddable function to construct a date from strings or integers"""
    return date(year, month, day)


def datetime_(
    context: RuntimeContext,
    *,
    year: Union[str, int],
    month: Union[str, int],
    day: Union[str, int],
    hour=0,
    minute=0,
    second=0,
    microsecond=0,
):
    """A YAML-embeddable function to construct a datetime from strings or integers"""
    return datetime(year, month, day, hour, minute, second, microsecond)


def date_between(context: RuntimeContext, start_date, end_date):
    """A YAML-embeddable function to pick a date between two ranges"""
    start_date = parse_date(start_date) or start_date
    end_date = parse_date(end_date) or end_date
    try:
        return fake.date_between(start_date, end_date)
    except ValueError as e:
        if "empty range" not in str(e):
            raise
    # swallow empty range errors per Python conventions


def reference(context: RuntimeContext, x: Union[ObjectRow, str]):
    """YAML-embeddable function to Reference another object."""
    if hasattr(x, "id"):  # reference to an object with an id
        target = x
    elif isinstance(x, str):  # name of an object
        obj = context.field_vars()[x]
        if not getattr(obj, "id"):
            raise DataGenError(f"Reference to incorrect object type {obj}", None, None)
        target = obj
    else:
        raise DataGenError(
            f"Can't get reference to object of type {type(x)}: {x}", None, None
        )

    return target


def render_boolean(context: RuntimeContext, value: FieldDefinition) -> bool:
    val = value.render(context)
    if isinstance(val, str):
        val = literal_eval(val)

    return bool(val)


@lazy
def if_(context: RuntimeContext, *choices: FieldDefinition):
    """Template helper for conditional choices.

    Supports structures like this:

    if:
        - choice:
            when: <<something>>
            pick: A
        - choice:
            when: <<something>>
            pick: B

    Pick-items can have arbitrary internal complexity.

    Pick-items are lazily evaluated.
    """
    if not choices:
        raise ValueError("No choices supplied!")

    choices = [choice.render(context) for choice in choices]
    for when, choice in choices[:-1]:
        if when is None:
            raise SyntaxError(
                "Every choice except the last one should have a when-clause"
            )
    true_choices = (
        choice for when, choice in choices if when and render_boolean(context, when)
    )
    rc = next(true_choices, choices[-1][-1])  # default to last choice
    if hasattr(rc, "render"):
        rc = rc.render(context)
    return rc


template_funcs = {
    "int": lambda context, number: int(number),
    "choice": choice_wrapper,
    "random_number": random_number,
    "random_choice": random_choice,
    "date_between": date_between,
    "reference": reference,
    "date": date_,
    "datetime": datetime_,
    "if": if_,
}

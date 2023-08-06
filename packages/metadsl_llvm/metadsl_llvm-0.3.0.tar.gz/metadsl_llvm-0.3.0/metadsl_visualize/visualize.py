import typing

import IPython
import IPython.core.display
from metadsl import *
from metadsl_rewrite import *

from .typez import *

__all__ = ["execute_and_visualize"]


T = typing.TypeVar("T")


def execute_and_visualize(ref: ExpressionReference, strategy: Strategy) -> object:
    """
    Returns the replaced version of this expression and also displays the execution trace.
    """
    expression_display = ExpressionDisplay(ref)

    # Only display expressions if in notebook, not in shell
    if (
        IPython.get_ipython()
        and IPython.get_ipython().__class__.__name__ == "ZMQInteractiveShell"
    ):
        IPython.core.display.display(expression_display)

    # Update the typez display as we execute the strategys
    for result in strategy(ref):
        expression_display.update(result)
    return ref.expression


def monkeypatch():
    """
    Monkeypatches Expression should it displays the result as well as each intermediate step.
    """
    Expression._ipython_display_ = _expression_ipython_display  # type: ignore
    # only change if we are in a kernel
    if IPython.get_ipython():
        execute.execute = execute_and_visualize  # type: ignore


def _expression_ipython_display(self):
    res = execute(self)
    # Only display result if we get back a non expression object
    if not isinstance(res, Expression):
        IPython.core.display.display(res)


monkeypatch()

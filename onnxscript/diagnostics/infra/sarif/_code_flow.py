# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import List, Optional

from onnxscript.diagnostics.infra.sarif import _message, _property_bag, _thread_flow


@dataclasses.dataclass
class CodeFlow:
    """A set of threadFlows which together describe a pattern of code execution relevant to detecting a result."""

    thread_flows: List[_thread_flow.ThreadFlow] = dataclasses.field(
        metadata={"schema_property_name": "threadFlows"}
    )
    message: Optional[_message.Message] = dataclasses.field(
        default=None, metadata={"schema_property_name": "message"}
    )
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )


# flake8: noqa
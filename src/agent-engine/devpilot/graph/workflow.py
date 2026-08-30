from langgraph.graph import StateGraph, START, END

from devpilot.graph.nodes import (
    receive_requirement,
    validate_requirement,
)
from devpilot.graph.state import DevPilotState


def build_workflow():
    workflow = StateGraph(DevPilotState)

    workflow.add_node(
        "receive_requirement",
        receive_requirement,
    )

    workflow.add_node(
        "validate_requirement",
        validate_requirement,
    )

    workflow.add_edge(
        START,
        "receive_requirement",
    )

    workflow.add_edge(
        "receive_requirement",
        "validate_requirement",
    )

    workflow.add_edge(
        "validate_requirement",
        END,
    )

    return workflow.compile()
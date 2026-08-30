from devpilot.graph.state import DevPilotState


def receive_requirement(state: DevPilotState) -> DevPilotState:
    requirement = state["requirement"]

    print(f"Received requirement: {requirement}")

    return {
        **state,
        "status": "requirement_received",
    }


def validate_requirement(state: DevPilotState) -> DevPilotState:
    requirement = state["requirement"]

    if not requirement.strip():
        raise ValueError("Requirement cannot be empty.")

    print("Requirement validated.")

    return {
        **state,
        "status": "requirement_validated",
    }
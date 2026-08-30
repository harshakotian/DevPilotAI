from typing import TypedDict

from devpilot.models.requirement import RequirementAnalysis


class DevPilotState(TypedDict, total=False):
    requirement: str

    requirement_analysis: RequirementAnalysis

    status: str

    errors: list[str]
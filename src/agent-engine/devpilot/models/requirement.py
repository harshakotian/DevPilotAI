from pydantic import BaseModel, Field


class RequirementAnalysis(BaseModel):
    summary: str = Field(
        description="Concise summary of the requirement."
    )

    business_goal: str = Field(
        description="Business or engineering goal."
    )

    affected_areas: list[str] = Field(
        default_factory=list,
        description="Likely system areas affected.",
    )

    assumptions: list[str] = Field(
        default_factory=list,
    )

    questions: list[str] = Field(
        default_factory=list,
        description="Questions requiring clarification.",
    )
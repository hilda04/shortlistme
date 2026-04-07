from typing import TypedDict, List, Optional


class AnalysisScores(TypedDict):
    matchScore: int
    skillsMatchScore: int
    experienceMatchScore: int
    roleAlignmentScore: int
    presentationScore: int


class AnalysisResult(AnalysisScores):
    strengths: List[str]
    missingRequirements: List[str]
    recruiterView: str
    improvementSuggestions: List[str]


class CreateAnalysisPayload(TypedDict):
    cvObjectKey: str
    targetRole: str
    companyName: Optional[str]
    jobDescription: Optional[str]

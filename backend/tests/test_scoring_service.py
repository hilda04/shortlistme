from services.scoring_service import ScoringService


def test_scoring_range():
    svc = ScoringService()
    result = svc.score(
        "Software Developer",
        "Python API Git SQL testing delivered improved systems",
        {"experience": "led built managed"},
        "Need Python and API skills with stakeholder communication",
    )
    assert 0 <= result["matchScore"] <= 100
    assert result["skillsMatchScore"] <= 40

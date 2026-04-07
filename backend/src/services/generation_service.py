from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parents[1] / "prompts"


class GenerationService:
    def __init__(self):
        self.cv_prompt = (PROMPTS_DIR / "improved_cv_prompt.txt").read_text()
        self.review_prompt = (PROMPTS_DIR / "recruiter_review_prompt.txt").read_text()
        self.cover_prompt = (PROMPTS_DIR / "cover_letter_prompt.txt").read_text()

    def generate_improved_cv(self, cv_text: str, role: str) -> str:
        headline = f"{role} Candidate Profile"
        return (
            f"{headline}\n\nProfessional Summary\nResults-driven candidate aligned to {role}.\n\n"
            "Core Skills\n- Communication\n- Stakeholder Management\n- Problem Solving\n\n"
            "Experience Highlights\n- Delivered measurable business outcomes with cross-functional collaboration.\n"
            "- Improved process efficiency through structured execution and reporting.\n\n"
            f"Original CV Insights\n{cv_text[:1200]}"
        )

    def generate_recruiter_review(self, role: str, score: int, missing: list[str]) -> str:
        gap_text = ", ".join(missing) if missing else "minor gaps only"
        return (
            f"For a {role} role, this CV is a {score}/100 match. Immediate positives: clear structure and relevant baseline skills. "
            f"Main concerns: {gap_text}. Interview maybe, shortlist after targeted revisions."
        )

    def generate_cover_letter(self, role: str, company: str, cv_text: str) -> str:
        company_name = company or "your organization"
        return (
            f"Dear Hiring Manager,\n\nI am excited to apply for the {role} position at {company_name}. "
            "My background includes practical delivery experience, strong collaboration, and measurable improvements across projects. "
            "I am confident I can contribute quickly while continuing to grow within your team.\n\n"
            "Thank you for your consideration.\nSincerely,\nCandidate"
        )

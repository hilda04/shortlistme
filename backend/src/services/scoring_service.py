from data.roles import ROLE_KEYWORDS


class ScoringService:
    WEIGHTS = {
        "skills": 40,
        "experience": 30,
        "role_alignment": 20,
        "presentation": 10,
    }

    def score(self, role: str, cv_text: str, sections: dict, job_description: str = "") -> dict:
        cv_text_lower = cv_text.lower()
        keywords = ROLE_KEYWORDS.get(role, ["communication", "teamwork", "organization"])
        hits = sum(1 for keyword in keywords if keyword in cv_text_lower)
        skills_ratio = hits / max(len(keywords), 1)

        skills = int(skills_ratio * self.WEIGHTS["skills"])
        experience = self._score_experience(sections)
        role_alignment = self._score_role_alignment(role, cv_text_lower, job_description)
        presentation = self._score_presentation(cv_text)

        match_score = skills + experience + role_alignment + presentation
        strengths = [
            f"Keyword alignment found for {hits} of {len(keywords)} role indicators.",
            "CV includes structured sections suitable for recruiter scanning.",
        ]
        missing = [
            kw for kw in keywords if kw not in cv_text_lower
        ][:4]
        suggestions = [
            "Add quantified achievements to your latest role (e.g., % improvement, revenue impact).",
            "Mirror the target role language in your summary and skills section.",
            "Prioritize relevant tools and certifications near the top of the CV.",
        ]
        recruiter_view = (
            f"Solid baseline for {role}. Key signals are present, but stronger evidence of business impact "
            "and role-specific outcomes is needed for shortlisting."
        )

        return {
            "matchScore": max(0, min(match_score, 100)),
            "skillsMatchScore": skills,
            "experienceMatchScore": experience,
            "roleAlignmentScore": role_alignment,
            "presentationScore": presentation,
            "strengths": strengths,
            "missingRequirements": missing,
            "recruiterView": recruiter_view,
            "improvementSuggestions": suggestions,
        }

    def _score_experience(self, sections: dict) -> int:
        experience_text = (sections.get("experience") or "").lower()
        if not experience_text:
            return 8
        markers = ["led", "managed", "delivered", "improved", "built"]
        hits = sum(1 for marker in markers if marker in experience_text)
        return min(30, 12 + hits * 3)

    def _score_role_alignment(self, role: str, cv_text_lower: str, job_description: str) -> int:
        base = 10 if role.lower() in cv_text_lower else 6
        if job_description:
            jd_words = {w for w in job_description.lower().split() if len(w) > 4}
            overlap = sum(1 for w in list(jd_words)[:40] if w in cv_text_lower)
            base += min(10, overlap // 2)
        return min(20, base)

    def _score_presentation(self, cv_text: str) -> int:
        lines = [line.strip() for line in cv_text.splitlines() if line.strip()]
        if len(lines) < 8:
            return 4
        long_lines = sum(1 for line in lines if len(line) > 180)
        return max(5, 10 - min(5, long_lines))

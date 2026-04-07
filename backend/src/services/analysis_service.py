import uuid
from services.storage_service import StorageService
from services.cv_parser_service import CvParserService
from services.scoring_service import ScoringService
from services.generation_service import GenerationService
from services.pdf_service import PdfService
from repositories.analysis_repository import AnalysisRepository


class AnalysisService:
    def __init__(self):
        self.storage = StorageService()
        self.cv_parser = CvParserService()
        self.scorer = ScoringService()
        self.generator = GenerationService()
        self.pdf = PdfService()
        self.repo = AnalysisRepository()

    def run_analysis(self, user_id: str, payload: dict):
        analysis_id = str(uuid.uuid4())
        cv_bytes = self.storage.get_bytes(payload["cvObjectKey"])
        cv_text = self.cv_parser.extract_text(cv_bytes)
        sections = self.cv_parser.normalize_sections(cv_text)

        scores = self.scorer.score(
            payload["targetRole"],
            cv_text,
            sections,
            payload.get("jobDescription", "") or "",
        )
        improved_cv = self.generator.generate_improved_cv(cv_text, payload["targetRole"])
        recruiter_review = self.generator.generate_recruiter_review(
            payload["targetRole"], scores["matchScore"], scores["missingRequirements"]
        )
        cover_letter = self.generator.generate_cover_letter(
            payload["targetRole"], payload.get("companyName", ""), cv_text
        )

        improved_key = f"outputs/{user_id}/{analysis_id}/improved-cv.pdf"
        cover_key = f"outputs/{user_id}/{analysis_id}/cover-letter.pdf"
        self.storage.put_bytes(improved_key, self.pdf.build_document("Improved CV", improved_cv))
        self.storage.put_bytes(cover_key, self.pdf.build_document("Tailored Cover Letter", cover_letter))

        result = {
            **scores,
            "recruiterView": recruiter_review,
            "improvedCvKey": improved_key,
            "coverLetterKey": cover_key,
        }
        item = self.repo.build_item(user_id, analysis_id, payload, result)
        self.repo.save(item)
        return item

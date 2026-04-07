from datetime import datetime, UTC
import boto3
from boto3.dynamodb.conditions import Key
from utils.config import ANALYSES_TABLE_NAME


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(ANALYSES_TABLE_NAME)


class AnalysisRepository:
    def save(self, item: dict):
        table.put_item(Item=item)

    def get(self, user_id: str, analysis_id: str):
        response = table.get_item(
            Key={"pk": f"USER#{user_id}", "sk": f"ANALYSIS#{analysis_id}"}
        )
        return response.get("Item")

    def list(self, user_id: str):
        response = table.query(
            KeyConditionExpression=Key("pk").eq(f"USER#{user_id}")
            & Key("sk").begins_with("ANALYSIS#")
        )
        return response.get("Items", [])

    def build_item(self, user_id: str, analysis_id: str, payload: dict, result: dict):
        now = datetime.now(UTC).isoformat()
        return {
            "pk": f"USER#{user_id}",
            "sk": f"ANALYSIS#{analysis_id}",
            "analysisId": analysis_id,
            "userId": user_id,
            "status": "completed",
            "targetRole": payload["targetRole"],
            "companyName": payload.get("companyName", ""),
            "originalCvKey": payload["cvObjectKey"],
            "improvedCvKey": result["improvedCvKey"],
            "coverLetterKey": result["coverLetterKey"],
            "matchScore": result["matchScore"],
            "skillsMatchScore": result["skillsMatchScore"],
            "experienceMatchScore": result["experienceMatchScore"],
            "roleAlignmentScore": result["roleAlignmentScore"],
            "presentationScore": result["presentationScore"],
            "strengths": result["strengths"],
            "missingRequirements": result["missingRequirements"],
            "recruiterView": result["recruiterView"],
            "improvementSuggestions": result["improvementSuggestions"],
            "createdAt": now,
            "updatedAt": now,
        }

# API Reference

Base URL: `https://<api-id>.execute-api.<region>.amazonaws.com`

## Public endpoints

### GET /health
Response:
```json
{ "status": "ok", "service": "shortlistme-api" }
```

### GET /roles
Response:
```json
{ "roles": ["Graduate Trainee", "Administrator", "..."] }
```

## Protected endpoints
> Requires `Authorization: Bearer <jwt>`

### GET /me
Returns authenticated user identity summary.

### POST /uploads/presign
Body:
```json
{ "fileName": "cv.pdf", "sizeBytes": 123456 }
```
Response:
```json
{ "uploadUrl": "...", "objectKey": "uploads/<userId>/..." }
```

### POST /analyses
Body:
```json
{
  "cvObjectKey": "uploads/<userId>/...pdf",
  "targetRole": "Software Developer",
  "companyName": "Acme",
  "jobDescription": "optional text"
}
```
Response includes scoring breakdown, generated artifact keys, and metadata.

### GET /analyses
List all analyses for current user.

### GET /analyses/{analysisId}
Get one analysis.

### GET /analyses/{analysisId}/download/{type}
Where `type` is `improved-cv` or `cover-letter`.
Response returns presigned download URL.

## Error structure
```json
{ "error": "ValidationError", "message": "Clear detail" }
```

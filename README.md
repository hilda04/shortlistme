# ShortlistMe MVP

ShortlistMe is a production-style SaaS MVP that helps job seekers upload a CV, analyze fit for a target role, and generate recruiter-ready outputs.

## Monorepo structure

```
shortlistme/
  frontend/    # React + Vite + TypeScript (Amplify-ready)
  backend/     # AWS SAM + Python Lambda router
  docs/        # architecture, API, deployment guides
  README.md
```

## Key features
- CV upload via S3 presigned URL (PDF-only with max-size validation).
- Deterministic match scoring with weighted components.
- Mock AI generation pipeline for improved CV, recruiter review, and cover letter.
- PDF generation for improved CV and tailored cover letter, stored in S3.
- Cognito JWT-protected API routes.
- DynamoDB single-table persistence for analyses.

## Quick start

### Backend (AWS SAM)
1. Install AWS CLI + SAM CLI.
2. Copy env values from `backend/.env.example`.
3. Build and deploy:
   ```bash
   cd backend
   sam build
   sam deploy --guided
   ```
4. Save outputs (HTTP API URL, table, bucket) for frontend env vars.

### Frontend (Vite)
1. Copy env values from `frontend/.env.example`.
2. Install and run:
   ```bash
   cd frontend
   npm ci
   npm run dev
   ```
3. For production:
   ```bash
   npm run build
   ```

## Extensibility notes
- Add payment/referral modules by introducing new protected routes and services under `backend/src/services`.
- Add application tracking by extending DynamoDB entity patterns (`pk=USER#...`, `sk=APPLICATION#...`).
- Swap mock AI generation by replacing methods in `backend/src/services/generation_service.py`.

See full details in:
- `docs/architecture.md`
- `docs/api.md`
- `docs/deployment.md`

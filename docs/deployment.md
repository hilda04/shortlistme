# Deployment Guide

## 1) Backend deployment (SAM)
1. Configure AWS credentials.
2. In `backend/template.yaml`, keep defaults or pass parameter overrides for:
   - `AllowedOrigin`
   - `JwtIssuer`
   - `JwtAudience`
3. Run:
   ```bash
   cd backend
   sam build
   sam deploy --guided
   ```
4. Capture outputs:
   - `HttpApiUrl`
   - `AnalysesTableName`
   - `ArtifactsBucketName`

## 2) Cognito setup checklist
- Create User Pool.
- Create App Client.
- Note Issuer URL and Audience (App Client ID).
- Update SAM deploy parameters for JWT authorizer.
- Update frontend env vars.

## 3) Frontend deployment (Amplify)
1. Push repository to GitHub.
2. In Amplify Console, connect repo and set app root to `frontend`.
3. Amplify uses `frontend/amplify.yml`.
4. Set environment variables:
   - `VITE_API_BASE_URL`
   - `VITE_COGNITO_USER_POOL_ID`
   - `VITE_COGNITO_CLIENT_ID`
   - `VITE_COGNITO_REGION`
   - `VITE_MAX_UPLOAD_BYTES`
5. Deploy branch.

## 4) Post-deploy smoke tests
- `GET /health` returns 200.
- `GET /roles` returns configured role list.
- Sign in and run a full upload + analysis.
- Verify both PDF downloads.

## 5) Local dev checklist
- Backend: `sam local start-api` (optional) or deploy to dev stack.
- Frontend: `npm run dev`.
- Ensure CORS origin matches frontend URL.

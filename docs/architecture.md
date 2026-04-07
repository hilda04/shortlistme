# Architecture

## Overview
ShortlistMe uses a two-tier architecture:
- **Frontend:** React + Vite + TypeScript, deployed on AWS Amplify.
- **Backend:** Single AWS Lambda router behind API Gateway HTTP API, provisioned by AWS SAM.

## AWS resources
- **API Gateway HTTP API** with CORS and Cognito JWT authorizer placeholders.
- **Lambda (single router)** handling public and protected routes.
- **DynamoDB** single-table `pk/sk` schema for analysis records.
- **S3 bucket** for CV uploads and generated PDFs.

## Backend code organization
- `handlers/`: endpoint handlers (public + protected).
- `services/`: analysis orchestration, scoring, parsing, generation, PDF, storage.
- `repositories/`: DynamoDB data access.
- `utils/`: router, auth claim extraction, response helpers, validation.
- `prompts/`: modular prompt templates for future LLM provider.
- `types/`: typed payload and result contracts.

## Scoring model
Deterministic weighted model:
- Skills match: **40**
- Experience match: **30**
- Role alignment: **20**
- Presentation clarity: **10**

Returns:
- `matchScore`
- `skillsMatchScore`
- `experienceMatchScore`
- `roleAlignmentScore`
- `presentationScore`
- strengths, missing requirements, recruiter summary, suggestions.

## Security and auth
- Public routes: `/health`, `/roles`.
- Protected routes require JWT claims from Cognito via API Gateway authorizer.
- User identity extracted from `requestContext.authorizer.jwt.claims`.

## Extensibility
The monorepo intentionally keeps clear seams:
- Replace mock generation service with Bedrock/OpenAI/Anthropic provider.
- Add payments/referrals as new route modules.
- Add application tracking entities in DynamoDB with additional sort-key prefixes.

export interface Analysis {
  analysisId: string;
  targetRole: string;
  companyName?: string;
  matchScore: number;
  skillsMatchScore: number;
  experienceMatchScore: number;
  roleAlignmentScore: number;
  presentationScore: number;
  strengths: string[];
  missingRequirements: string[];
  recruiterView: string;
  improvementSuggestions: string[];
  improvedCvKey: string;
  coverLetterKey: string;
  createdAt: string;
}

export interface UserProfile {
  userId: string;
}

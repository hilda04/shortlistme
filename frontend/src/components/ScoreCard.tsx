import { Analysis } from '../types';

export function ScoreCard({ analysis }: { analysis: Analysis }) {
  return (
    <div className="card">
      <h3>Match Score: {analysis.matchScore}/100</h3>
      <div className="grid four">
        <p>Skills: {analysis.skillsMatchScore}/40</p>
        <p>Experience: {analysis.experienceMatchScore}/30</p>
        <p>Role Alignment: {analysis.roleAlignmentScore}/20</p>
        <p>Presentation: {analysis.presentationScore}/10</p>
      </div>
    </div>
  );
}

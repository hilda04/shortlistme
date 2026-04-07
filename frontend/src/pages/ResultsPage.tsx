import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { api } from '../api/client';
import { DownloadCards } from '../components/DownloadCards';
import { RecruiterViewCard } from '../components/RecruiterViewCard';
import { ScoreCard } from '../components/ScoreCard';
import { SuggestionsList } from '../components/SuggestionsList';
import { ErrorState, LoadingState } from '../components/States';
import { Analysis } from '../types';

export function ResultsPage() {
  const { analysisId = '' } = useParams();
  const [analysis, setAnalysis] = useState<Analysis | null>(null);
  const [error, setError] = useState('');

  useEffect(() => {
    api.analysis(analysisId).then((res) => setAnalysis(res as Analysis)).catch((e) => setError(String(e)));
  }, [analysisId]);

  const onDownload = async (type: 'improved-cv' | 'cover-letter') => {
    const { downloadUrl } = await api.download(analysisId, type);
    window.open(downloadUrl, '_blank');
  };

  if (error) return <ErrorState message={error} />;
  if (!analysis) return <LoadingState label="Loading result..." />;

  return (
    <div className="stack">
      <ScoreCard analysis={analysis} />
      <RecruiterViewCard recruiterView={analysis.recruiterView} />
      <div className="grid two">
        <SuggestionsList title="Strengths" items={analysis.strengths} />
        <SuggestionsList title="Missing Requirements" items={analysis.missingRequirements} />
      </div>
      <SuggestionsList title="Actionable Suggestions" items={analysis.improvementSuggestions} />
      <DownloadCards onDownload={onDownload} />
    </div>
  );
}

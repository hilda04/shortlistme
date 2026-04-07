import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../api/client';
import { EmptyState, ErrorState, LoadingState } from '../components/States';
import { Analysis } from '../types';
import { formatDate } from '../utils/format';

export function HistoryPage() {
  const [items, setItems] = useState<Analysis[] | null>(null);
  const [error, setError] = useState('');

  useEffect(() => {
    api.analyses()
      .then((res) => setItems((res.items as Analysis[]) || []))
      .catch((e) => setError(String(e)));
  }, []);

  if (error) return <ErrorState message={error} />;
  if (!items) return <LoadingState label="Loading history..." />;
  if (items.length === 0) return <EmptyState title="No analyses yet" description="Run your first analysis." />;

  return (
    <div className="stack">
      {items.map((item) => (
        <Link className="card" key={item.analysisId} to={`/results/${item.analysisId}`}>
          <h3>{item.targetRole}</h3>
          <p>Score: {item.matchScore}/100</p>
          <p>{formatDate(item.createdAt)}</p>
        </Link>
      ))}
    </div>
  );
}

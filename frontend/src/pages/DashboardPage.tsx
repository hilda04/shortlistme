import { Link } from 'react-router-dom';

export function DashboardPage() {
  return (
    <div className="stack">
      <div className="card">
        <h2>Welcome to ShortlistMe</h2>
        <p>Start a new CV analysis to generate your match report and downloadable outputs.</p>
        <Link className="button" to="/upload">
          New Analysis
        </Link>
      </div>
    </div>
  );
}

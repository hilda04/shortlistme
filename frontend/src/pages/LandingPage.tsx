import { Link } from 'react-router-dom';

export function LandingPage() {
  return (
    <div className="hero">
      <h1>Land interviews faster with smarter CV analysis.</h1>
      <p>
        ShortlistMe rewrites your CV, scores your role fit, highlights missing requirements, and generates
        polished recruiter-ready documents.
      </p>
      <Link className="button" to="/auth">
        Get Started
      </Link>
    </div>
  );
}

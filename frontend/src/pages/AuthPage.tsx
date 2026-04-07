import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { authStore } from '../auth/auth';

export function AuthPage() {
  const [token, setToken] = useState('demo-jwt-token');
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    authStore.setToken(token);
    navigate('/dashboard');
  };

  return (
    <div className="card auth-card">
      <h2>Sign in / Sign up</h2>
      <p>Connect Cognito Hosted UI here. For MVP, paste a token to simulate auth.</p>
      <form onSubmit={handleSubmit} className="stack">
        <input className="input" value={token} onChange={(e) => setToken(e.target.value)} />
        <button type="submit">Continue</button>
      </form>
    </div>
  );
}

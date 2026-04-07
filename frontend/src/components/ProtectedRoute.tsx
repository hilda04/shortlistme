import { Navigate } from 'react-router-dom';
import { authStore } from '../auth/auth';

export function ProtectedRoute({ children }: { children: JSX.Element }) {
  if (!authStore.isAuthenticated()) {
    return <Navigate to="/auth" replace />;
  }
  return children;
}

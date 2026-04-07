import { authStore } from '../auth/auth';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const headers = new Headers(options.headers);
  headers.set('Content-Type', 'application/json');
  const token = authStore.getToken();
  if (token) headers.set('Authorization', `Bearer ${token}`);

  const response = await fetch(`${API_BASE_URL}${path}`, { ...options, headers });
  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || 'Request failed');
  }
  return response.json() as Promise<T>;
}

export const api = {
  health: () => request<{ status: string }>('/health'),
  roles: () => request<{ roles: string[] }>('/roles'),
  me: () => request<{ userId: string }>('/me'),
  presignUpload: (payload: { fileName: string; sizeBytes: number }) =>
    request<{ uploadUrl: string; objectKey: string }>('/uploads/presign', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),
  createAnalysis: (payload: {
    cvObjectKey: string;
    targetRole: string;
    companyName?: string;
    jobDescription?: string;
  }) => request('/analyses', { method: 'POST', body: JSON.stringify(payload) }),
  analyses: () => request<{ items: unknown[] }>('/analyses'),
  analysis: (analysisId: string) => request(`/analyses/${analysisId}`),
  download: (analysisId: string, type: 'improved-cv' | 'cover-letter') =>
    request<{ downloadUrl: string }>(`/analyses/${analysisId}/download/${type}`),
};

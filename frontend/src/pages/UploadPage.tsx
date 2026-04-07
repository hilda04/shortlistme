import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { ErrorState, LoadingState } from '../components/States';
import { UploadDropzone } from '../components/UploadDropzone';
import { RoleSelector } from '../components/RoleSelector';

const MAX_UPLOAD_BYTES = Number(import.meta.env.VITE_MAX_UPLOAD_BYTES || 5242880);

export function UploadPage() {
  const [roles, setRoles] = useState<string[]>([]);
  const [file, setFile] = useState<File | null>(null);
  const [role, setRole] = useState('');
  const [companyName, setCompanyName] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    api.roles().then((res) => setRoles(res.roles)).catch((e) => setError(String(e)));
  }, []);

  const submit = async () => {
    if (!file || !role) {
      setError('Please upload a CV and choose a role.');
      return;
    }
    if (file.size > MAX_UPLOAD_BYTES) {
      setError(`File too large. Max ${MAX_UPLOAD_BYTES} bytes.`);
      return;
    }

    setLoading(true);
    setError('');
    try {
      const presign = await api.presignUpload({ fileName: file.name, sizeBytes: file.size });
      await fetch(presign.uploadUrl, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/pdf' },
        body: file,
      });

      const created = (await api.createAnalysis({
        cvObjectKey: presign.objectKey,
        targetRole: role,
        companyName,
        jobDescription,
      })) as { analysisId: string };
      navigate(`/results/${created.analysisId}`);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  };

  if (!roles.length && !error) return <LoadingState label="Loading roles..." />;

  return (
    <div className="stack">
      <div className="card">
        <h2>New Analysis</h2>
        <p>Upload CV → Select role → Optionally add company and job description.</p>
      </div>
      <div className="card stack">
        <UploadDropzone file={file} onFileChange={setFile} />
        <RoleSelector roles={roles} value={role} onChange={setRole} />
        <input
          className="input"
          placeholder="Company name (optional)"
          value={companyName}
          onChange={(e) => setCompanyName(e.target.value)}
        />
        <textarea
          className="input"
          rows={6}
          placeholder="Paste job description (optional)"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />
        <button onClick={submit} disabled={loading}>
          {loading ? 'Analyzing...' : 'Run analysis'}
        </button>
      </div>
      {error && <ErrorState message={error} />}
    </div>
  );
}

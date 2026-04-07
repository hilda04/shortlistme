interface UploadDropzoneProps {
  file: File | null;
  onFileChange: (file: File | null) => void;
}

export function UploadDropzone({ file, onFileChange }: UploadDropzoneProps) {
  return (
    <label className="dropzone">
      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => onFileChange(e.target.files?.[0] ?? null)}
      />
      <div>
        <strong>{file ? file.name : 'Upload your CV PDF'}</strong>
        <p>Drag-and-drop or click to select (PDF only).</p>
      </div>
    </label>
  );
}

interface DownloadCardsProps {
  onDownload: (type: 'improved-cv' | 'cover-letter') => Promise<void>;
}

export function DownloadCards({ onDownload }: DownloadCardsProps) {
  return (
    <div className="grid two">
      <div className="card">
        <h3>Improved CV PDF</h3>
        <button onClick={() => onDownload('improved-cv')}>Download</button>
      </div>
      <div className="card">
        <h3>Cover Letter PDF</h3>
        <button onClick={() => onDownload('cover-letter')}>Download</button>
      </div>
    </div>
  );
}

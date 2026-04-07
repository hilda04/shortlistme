export function LoadingState({ label = 'Loading...' }: { label?: string }) {
  return <div className="state-card">{label}</div>;
}

export function ErrorState({ message }: { message: string }) {
  return <div className="state-card error">{message}</div>;
}

export function EmptyState({ title, description }: { title: string; description: string }) {
  return (
    <div className="state-card">
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

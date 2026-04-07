export function SuggestionsList({ title, items }: { title: string; items: string[] }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export function RoleSelector({
  roles,
  value,
  onChange,
}: {
  roles: string[];
  value: string;
  onChange: (value: string) => void;
}) {
  return (
    <select className="input" value={value} onChange={(e) => onChange(e.target.value)}>
      <option value="">Choose target role</option>
      {roles.map((role) => (
        <option key={role} value={role}>
          {role}
        </option>
      ))}
    </select>
  );
}

import { Link, NavLink } from 'react-router-dom';
import { ReactNode } from 'react';

const navItems = [
  ['Dashboard', '/dashboard'],
  ['New Analysis', '/upload'],
  ['History', '/history'],
  ['Settings', '/settings'],
] as const;

export function AppShell({ children }: { children: ReactNode }) {
  return (
    <div className="shell">
      <header className="header">
        <Link to="/dashboard" className="brand">ShortlistMe</Link>
        <nav className="nav">
          {navItems.map(([label, path]) => (
            <NavLink key={path} to={path} className={({ isActive }) => (isActive ? 'active' : '')}>
              {label}
            </NavLink>
          ))}
        </nav>
      </header>
      <main className="content">{children}</main>
    </div>
  );
}

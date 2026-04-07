export function RecruiterViewCard({ recruiterView }: { recruiterView: string }) {
  return (
    <div className="card">
      <h3>Recruiter 10-Second Review</h3>
      <p>{recruiterView}</p>
    </div>
  );
}

export default function MetricCard({ label, value }: { label: string, value: string }) {
  return (
    <div className="p-6 bg-surface-card border border-border-subtle rounded-xl flex flex-col gap-2">
      <span className="text-sm text-text-muted font-mono">{label}</span>
      <span className="text-3xl font-bold text-text-primary tracking-tight">{value}</span>
    </div>
  );
}

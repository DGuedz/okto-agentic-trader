export default function FeatureCard({ title, desc }: { title: string, desc: string }) {
  return (
    <div className="p-6 bg-surface-card border border-border-subtle rounded-xl hover:border-border-default hover:bg-surface-cardHover transition-all group">
      <h3 className="font-bold text-text-primary mb-2 group-hover:text-accent-amber-400 transition-colors">{title}</h3>
      <p className="text-sm text-text-secondary">{desc}</p>
    </div>
  );
}

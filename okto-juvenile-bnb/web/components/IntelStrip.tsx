import React from "react";

type StripItem = {
  id: string;
  label: string;
  value: string;
  delta?: string;
  hint?: string;
};

export function IntelStrip({
  title = "Intel Feed (BNB)",
  subtitle = "Evidence-linked ecosystem signals. Policy-ready diffs. No profit promises.",
  mode = "preview",
  items,
}: {
  title?: string;
  subtitle?: string;
  mode?: "preview" | "live";
  items: StripItem[];
}) {
  return (
    <section className="w-full">
      <div className="mb-4 flex items-end justify-between gap-4">
        <div>
          <div className="text-sm uppercase tracking-widest text-zinc-400">
            {title} <span className="text-zinc-600">/ {mode}</span>
          </div>
          <div className="mt-1 text-sm text-zinc-500">{subtitle}</div>
        </div>
        <div className="rounded-md border border-zinc-800 px-3 py-2 text-xs text-zinc-600">
          Evidence-linked · Explorer-first
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3 md:grid-cols-3 lg:grid-cols-6">
        {items.map((m) => (
          <div
            key={m.id}
            className="rounded-xl border border-zinc-800 bg-zinc-950/40 px-4 py-3"
          >
            <div className="text-xs text-zinc-500">{m.label}</div>
            <div className="mt-2 flex items-baseline justify-between gap-2">
              <div className="text-lg font-semibold text-zinc-100">{m.value}</div>
              {m.delta ? (
                <div className="text-xs text-zinc-400">{m.delta}</div>
              ) : null}
            </div>
            {m.hint ? <div className="mt-2 text-xs text-zinc-600">{m.hint}</div> : null}
          </div>
        ))}
      </div>
    </section>
  );
}

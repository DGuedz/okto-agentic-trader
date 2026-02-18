"use client";

import React, { useMemo, useState } from "react";

type Evidence = { label: string; type: "tx" | "address" | "block"; value: string };

type PolicyPatch = {
  allowlist_add?: string[];
  budgets?: { max_fee_native?: string; max_slippage_bps?: number };
  guards?: {
    simulation_first?: boolean;
    circuit_breaker?: { max_failures: number; window_minutes: number; cooldown_minutes: number };
  };
};

export type IntelItem = {
  id: string;
  title: string;
  tag: string;
  risk: "Low" | "Medium" | "High";
  timestamp: string;
  summary: string;
  evidence: Evidence[];
  policy_patch: PolicyPatch;
};

function bscScanUrl(e: Evidence) {
  const base = "https://bscscan.com";
  if (e.type === "tx") return `${base}/tx/${e.value}`;
  if (e.type === "address") return `${base}/address/${e.value}`;
  if (e.type === "block") return `${base}/block/${e.value}`;
  return base;
}

function riskBadge(risk: IntelItem["risk"]) {
  const common = "rounded-md border px-2 py-1 text-xs";
  if (risk === "Low") return `${common} border-zinc-700 text-zinc-300`;
  if (risk === "Medium") return `${common} border-amber-700 text-amber-300`;
  return `${common} border-red-700 text-red-300`;
}

function yamlFromPatch(patch: PolicyPatch) {
  const lines: string[] = [];
  lines.push("patch:");
  if (patch.allowlist_add && patch.allowlist_add.length) {
    lines.push("  allowlist_add:");
    patch.allowlist_add.forEach((a) => lines.push(`    - "${a}"`));
  } else {
    lines.push("  allowlist_add: []");
  }
  lines.push("  budgets:");
  lines.push(`    max_fee_native: "${patch.budgets?.max_fee_native ?? ""}"`);
  lines.push(`    max_slippage_bps: ${patch.budgets?.max_slippage_bps ?? 0}`);
  lines.push("  guards:");
  lines.push(`    simulation_first: ${patch.guards?.simulation_first ? "true" : "false"}`);
  if (patch.guards?.circuit_breaker) {
    const cb = patch.guards.circuit_breaker;
    lines.push("    circuit_breaker:");
    lines.push(`      max_failures: ${cb.max_failures}`);
    lines.push(`      window_minutes: ${cb.window_minutes}`);
    lines.push(`      cooldown_minutes: ${cb.cooldown_minutes}`);
  }
  return lines.join("\n");
}

export function IntelBoard({
  title = "Community Intel Board",
  subtitle = "Explorer-first cards with evidence, timestamps, and neutral policy patches.",
  mode = "preview",
  items,
}: {
  title?: string;
  subtitle?: string;
  mode?: "preview" | "live";
  items: IntelItem[];
}) {
  const [tag, setTag] = useState<string>("All");
  const [risk, setRisk] = useState<string>("All");
  const [selected, setSelected] = useState<IntelItem | null>(null);

  const tags = useMemo(() => ["All", ...Array.from(new Set(items.map((i) => i.tag)))], [items]);
  const risks = ["All", "Low", "Medium", "High"];

  const filtered = useMemo(() => {
    return items
      .filter((i) => (tag === "All" ? true : i.tag === tag))
      .filter((i) => (risk === "All" ? true : i.risk === risk));
  }, [items, tag, risk]);

  return (
    <section className="mt-14 w-full">
      <div className="mb-5 flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
        <div>
          <div className="text-sm uppercase tracking-widest text-zinc-400">
            {title} <span className="text-zinc-600">/ {mode}</span>
          </div>
          <div className="mt-1 text-sm text-zinc-500">{subtitle}</div>
        </div>

        <div className="flex gap-2">
          <select
            className="rounded-md border border-zinc-800 bg-zinc-950/40 px-3 py-2 text-sm text-zinc-200"
            value={tag}
            onChange={(e) => setTag(e.target.value)}
          >
            {tags.map((t) => (
              <option key={t} value={t}>
                {t}
              </option>
            ))}
          </select>

          <select
            className="rounded-md border border-zinc-800 bg-zinc-950/40 px-3 py-2 text-sm text-zinc-200"
            value={risk}
            onChange={(e) => setRisk(e.target.value)}
          >
            {risks.map((r) => (
              <option key={r} value={r}>
                {r}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        {filtered.map((i) => (
          <div key={i.id} className="rounded-2xl border border-zinc-800 bg-zinc-950/40 p-5">
            <div className="flex items-start justify-between gap-3">
              <div className="leading-snug text-zinc-100">{i.title}</div>
              <div className={riskBadge(i.risk)}>{i.risk}</div>
            </div>

            <div className="mt-2 flex items-center gap-2 text-xs text-zinc-500">
              <span className="rounded-md border border-zinc-800 px-2 py-1">{i.tag}</span>
              <span className="text-zinc-700">·</span>
              <span>{new Date(i.timestamp).toISOString()}</span>
            </div>

            <div className="mt-3 text-sm text-zinc-400">{i.summary}</div>

            <div className="mt-4 space-y-2">
              {i.evidence.map((e, idx) => (
                <a
                  key={idx}
                  href={bscScanUrl(e)}
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center justify-between rounded-xl border border-zinc-800 px-3 py-2 text-sm hover:bg-zinc-900/30"
                >
                  <span className="text-zinc-400">{e.label}</span>
                  <span className="font-mono text-xs text-zinc-200">
                    {e.value.slice(0, 8)}...{e.value.slice(-6)}
                  </span>
                </a>
              ))}
            </div>

            <div className="mt-5 flex gap-2">
              <button
                onClick={() => setSelected(i)}
                className="flex-1 rounded-xl border border-zinc-700 bg-zinc-100 px-4 py-2 text-sm font-semibold text-zinc-900 hover:bg-white"
              >
                Generate policy patch
              </button>
              <a
                href={i.evidence[0] ? bscScanUrl(i.evidence[0]) : "https://bscscan.com"}
                target="_blank"
                rel="noreferrer"
                className="rounded-xl border border-zinc-800 px-4 py-2 text-sm text-zinc-200 hover:bg-zinc-900/30"
              >
                Open evidence
              </a>
            </div>

            <div className="mt-3 text-xs text-zinc-600">
              Evidence-linked only. Patch is neutral YAML diff (no strategy).
            </div>
          </div>
        ))}
      </div>

      {selected ? (
        <PolicyPatchModal item={selected} onClose={() => setSelected(null)} />
      ) : null}
    </section>
  );
}

function PolicyPatchModal({ item, onClose }: { item: IntelItem; onClose: () => void }) {
  const yaml = yamlFromPatch(item.policy_patch);

  async function copy() {
    await navigator.clipboard.writeText(yaml);
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 p-4">
      <div className="w-full max-w-2xl rounded-2xl border border-zinc-800 bg-zinc-950 p-5">
        <div className="flex items-start justify-between gap-3">
          <div>
            <div className="font-semibold text-zinc-100">Policy patch (YAML diff)</div>
            <div className="mt-1 text-sm text-zinc-500">
              Generated from evidence-linked item: <span className="text-zinc-300">{item.id}</span>
            </div>
          </div>
          <button onClick={onClose} className="text-zinc-400 hover:text-zinc-200">
            Close
          </button>
        </div>

        <pre className="mt-4 overflow-auto rounded-xl border border-zinc-800 bg-black/40 p-4 text-xs text-zinc-200">
{yaml}
        </pre>

        <div className="mt-4 flex gap-2">
          <button
            onClick={copy}
            className="rounded-xl border border-zinc-700 bg-zinc-100 px-4 py-2 text-sm font-semibold text-zinc-900 hover:bg-white"
          >
            Copy patch
          </button>
          <div className="self-center text-xs text-zinc-600">
            Apply via CLI only. No execution from the web UI.
          </div>
        </div>
      </div>
    </div>
  );
}

"use client";

import LText from "@/components/LText";

export type OpportunityItem = {
  id: string;
  title_en: string;
  title_pt: string;
  category_en: string;
  category_pt: string;
  benefit_en: string;
  benefit_pt: string;
  evidence_label: string;
  evidence_url: string;
  policy_hint_en: string;
  policy_hint_pt: string;
  risk: "Low" | "Medium" | "High";
};

function riskClass(risk: OpportunityItem["risk"]) {
  const common = "rounded-md border px-2 py-1 text-xs";
  if (risk === "Low") return `${common} border-zinc-700 text-zinc-300`;
  if (risk === "Medium") return `${common} border-amber-700 text-amber-300`;
  return `${common} border-red-700 text-red-300`;
}

export default function OpportunityMarketplace({ items }: { items: OpportunityItem[] }) {
  if (!items?.length) return null;

  return (
    <section className="mt-14 w-full">
      <div className="mb-5 flex flex-col gap-2">
        <div className="text-sm uppercase tracking-widest text-zinc-400">
          <LText en="Opportunity Marketplace" pt="Marketplace de Oportunidades" />
        </div>
        <div className="text-sm text-zinc-500">
          <LText
            en="Operational benefits catalog with evidence links and policy-first guidance. No opportunity sales. No profit promises."
            pt="Catalogo de beneficios operacionais com links de evidencia e orientacao policy-first. Sem venda de oportunidades. Sem promessa de lucro."
          />
        </div>
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        {items.map((item) => (
          <article key={item.id} className="rounded-2xl border border-zinc-800 bg-zinc-950/40 p-5">
            <div className="flex items-start justify-between gap-3">
              <h3 className="leading-snug text-zinc-100">
                <LText en={item.title_en} pt={item.title_pt} />
              </h3>
              <span className={riskClass(item.risk)}>{item.risk}</span>
            </div>

            <div className="mt-2">
              <span className="rounded-md border border-zinc-800 px-2 py-1 text-xs text-zinc-400">
                <LText en={item.category_en} pt={item.category_pt} />
              </span>
            </div>

            <p className="mt-3 text-sm text-zinc-400">
              <LText en={item.benefit_en} pt={item.benefit_pt} />
            </p>

            <a
              href={item.evidence_url}
              target="_blank"
              rel="noreferrer"
              className="mt-4 block rounded-xl border border-zinc-800 px-3 py-2 text-sm text-zinc-200 hover:bg-zinc-900/30"
            >
              {item.evidence_label}
            </a>

            <div className="mt-4 rounded-xl border border-zinc-800 bg-black/30 px-3 py-2 text-xs text-zinc-500">
              <LText en={item.policy_hint_en} pt={item.policy_hint_pt} />
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}

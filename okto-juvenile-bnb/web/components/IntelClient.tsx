"use client";

import { useEffect, useState } from "react";
import { IntelBoard, type IntelItem } from "@/components/IntelBoard";
import { IntelStrip } from "@/components/IntelStrip";
import OpportunityMarketplace, { type OpportunityItem } from "@/components/OpportunityMarketplace";

type IntelJson = {
  meta: {
    mode: "preview" | "live";
    network: string;
    updated_at: string;
    disclaimer: string;
  };
  strip: { id: string; label: string; value: string; delta?: string; hint?: string }[];
  board: IntelItem[];
  marketplace?: OpportunityItem[];
};

export default function IntelClient() {
  const [data, setData] = useState<IntelJson | null>(null);

  useEffect(() => {
    fetch("/intel_items.json", { cache: "no-store" })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to load intel_items.json");
        return res.json();
      })
      .then((json: IntelJson) => setData(json))
      .catch(() => setData(null));
  }, []);

  if (!data) return null;

  return (
    <>
      <IntelStrip mode={data.meta.mode} items={data.strip} />
      <IntelBoard mode={data.meta.mode} items={data.board} />
      <OpportunityMarketplace items={data.marketplace ?? []} />
    </>
  );
}

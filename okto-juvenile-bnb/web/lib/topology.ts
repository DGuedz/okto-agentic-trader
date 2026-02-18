export type TopologyCard = {
  id: "genesis" | "market" | "intel" | "execution";
  title: string;
  body: string;
  accentColor: string;
  iconChar: string;
};

export type Anchor = {
  id: TopologyCard["id"];
  endX: number;
  endY: number;
  side: "left" | "right";
};

export const TOPOLOGY_CARDS: TopologyCard[] = [
  {
    id: "genesis",
    title: "Genesis Spec",
    body: "Spec defines the laws. No UI drift. Pure intent.",
    accentColor: "#F6C356",
    iconChar: "</>",
  },
  {
    id: "market",
    title: "Market Data",
    body: "Evidence-sourced signals from BNB Chain RPC.",
    accentColor: "#4AA3FF",
    iconChar: "⚡",
  },
  {
    id: "intel",
    title: "Intel Layer",
    body: "Evidence-linked events. Generates policy-ready diffs.",
    accentColor: "#49E2A1",
    iconChar: "✹",
  },
  {
    id: "execution",
    title: "Execution",
    body: "Guardrailed actions with audit receipts.",
    accentColor: "#B57BFF",
    iconChar: "↯",
  },
];

export const TOPOLOGY_ANCHORS = {
  desktop: {
    core: { x: 50, y: 55 },
    points: [
      { id: "genesis", endX: 18, endY: 28, side: "left" },
      { id: "market", endX: 18, endY: 62, side: "left" },
      { id: "intel", endX: 82, endY: 28, side: "right" },
      { id: "execution", endX: 82, endY: 62, side: "right" },
    ] as Anchor[],
  },
  tablet: {
    core: { x: 50, y: 36 },
    points: [
      { id: "genesis", endX: 24, endY: 58, side: "left" },
      { id: "market", endX: 24, endY: 84, side: "left" },
      { id: "intel", endX: 76, endY: 58, side: "right" },
      { id: "execution", endX: 76, endY: 84, side: "right" },
    ] as Anchor[],
  },
  mobile: {
    core: { x: 50, y: 28 },
    points: [
      { id: "genesis", endX: 24, endY: 56, side: "left" },
      { id: "market", endX: 24, endY: 76, side: "left" },
      { id: "intel", endX: 76, endY: 56, side: "right" },
      { id: "execution", endX: 76, endY: 76, side: "right" },
    ] as Anchor[],
  },
};


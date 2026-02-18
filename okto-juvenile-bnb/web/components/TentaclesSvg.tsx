import type { Anchor } from "@/lib/topology";

type CorePoint = { x: number; y: number };

function gradientFor(id: Anchor["id"]) {
  if (id === "genesis") return "tentacle-amber";
  if (id === "market") return "tentacle-blue";
  if (id === "intel") return "tentacle-green";
  return "tentacle-purple";
}

function glowFor(id: Anchor["id"]) {
  if (id === "genesis") return "rgba(246,195,86,0.42)";
  if (id === "market") return "rgba(74,163,255,0.42)";
  if (id === "intel") return "rgba(73,226,161,0.42)";
  return "rgba(181,123,255,0.42)";
}

function tentaclePath(core: CorePoint, anchor: Anchor) {
  const { x: cx, y: cy } = core;
  const { endX: ex, endY: ey, side } = anchor;
  const dir = side === "left" ? -1 : 1;

  const c1x = cx + dir * 13;
  const c1y = cy - Math.abs(cy - ey) * 0.55;
  const c2x = ex - dir * 11;
  const c2y = ey + (ey < cy ? 8 : -8);

  return `M ${cx} ${cy} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${ex} ${ey}`;
}

export default function TentaclesSvg({
  core,
  anchors,
  reduced = false,
}: {
  core: CorePoint;
  anchors: Anchor[];
  reduced?: boolean;
}) {
  return (
    <svg
      className="pointer-events-none absolute inset-0 h-full w-full"
      viewBox="0 0 100 100"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <defs>
        <linearGradient id="tentacle-amber" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="rgba(246,195,86,0.95)" />
          <stop offset="100%" stopColor="rgba(246,195,86,0.08)" />
        </linearGradient>
        <linearGradient id="tentacle-blue" x1="0%" y1="100%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="rgba(74,163,255,0.95)" />
          <stop offset="100%" stopColor="rgba(74,163,255,0.08)" />
        </linearGradient>
        <linearGradient id="tentacle-green" x1="100%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stopColor="rgba(73,226,161,0.95)" />
          <stop offset="100%" stopColor="rgba(73,226,161,0.08)" />
        </linearGradient>
        <linearGradient id="tentacle-purple" x1="100%" y1="100%" x2="0%" y2="0%">
          <stop offset="0%" stopColor="rgba(181,123,255,0.95)" />
          <stop offset="100%" stopColor="rgba(181,123,255,0.08)" />
        </linearGradient>
      </defs>

      {anchors.map((a) => {
        const d = tentaclePath(core, a);
        const grad = gradientFor(a.id);
        const glow = glowFor(a.id);
        return (
          <g key={a.id}>
            <path
              d={d}
              fill="none"
              stroke={`url(#${grad})`}
              strokeWidth={reduced ? 4 : 10}
              strokeLinecap="round"
              opacity={reduced ? 0.04 : 0.08}
              style={{ filter: `drop-shadow(0 0 18px ${glow})` }}
            />
            <path
              d={d}
              fill="none"
              stroke={`url(#${grad})`}
              strokeWidth={reduced ? 2.4 : 6}
              strokeLinecap="round"
              opacity={reduced ? 0.08 : 0.14}
            />
            <path
              d={d}
              fill="none"
              stroke={`url(#${grad})`}
              strokeWidth={2.2}
              strokeLinecap="round"
              opacity={reduced ? 0.55 : 0.9}
            />
            <circle cx={a.endX} cy={a.endY} r={0.95} fill={glow} />
            <circle cx={a.endX} cy={a.endY} r={0.48} fill="rgba(255,255,255,0.95)" />
          </g>
        );
      })}
    </svg>
  );
}


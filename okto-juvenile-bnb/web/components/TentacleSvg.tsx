import React from "react";

type TentaclePath = {
  d: string;
  gradientId: string;
  glow?: string;
};

export default function TentacleSvg({ paths }: { paths: TentaclePath[] }) {
  return (
    <svg
      className="pointer-events-none absolute inset-0 h-full w-full"
      viewBox="0 0 1200 700"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <defs>
        <linearGradient id="tentacle-amber" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="rgba(246,195,86,0.9)" />
          <stop offset="100%" stopColor="rgba(246,195,86,0.08)" />
        </linearGradient>
        <linearGradient id="tentacle-blue" x1="0%" y1="100%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="rgba(74,163,255,0.9)" />
          <stop offset="100%" stopColor="rgba(74,163,255,0.08)" />
        </linearGradient>
        <linearGradient id="tentacle-green" x1="100%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stopColor="rgba(73,226,161,0.9)" />
          <stop offset="100%" stopColor="rgba(73,226,161,0.08)" />
        </linearGradient>
        <linearGradient id="tentacle-purple" x1="100%" y1="100%" x2="0%" y2="0%">
          <stop offset="0%" stopColor="rgba(181,123,255,0.9)" />
          <stop offset="100%" stopColor="rgba(181,123,255,0.08)" />
        </linearGradient>
      </defs>

      {paths.map((p, idx) => (
        <g key={idx}>
          <path
            d={p.d}
            fill="none"
            stroke={`url(#${p.gradientId})`}
            strokeWidth="6"
            strokeLinecap="round"
            opacity="0.18"
            style={{ filter: `drop-shadow(0 0 16px ${p.glow ?? "rgba(255,255,255,0.2)"})` }}
          />
          <path
            d={p.d}
            fill="none"
            stroke={`url(#${p.gradientId})`}
            strokeWidth="2.2"
            strokeLinecap="round"
            opacity="0.9"
          />
        </g>
      ))}
    </svg>
  );
}

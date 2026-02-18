import TentaclesSvg from "@/components/TentaclesSvg";
import { TOPOLOGY_ANCHORS, TOPOLOGY_CARDS } from "@/lib/topology";

function Card({
  title,
  body,
  accentColor,
  iconChar,
}: {
  title: string;
  body: string;
  accentColor: string;
  iconChar: string;
}) {
  return (
    <article className="rounded-2xl border border-white/12 bg-[rgba(15,18,24,0.55)] p-6 shadow-[0_10px_40px_rgba(0,0,0,0.6)] backdrop-blur-md">
      <header className="mb-3 flex items-center gap-3">
        <span className="text-xl" aria-hidden="true">
          {iconChar}
        </span>
        <h3 className="text-3xl font-semibold tracking-tight" style={{ color: accentColor }}>
          {title}
        </h3>
      </header>
      <p className="font-mono text-[1.85rem] leading-[1.35] text-zinc-300">{body}</p>
    </article>
  );
}

function NodeCore() {
  return (
    <div className="relative flex h-[320px] w-[320px] items-center justify-center rounded-full border-[3px] border-[#F6C356] bg-[#0B0F14] shadow-[0_0_60px_rgba(246,195,86,0.18)] md:h-[360px] md:w-[360px] lg:h-[380px] lg:w-[380px]">
      <span className="absolute -top-3 h-6 w-6 rounded-full bg-[#4AA3FF] shadow-[0_0_18px_rgba(74,163,255,0.9)]" aria-hidden="true" />
      <span className="absolute -bottom-3 h-6 w-6 rounded-full bg-[#49E2A1] shadow-[0_0_18px_rgba(73,226,161,0.9)]" aria-hidden="true" />
      <span className="absolute bottom-[18%] right-[7%] h-5 w-5 rounded-full bg-[#B57BFF] shadow-[0_0_18px_rgba(181,123,255,0.9)]" aria-hidden="true" />

      <div className="text-center">
        <div className="mx-auto mb-4 h-14 w-14 rounded-full bg-gradient-to-b from-zinc-400 to-zinc-800 opacity-80 shadow-[0_0_18px_rgba(255,255,255,0.18)]" aria-hidden="true" />
        <div className="font-mono text-5xl font-semibold tracking-[0.18em] text-zinc-100 md:text-6xl">OKTO NODE</div>
        <div className="mx-auto mt-4 inline-flex rounded-full border border-white/10 bg-[#F6C356]/18 px-4 py-2 font-mono text-2xl tracking-[0.12em] text-[#F6C356]">
          v1.1 STABLE
        </div>
      </div>
    </div>
  );
}

export default function HeadlessTopologySection() {
  const leftCards = TOPOLOGY_CARDS.filter((c) => c.id === "genesis" || c.id === "market");
  const rightCards = TOPOLOGY_CARDS.filter((c) => c.id === "intel" || c.id === "execution");

  return (
    <section className="relative mt-16 w-full">
      <header className="mb-10 text-center">
        <h2 className="text-6xl font-semibold tracking-tight text-zinc-100 md:text-7xl">
          The <span className="text-[#F6C356]">Headless</span> Topology
        </h2>
      </header>

      <div className="relative overflow-hidden rounded-3xl border border-white/5 bg-[radial-gradient(circle_at_50%_52%,rgba(246,195,86,0.1),transparent_40%),radial-gradient(circle_at_20%_30%,rgba(74,163,255,0.08),transparent_35%),radial-gradient(circle_at_80%_30%,rgba(73,226,161,0.08),transparent_35%),#070A0D] p-5 md:p-8 lg:p-10">
        <div className="hidden lg:block">
          <TentaclesSvg core={TOPOLOGY_ANCHORS.desktop.core} anchors={TOPOLOGY_ANCHORS.desktop.points} />
        </div>
        <div className="hidden md:block lg:hidden">
          <TentaclesSvg core={TOPOLOGY_ANCHORS.tablet.core} anchors={TOPOLOGY_ANCHORS.tablet.points} reduced />
        </div>
        <div className="block md:hidden">
          <TentaclesSvg core={TOPOLOGY_ANCHORS.mobile.core} anchors={TOPOLOGY_ANCHORS.mobile.points} reduced />
        </div>

        <div className="relative z-10 grid grid-cols-1 gap-7 lg:grid-cols-3 lg:items-center">
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-1">
            {leftCards.map((card) => (
              <Card key={card.id} {...card} />
            ))}
          </div>

          <div className="flex justify-center py-2 lg:py-6">
            <NodeCore />
          </div>

          <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-1">
            {rightCards.map((card) => (
              <Card key={card.id} {...card} />
            ))}
          </div>
        </div>
      </div>

      <p className="mt-5 text-center font-mono text-2xl text-zinc-500">
        Evidence-linked only. No profit promises.
      </p>
    </section>
  );
}


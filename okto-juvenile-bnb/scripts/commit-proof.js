const hre = require("hardhat");

async function main() {
  const addr = process.env.OKTO_PROOF_ADDRESS;
  const runId = process.env.RUN_ID;
  const reportHash = process.env.REPORT_HASH;
  const tag = process.env.TAG || "BINANCE->ASTER:dryrun";

  if (!addr) throw new Error("OKTO_PROOF_ADDRESS missing");
  if (!runId) throw new Error("RUN_ID missing");
  if (!reportHash) throw new Error("REPORT_HASH missing");

  const c = await hre.ethers.getContractAt("OktoProof", addr);
  const tx = await c.commit(runId, reportHash, tag);
  console.log("TX_HASH=", tx.hash);
  await tx.wait();
  console.log("MINED");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});

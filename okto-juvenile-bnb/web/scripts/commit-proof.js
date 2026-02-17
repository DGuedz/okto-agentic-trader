const hre = require("hardhat");

async function main() {
  const address = process.env.OKTO_PROOF_ADDRESS;
  const runId = process.env.RUN_ID;
  const reportHash = process.env.REPORT_HASH;
  const tag = process.env.TAG || "BINANCE->ASTER:dryrun";

  const contract = await hre.ethers.getContractAt("OktoProof", address);
  const tx = await contract.commit(runId, reportHash, tag);
  console.log("TX_HASH=", tx.hash);
  await tx.wait();
  console.log("MINED");
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

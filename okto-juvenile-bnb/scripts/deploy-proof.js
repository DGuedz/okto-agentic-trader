const hre = require("hardhat");

async function main() {
  const C = await hre.ethers.getContractFactory("OktoProof");
  const c = await C.deploy();
  await c.waitForDeployment();
  console.log("OKTO_PROOF_ADDRESS=", await c.getAddress());
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});

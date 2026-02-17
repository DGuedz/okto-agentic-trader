const hre = require("hardhat");

async function main() {
  const Contract = await hre.ethers.getContractFactory("OktoProof");
  const instance = await Contract.deploy();
  await instance.waitForDeployment();
  console.log("OKTO_PROOF_ADDRESS=", await instance.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

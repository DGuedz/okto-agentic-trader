require("@nomicfoundation/hardhat-ethers");
require("dotenv").config({ path: ".env.local" });

const deployerKey = process.env.DEPLOYER_PK;
const deployerAccounts =
  deployerKey && /^0x[0-9a-fA-F]{64}$/.test(deployerKey) ? [deployerKey] : [];

module.exports = {
  solidity: "0.8.20",
  networks: {
    bscTestnet: {
      url: process.env.BSC_TESTNET_RPC,
      accounts: deployerAccounts,
    },
  },
};

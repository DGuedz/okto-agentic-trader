// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract OktoProof {
    event Proof(bytes32 indexed runId, bytes32 indexed reportHash, string tag, address indexed sender);

    function commit(bytes32 runId, bytes32 reportHash, string calldata tag) external {
        emit Proof(runId, reportHash, tag, msg.sender);
    }
}

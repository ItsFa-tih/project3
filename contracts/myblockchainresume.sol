pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract Resume is ERC721Full {

    constructor() public ERC721Full("Resume", "RES") {}

    function loadResume(address candidate, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newResumeID = totalSupply();
        _mint(candidate, newResumeID);
        _setTokenURI(newResumeID,tokenURI);
        
        return newResumeID;
    
    }
}
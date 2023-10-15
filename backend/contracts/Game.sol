pragma solidity ^0.8.0;

contract WitcherBattleGame {
    // Mapping to store player scores
    mapping(address => uint256) public playerScores;

    // Event to log score updates
    event ScoreUpdated(address indexed player, uint256 newScore);

    // Function to set a player's score
    function setScore(uint256 _score) public {
        playerScores[msg.sender] = _score;
        emit ScoreUpdated(msg.sender, _score);
    }

    // Function to get a player's score
    function getScore(address _player) public view returns (uint256) {
        return playerScores[_player];
    }
}

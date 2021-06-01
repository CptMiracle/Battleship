
The game must have a maximum of 2 players (Player 1, Player 2).
At the main menu, player(s) have the option to start playing (PvP or AI), view the instructions, view the leaderboards, or quit the game.
At the beginning, both players each have 5 ships to place on a 10 by 10 grid array, consisting of 1 grid (1x1), 2 grid (2x1), 3 grid (3x1), 4 grid (4x1), and 5 grid (5x1) ships.
Ships can not be diagonal, overlap other ships, or be out of bounds.
Ships are static and cannot move position when the game starts (anchored).
Once both players have chosen their locations for their ships, the game begins with Player 1 firing the first shot.
Input will be through mouse clicks on specific grids.
Output shows whether the input hits the water or an enemy ship.
If the shot fired misses and does not hit an enemy ship, that grid is marked white for a miss. If the shot fired hits an enemy ship, that grid is marked red for a hit. If the ship is sunk, x’s are displayed on the grids where the enemy ship was positioned.
Each player may fire once every round, and every enemy ship sunk means an additional point to that player who shot.
A ship is destroyed when all grids of that ship are hit.
If a player has hit a grid where a part of the enemy ship is positioned, that player goes into a streak duration where he/she is able to fire again unless the following shot does not hit an enemy ship.
Whichever player sinks their enemy’s ships first wins.
When the game is over, players are led to the end screen and a leaderboard.
Players can choose to play again or quit.

*For the Leaderboard file, ensure that there is no more than 1 extra blank line in the file otherwise an IndexError would occur.
Leaderboard scores are in order by the time played and lower scores mean less shots fired to win the game (in short, the lower the score, the better)
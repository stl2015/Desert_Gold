# Game of Isolation

1. Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board.  Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game.  The first player with no remaining legal moves loses, and the opponent is declared the winner.  These rules are implemented in the `isolation.Board` class provided in the repository. 

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a rectangular grid (like a chess or checkerboard).  The agents can move to any open cell on the board that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. Movements are blocked at the edges of the board (the board does not wrap around), however, the player can "jump" blocked or occupied spaces (just like a knight in chess).

Additionally, agents will have a fixed time limit each turn to search for the best move and respond.  If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins.

2. Classical Min-Max solution: complexity = (branch factor)^depth. Depth limited search: design appropriate score function for the end k-th step, which will be the value in the min-max strategy of game tree.  

3. Here I used Iterative deepening search for Alpha-Beta pruning algorithm,

For the max layer -
Test if search depth is zero: if yes, return score function from the point view of current player. Pre-assign the current value so that any thing is greater than it.
Loop through game's available subsequent moves from current player:

* a) apply the move and create the next min layer with (search depth -1), update current maximum value if it is less than next value;
* b) pruning: if current maximum is greater than or equal to beta – the upper bound of search on max layer, then return current maximum.
* c) update alpha if it is less than current maximum.
Return current maximum.

For the min layer -
Test if search depth is zero: if yes, return score function from the point view of current player. Pre-assign the current value so that any thing is less than it. Loop through game's available subsequent moves from current player:

* a) apply the move and create the next max layer with (search depth -1), update current minimum value if it is greater than next value;
* b) pruning: if current minimum is less than or equal to alpha – the lower bound of search on min layer, then return current minimum.
* c) update beta if it is greater than current minimum.
Return current minimum.

4. Custom score function

* a) (number of legal moves for current player – number of legal moves for its opponent)* number of filled spaces*0.5. It favors more moves for current player than its opponent. In addition, it favors more search into deeper depth.
* b) (number of legal moves for current player – number of legal moves for its opponent)* number of filled spaces. Similar to 1), but has a higher weight of favoring search depth.
* c) Using (number of legal moves for current player – number of legal moves for its opponent) at first, then in later stage of game – 80% of board is filled, use (number of legal moves for current player). It is a slightly more conservative version of AB_Improved.

5. Match result: Custom a) score function has the highest win rate (~60%) against all other agents. The reason is that it not only favors large difference between legal moves of player and its opponent, it also encourage explore searching into deeper trees. In term of complexity, it counts moves for player and opponent, as well as the filled spaces on the board. It is still order (size of board positions).

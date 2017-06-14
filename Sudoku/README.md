# Diagonal Sudoku
How do we use constraint propagation to solve the diagonal sudoku problem?  

A: For diagonal sudoku problem, there are 29 9-box-unit where each unit should have distinctive number 1 through 9 in its boxes. The constraints we could consider are followings:

a) elimination: when one box has been assigned a single number which means it is solved, then its peers in same units will not have the same number and we could eliminate it from the possibilities in its peers.

b) only-choice: for each unit, if one number only appears in one box as candidate and not in its peers, we could infer the number should be assigned to this box.

c) naked twins: There are 27 (or 29 in diagonal Sudoku) 9-box-unit in Sudoku that each unit should satisfy the constraints of having unique number from 1 through 9. Now in naked twins problem, for each unit if there are two boxes that have same two numbers (say '12'), then the peers (7 boxes) in the same unit will not have these two numbers. As a result, this could serve as a constraint to eliminate the possibilities of numbers in the peers.

We could use the method reduce_puzzle to iteratively apply the three constraints. We count the number of solved boxes - where it has been assigned a single number. The iteration stops if two successive iterations yields same number of solved boxes.

The reduce_puzzle may not be sufficient for harder sudoku. We use depth first search to exhaust the possibilities: basically we recursively search all possible candidate numbers in all unsolved boxes (with more than 1 number), until we find a solution or if no solution is found after exhausting the possibilities we return False.


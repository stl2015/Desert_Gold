
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # 1: 
    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
        
    w, h = game.width, game.height     
    blanks = len(game.get_blank_spaces())
    filled = w*h - blanks
    if filled <=0: filled = 1
    
    return float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player))))*filled*0.5

def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # 2:   
    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")   
    
    w, h = game.width, game.height     
    blanks = len(game.get_blank_spaces())
    filled = w*h - blanks
    if filled <=0: filled = 1
    
    return float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player))))*filled


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # 3: 
    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    w, h = game.width, game.height     
    blanks = game.get_blank_spaces()
    
    # beginning game
    if len(blanks) > 0.8*w*h: return float(len(game.get_legal_moves(player)))
    # later in the game                                      
    else:                               
        return float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player))))



class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
		# what finished in try block before exception occurs stay.
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        def max_value(game, depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
    
            moves = game.get_legal_moves()
            if not moves: return game.utility(self)
            
            if depth==0: return self.score(game, self)
            
            v=float("-inf")
            for move in moves:
                v = max(v, min_value(game.forecast_move(move), depth-1))
            return v


        def min_value(game, depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            moves = game.get_legal_moves()
            if not moves: return game.utility(self)
            
            if depth==0: return self.score(game, self)            
            
            v=float("inf")
            for move in moves:
                v = min(v, max_value(game.forecast_move(move), depth-1))
            return v			
		 
							
        best_move = (-1, -1)
        best_score = float("-inf")
		
		# get available moves for current player
        moves = game.get_legal_moves()

        if not moves: return game.utility(self)
        
        best_move = moves[0]
        
        try:
            for move in moves: # forecast move and get updated board
                    
                value = min_value(game.forecast_move(move), depth-1)
            
                if value > best_score:
                    best_score = value
                    best_move = move
					
            return best_move
			
        except SearchTimeout:
            pass
		
        return best_move
		

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. 
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left
        
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)
        moves = game.get_legal_moves()
        if len(moves)>0:
            best_move = moves[0]
        else:
            return best_move
									
        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            max_depth = len(game.get_blank_spaces())
			
            for depth in range(0, max_depth):
				
                best_move = self.alphabeta(game, depth)

            return best_move

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move				
		

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers (below)

        beta : float
            Beta limits the upper bound of search on maximizing layers (below)

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

		
		# maximizing layer
        def max_value(game, depth, alpha, beta):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

			# terminal test
            if depth==0: return self.score(game, self)

            v = float("-inf")
            for move in game.get_legal_moves():
                v = max(v, min_value(game.forecast_move(move), depth-1, alpha, beta))
                if v >= beta: return v
                alpha = max(v, alpha)
				
            return v

			
		# minimizing layer
        def min_value(game, depth, alpha, beta):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

			# terminal test
            if depth==0: return self.score(game, self)
		
            v = float("inf")
            for move in game.get_legal_moves():
                v = min(v, max_value(game.forecast_move(move), depth-1, alpha, beta))
                if v <= alpha: return v
                beta = min(v, beta)

            return v

        best_move = (-1, -1)
        best_score = float("-inf")

        for move in game.get_legal_moves():
            v = min_value(game.forecast_move(move), depth-1, alpha, beta)
				
            if v>best_score:
                best_score = v
                best_move = move
						
            alpha = max(v, alpha)		
		
        return best_move
		














		
		
		

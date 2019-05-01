from connectfour.agents.computer_player import RandomAgent
import random
import math


class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 4

    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            next_state = board.next_state(self.id, move[1])
            moves.append(move)
            vals.append(self.dfMiniMax(next_state, 1, -math.inf, math.inf))

        bestMove = moves[vals.index(max(vals))]
        return bestMove

    def dfMiniMax(self, board, depth, alpha, beta):
        # Goal return column with maximized scores of all possible next states

        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()

        for move in valid_moves:
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])
                value = math.inf
                value = min(value, self.dfMiniMax(next_state, depth + 1, alpha, beta))
                beta = min(beta, value)
                if alpha >= beta:
                    break
            else:
                next_state = board.next_state(self.id, move[1])
                value = -math.inf
                value = max(value, self.dfMiniMax(next_state, depth + 1, alpha, beta))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value

    def evaluateBoardState(self, board):
        """
        Your evaluation function should look at the current state and return a score for it.
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.
        """

        """
        These are the variables and functions for board objects which may be helpful when creating your Agent.
        Look into board.py for more information/descriptions of each, or to look for any other definitions which may help you.

        Board Variables:
            board.width
            board.height
            board.last_move
            board.num_to_connect
            board.winning_zones
            board.score_array
            board.current_player_score

        Board Functions:
            get_cell_value(row, col)
            try_move(col)
            valid_move(row, col)
            valid_moves()
            terminal(self)
            legal_moves()
            next_state(turn)
            winner()
        """


        score = 0

        #MIDDLE PREFERENCE
        for r in range(board.height-1, -1, -1):
            row_array = board.board[r]

            if row_array[3] == (self.id):
                score += 3
            if row_array[2] == (self.id):
                score += 2
            if row_array[4] == (self.id):
                score += 2
            if row_array[1] == (self.id):
                score += 1
            if row_array[5] == (self.id):
                score += 1
            if row_array[3] == (self.id%2 +1):
                score -= 3
            if row_array[2] == (self.id%2 +1):
                score -= 2
            if row_array[4] == (self.id%2 +1):
                score -= 2
            if row_array[1] == (self.id%2 +1):
                score -= 1
            if row_array[5] == (self.id%2 +1):
                score -= 1

        #HORIZONTAL CHECKING
        for r in range(board.height-1, -1, -1):
            row_array = board.board[r]
            for c in range(board.width-3):
                window = row_array[c:c+4]

                if window.count(self.id)==4:
                    score += 100
                if window.count(self.id) == 3 and window.count(0) == 1:
                    score += 20
                if window.count(self.id) == 2 and window.count(0) == 2:
                    score += 5
                if window.count(self.id%2 + 1) == 3 and window.count(0) == 1:
                    score -= 80
                if window.count(self.id%2 + 1) == 2 and window.count(0) == 2:
                    score -= 10

        #VERTICAL CHECKING
        for c in range(board.width):
            col_array = [board.board[r][c] for r in range(board.height)]
            for r in range(board.height-3):
                window = col_array[r:r+4]

                if window.count(self.id)==4:
                    score += 100
                if window.count(self.id) == 3 and window.count(0) == 1:
                    score += 20
                if window.count(self.id) == 2 and window.count(0) == 2:
                    score += 5
                if window.count(self.id%2 + 1) == 3 and window.count(0) == 1:
                    score -= 80
                if window.count(self.id%2 + 1) == 2 and window.count(0) == 2:
                    score -= 10


        #DIAGONAL CHECKING (POSITIVE)
        for r in range(board.height-3):
            for c in range(board.width-3):
                window = [board.board[r+i][c+i] for i in range(4)]

                if window.count(self.id)==4:
                    score += 100
                if window.count(self.id) == 3 and window.count(0) == 1:
                    score += 20
                if window.count(self.id) == 2 and window.count(0) == 2:
                    score += 5
                if window.count(self.id%2 + 1) == 3 and window.count(0) == 1:
                    score -= 80
                if window.count(self.id%2 + 1) == 2 and window.count(0) == 2:
                    score -= 10

        #DIAGONAL CHECKING (NEGATIVE)
        for r in range(board.height-3):
            for c in range(board.width-3):
                window = [board.board[r+3-i][c+i] for i in range(4)]

                if window.count(self.id)==4:
                    score += 100
                if window.count(self.id) == 3 and window.count(0) == 1:
                    score += 20
                if window.count(self.id) == 2 and window.count(0) == 2:
                    score += 5
                if window.count(self.id%2 + 1) == 3 and window.count(0) == 1:
                    score -= 80
                if window.count(self.id%2 + 1) == 2 and window.count(0) == 2:
                    score -= 10

        return score

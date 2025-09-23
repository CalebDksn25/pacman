
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A simple agent for PacMan
    """

    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        return directions.stop
        """

        pacmanPos = pacman.getPosition()
        isScared = ghost.scaredTimer > 0
        ghostPos = ghost.getPosition()

        #First, if the pacman is not in danger, we return Directions.STOP
        if isScared:
            return Directions.STOP
        if pacmanPos[0] == ghostPos[0]: ##If the pacman and ghost are in same row and column
            if abs(pacmanPos[1] - ghostPos[1]) <= dist: #If the distance is less than or equal to Y dist
                return Directions.NORTH if ghostPos[1] > pacmanPos[1] else Directions.SOUTH
        elif pacmanPos[1] == ghostPos[1]: ##If the pacman and ghost are in same row and column
            if abs(pacmanPos[0] - ghostPos[0]) <= dist: #If the distance is less than or equal to X distance
                return Directions.EAST if ghostPos[0] > pacmanPos[0] else Directions.WEST
        
        return Directions.STOP

    
    def getAction(self, state):
        """
        state - GameState
        
        Fill in appropriate documentation
        """

        pacman = state.getPacmanState()
        ghostStates = state.getGhostStates()
        heading = pacman.getDirection()
        legal = state.getLegalPacmanActions()


        for ghost in ghostStates:
            ##If direction.stop was returned
            inDanger = self.inDanger(pacman, ghost)
            if inDanger != Directions.STOP:

                legalMoves = state.getLegalActions()
                reverseDirection = Directions.REVERSE[inDanger]
                leftDirection = Directions.LEFT[inDanger]
                rightDirection = Directions.RIGHT[inDanger]

                if reverseDirection in legalMoves:
                    return reverseDirection
                elif leftDirection in legalMoves:
                    return leftDirection
                elif rightDirection in legalMoves:
                    return rightDirection
                elif inDanger in legalMoves:
                    return inDanger
                return Directions.STOP
            
        if heading == Directions.STOP:
            # Pacman is stopped, assume North (true at beginning of game)
            heading = Directions.NORTH

        # Turn left if possible
        left = Directions.LEFT[heading]  # What is left based on current heading
        if left in legal:
            action = left
        else:
            # No left turn
            if heading in legal:
                action = heading  # continue in current direction
            elif Directions.RIGHT[heading] in legal:
                action = Directions.RIGHT[heading]  # Turn right
            elif Directions.REVERSE[heading] in legal:
                action = Directions.REVERSE[heading]  # Turn around
            else:
                action = Directions.STOP  # Can't move!

        return action


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

        pacmanPos = pacman.getPositin()
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


        for ghost in ghostStates:
            ##If direction.stop was returned
            inDanger = self.inDanger(pacman, ghost)
            if inDanger != Directions.STOP:
                ##TODO: Check if is a legal move 
                
                return Directions.REVERSE(inDanger) #Return the opposite direction of the danger so we can head that direction



        raise NotImplemented

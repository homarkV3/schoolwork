# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        ghostDistances = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
        nearestGhostDistance = min(ghostDistances) if ghostDistances else float('inf')

        if nearestGhostDistance > 0 and nearestGhostDistance < 2:
                return -float('inf')

        foodDistances = [manhattanDistance(newPos, food) for food in newFood.asList()]
        nearestFoodDistance = min(foodDistances) if foodDistances else 0
        return successorGameState.getScore() + 1.0 / (nearestFoodDistance + 1)

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        def minimax(agentIndex, depth, gameState):
                if gameState.isWin() or gameState.isLose() or depth == self.depth:
                    return self.evaluationFunction(gameState)
                if agentIndex == 0:
                    return max(minimax(1, depth, gameState.generateSuccessor(agentIndex, action)) for action in gameState.getLegalActions(agentIndex))
                else: 
                    nextAgent = agentIndex + 1
                    if gameState.getNumAgents() == nextAgent:
                        nextAgent = 0
                        depth += 1
                    return min(minimax(nextAgent, depth, gameState.generateSuccessor(agentIndex, action)) for action in gameState.getLegalActions(agentIndex))
        return max(gameState.getLegalActions(0), key=lambda x: minimax(1, 0, gameState.generateSuccessor(0, x)))


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def alphaBeta(agentIndex, depth, gameState, alpha, beta):
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            if agentIndex == 0:
                value = -float('inf')
                for action in gameState.getLegalActions(agentIndex):
                    value = max(value, alphaBeta(1, depth, gameState.generateSuccessor(agentIndex, action), alpha, beta))
                    alpha = max(alpha, value)
                    if beta < alpha:
                        break
                return value
            else:
                value = float('inf')
                nextAgent = agentIndex + 1
                if nextAgent == gameState.getNumAgents():
                    nextAgent = 0
                    depth += 1
                for action in gameState.getLegalActions(agentIndex):
                    value = min(value, alphaBeta(nextAgent, depth, gameState.generateSuccessor(agentIndex, action), alpha, beta))
                    beta = min(beta, value)
                    if beta < alpha:
                        break
                return value

        alpha = -float('inf')
        beta = float('inf')
        bestAction = Directions.STOP
        for action in gameState.getLegalActions(0):
            value = alphaBeta(1, 0, gameState.generateSuccessor(0, action), alpha, beta)
            if value > alpha:
                alpha = value
                bestAction = action
        return bestAction

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax(agentIndex, depth, gameState):
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            if agentIndex == 0:  
                return max(expectimax(1, depth, gameState.generateSuccessor(agentIndex, action)) for action in gameState.getLegalActions(agentIndex))
            else:  
                nextAgent = agentIndex + 1
                if nextAgent == gameState.getNumAgents():
                    nextAgent = 0
                    depth += 1
                return sum(expectimax(nextAgent, depth, gameState.generateSuccessor(agentIndex, action)) for action in gameState.getLegalActions(agentIndex)) / len(gameState.getLegalActions(agentIndex))

        return max(gameState.getLegalActions(0), key=lambda x: expectimax(1, 0, gameState.generateSuccessor(0, x)))

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pos = currentGameState.getPacmanPosition()
    food = currentGameState.getFood().asList()
    ghostStates = currentGameState.getGhostStates()
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]

    foodDistances = [manhattanDistance(pos, foodPos) for foodPos in food]
    nearestFoodDistance = min(foodDistances) if foodDistances else 0

    ghostDistances = [manhattanDistance(pos, ghost.getPosition()) for ghost in ghostStates if ghost.scaredTimer == 0]
    nearestGhostDistance = min(ghostDistances) if ghostDistances else float('inf')

    scaredGhostDistances = [manhattanDistance(pos, ghost.getPosition()) for ghost in ghostStates if ghost.scaredTimer > 0]
    nearestScaredGhostDistance = min(scaredGhostDistances) if scaredGhostDistances else 0

    score = currentGameState.getScore()
    score += -1.5 * nearestFoodDistance  
    if nearestGhostDistance != float('inf'):
        score += -2 * (1.0 / (nearestGhostDistance + 0.1))
    score += 2 * (1.0 / (nearestScaredGhostDistance + 0.1)) if nearestScaredGhostDistance > 0 else 0

    return score

# Abbreviation
better = betterEvaluationFunction

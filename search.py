# search.py
# ---------
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

# Trabalho FIA 
# Grupo: Gabriella Selbach, Geovana Silveira e Luiza Cruz

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
	"""
	This class outlines the structure of a search problem, but doesn't implement
	any of the methods (in object-oriented terminology: an abstract class).

	You do not need to change anything in this class, ever.
	"""

	def getStartState(self):
		"""
		Returns the start state for the search problem.
		"""
		util.raiseNotDefined()

	def isGoalState(self, state):
		"""
		  state: Search state

		Returns True if and only if the state is a valid goal state.
		"""
		util.raiseNotDefined()

	def getSuccessors(self, state):
		"""
		  state: Search state

		For a given state, this should return a list of triples, (successor,
		action, stepCost), where 'successor' is a successor to the current
		state, 'action' is the action required to get there, and 'stepCost' is
		the incremental cost of expanding to that successor.
		"""
		util.raiseNotDefined()

	def getCostOfActions(self, actions):
		"""
		 actions: A list of actions to take

		This method returns the total cost of a particular sequence of actions.
		The sequence must be composed of legal moves.
		"""
		util.raiseNotDefined()


def tinyMazeSearch(problem):
	"""
	Returns a sequence of moves that solves tinyMaze.  For any other maze, the
	sequence of moves will be incorrect, so only use this for tinyMaze.
	"""
	from game import Directions
	s = Directions.SOUTH
	w = Directions.WEST
	return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
	"""
	Search the deepest nodes in the search tree first.

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.

	To get started, you might want to try some of these simple commands to
	understand the search problem that is being passed in:

	print "Start:", problem.getStartState()
	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	print "Start's successors:", problem.getSuccessors(problem.getStartState())
	"""
	"*** YOUR CODE HERE ***"
	util.raiseNotDefined()

def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""
	"*** YOUR CODE HERE ***"
	util.raiseNotDefined()

def nullHeuristic(state, problem=None):
	"""
	A heuristic function estimates the cost from the current state to the nearest
	goal in the provided SearchProblem.  This heuristic is trivial.
	"""
	return 0

########################################################################################
""" Busca de Custo Uniforme """

def uniformCostSearch(problem):
	"""Search the node of least total cost first."""
	# Define o nodo como um conjunto contendo o estado inicial, o custo do caminho e a lista de passos percorridos
	nodo = (problem.getStartState(),0,[])  
	# Cria a fila de prioridade 
	fila = util.PriorityQueue()  
	# Insere o nodo e a prioridade definida na fila
	fila.push(nodo,problem)
	nodosExplorados = []
	while True:
	  # Verifica se a fila estar vazia, se estiver encerrar a iteracao
	  if fila.isEmpty(): 
	  	return False
	  estado, custoMeta, caminho = fila.pop() # Desempilha o estado, o custo, e o elemento com a maior prioridade da fila
	  if problem.isGoalState(estado):   # Verifica se estar no estado meta
		  return caminho   # Retorna o caminho do no inicial ate o estado
	  if estado not in nodosExplorados:  
		 nodosExplorados.append(estado) # Adiciona o nodo na lista de nodos explorados
		 sucessores = problem.getSuccessors(estado)
	  # Percorre os filhos do elemento desempilhado 
	  for sucessor, direcao, custoNo in sucessores:
	  	if sucessor not in nodosExplorados:
		  custoCaminho = custoMeta + custoNo
		  # Insere o filho do elemento desempilhado com o menor custo acumulado como prioridade para realizar a expansao
		  fila.push((sucessor,custoCaminho,caminho+[direcao]), custoCaminho)
		  print "Caminho percorrido:\n", caminho
		  print "Numero de estados:\n", len(caminho)
	return caminho
#########################################################################################
""" Busca A* """

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""     
	"""Search the node that has the lowest combined cost and heuristic first."""     
	# Cria a fila de prioridade 
	fila = util.PriorityQueue()  
	# estado inicial do nodo
	nodo = problem.getStartState()
	#incializo a fila com o primeiro nodo 
    fila.push((nodo, 0), heuristic(nodo, problem))
    #todos explorados
    nodosExplorados = []
    #enquanto a fila não estiver vazia fico no laço
    while True:
  		if  fila.isEmpty():
     		return False
     	estado, caminho = fila.pop() # Desempilha o estado atual e o caminho
     	if problem.isGoalState(atual):
        	return caminho
        if estado not in nodosExplorados
        	nodosExplorados.append(estado) # Adiciona o nodo na lista de nodos explorados
         sucessores = problem.getSuccessors(estado)
          # Percorre os filhos do elemento desempilhado 
        for sucessor,direcao in sucessores
        	if sucessor not in nodosExplorados:
        		custovizinho = caminho + [direcao]
        		custoCaminho = problem.getCostOfActions(custovizinho) + heuristic(sucessor, problem)
        		fila.push((sucessor, custovizinho),custoCaminho)
        		print "Caminho percorrido:\n", caminho
		  		print "Numero de estados:\n", len(caminho)
	return caminho

#########################################################################################
""" Busca Tempera Simulada """
def simulatedAnnealingSearch(problem, heuristic=nullHeuristic):

	util.raiseNotDefined()

#########################################################################################	
""" Busca Subida de Encosta """
def hillClimbingSearch(problem):
	
	
	state = problemStartState()
	node = {}
	node["pai"] = None
	node["state"] = state
	node["value"] = 0
	node["way"] = None
	nodosExplorados = []
	fila.push(node, node["value"])

	while not fila.isEmpty():

		#desempilha o nó atual
		node = fila.pop()
		estado = node["state"]
		valor = node["value"]
		caminho = node["way"]

		if problem.isGoalState(estado): #verifica se é o objetivo
		  return caminho  
		if estado not in nodosExplorados:  #verifica se ainda não foi explorado
		 	nodosExplorados.append(estado)

		neighbor = problem.getSuccessors(estado)

		for succ, direcao, value_no in neighbor:
			if succ not in nodosExplorados:

			# cria nó vizinho
			neighbors = {}
		        neighbors["pai"] = node
		        neighbors["state"] = succ
		        neighbors["direcao"] = direcao
		        if value_no > valor: # verifica se o valor do pai é menor que o valor do vizinho
		        	return caminho

		        neighbors["value"] = value_no + valor
		        fila.push(neighbors, neighbors["value"])
			print "Caminho percorrido:\n", caminho
			print "Numero de estados:\n", len(caminho)

	return caminho
	
	#util.raiseNotDefined()

#########################################################################################	

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
sa = simulatedAnnealingSearch
hc = hillClimbingSearch

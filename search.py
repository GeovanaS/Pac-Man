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
import math
import random

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
	# Cria a fila de prioridade 
	fila = util.PriorityQueue()  
	# estado inicial do nodo
	nodo = problem.getStartState()
	#incializo a fila com o primeiro nodo 
    	fila.push((nodo, []), heuristic(nodo, problem))
    	#todos explorados
    	nodosExplorados = []
    	#enquanto a fila nao estiver vazia fico no laco
    	while True:
  		if  fila.isEmpty():
     			return False
     		estado, caminho = fila.pop() # Desempilha o estado atual e o caminho
     		if problem.isGoalState(estado):
        		return caminho
        	if estado not in nodosExplorados:
        		nodosExplorados.append(estado) # Adiciona o nodo na lista de nodos explorados
         	sucessores = problem.getSuccessors(estado)
          	# Percorre os filhos do elemento desempilhado 
        	for sucessor,direcao,custo in sucessores:
        		if sucessor not in nodosExplorados:
        			custovizinho = caminho + [direcao]
        			custoCaminho = problem.getCostOfActions(custovizinho) + heuristic(sucessor, problem)
        			fila.push((sucessor, custovizinho),custoCaminho)
        		print "Caminho percorrido:\n", caminho
		  	print "Numero de estados:\n", len(caminho)
	return caminho

#########################################################################################
""" Busca Tempera Simulada """
def simulatedAnnealingSearch(problem):
	caminho = []
	direcaoNodo = []
	# estado inicial do nodo
	nodo = problem.getStartState()
	#tempo
	t = 1.0
	alfa = 1.5
    #loop infinito porque o algoritmo teorico mostra que deve ser feito um loop de t=1 ate infinto
	while True:
         cont = 0
         # Cria a fila 
    	 fila = util.Queue()
    	 # T = escalonamento(t)
    	 sucessores = problem.getSuccessors(nodo)
    	 for proximo, direcao, cam in sucessores:
    		fila.push((proximo,[direcao]))
    		cont = cont + 1
    	 #escolho um valor randomico de 0 ate a quantidade que ja abri
    	 valorRandom = random.randint(0,cont-1)
    	 if valorRandom > 0:
    		for j in range(0,valorRandom+1):
    			novoEstado,novaAcao = fila.pop()
    	 else:
    	     novoEstado,novaAcao = fila.pop()
    	 e = problem.getCostOfActions(novaAcao) - problem.getCostOfActions(direcaoNodo) 
    	 #e = valor[proximo] - valor[nodo]
    	 if e < 0:
    	      nodo = novoEstado
    	      direcaoNodo = novaAcao
    	      caminho = caminho + direcaoNodo
    	 else:
    	 	#e^e/t 
    	    if math.exp(-e/t):
    	    	nodo = novoEstado
    	    	direcaoNodo = novaAcao
    	    	caminho = caminho + direcaoNodo
    	 if problem.isGoalState(nodo):
    		 return caminho

    	 t = t * alfa
         print "Caminho percorrido:\n",caminho
         print "Numero de estados:\n",len(caminho)

 	return caminho 	
#########################################################################################	
""" Busca Subida de Encosta """
def hillClimbingSearch(problem, heuristic = nullHeuristic):

    custo = 1 # Para a busca funcionar, o pai precisa começar sendo maior.
    custoFilho = 0 
    fila = util.PriorityQueue()
    caminho =[]

    estado = ((estado = problem.getStartState(), []), heuristic(estado, problem))

    while custo > custoFilho:
    	
        fila = util.PriorityQueue()
	custo = heuristic(estado, problem)
	
        if fila.isEmpty():
        	return False
        
        if problem.isGoalState(estado):
           print "Caminho percorrido: ", caminho
           print "Numero de estados: ", len(caminho)           
           return caminho

        sucessores = problem.getSuccessors(estado[0][0])

        for child in sucessores:
            custoCaminho = problem.getCostOfActions([child[1]]) + heuristic(child[0], problem)
            queue.push((child[0], child[1]), custoCaminho)

        estadoProx = queue.pop()
        #calcula o custo do proximo nodo
        custoFilho = problem.getCostOfActions([estadoProx[1]]) + heuristic(estadoProx[0], problem) - 1
    
    #soma o caminho ja percorrido com o proximo
    caminho = caminho + [estadoProx[1]] 
    estado = ((estadoProx[0], estadoProx[1]), custoFilho)

    print "Caminho percorrido: ", caminho
    print "Numero de estados: ", len(caminho)  

    return caminho
	

#########################################################################################	

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
sa = simulatedAnnealingSearch
hc = hillClimbingSearch

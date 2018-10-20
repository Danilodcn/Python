

class Tree:
	def __init__(self, dado, left = None, right = None):
		self.dado = dado
		self.left = left
		self.right = right
		self.pai = None
	
	def __str__(self): return f"Tree: {self.dado}"
	
left = Tree(1, Tree(-1, Tree(0)), Tree(2, Tree(1), Tree(3)))
right = Tree(3, Tree(2), Tree(4))

tree = Tree(2, left, right)

def total(t):	
	if t == None: return 1
	if t.dado == -1: return 0
	else: return total(t.left) + total(t.right)
	
	
print(total(tree) / 2)

def concatena(t):
	if t == None: return ""
	else: return concatena(t.left)+ " " + str(t) + " " + concatena(t.right) 
	
def printTree(tree) :
	if tree == None : return
	print (tree.dado, end = " ")
	printTree(tree.left)
	printTree(tree.right)
  
def printTreeInordem(t, level = 0):
	if t == None: return
	printTreeInordem(t.left, level + 2)
	print("  " * level + str(t.dado))
	printTreeInordem(t.right, level + 2)
 
 
tree1 = Tree("+", Tree(1), Tree("*", Tree(2), Tree(4)))
printTree(tree1)
print("\n")
printTreeInordem(tree)
print("\n")






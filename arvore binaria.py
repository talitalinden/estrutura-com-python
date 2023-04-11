#Arvore Binaria para estrutura de dados.
# Node é o nó que é o elemento raiz. Cada elemento raiz pode ter 2 filhos.
# Um nó sem filhos é chamado de folha.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ArvoreBinaria:
    def __init__(self, root):
        self.root = Node(root)
    
    def print_arvore(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Tipo transversal" + str(traversal_type) + "não é definido.")
            return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print (self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
        return traversal
    
#Para criar uma arvore binaria simples

arvore = ArvoreBinaria(1)
arvore.root.left = Node(2)
arvore.root.right = Node(3)
arvore.root.left.left = Node(4)
arvore.root.right.right = Node(5)

#Imprimindo a arvore binaria

print("Pré ordem: " + arvore.print_arvore("preorder"))
print("Em ordem: " + arvore.print_arvore("inorder"))
print("Pós ordem: " + arvore.print_arvore("postorder"))
            


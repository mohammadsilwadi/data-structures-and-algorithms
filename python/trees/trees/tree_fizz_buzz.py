class Node:
    def __init__(self,value=''):
        self.value = value
        self.children = []

class KTree:
    def __init__(self):
        self.root = None

def fizz_buzz_tree(root):
        if root == None:
            return root
        crruent = root
        data = []
        data.append(crruent)
        while len(data) !=0:
            crruent = data.pop(0)
            if crruent.value % 15==0:
                crruent.value = 'FizzBuzz'
            elif crruent.value % 5 == 0:
                crruent.value = 'Buzz'
            elif crruent.value % 3 == 0:
                crruent.value = 'Fizz'
            else:
                crruent.value = str(crruent.value)
            for node in crruent.children:
                data.append(node)
        return root

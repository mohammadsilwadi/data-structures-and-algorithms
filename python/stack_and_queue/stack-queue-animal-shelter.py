########################
###code challenge 12####
########################
class dog:
    def __init__(self):
        self.name ="dog"
        self.next= None
    def __str__(self):
        return str(self)
class cat:
    def __init__(self):
        self.name = "cat"
        self.next= None
    def __str__(self):
        return str(self)
class AnimalShelter:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self, value):
        if value == 'dog' or value == 'cat':
            if value == 'dog':
                node= dog()
            if value == 'cat':
                node= cat()
            if not self.front:
                self.front=node
                self.rear=node
            else:
                self.rear.next=node
                self.rear=node

        else :
            return('only dog or cat are allowed')
    def dequeue(self, pref):
        if not self.front:
         raise "SomeException"
        elif self.front.name == pref and not self.front.next:
            temp = self.front
            self.front = temp.next
            return temp
        elif self.front.next and (self.front.name != pref):
              current = self.front
              while current.next:
                    if current.next.name == pref:
                        current.next = current.next.next
                        return current
                    current = current.next

if __name__=='__main__':
    shelter = AnimalShelter()
    shelter.enqueue('dog')

    print(shelter.enqueue('dog'))

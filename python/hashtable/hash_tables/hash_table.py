from collections import Counter
import re
class Node:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_

class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)

class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table

        """
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
      """
      Retrieve the most recent value of in oour hasmap for the given key

      :param key str
      :rvalue any
      """
      # calculate index
      index = self.__hash(key)
      # check if there is a non empty bucket at the index
      if self.__buckets[index]:
        # iterate over linked list
        linked_list = self.__buckets[index]
        current = linked_list.head
        while current:
          # check if the key in each node matches
          if current.value[0] == key:
            # return the value of the node with the mathcing key
            return current.value[1]
          current = current.next

      # return None
      return None


    def contains(self,key):
        # calculate index
        index = self.__hash(key)
        if not self.__buckets[index]:
            return False
        linked_list = self.__buckets[index]
        current = linked_list.head
        while current:
          # check if the key in each node matches
          if current.value[0] == key:
            # return the value of the node with the mathcing key
            return True
          current = current.next

    def repeated_word(self,str):
        """
        return first repetend word  in str as string
        """
        if str == "":
         return str
        arr1 = str.split(',')
        arr2 = ' '.join(arr1)
        arr = arr2.split()
        for value in arr:
            repeted_word = value.lower()
            if self.contains(repeted_word):
                return value
            else:
                self.add(repeted_word,value)
def left_join(left_hash, right_hash):

    output = []
    for item in left_hash._HashTable__buckets:
        if item:
            if right_hash.contains(item.head.value[0]):
                right_item = right_hash.get(item.head.value[0])
                output.append([item.head.value[0], item.head.value[1],right_item])
            else:
                output.append([item.head.value[0], item.head.value[1],'Null'])
    return output

if __name__ == "__main__":
    hash1 = HashTable()
    hash1.add('good','fine')

    hash2 = HashTable()
    hash2.add('good','bad')


    
    print(left_join(hash1, hash2))

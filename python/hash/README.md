# Hashtables
<!-- Short summary or background information -->
Hashing is the process of taking a string and converting it into another type of value that can be used to for other purposes like determining the index of an array in the case of a hashtable. When we refer to what is stored or contained in each index of the array, it is called a bucket, and it could contain multiple key/ value pairs in a linked list if a collision occurs, and collisions themselves is what happens when more than one key gets hashed to the same location of the hashtable.
## Challenge
<!-- Description of the challenge -->
- do the implementation of the hash table in python and handle the collision case
- add the hash functions add, remove, contains, and get
- do the testing of the hash table

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O for time is O(1).

Big O for space complexity of O(n)


## API
<!-- Description of each method publicly available in each of your hashtable -->
- add(key, value): adds a key-value pair to the hash table
- contains(key): contains a key in the hash table
- get(key): gets the key from the hash table
- hash(key): hashes the key and return index

## pull request
[PR](https://github.com/mohammadsilwadi/data-structures-and-algorithms/pull/39)

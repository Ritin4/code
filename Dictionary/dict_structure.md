1. Dictionary

A dictionary is a built-in data structure that stores key-value pairs.

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

- Keys are unique and immutable 
- Values are non unique, mutable and can be of any data type

2. Key Properties 

- Dictionaries are mutable i.e you can add, delete amd update the values in a dictionary
- The keys in a dictionary must be unique 
- The dictionary usues hashing mechanism to lookup keys in O(1) complexity
- The items in dictionary are indexed by keys and not with positions like list or array

3. Creatimg Dictionaries

a) Syntax 

    persom = {"mame": "Jason", "age": "5", "grade": "A"}

b) Using 'dict()'

    person = dict(name="John", age=30)

c) Empty dictionary

    persom = {}


4. Aceessing the dictionary 

    - Fetching value using key

        print(person["name"]) # Jason

    - Error occurs when tried to access the non-existing key

        print(person["grade"]) #key error

    - Safe Access
    
        print(person.get("grade"))       #None
        print(person.get("grade"), "A")  #A


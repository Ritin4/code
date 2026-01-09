1. Dictionary

A Dictionary is a built-in data structure that stores key-value pairs.

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

c) Empty Dictionary

    persom = {}


4. Aceessing the Dictionary 

    - Fetching value using key

        print(person["name"]) # Jason

    - Error occurs when tried to access the non-existing key

        print(person["grade"]) #key error

    - Safe Access

        print(person.get("grade"))       #None
        print(person.get("grade"), "A")  #A

5. Adding and updating Dictionary items

    person["city"] = "Hyderabd"  #Add
    person["age"] = 19           #Update

    - In the case of update if the key already exists the value is update,
        if the key is not existing, a new key value pair will be created.

6. Removing Dictionary items

    del person["city"]        #Removes key "city" 
    age = person.pop("age")   #Removes and returns the value 
    person.clear()            #Empties the entire dictionary

7. Looping through Dictionary

    - Looping keys:

            for key in person:
                print(key)
    
    - Looping Values:

            for value in person.values():
                print(value)

    - Looping key-value pairs:
            
            for key, value in person.items():
                print(key, value)

8. Dictionary Core Methods 

     - d.keys()   #Get all the keys
     - d.values() #Get all the values
     - d.items()  #Get all (key-value) pairs
     - d.update() #Merge two dictionaries \
            Ex: 
                d1 = {"a": 1}
                d2 = {"b": 2}
                d1.update(d2)


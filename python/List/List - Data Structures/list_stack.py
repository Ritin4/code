'''
Problem: Implement a stack using a list (push, pop, peek, is_empty).
Input: input to list from user 
Output: stack operations using push, pop, peek, is_empty
'''

def list_stack():
    stack = []

    n = int(input("Enter the number of elements to push initially: "))
    for i in range(n):
        item = input(f"Enter the element {i+1}: ")
        stack.append(item)

    def push(item):
        stack.append(item)

    def pop():
        if is_empty():
            print("Stack is empty. No item to pop.")
        else:
            print(f"Popped: {stack.pop()}")

    def peek():
        if is_empty():
            print("Stack empty. Nothing to peek.")
        else:
            print(f"Top element: {stack[-1]}")

    def is_empty():
        return len(stack) == 0

    
    while True:
        print("\n1. Push\n2. Pop\n3. Peek\n4. Is Empty\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter element to push: ")
            push(item)
        
        elif choice == 2:
            pop()

        elif choice == 3:
            peek()
        
        elif choice == 4:
            if is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")

        elif choice == 5:
            print("Shutting down..")
            break

        else:
            print("Invalid Choice") 

list_stack()

# declare a todos list
todos = []

# while loop for repeated user inputs
while True:
    user_action = input("Type add, show, edit, or exit : ")
    user_action = user_action.strip()
    
    match user_action: # for checking variable value
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo) # method to add todo to the todos list
        
        case 'show':
            for index, item in enumerate(todos) : # for printing todo single by single
                row = f"{index + 1} - {item}"
                print(index,'-', item)
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit : "))
            number = number-1
            new_todo = input("Enter new todo : ")
            todos[number] = new_todo

        case 'complete':
            number = int(input("Number of the todo to edit : "))
            todos.pop(number)

        case 'exit':
            break


print("Bye")
        

    

    
    
    
    



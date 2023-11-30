import functions
import time

now = time.strftime("%b, %d, %Y  %H:%M:%S")

print("it is"+" "+now)

#while loop to run programme until user advises to stop

while True:

#Asking user's choice

    user_choice = input("Type 'add' or 'show' or 'exit' or 'edit' or 'complete' : ")



    #add item
    if user_choice.startswith("add"):
        todo = user_choice[4:]

        #adding  to file
        todos = functions.get_todos()

        todos.append(todo + '\n')

        #adding new items to file without overriding
        functions.write_todos( todos)

    # show the complte todo list
    elif user_choice.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    #to edit the todo list
    elif user_choice.startswith("edit"):
        try:
            index = int(user_choice[5:])
            index = index - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo :")
            todos[index] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            continue

    #to show complete list with indexes
    elif user_choice.startswith("complete"):
        try:
            number = int(user_choice[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"This Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("There is no item with that number")
            continue

    #to end the programme
    elif user_choice.startswith("exit"):
        break

    else:
        print("Sorry you entered wrong command. Please check your input !!!!")

print("Bye...")
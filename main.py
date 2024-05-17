import math
todos = []
#while loop syntax: while variable =  value
# examples 
#while True:
#while False:
while True:
    user_action = input("type add, show, edit or exit: ")
    #strip method removes spaces from user input
    user_action = user_action.strip()
    #switch statement
    match user_action:
        case 'add':
            todo = input("enter a todo")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            index = int(input("chose the index of the todo item you wish to edit"))
            print(todos[index-1])
            new_todo = (input("please enter the new name of the todo item"))
            todos[index-1] = new_todo
        case 'exit':
            break
        case _:
            print('invalid command')

print("goodbye")
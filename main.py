from datetime import datetime
from time import strftime
from functions import *


now = strftime("%Y-%m-%d %H:%M:%S")
print(f"It's now {now}")

while True:
    user_prompt = "Type add, show, edit, complete or exit the todos: "
    user_action = input(user_prompt).strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)


    elif 'show' in user_action or 'display' in user_action:
        todos = get_todos()

        for index, item in enumerate (todos):
            index = index + 1
            item = item.strip('\n')
            # fstring index and item to print in a row format with a dot in between and a space
            row = f"{index}. {item}"
            print(row)


    elif 'edit' in user_action or 'change' in user_action:
        number = int(user_action[5:]) - 1

        todos = get_todos()
        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + "\n"

        write_todos(todos)


    elif 'complete' in user_action or 'done' in user_action:
        todos = get_todos()
        number = int(user_action[9:])
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop( index )
        write_todos(todos)
        message = f"Todo {index} {todo_to_remove} was removed from the list"
        print(message)


    elif 'exit' in user_action or 'quit' in user_action:
        break
    else:
        print("Command not valid, please enter 'add,show,edit,complete or exit'")

print("Bye!")


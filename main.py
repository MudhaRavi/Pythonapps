# Function to get todos from a file
def get_todos(file_path): #param file_path
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(file_path, todos_arg):
    with open(file_path, "w") as file:
        file.writelines(todos_arg)


while True:
    user_prompt = "Type add, show, edit, complete or exit the todos: "
    user_action = input(user_prompt).strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        todos = get_todos(file_path="todos.txt")
        todos.append(todo + "\n")
        write_todos("todos.txt", todos)

    elif 'show' in user_action or 'display' in user_action:
        todos = get_todos("todos.txt")

        for index, item in enumerate (todos):
            index = index + 1
            item = item.strip('\n')
            # fstring index and item to print in a row format with a dot in between and a space
            row = f"{index}. {item}"
            print(row)

    elif 'edit' in user_action or 'change' in user_action:
        number = int(user_action[5:]) - 1

        todos = get_todos("todos.txt")
        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + "\n"

        write_todos("todos.txt", todos)

    elif 'complete' in user_action or 'done' in user_action:
        todos = get_todos("todos.txt")
        number = int(user_action[9:])
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop( index )
        write_todos("todos.txt", todos)
        message = f"Todo {index} {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action or 'quit' in user_action:
        break
    else:
        print("Command not valid, please enter 'add,show,edit,complete or exit'")

print("Bye!")


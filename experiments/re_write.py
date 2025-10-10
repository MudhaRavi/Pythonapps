
while True:
    user_prompt = "Type add, show, edit, complete or exit the todos: "
    user_action = input(user_prompt).strip()

    if 'add' in user_action:
        todo = user_action[4:] + "\n"

        with open("test.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("test.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open("test.txt", "r") as file:
            todos = file.readlines()

            for index, item in enumerate(todos):
                index = index + 1
                item = item.strip()
                row = f"{index}-{item}"
                print(row)

    elif 'edit' in user_action:
         with open("test.txt", "r") as file:
             todos = file.readlines()
         number = int(user_action[4:])
         new_todo = input("Enter a new todo: ")
         todos[number] = new_todo + "\n"
         with open("test.txt", "w") as file:
                file.writelines(todos)

    elif 'complete' in user_action:
        with open("test.txt", "r") as file:
            todos = file.readlines()
            number = int(user_action[9:])
            index = number - 1
            removed_todo = todos[index] .strip('\n')
            todos.pop(index)
        with open("test.txt", "w") as file:
            file.writelines(todos)
        message = f"Todo {index} {removed_todo} was removed from the list"
        print(message)
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")
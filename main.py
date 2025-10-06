
while True:
    user_prompt = "Type add, show, edit, complete or exit the todos: "
    user_action = input(user_prompt).strip()

    match user_action :
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with  open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with  open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate (todos):
                index = index + 1
                item = item.strip('\n')
                # fstring index and item to print in a row format with a dot in between and a space
                row = f"{index}. {item}"
                print(row)

        case "edit":

            number = int(input("Enter a number: "))
            number = number - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            new_todos = input("Enter a new todo: ")
            todos[number] = new_todos + "\n"
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "complete":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            number = int(input("Enter a number to complete: "))
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            print(todo_to_remove)
            todos[index] = todo_to_remove
            todos.pop( index )
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            message = f"Todo {index} {todo_to_remove} was removed from the list"
            print(message)

        case "exit":
            break

print("Bye!")


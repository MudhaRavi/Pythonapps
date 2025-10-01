
while True:
    user_prompt = "Type add, show, edit, complete or exit the todos: "
    user_action = input(user_prompt).strip()

    match user_action :
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate (todos):
                index = index + 1
                item = item.strip('\n')
                row = f"{index}. {item}"
                print(row)

        case "edit":
            number = int(input("Enter a number: ")) -1
            #existing_todo = todos[number - 1] # -1 to convert to 0-based index
            new_todo = input("Enter a new todo: ").strip()
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter a number to complete: "))
            todos.pop(number - 1 )

        case "exit":
            break

print("Bye!")





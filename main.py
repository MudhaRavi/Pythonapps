user_prompt = "Type add, show, edit, complete or exit the todos: "

todos= []

while True:
    user_action = input(user_prompt).strip()

    match user_action :
        case "add":
            todo = input("Enter a todo: ")
            todo = todo.strip()
            todos.append(todo)
        case "show":
            for index, item in enumerate (todos):
                index = index + 1
                item = item.title()
                row = f"{index}. {item}"
                print(row)
        case "edit":
            number = int(input("Enter a number: "))-1
            #existing_todo = todos[number - 1] # -1 to convert to 0-based index
            new_todo = input("Enter a new todo: ").strip()
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter a number to complete: "))
            todos.pop(number - 1 )

        case "exit":
            break

print("Bye!")





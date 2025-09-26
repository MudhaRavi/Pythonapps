user_prompt = "Type add the todo or show the todos: "

todos= []

while True:
    user_action = input(user_prompt).strip()

    match user_action :
        case "add":
            todo = input("Enter a todo: ").strip()
            todos.append(todo)
        case "show":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break



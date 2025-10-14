# user_prompt = " Enter your prompt: "
# todo_list = []
#
# while True:
#
#     todo = input(user_prompt)
#     todo_list.append(todo)
#     if todo == "exit":
#         break
# print(f"Todo: {todo_list}")


def liters_to_m3(liters):
    cubic = liters/1000
    return cubic

print(liters_to_m3(5))  # Example usage

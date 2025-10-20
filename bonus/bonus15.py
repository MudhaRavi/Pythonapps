import json

with open( "questions.json" , "r") as f:
    data = json.load(f)


score=0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternates"]):
        index = index + 1
        print(f"{index}- {alternative}")
    answer = int(input("Your answer: "))
    question["user_choice"] = answer

for  question in data:
    if question["user_choice"] == question["correct_answer"]:
        score= score + 1
        result="Correct Answer !"
    else:
        result="Wrong Answer !"
    message = f"{result} Your answer: {question["user_choice"]}, Correct answer: {question["correct_answer"]}"
    print(message)

print(f"Your final score is: {score} out of {len(data)}")

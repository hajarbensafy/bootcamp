data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def quiz():
    correct = 0
    incorrect = 0
    wrong_answers = []

    for item in data:
        user_answer = input(item["question"] + " ")
        if user_answer.lower() == item["answer"].lower():
            correct += 1
        else:
            incorrect += 1
            wrong_answers.append({
                "question": item["question"],
                "user_answer": user_answer,
                "correct_answer": item["answer"]
            })

    print(f"\nYou got {correct} correct and {incorrect} incorrect answers.")

    if wrong_answers:
        print("\nHere are the questions you answered wrong:")
        for wrong in wrong_answers:
            print(f"Question: {wrong['question']}")
            print(f"Your answer: {wrong['user_answer']}")
            print(f"Correct answer: {wrong['correct_answer']}\n")

    if incorrect > 3:
        print("You had more than 3 wrong answers. Would you like to play again?")
        if input("Type 'yes' to play again: ").lower() == "yes":
            quiz()

quiz()
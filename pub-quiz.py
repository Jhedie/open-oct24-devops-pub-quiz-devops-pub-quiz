# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["A) K2", "B) Kangchenjunga", "C) Mount Everest", "D) Lhotse"],
        "answer": "C",
        "type" : "multiple-choice"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) William Shakespeare", "B) Charles Dickens", "C) J.K. Rowling", "D) Mark Twain"],
        "answer": "A",
        "type" : "multiple-choice"

    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"],
        "answer": "A",
        "type" : "multiple-choice"

    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["A) China", "B) Japan", "C) South Korea", "D) Thailand"],
        "answer": "B",
        "type" : "multiple-choice"

    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D",
        "type" : "multiple-choice"

    },
    {
        "question": "Can you guess the word from the anagram below?",
        "options": ["weets"],
        "answer": "sweet",
        "type" : "non-multiple-choice"

    },
]

user_points = 0
total_points = len(quiz_questions) * 10

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    if question["type"] == "multiple-choice":
        user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    else:
        user_answer = input("Please enter your answer: ").strip().lower()
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        user_points += 10
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")
    print("You currently have " + str(user_points) + " points")
# Goodbye message
print("Thanks for playing the Pub Quiz!")
print("You scored " + str(user_points) + "/" + str(total_points) + " points")

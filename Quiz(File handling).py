import random

# Step 1: Create a file with quiz questions
questions_file = "quiz_questions.txt"
responses_file = "user_responses.txt"

# Sample quiz questions
quiz_questions = [
    "What is the output of `print(2**3)`?\nA) 6\nB) 8\nC) 9\nD) 4\nAnswer: B",
    "Which of these is a mutable data type in Python?\nA) Tuple\nB) List\nC) String\nD) Set\nAnswer: B",
    "What is the correct file extension for Python files?\nA) .py\nB) .python\nC) .pt\nD) .txt\nAnswer: A",
    "Which keyword is used to define a function in Python?\nA) func\nB) def\nC) function\nD) define\nAnswer: B",
    "How do you insert comments in Python code?\nA) //\nB) <!-- -->\nC) #\nD) /**/\nAnswer: C"
]

# Write questions to a file
with open(questions_file, "w") as file:
    for question in quiz_questions:
        file.write(question + "\n\n")

# Step 2: Read questions and present the quiz
def conduct_quiz():
    # Load questions from the file
    with open(questions_file, "r") as file:
        questions = file.read().strip().split("\n\n")
        print(questions)
    
    # Randomly select 5 questions
    random_questions = random.sample(questions, 5)
    
    # Prepare to save user responses
    with open(responses_file, "w") as response_file:
        response_file.write("User Responses:\n\n")
        
        score = 0
        for i, question in enumerate(random_questions, 1):
            print(f"Question {i}:\n{question.split('Answer:')[0].strip()}")
            answer = input("Your Answer (A/B/C/D): ").strip().upper()
            
            # Write response to file
            response_file.write(f"Question {i}: {question.split('Answer:')[0].strip()}\n")
            response_file.write(f"Your Answer: {answer}\n\n")
            
            # Check answer
            correct_answer = question.split('Answer:')[1].strip()
            if answer == correct_answer:
                score += 1
        
        response_file.write(f"Total Score: {score}/5\n")
        print(f"\nYour Total Score: {score}/5")

# Run the quiz
conduct_quiz()

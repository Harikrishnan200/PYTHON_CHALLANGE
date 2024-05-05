import random

#There are 3 set of questions
question_sets = [
    {
        "questions": [
            {"question": "What is 2+2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
            {"question": "Who is the author of 'To Kill a Mockingbird'?", "options": ["Harper Lee", "J.K. Rowling", "Stephen King", "Charles Dickens"], "answer": "Harper Lee"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"},
            {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"}
        ]
    },
    {
        "questions": [
            {"question": "What is the capital of Japan?", "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"], "answer": "Tokyo"},
            {"question": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], "answer": "Leonardo da Vinci"},
            {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Fe", "Pb"], "answer": "Au"},
            {"question": "What is the tallest mammal?", "options": ["Giraffe", "Elephant", "Horse", "Rhino"], "answer": "Giraffe"},
            {"question": "Which is the largest organ in the human body?", "options": ["Liver", "Skin", "Heart", "Brain"], "answer": "Skin"}
        ]
    },
    {
        "questions": [
            {"question": "Who invented the telephone?", "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"], "answer": "Alexander Graham Bell"},
            {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "NaCl", "O2"], "answer": "H2O"},
            {"question": "Which planet is known as the 'Morning Star' or 'Evening Star'?", "options": ["Mercury", "Venus", "Mars", "Jupiter"], "answer": "Venus"},
            {"question": "What is the currency of Germany?", "options": ["Euro", "Dollar", "Pound", "Yen"], "answer": "Euro"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "answer": "William Shakespeare"}
        ]
    }
]

def quiz():
    random_set = random.choice(question_sets) #randomly select a set of questions
    random_questions = random.sample(random_set["questions"], 5) #randomly select 5 questions from the set

    for index, question in enumerate(random_questions, start=1):
        print(f"Question {index}: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the option number): ").strip()
        correct_answer = question['answer']
        if user_answer == str(question['options'].index(correct_answer) + 1):
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer}")


quiz()


'''  
output

Question 1: What is the tallest mammal?
1. Giraffe
2. Elephant
3. Horse
4. Rhino
Your answer (enter the option number): 1
Correct!
Question 2: What is the chemical symbol for gold?
1. Au
2. Ag
3. Fe
4. Pb
Your answer (enter the option number): 2
Wrong! The correct answer is Au
Question 3: Who painted the Mona Lisa?
1. Vincent van Gogh
2. Leonardo da Vinci
3. Pablo Picasso
4. Michelangelo
Your answer (enter the option number): 2
Correct!
Question 4: What is the capital of Japan?
1. Tokyo
2. Beijing
3. Seoul
4. Bangkok
Your answer (enter the option number): 1
Correct!
Question 5: Which is the largest organ in the human body?
1. Liver
2. Skin
3. Heart
4. Brain
Your answer (enter the option number): 1
Wrong! The correct answer is Skin
'''
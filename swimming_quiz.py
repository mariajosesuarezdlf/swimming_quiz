print("==============================")
print("      Are You a Real Swimmer?")
print("==============================\n")

# Class to represent each quiz question
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Class to run the quiz game
class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run_quiz(self):
        for question in self.questions:
            print(question.prompt)
            user_answer = input("Enter your answer (A, B, C, or D): ").upper()

            if user_answer == question.answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.answer}\n")

    def save_score(self, name):
        with open("scores.txt", "a") as file:
            file.write(f"{name}: {self.score}/{len(self.questions)}\n")

def main():
    # Create quiz game
    quiz = QuizGame()

    # Define questions
    q1 = Question("What is the length of an Olympic swimming pool?\nA) 25 meters\nB) 50 meters\nC) 75 meters\nD) 100 meters", "B")
    q2 = Question("Which stroke is the fastest?\nA) Breaststroke\nB) Butterfly\nC) Freestyle\nD) Backstroke", "C")
    q3 = Question("How many lanes are there in an Olympic swimming pool?\nA) 6\nB) 8\nC) 10\nD) 12", "C")
    q4 = Question("What stroke requires two-hand touch at turns and finish?\nA) Freestyle\nB) Backstroke\nC) Butterfly and Breaststroke\nD) None", "C")
    q5 = Question("Who is the most decorated Olympian swimmer?\nA) Michael Phelps\nB) Ian Thorpe\nC) Katie Ledecky\nD) Ryan Lochte", "A")

    # Add questions to quiz
    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    quiz.add_question(q4)
    quiz.add_question(q5)

    # Start quiz
    name = input("Enter your name: ")
    quiz.run_quiz()
    print(f"You got {quiz.score} out of {len(quiz.questions)} correct!")

    # Save score
    quiz.save_score(name)
    print("Your score has been saved.\nThank you for playing!")

if __name__ == "__main__":
    main()

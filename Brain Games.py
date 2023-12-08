#We randomly select a madlib for the user
import random

#Word list for Word Guessing Game
def load_word_list():
    file_path = "Brain Games Word List.txt"
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

#10 madlib story structures to be called
def madlib_1():
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adv = input("Enter an adverb: ")
    verb2 = input("Enter another verb: ")
    noun2 = input("Enter another noun: ")

    madlib_story = f"Once upon a time in a {adj1} land, there was a {adj2} {noun1}. " \
            f"This {noun1} loved to {verb1} {adv} every day. One day, it decided to " \
            f"{verb2} a magical {noun2}. And that's how the {adj1} land became even more {adj2}!"

    print(madlib_story)

def madlib_2():
    animal = input("Enter an animal: ")
    verb1 = input("Enter a verb: ")
    adv = input("Enter an adverb: ")
    adj1 = input("Enter an adjective: ")
    verb2 = input("Enter another verb: ")
    noun = input("Enter a noun: ")
    adj2 = input("Enter another adjective: ")

    madlib_story = f"The {animal} decided to {verb1} {adv} in the {adj1} {noun}. " \
            f"Suddenly, it started to {verb2} and became the most {adj2} {animal} ever seen!"

    print(madlib_story)

def madlib_3():
    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adv = input("Enter an adverb: ")
    adj2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")

    madlib_story = f"In a {adj1} {noun1}, a {verb1} {adv} looked at the {adj2} {noun2}. " \
                    f"Suddenly, it started to {verb2}! What a {adj1} and {adj2} sight!"

    print(madlib_story)

def madlib_4():
    color = input("Enter a color: ")
    food = input("Enter a type of food: ")
    emotion = input("Enter an emotion: ")
    verb = input("Enter a verb: ")
    adj1 = input("Enter an adjective: ")
    noun = input("Enter a plural noun: ")
    adj2 = input("Enter another adjective: ")

    madlib_story = f"In a {color} world, a {food} decided to {verb} {adj1}. " \
                    f"The {noun} were feeling very {emotion}, and everyone became {adj2}!"

    print(madlib_story)

def madlib_5():
    verb = input("Enter a verb: ")
    adj1 = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    adj2 = input("Enter another adjective: ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")
    verb2 = input("Enter another verb: ")

    madlib_story = f"To {verb} the {adj1} {noun}, you must be very {adj2}. " \
                    f"If you do it in {place}, you'll feel so {emotion} that you might {verb2}!"

    print(madlib_story)

def madlib_6():
    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adv = input("Enter an adverb: ")
    adj2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")

    madlib_story = f"In a {adj1} {noun1}, someone decided to {verb} {adv}. " \
                    f"Out of nowhere, a {adj2} {noun2} appeared and started to {verb2}!"

    print(madlib_story)

def madlib_7():
    adj1 = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adj2 = input("Enter another adjective: ")
    place = input("Enter a place: ")
    verb2 = input("Enter another verb: ")
    noun2 = input("Enter another noun: ")

    madlib_story = f"The {adj1} {noun} decided to {verb} in the {adj2} {place}. " \
                    f"Suddenly, it started to {verb2} and transformed into a {noun2}!"

    print(madlib_story)

def madlib_8():
    adj = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adj2 = input("Enter another adjective: ")
    food = input("Enter a type of food: ")
    emotion = input("Enter an emotion: ")
    verb2 = input("Enter another verb: ")

    madlib_story = f"A {adj} {noun1} decided to {verb} very {adj2}. " \
                    f"It started to {verb2} and everyone felt so {emotion} that they craved {food}!"

    print(madlib_story)

def madlib_9():
    verb = input("Enter a verb: ")
    adj1 = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    adj2 = input("Enter another adjective: ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")
    verb2 = input("Enter another verb: ")

    madlib_story = f"To {verb} the {adj1} {noun}, you must be very {adj2}. " \
                    f"If you do it in {place}, you'll feel so {emotion} that you might {verb2}!"

    print(madlib_story)

def madlib_10():
    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adv = input("Enter an adverb: ")
    adj2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")

    madlib_story = f"In a {adj1} {noun1}, someone decided to {verb1} {adv}. " \
                    f"Out of nowhere, a {adj2} {noun2} appeared and started to {verb2}!"

    print(madlib_story)    

#main calls this, which then calls a random madlib
def generate_random_madlib():
    madlib_functions = [madlib_1, madlib_2, madlib_3, madlib_4, madlib_5, 
                        madlib_6, madlib_7, madlib_8, madlib_9, madlib_10]
    selected_madlib = random.choice(madlib_functions)
    selected_madlib()

#main calls this, which then calls for a random word from .txt
def word_guessing_game(word_list):
    word_to_guess = random.choice(word_list)
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("Can you guess the word?")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in word_to_guess:
                print("Good guess!")
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                        guessed_word[i] = guess
            else:
                print("Incorrect guess. Try again.")
                attempts -= 1

            print("Attempts left:", attempts)
            print(" ".join(guessed_word))

            if "_" not in guessed_word:
                print("Congratulations! You guessed the word:", word_to_guess)
                break
        else:
            print("Invalid input. Please enter a single letter.")

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word_to_guess)

#trivia game function + its questions
def trivia_game(questions, num_questions=10):
    score = 0
    random.shuffle(questions)

    for i, (question, choices, correct_answer) in enumerate(questions[:num_questions], start=1):
        user_answer = ask_question(question, choices)
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            user_answer = int(user_answer)
            if choices[user_answer - 1] == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}\n")
        else:
            print("Invalid input. Please enter a number between 1 and 4.\n")

    print(f"Your final score is: {score} out of 10")
    return score

def ask_question(question, choices):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    user_answer = input("Enter the number of your answer (1-4): ")
    return user_answer

questions = [
    ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Perth"], "Canberra"),
    ("Which planet is known as the 'Red Planet'?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),
    ("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale"),
    ("In what year did the Titanic sink?", ["1905", "1912", "1920", "1931"], "1912"),
    ("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Emily Brontë"], "William Shakespeare"),
    ("What is the chemical symbol for gold?", ["Au", "Ag", "Fe", "Cu"], "Au"),
    ("Which ocean is the largest?", ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"], "Pacific Ocean"),
    ("How many continents are there?", ["5", "6", "7", "8"], "7"),
    ("What is the capital of Japan?", ["Beijing", "Seoul", "Tokyo", "Bangkok"], "Tokyo"),
    ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "Leonardo da Vinci"),
    ("Which planet is known as the 'Morning Star'?", ["Earth", "Mars", "Venus", "Jupiter"], "Venus"),
    ("Who was the first woman to win a Nobel Prize?", ["Marie Curie", "Ada Lovelace", "Jane Goodall", "Rosalind Franklin"], "Marie Curie"),
    ("What is the largest organ in the human body?", ["Heart", "Brain", "Liver", "Skin"], "Skin"),
    ("In which year did World War II end?", ["1943", "1945", "1950", "1960"], "1945"),
    ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "George Orwell"], "Harper Lee"),
    ("What is the capital of Brazil?", ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "Brasília"),
    ("Which element has the chemical symbol 'O'?", ["Osmium", "Oxygen", "Gold", "Iron"], "Oxygen"),
    ("How many bones are in the adult human body?", ["206", "214", "230", "248"], "206"),
    ("What is the world's largest desert?", ["Sahara Desert", "Arctic Desert", "Antarctic Desert", "Gobi Desert"], "Antarctic Desert"),
    ("Who invented the telephone?", ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Michael Faraday"], "Alexander Graham Bell"),
    ("What is the largest ocean mammal?", ["Dolphin", "Whale Shark", "Narwhal", "Blue Whale"], "Blue Whale"),
    ("In what year did the Berlin Wall fall?", ["1985", "1989", "1991", "1995"], "1989"),
    ("Who wrote '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "F. Scott Fitzgerald"], "George Orwell"),
    ("What is the currency of Japan?", ["Yuan", "Euro", "Yen", "Dollar"], "Yen"),
    ("Which famous scientist developed the theory of general relativity?", ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"], "Albert Einstein"),
    ("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
    ("In what year did the first manned moon landing occur?", ["1965", "1969", "1972", "1975"], "1969"),
    ("Who is known as the 'Father of Computer Science'?", ["Ada Lovelace", "Alan Turing", "Charles Babbage", "Bill Gates"], "Alan Turing"),
    ("What is the smallest prime number?", ["0", "1", "2", "3"], "2"),
    ("Which famous artist painted the 'Starry Night'?", ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci"], "Vincent van Gogh"),
]

#Welcome user. Then offer madlib, word guess, trivia, or exit
def main():
    word_list = load_word_list()
    
    while True:
        print("Welcome to the Brain Teaser App!")
        print("Please select one of the following:")
        print("1. Mad Libs")
        print("2. Word Guessing")
        print("3. Trvia") 
        print("4. Exit the application")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            generate_random_madlib()
        elif choice == "2":
            word_guessing_game(word_list)
        elif choice == "3":
            trivia_game(questions, num_questions=10)
        elif choice == "4":
            print("Exiting the Word Games app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter either 1, 2, or 3.")
            print("Quinn - So help me God if you use recursion to crash another app")

if __name__ == "__main__":
    main()


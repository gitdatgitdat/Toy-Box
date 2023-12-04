#We randomly select a madlib for the user
import random

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
def generate_random_mad_lib():
    madlib_functions = [madlib_1, madlib_2, madlib_3, madlib_4, madlib_5, 
                        madlib_6, madlib_7, madlib_8, madlib_9, madlib_10]
    selected_madlib = random.choice(madlib_functions)
    selected_madlib()

#Welcome user, offer madlib, offer to exit
def main():
    while True:
        print("Welcome to the Random Mad Libs App!")
        print("1 - Get a Random Mad Lib")
        print("2 - Exit the application")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            generate_random_mad_lib()
        elif choice == "2":
            print("Exiting Mad Libs app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter either 1 or 2.")
            print("Quinn - So help me God if you use recursion to crash another app")

if __name__ == "__main__":
    main()


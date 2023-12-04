
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

def main():
    while True:
        print("Welcome!")
        print("Please choose a Mad Lib to complete:")
        print()
        print("1. Mad Lib 1")
        print("2. Mad Lib 2")
        print("3. Mad Lib 3")
        print("4. Quit")
        print()
        print("Or if you are a dirty, dirty quitter")
        print("press enter 4 to exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            madlib_1()
        elif choice == "2":
            madlib_2()
        elif choice == "3":
            madlib_3()
        elif choice == "4":
                print("Exiting Mad Libs app. Goodbye!")
                break
        else:
            print("Invalid choice. Please enter a number between 1, 2, or 3.")
            print("Quinn - So help me God if you use recursion to crash another app")

if __name__ == "__main__":
    main()
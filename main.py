# HangMan Game
from WordsList import words
import random

hangman_art = { 0:("    ",
                   "    ",
                   "    ",),

                1:("  O  ",
                   "    ",
                   "    ",),

                2:("  O  ",
                   "  |  ",
                   "    ",),

                3:("  O  ",
                   " /|  ",
                   "    ",),

                4:("  O  ",
                   " /|\\ "
                   "     ",
                   "     ",),

                5:("  O  ",
                   " /|\\ ",
                   " /   ",),

                6:("  O  ",
                   " /|\\ ",
                   " / \\ ",),
}

def display_man(wrong_guesses):
    print("HANGMAN")
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answers(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint=['_']*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running = True


    while is_running :
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if (len(guess) != 1 or not guess.isalpha()):
            print("Please enter a single letter/ invalid character")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter {guess}")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        
        if "_" not in hint:
            print("You win!")
            display_answers(answer)
            is_running = False
        elif wrong_guesses == 6:
            print("You lose!")
            print(f"The Correct Answer is {" ".join(answer)}")
            is_running = False
                
if __name__ == '__main__':
    main()
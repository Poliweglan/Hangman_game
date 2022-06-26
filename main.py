from HANGMAN_PRINTS import HANGMAN, ALIVE
from random import choice
import csv
import os
from time import sleep


def clear_console():
    os.system("cls")


def get_word_from_file(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file)
        return choice(list(reader))[0].upper()


def get_blanks(word, used_letter):
    blank = []
    for letter in word:
        if letter in used_letter:
            blank.append(letter)
        else:
            blank.append("_")
    return ' '.join(blank)


def get_used_letters(sets):
    if len(sets) == 0:
        return ''
    return str(sets)[1:-1]


def get_stats(lives, used_letters):
    print(f"Lives: {lives}, Used letters: {get_used_letters(used_letters)}")


def start_game():
    # VARIABLE
    word = get_word_from_file("words.csv")
    set_word = {letter for letter in word}
    used_letters = set()
    lives = 7

    # THE GAME
    stop_game = False
    while not stop_game:
        clear_console()

        if lives >= 1:
            print(HANGMAN[-lives - 1])
            print(get_blanks(word, used_letters))
            print()
            get_stats(lives, used_letters)
            letter_input = (input("\nGive me letter: ")).upper()

            if len(letter_input) == 1:
                if letter_input in used_letters:
                    print("YOU ALREADY USED THAT LETTER!")
                    sleep(1)

                if letter_input in set_word:
                    used_letters.add(letter_input)

                    if used_letters & set_word == set_word:
                        clear_console()
                        print(ALIVE)
                        print("\nYOU ALIVE!!! WIN GAME!!!")
                        print(f"\nWord: {get_blanks(word, used_letters)}")
                        stop_game = True
                        print("\nEnd in 5 sec")
                        sleep(5)
                else:
                    lives -= 1
                    used_letters.add(letter_input)

            elif len(letter_input) > 1:
                print("PLEASE GIVE ONY ONE LETTER!")
                sleep(1)
            else:
                print("YOU MUST GIVE ANY ONE LETTER!")
                sleep(1)
        else:
            print(HANGMAN[-lives - 1])
            get_stats(lives, used_letters)
            print("\nGAME OVER!!!\nYOU DEAD!!!")
            print(f"\nThe word searched was: {word}")
            stop_game = True
            print("\nEnd in 5 sec")
            sleep(5)


def main():
    start_game()
    stop = False

    while not stop:
        clear_console()
        print("Do you want to play again?")
        user_answer = (input("YES or NO: ")).lower()

        if user_answer == '':
            print("you must write YES or NO!!!")
            sleep(1)
        elif user_answer[0] == 'y':
            start_game()
        elif user_answer[0] == 'n':
            clear_console()
            print("Thanks for play!\nExit in 1 sec")
            sleep(1)
            stop = True
        else:
            print("you must write YES or NO!!!")
            sleep(1)


if __name__ == "__main__":
    main()

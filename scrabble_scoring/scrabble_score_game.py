from scrabble_score_function import *
from opening_and_writing_files import *

overwrite_file("scrabble_scores.txt", "New Game:\n")

user1_total_score = 0
user2_total_score = 0
game_over = False

while game_over == False:
    user1_word = input("Player 1: please input your word here:").upper()
    user2_word = input("Player 2: please input your word here:").upper()

    user1_score = scrabble_score(user1_word)
    user2_score = scrabble_score(user2_word)

    user1_total_score += user1_score
    user2_total_score += user2_score

    write_to_file("scrabble_scores.txt", f"1. {user1_word}: {user1_score}")
    write_to_file("scrabble_scores.txt", f"2. {user2_word}: {user2_score}")



    game_over_query = input("Do you want to continue playing: Yes or No?").capitalize()
    if game_over_query == "No":
        if user1_total_score > user2_total_score:
            write_to_file("scrabble_scores.txt", "Player 1 wins!")
        elif user2_total_score > user1_total_score:
            write_to_file("scrabble_scores.txt", "Player 2 wins!")
        else:
            write_to_file("scrabble_scores.txt", "Draw!")
        game_over = True

open_and_print_file("scrabble_scores.txt")
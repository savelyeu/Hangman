import random

from images import logo
print(logo)
print("HUĹNIA Ŭ SLOVY")

from list_of_words import level
chosen_word = random.choice(level)

display = []
word_lenght = len(chosen_word)

lives = 6

for _ in range(word_lenght) :
    display += "_"
print(display)

end_of_game = False

while not end_of_game :
    users_letter = input("Adhadaj litaru:\n")

    if users_letter in display:
        print(f"Ty ŭžo vybraŭ litaru {users_letter}")

    for position in range(word_lenght) :
        letter = chosen_word[position]
        if letter == users_letter :
            display[position] = letter

    if users_letter not in chosen_word:
        print(f"Niama litary {users_letter}.Ratunku!")
        lives -= 1
        if lives == 0 :
            end_of_game = True
        print("Byvaj,och!")
        print(f"Heta bylo slova: {chosen_word}")

    print(display)

    if "_" not in display :
        end_of_game = True
        print("TVAJA PIERAMOHA!")
        
    from images import stages
    print(stages[lives])
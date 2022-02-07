import random
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
lives = 6
display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)
while True:
    guess = input("guess the letter ").lower()
    if not guess:
        break
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("you lose")
            break
    print(f"lives left: {lives}")
    print(f"{' '.join(display)}")

    if "_" not in display:
        print("you win")
        break

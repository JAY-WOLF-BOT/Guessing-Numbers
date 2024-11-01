print("!!!!Welcome to then guess game!!!!")
print("------------- ENJOY---------------")

secret = 53
guess_count = 0
guess_limit = 3


while True:
    guess_count = guess_count + 1
    
    guess = int(input("Guess any of the right numbers: "))

    if guess == secret:
        print("--WELL DONE--")
    else:
        print("TRY AGAIN")

    if guess_count == guess_limit:
        print("!!!GAMEOVER!!!")
    

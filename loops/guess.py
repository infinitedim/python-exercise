from mimetypes import guess_all_extensions


secret_number = 5
guess_count = 1
guess_limit = 3

while guess_count <= guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break

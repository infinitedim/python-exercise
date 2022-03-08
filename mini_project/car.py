command = ""
started = False


while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car Already started")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car Already stopped")
        else:
            started = False
            print("Car Stoped")
    elif command == "help":
        messege = """
help - to get a help
start - to start the car
stop - to stop the car
quit - to quit the program
        """
        print(messege)
    elif command == "quit":
        break
    else:
        print("Sorry we don't understand that")

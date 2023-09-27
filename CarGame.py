command = ""
started = False
print("Type in your command. If you need support, type 'help' in the terminal.")
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to sart the car
stop - to stop the car
quit - to quit """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.")
        
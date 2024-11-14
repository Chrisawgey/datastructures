def main():
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))

    myNumber = int(input("Enter the secret number: "))
    print("myNumber", myNumber)
    count = 0
    while True:
        count += 1
        print("count", count)
        userNumber = int(input("Enter your guess: ")) 
        if userNumber < myNumber:
            print(userNumber, "<", myNumber)
            print("Too small")
        elif userNumber > myNumber:
            print(userNumber, ">", myNumber)
            print("Too large")
        else:
            print("You've got it in", count, "tries")
            break
if __name__ == "__main__":
    main()

    
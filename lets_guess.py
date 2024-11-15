"""
    This project takes 10 guesses for a 3-digit number.
    Returns 'Try Again' if none of the numbers are correct
    Returns 'Try Better' if a number is in the wrong position
    Returns 'Getting Cool' if a number is in the correct position
"""

the_number = 269


def check_number_index(num, index):
    return str(the_number)[index] == num


def main():
    guess_count = 0
    win = False
    guess = input("Guess the 3-digit number: ")
    # CHECK USER INPUT is clean
    while True:
        try:
            int(guess)
        except ValueError:
            print("That is not a number")
            guess = input("Guess the 3-digit number: ")
        else:
            if len(guess) != 3:
                print("That is not three digits")
                guess = input("Guess the 3-digit number: ")
            else:
                break

    while guess_count < 10:
        # update/increment guess_count
        guess_count += 1
        feedback = None
        # check if guess is correct
        if int(guess) == the_number:
            print("Perfect!")
            win = True
            break
        # loop through guess digits for correct index or existence
        for i in range(0, len(guess)):
            a_digit = guess[i]
            in_index = check_number_index(a_digit, i)
            if in_index is True:
                feedback = 'Getting Cool'
            # checking if feedback has been correct in the previous
            # so that the user knows that he/she was correct at some point
            # printing 'Try better' when a digit is correct confuses the user
            elif a_digit in str(the_number) and feedback is None:
                print(a_digit)
                feedback = 'Try Better'
        if feedback is None:
            feedback = 'Try Again'
        print(f'{feedback}. {10-guess_count} more tries')
        guess = input("Take Another Guess: ")
    if win is False:
        print("Sorry, you lost")


if __name__ == '__main__':
    main()

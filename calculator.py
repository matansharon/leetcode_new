
import random

def main():
    while True:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print("The two numbers are:", num1, num2)
        print('Guess the multiplication of the two numbers or enter "q" to quit:')
        
        user_input = input()
        
        if user_input.lower() == "q":
            print("Goodbye!")
            break
        
        try:
            guess = int(user_input)
            if guess == num1 * num2:
                print('Correct')
            else:
                print('Wrong, the answer is:', num1 * num2)
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")

if __name__ == "__main__":
    main()


# import random

# def main():
#     while True:
#         num1 = random.randint(1, 100)
#         num2 = random.randint(1, 100)
#         print("The two numbers are:", num1, num2)
#         print('Guess the multiplication of the two numbers or enter "q" to quit:')
        
#         user_input = input()
        
#         if user_input.lower() == "q":
#             print("Goodbye!")
#             break
        
#         try:
#             guess = int(user_input)
#             if guess == num1 * num2:
#                 print('Correct')
#             else:
#                 print('Wrong, the answer is:', num1 * num2)
#         except ValueError:
#             print("Please enter a valid number or 'q' to quit.")

# if __name__ == "__main__":
#     main()


import streamlit as st
import random

def main():
    st.title("Calculator Game")
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    st.write(f"The two numbers are: {num1} and {num2}")
    user_input = st.text_input("Guess the multiplication of the two numbers or enter 'q' to quit:")
    
    if user_input.lower() == "q":
        st.write("Goodbye!")
    else:
        try:
            guess = int(user_input)
            if guess == num1 * num2:
                st.write('Correct')
            else:
                st.write(f'Wrong, the answer is: {num1 * num2}!!!')
        except ValueError:
            st.write("Please enter a valid number or 'q' to quit.")

if __name__ == "__main__":
    main()
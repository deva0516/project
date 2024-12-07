import streamlit as st

# Title of the app
st.title("Guess the Number Game")

# Text input for user to enter their guess
user_guess = st.text_input("Enter your guess:")

# Submit button
if st.button("Guess"):
    if user_guess:
        st.write(f"Your guess number is: {user_guess}")
    else:
        st.write("Please enter a number before clicking the guess button.")
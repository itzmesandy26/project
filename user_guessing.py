import streamlit as st
import random
import time

def guessing_game():
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 50)
        st.session_state.attempts = 0

    st.title("🎉 Guess the Number! 🎉")
    st.write("I'm thinking of a number between 1 and 50. Can you guess what it is?")

    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=50, step=1, key='guess')

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        with st.spinner('Checking your guess...🤔'):
           time.sleep(1.5)

        if user_guess < st.session_state.number_to_guess:
            st.error("❌ Too low 📉⬇️ ! Try again.")
        elif user_guess > st.session_state.number_to_guess:
            st.error("❌ Too high 📈⬆️! Try again.")
        else:
            st.success(f"🎉 Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
            st.snow()
            # Reset the game
            st.session_state.number_to_guess = random.randint(1, 50)
            st.session_state.attempts = 0
            st.write("I've thought of a new number, try to guess it!")

guessing_game()

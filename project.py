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
            st.balloons()
            # Reset the game
            st.session_state.number_to_guess = random.randint(1, 50)
            st.session_state.attempts = 0
            st.write("I've thought of a new number, try to guess it!")

def machine_guessing_game():
    if 'low' not in st.session_state:
        st.session_state.low = 1
        st.session_state.high = 50
        
        st.session_state.attempts = 0
        st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
        st.session_state.correct_guess = False

    st.title("🤖 Machine Guessing Game 🎉")
    st.write("Think of a number between 1 and 50, and I'll try to guess it!")

    if not st.session_state.correct_guess:
        if st.button("Make a Guess"):
            with st.spinner('guessing...🤔'):
                time.sleep(1.5)
            st.session_state.attempts += 1
            st.write(f"My guess is: {st.session_state.guess}")

        feedback = st.radio("Is my guess too low (L), too high (H), or correct (C)?", ('L', 'H', 'C'), key='feedback')

        if st.button("Submit Feedback"):
            if feedback == 'C':
                st.session_state.correct_guess = True
                st.success(f"Yay🎉! I guessed your number in {st.session_state.attempts} attempts.")
                st.balloons()
            elif feedback == 'L':
                st.session_state.low = st.session_state.guess + 1
                st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            elif feedback == 'H':
                st.session_state.high = st.session_state.guess - 1
                st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)

    if st.session_state.correct_guess and st.button("Play Again"):
        st.session_state.low = 1
        st.session_state.high = 50
        st.session_state.attempts = 0
        st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
        st.session_state.correct_guess = False


st.sidebar.title("Game Selection")
game_choice = st.sidebar.radio("Choose a game:", ("User Guessing Game", "Machine Guessing Game"))

if game_choice == "User Guessing Game":
    guessing_game()
else:
    machine_guessing_game()

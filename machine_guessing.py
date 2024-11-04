import streamlit as st
import random
import time

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

machine_guessing_game()

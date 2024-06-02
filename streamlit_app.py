import streamlit as st

# Set up the app title
st.title("PA-TSA Parliamentary Procedure Help Guide")

# Define a list of questions and preset answers
questions_answers = {
    "What is your name?": "My name is Streamlit.",
    "How are you?": "I'm doing great, thank you!",
    "What can you do?": "I can create interactive web apps with Python!",
    "Where are you located?": "I exist in the cloud."
}

# Create a dropdown for questions
question = st.selectbox("Choose a question:", list(questions_answers.keys()))

# Display the selected question
st.write(f"**Question:** {question}")

# Display the preset answer for the selected question
answer = questions_answers[question]
st.write(f"**Answer:** {answer}")

# Display a text input for user responses
user_response = st.text_input("Your response:")

# Button to submit the response
if st.button("Submit"):
    st.write(f"**Your Response:** {user_response}")



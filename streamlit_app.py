import streamlit as st

# Set up the app title
st.title("PA-TSA Parliamentary Procedure Help Guide")
st.subheader("Hey PA-TSA! This guide is a one-stop for all things parliamentary procedure related. Simply use the dropdown to browse the resources we have to offer and let the app direct you where to go.")

# Define a list of questions and preset answers
questions_answers = {
    "Chapter Team Event Rules": 'The linked pdf contains the event rules + rubrics; please note that it is an older guide and LEAP reports are no longer necessary', 'https://tmhs-tsa.weebly.com/uploads/9/3/9/7/93976199/chapter_team.pdf',
    "Official Study Guide": ("See the linked file", "https://docs.google.com/document/d/12QG02jRmP3kWenzUMgfUDQMjo_e8R8sIThZewhv8cOE/edit?usp=sharing"),
    "Official Practice Test": ("See the linked file", "https://docs.google.com/document/d/1aFigVc8EfmsY15gJmPGAYE15OqPS3UDLnbSeW8obFG0/edit?usp=sharing"),
    "Official Chapter Team Sample Docket": ("See the linked file", "https://docs.google.com/document/d/1lEx-m-VvngJfjOvydoYnVC8GepMzEOtqWQ9_Rc4L6dU/edit?usp=sharing"),
}

# Create a dropdown for questions
question = st.selectbox("Choose a question:", list(questions_answers.keys()))

# Display the preset answer for the selected question
answer = questions_answers[question]
st.write(f"{answer}")



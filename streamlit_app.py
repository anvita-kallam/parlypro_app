cimport streamlit as st
from streamlit_chat import message

# Set up the app title
st.title("PA-TSA Parliamentary Procedure Help Guide")
st.subheader("Hey PA-TSA! This guide is a one-stop for all things parliamentary procedure related. Simply use the dropdown to browse the resources we have to offer and let the app direct you where to go.")

# Define a list of questions and preset answers
questions_answers = {
    "Chapter Team Event Rules": ('The linked pdf contains the event rules + rubrics; please note that it is an older guide and LEAP reports are no longer necessary.', 'https://tmhs-tsa.weebly.com/uploads/9/3/9/7/93976199/chapter_team.pdf'),
    "Official Study Guide": ("The study guide includes links, term definitions, and charts to help prepare you for both the chapter team and parliamentarian tests.", "https://docs.google.com/document/d/12QG02jRmP3kWenzUMgfUDQMjo_e8R8sIThZewhv8cOE/edit?usp=sharing"),
    "Official Practice Test": ("The practice test contains 65 questions + annotated answer explanations that resemble those on the chapter team and parliamentarian tests.", "https://docs.google.com/document/d/1aFigVc8EfmsY15gJmPGAYE15OqPS3UDLnbSeW8obFG0/edit?usp=sharing"),
    "Official Chapter Team Sample Docket": ("The sample docket aims to model the packet given to teams during the chapter team semi-final portion; except some differences depending on the conference.", "https://docs.google.com/document/d/1lEx-m-VvngJfjOvydoYnVC8GepMzEOtqWQ9_Rc4L6dU/edit?usp=sharing"),
    "Parly Pro Basics Slideshow": ("This presentation is a great introduction if you're new to parliamentary procedure and a helpful review guide if you're preparing for a conference.", "https://docs.google.com/presentation/d/19JnTf9YjODwRgyt2N4jIxER_rYEQZaEyjZtwk_zvyRs/edit?usp=sharing"),
}

# Create a dropdown for questions
question = st.selectbox("Choose a resource:", list(questions_answers.keys()))

# Display the preset answer for the selected question
answer, url = questions_answers[question]
st.write(answer)
st.markdown(
    f'''
    <a href="{url}" target="_blank">
        <button style="
            background-color: #FF2400;
            color: white;
            border: none; 
            padding: 10px 20px; 
            text-align: center; 
            text-decoration: none; 
            display: inline-block; 
            font-size: 16px; 
            margin: 4px 2px; 
            cursor: pointer; 
            border-radius: 12px;
        ">
            Click here
        </button>
    </a>
    ''', 
    unsafe_allow_html=True
)

st.write("")

st.subheader("Still Need Help? Ask the PA-TSA Bot")
st.write("Possible Questions: What is Parliamentary Procedure? What is a motion? What is the difference between a majority and a plurality?...and more!")
chatbot_questions_answers = {
    "What is Parliamentary Procedure?": "Parliamentary Procedure is a set of rules for conducting orderly meetings that accomplish goals fairly.",
    "Why is Parliamentary Procedure important?": "It ensures that meetings are conducted in an efficient, democratic, and orderly manner, allowing all members to have a voice.",
    "What is a motion?": "A motion is a formal proposal made by a member of a group that the group take certain action.",
    "What are the types of motions?": "There are several types of motions including main motions, subsidiary motions, privileged motions, incidental motions, and motions that bring a question again before the assembly.",
    "What is a main motion?": "A main motion is a proposal that brings business before the assembly for consideration and action.",
    "What is a subsidiary motion?": "A subsidiary motion is used to change or affect how the main motion is handled, and is voted on before the main motion.",
    "What is a privileged motion?": "A privileged motion is a motion that is urgent or important enough to interrupt discussion, such as a motion to adjourn the meeting.",
    "What is an incidental motion?": "An incidental motion is related to the main motion or other business but must be dealt with immediately, such as a point of order.",
    "What is a point of order?": "A point of order is a claim made by a member that a rule of the assembly has been broken.",
    "What is an amendment?": "An amendment is a motion to change the wording of a main motion before the main motion is voted on.",
    "How do you make a motion?": "To make a motion, a member should say 'I move that...' and then state the proposal.",
    "How is a motion seconded?": "Another member says 'Second' to show that at least one other member agrees that the motion should be considered.",
    "What happens after a motion is seconded?": "The chairperson will restate the motion and then open the floor for debate. After debate, the motion is put to a vote.",
    "What is a quorum?": "A quorum is the minimum number of members who must be present for the assembly to conduct business legally.",
    "What is the role of the chairperson?": "The chairperson, or presiding officer, is responsible for conducting the meeting according to parliamentary procedure and ensuring that all members have an opportunity to participate.",
    "How do you end a debate?": "To end a debate, a member can move to 'call the question,' which requires a second and a two-thirds vote to pass.",
    "What is the difference between a majority and a plurality?": "A majority is more than half of the votes cast, while a plurality is the largest number of votes received by a candidate or proposal when three or more options are available.",
    "What is a tie vote?": "A tie vote occurs when the votes for and against a motion are equal. The motion fails unless the chairperson casts a deciding vote.",
    "How do you adjourn a meeting?": "A member can move to adjourn the meeting, which requires a second and a majority vote to pass.",
    "What is a recess?": "A recess is a short break in the meeting, which can be called by a motion that must be seconded and approved by a majority vote.",
    "What is a special meeting?": "A special meeting is a meeting held at a time other than the regularly scheduled time, usually to address urgent business.",
    "Can a motion be withdrawn?": "Yes, the member who made the motion can withdraw it before it is voted on, with the consent of the assembly.",
    "What is a committee?": "A committee is a small group of members assigned to consider or investigate a specific matter and report back to the assembly.",
    "How do you amend a motion?": "To amend a motion, a member can say 'I move to amend the motion by...' and state the change. The amendment must be seconded and voted on before the main motion is considered.",
    "What is the order of precedence of motions?": "Motions have an order of precedence, meaning some motions take priority over others, such as privileged motions taking precedence over main motions.",
    "What is a standing rule?": "A standing rule is a rule related to the administration of the organization, which remains in effect until it is rescinded or amended.",
    "What is a roll call vote?": "A roll call vote is when each member's vote is recorded individually, often used for important decisions.",
    "What is a unanimous consent?": "Unanimous consent is a method of approving actions without a formal vote, used when no member objects to the proposal.",
    "What is a division of the assembly?": "A division of the assembly is a request for a re-vote by a more accurate method, such as a show of hands or standing vote, often requested when the result of a voice vote is unclear.",
}

# Initialize session state if not already present
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input
user_question = st.text_input("Type your question here:")

if user_question:
    # Find the answer or give a default response
    answer = chatbot_questions_answers.get(user_question, "Sorry, I don't have an answer to that question.")
    
    # Update chat history
    st.session_state['chat_history'].append({"role": "user", "content": user_question})
    st.session_state['chat_history'].append({"role": "bot", "content": answer})

# Display the chat history
for chat in st.session_state['chat_history']:
    message(chat['content'], is_user=(chat['role'] == 'user'))

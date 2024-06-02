import streamlit as st
from openai import OPENAI 

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

st.header("Parliamentary Procedure Help ChatBot")
st.subheader("Have any specific questions? Ask the chatbot below for help!")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

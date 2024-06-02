import streamlit as st

# Set up the app title
# Google Drive link to direct link conversion
def convert_to_direct_link(google_drive_link):
    file_id = google_drive_link.split('/')[5]
    direct_link = f"https://drive.google.com/uc?export=view&id={file_id}"
    return direct_link

# URL of the image on Google Drive
google_drive_link = "https://drive.google.com/file/d/1PRZyzop8x9rug5fLTCsx8DbLoGh-TQhN/view?usp=sharing"
direct_link = convert_to_direct_link(google_drive_link)

# Display the image
st.image(direct_link, use_column_width=True)


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

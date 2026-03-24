import streamlit as st

st.title("AI Virtual Assistant")

user_input = st.text_area("Enter your request:")

if st.button("Generate"):

    if "email" in user_input.lower():
        response = "Dear Client,\n\nI hope you're doing well. I wanted to inform you that the project is slightly delayed but will be delivered soon.\n\nBest regards,\nHicham"

    elif "price" in user_input.lower():
        response = "My pricing depends on your needs. Basic packages start from $100."

    elif "task" in user_input.lower():
        response = "- Check emails\n- Work on project\n- Client meeting at 3PM"

    else:
        response = "I'm your AI assistant. Please ask about emails, tasks, or client replies."

    st.write(response)
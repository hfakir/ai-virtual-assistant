import streamlit as st

st.title("AI Virtual Assistant")

user_input = st.text_area("Enter your request:")

if st.button("Generate"):

    text = user_input.lower()

    # Email
    if "email" in text or "mail" in text or "ايميل" in text or "رسالة" in text:
        if "fr" in text or "écris" in text:
            response = "Bonjour,\n\nJ'espère que vous allez bien. Je voulais vous informer que le projet sera livré bientôt.\n\nCordialement"
        elif "ايميل" in text or "رسالة" in text:
            response = "مرحبا،\n\nأتمنى أن تكون بخير. أود إبلاغك أن المشروع سيتم تسليمه قريباً.\n\nمع تحياتي"
        else:
            response = "Dear Client,\n\nI hope you're doing well. I wanted to inform you that the project will be delivered soon.\n\nBest regards"

    # Price
    elif "price" in text or "prix" in text or "ثمن" in text:
        if "prix" in text:
            response = "Mes prix dépendent de vos besoins. Les offres commencent à partir de 100$."
        elif "ثمن" in text:
            response = "الأسعار تعتمد على احتياجاتك وتبدأ من 100 دولار."
        else:
            response = "My pricing depends on your needs. Packages start from $100."

    # Tasks
    elif "task" in text or "tâche" in text or "مهام" in text:
        if "tâche" in text:
            response = "- Vérifier les emails\n- Travailler sur le projet\n- Réunion client à 15h"
        elif "مهام" in text:
            response = "- التحقق من الرسائل\n- العمل على المشروع\n- اجتماع مع العميل"
        else:
            response = "- Check emails\n- Work on project\n- Client meeting at 3PM"

    else:
        response = "I'm your AI assistant. Ask me in English, French, or Arabic 😊"

    st.write(response)
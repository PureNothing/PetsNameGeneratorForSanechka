import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

user_animal_type = st.sidebar.text_area("What is you pet?", max_chars=15)


user_pet_color = st.sidebar.text_area("What color is your buddy?", max_chars=15)

if user_pet_color:
    response = lch.generate_pet_name(user_animal_type, user_pet_color)
    st.text(response)
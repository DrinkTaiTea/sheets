import streamlit as st
import streamlit_survey as ss
import pandas as pd
import numpy as np

def generate_survey():
    survey = ss.StreamlitSurvey()
    for i in range(1, 11):
        question = f"Question {i}"
        options = list(range(1, 11))
        survey.radio(question, options)
    return survey

def generate_responses():
    responses = []
    for i in range(30):
        response = np.random.randint(1, 11, size=10)
        responses.append(response)
    return pd.DataFrame(responses)

def main():
    st.set_page_config(page_title="Survey", page_icon=":pencil2:")
    st.title("Survey")
    st.write("Please answer the following questions:")
    survey = generate_survey()
    if survey.submit_button():
        responses = generate_responses()
        st.write("Thank you for your response!")
        st.write("Here are the results:")
        st.dataframe(responses)

if __name__ == "__main__":
    main()

import ai21
import streamlit as st
import os
import dotenv

st.subheader('Grammar Corrector and Text Improvements')

dotenv.load_dotenv(dotenv_path="E:\hackathon\grammar checker\.env")
ai21.api_key = os.environ.get('api_key')
text = st.text_area(label="Input your text here")
response = ai21.GEC.execute(text=text)
corrected_text = text
corrections = response["corrections"]
for curr_correction in reversed(corrections):
    corrected_text = corrected_text[:curr_correction["startIndex"]] + curr_correction['suggestion'] + corrected_text[curr_correction["endIndex"]:]

st.subheader('Grammar correction')
st.write(corrected_text)

p_response = ai21.Improvements.execute(text=corrected_text, types=["fluency", "vocabulary/specificity", "vocabulary/variety", "clarity/short-sentences", "clarity/conciseness"])
improved_text = corrected_text
improvements = p_response["improvements"]
for curr_improvement in reversed(improvements):
    improved_text =  improved_text[:curr_improvement["startIndex"]] + curr_improvement['suggestions'][0] + improved_text[curr_improvement["endIndex"]:]

st.subheader('Text Improvement')
st.write(improved_text)
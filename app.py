from dotenv import load_dotenv

load_dotenv()

from PIL import Image

from constants import gemini_api

import streamlit as st 

import pdf2image 

import os

import google.generativeai as genai 

import io

import base64

genai.configure(api_key=gemini_api)

def get_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response= model.generate_content([input,pdf_content[0],prompt])
    return response.text

def convert_pdf(uploaded_file):
    if uploaded_file is not None:
        images= pdf2image.convert_from_bytes(uploaded_file.read())
        first_page=images[0]

        img_byte = io.BytesIO()
        first_page.save(img_byte,format='JPEG')
        img_byte = img_byte.getvalue()

        pdf_part=[
            {
                "mime_type":'image/jpeg',
                "data":base64.b64encode(img_byte).decode()
            }
        ]
        return pdf_part
    else:
        raise FileNotFoundError("No file uploaded")


## streamlit app

st.set_page_config(page_title="ATS Resume Checker")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description:",key="input",placeholder="Write Description")
uploaded_file = st.file_uploader("Upload Your Resume(PDF)...",type=['PDF'])


if uploaded_file is not None:
    st.write("Uploaded Successfully")

bton1 = st.button("About Resume")
bton2 = st.button("Percentage Match")
bton3 = st.button("Improvement")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager in the field of any one job role from Data Science,Full Stack Web Development,Android Development,Big Data Engineering,DEVOPS,Data Analyst,your task is to review the provided resume against the job description for these profiles. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role Data Science,Full Stack Web Development,Android Development,Big Data Engineering,DEVOPS,Data Analyst and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt3 = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer,DEVOPS,Full Stack Web Development,Android Development. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on job description and
the missing keywords with high accuracy.
"""

if bton1:
    if uploaded_file is not None:
        pdf_content=convert_pdf(uploaded_file)
        response = get_response(input_prompt1,pdf_content,input_text)
        st.subheader("Response:-")
        st.write(response)

    else:
        st.write("Pls Upload The Resume")

elif bton2:
    if uploaded_file is not None:
        pdf_content=convert_pdf(uploaded_file)
        response = get_response(input_prompt2,pdf_content,input_text)
        st.subheader("Response:-")
        st.write(response)

    else:
        st.write("Pls Upload The Resume")

elif bton3:
    if uploaded_file is not None:
        pdf_content=convert_pdf(uploaded_file)
        response = get_response(input_prompt3,pdf_content,input_text)
        st.subheader("Response:-")
        st.write(response)

    else:
        st.write("Pls Upload The Resume")




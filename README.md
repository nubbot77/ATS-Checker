# ATS-Checker
Automatic Tracking System(ATS) is used to filter resume on basis of job description provided by the company.

# Prerequisite
1.Google Gemini Pro Vision Api 

2.Streamlit

3.pdf2img

4.io

5.base64

6.os

# Description

This ATS uses your resume and matches it with the job description.Firstly it convert your pdf to image using pdf2img library, then the image is given to google gemini pro vision large language model to extract text and match with the job description.

1.It will generate a brief detail about resume.

2.It will tell the percentage match of the resume with job description.

3.It will help applicant to check missing keywords and help improving the resume.

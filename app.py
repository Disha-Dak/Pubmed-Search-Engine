import streamlit as st

st.header("Article Sumarry genrator")

api ="gsk_*************************"


import os
from groq import Groq

def user_reply(api,input):
 client = Groq(
    api_key=api,  # This is the default and can be omitted
)

 chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content":"Hi you are bio-meta a seasoned bioinfomrtaican with experince of 20 years , yuu are trained to summarize complex bioinformatics articles in layman terms and help the person create a 5 page slide giving each slide contnet as if a kid can also understand"+input,
        }
    ],
    model="meta-llama/llama-4-scout-17b-16e-instruct",
)
 return (chat_completion.choices[0].message.content)

st.subheader("It helps in basically summarizer bioinformatics relaed articles")

input=st.text_area("Paste the article here")


if st.button(label="Submit") :
    st.write(f"Hi You just asked for    {input}")
    reply=user_reply(api,input)
    st.subheader("Summary")
    st.write("__________________________________________")
    st.write(reply)
    

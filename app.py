import streamlit as st
import pandas as pd

st.title("Slang Language Detector")
text=st.text_input("Enter the message")
df=pd.read_csv("bad-words.csv")


# def split_text(text):
#     split_value = []
#     tmp = ''
#     for c in text:
#         if c == ' ':
#             split_value.append(tmp)
#             tmp = ''
#         else:
#             tmp += c
#     if tmp:
#         split_value.append(tmp)
#     return split_value


def slang(text):
    text1 = text.split()
    slang_word = []
    for i in df['jigaboo']:
        for word in text1:
            word=word.lower()
            if word==i:
                slang_word.append(word)
    return slang_word

slng_word=slang(text)


text2=text.split()
for i in text2:
    i=i.lower()
    for x in slng_word:
        star=""
        if i==x:
            for x in range(0,len(i)):
                star=star+"*"
            text=text.replace(i,star)

st.balloons()
st.header(text)
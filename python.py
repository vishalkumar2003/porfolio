import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My webpage",page_icon=":tada:",layout="wide")
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_coding=load_lottieurl("https://lottie.host/0c66dad6-9532-48db-a36a-0b622483de89/6CE6nOL11x.json")
def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")        
img_contact_from=Image.open("images\Screenshot (554).png")
img_lottie_animation=Image.open("images\silambam.png")
flutter=Image.open("images/Screenshot (555).png")
java=Image.open("images/Screenshot (553).png")
with st.container():
    st.subheader("I am Vishal Kumar :)")
    st.title("A App Devolper From India")
    st.write("I am finding a ways to use Python")
    st.write("[Learn more  >](https://www.w3schools.com/sql/sql_backup_db.asp)")
with st.container():
    st.write("---")
    left_column,image_column=st.columns((1,2))
    with left_column:
        st.header("What I do :")
        st.write("##")
        st.write(
            """
            My Intrests: 
            - I have attend workshop in flutter/n.
            - Partiticipated in the hackathons(Problem solving an webathon).
            - Some of the basics of the Autocad(like drawing a top ,fornt and side of an object).
            - Field of Intrests:
                -openCV
                -computer vision
                -App development
                -Database Management
                -python  
            -basic communication in chinese      
            """
        )
        st.write(
            """
            Sports:    
                -State level Silambam(martial arts) palyer
            """
        )
        st.write("[github link > ](https://github.com/vishalkumar2003)")
        st.write("[linkedin >](https://www.linkedin.com/in/vishal-kumar-5328b5267/)")
    with image_column:
        st_lottie(lottie_coding,height=400,key="coding")    
with st.container():
    st.write("---")
    st.header("My Crtificates")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
        st.image(img_contact_from)
        st.image(flutter)
        st.image(java)    
with st.container():
    st.write("---")
    st.header("Get in Touch With Me!")
    st.write("##")
    contact_from="""
    <form action="https://formsubmit.co/codingisfun.viskav2003@gmail.com"method="Post">
    <input type="text" name="name" placeholder="Your name" requried>
    <input type="email" name="email" placeholder="Your email" requried>
    <textarea name="maessage" placeholder"Your message here here"></textarea>
    <button type="submit">Send</button>
    </form>
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_from,unsafe_allow_html=True)
    with right_column:
        st.empty()

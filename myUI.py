import streamlit as st
import subprocess
from PIL import Image
import os
from image_ids.image import predict
import time
from email_alert import send_email_alert
import base64
import streamlit.components.v1 as components
from streamlit_autorefresh import st_autorefresh
import sys

st.set_page_config(page_title="MedIDS", layout="wide")

st.title("🌐 MedIDS")
st.subheader("Lightweight healthcare IDS")  
st.write("Real-time IoMT Intrusion Detection System")

tab1, tab2 = st.tabs(["Network IDS","Image IDS"])
def alert_sound():
    with open("sounds/alert.mp3", "rb") as audio:
         audios = audio.read()
         b64 = base64.b64encode(audios).decode()
         md = f"""
         <audio autoplay>
         <source src = "data:audio/mp3;base64,{b64}" type="audio/mp3">
         </audio>
         """
         components.html(md, height=0)
    
with st.sidebar:
     st.title("About This App")
     st.success("Machine Learning Based Intrusion Detection System for real-time Network monitoring and image malware detection.")   
with tab1:
     st.header("Real-Time Network Monitoring")
     if "run_capture" not in st.session_state:
         st.session_state.run_capture = False
         
     col1, col2 = st.columns(2)
     with col1:
         if st.button("▶ Start Monitoring"):
             st.session_state.run_capture = True

     with col2:
         if st.button("⏹ Stop Monitoring"):
             st.session_state.run_capture = False

     st.divider()
     output_box = st.empty()

     if st.session_state.run_capture:
         st.success("✅ Live Network Capture Running")
         process = subprocess.Popen(["sudo",sys.executable,"-u","Network_ids/network.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
         alerts = ""
         for line in process.stdout:
             if "Attack" in line:
                st.toast( "🚨 Network Attack Detected!", icon="🚨")
                st.error("🚨 Suspicious IoMT Traffic Detected!")
                alert_sound()
             
             elif "Benign" in line:
                st.success("Normal IoMT Traffic")
                
             alerts = line + alerts
             output_box.text_area("Live IDS alerts", alerts, height=300)

     else:
         st.warning(" Monitoring Stopped")

with tab2:
     st.header("Image-Based Malware Detection")
     uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
     if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, width=300)
        prediction = predict(image)
        
        threshold=0.5
        if prediction > threshold:
            st.toast("🚨 Malware Detected 🚨", icon = "🚨")
            st.error(f"🚨 Malware Detected 🚨")
            send_email_alert(
              " MedIDS Malware Alert",
              " 🚨 MedIDS Malware Alert : Malware image Detected !! 🚨"
              ) 
            alert_sound()
        else:
            st.success(f"Benign")
            
st.markdown("---")
st.markdown("<h6 style='text-align: center; color: pink;'> Built with ❤️ by Alsafa</h6>", unsafe_allow_html=True)
        
        
    


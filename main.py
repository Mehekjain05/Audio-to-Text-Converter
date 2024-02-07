import streamlit as st 
import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav        
st.markdown("<h1 style='text-align:center;'>Audio to Text</h1>",unsafe_allow_html=True)     
st.markdown("---",unsafe_allow_html=True) 
audio = st.file_uploader("Upload the Audio")      
if audio:                                   
    sound = AudioSegment.from_mp3(audio)
    sound.export("transcript.wav", format="wav")


    # transcribe audio file                                                         
    AUDIO_FILE = "transcript.wav"

    # use the audio file as the audio source                                        
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file                
    
            st.text_area(label="Transcripted Text",value=r.recognize_google(audio))
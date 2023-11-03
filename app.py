import streamlit as st
from streamlit_custom_notification_box import custom_notification_box
import random
import modelModule as mm 
import db

st.image('./2.png')
#st.title('TuneFuse')

st.sidebar.title("🔍 About")
st.sidebar.write(db.about_txt)

st.sidebar.subheader("🔵 Cosine Similarity")
st.sidebar.write(db.cosine_sim_txt)

st.sidebar.subheader("🟢 Spotify API")
st.sidebar.write(db.spoti_txt)

txt_entered_song = ""
txt_recommended_song = ""

st.subheader("Enter The Tunes You Like 🎶")
tx1 = st.text_input(label="Song Input", label_visibility= "hidden", placeholder="More Tunes Better the results")

col1, col2 = st.columns(2, gap="small")

with col1:
    b1 = st.button(label="ADD Song", type= "primary")
    b3 = st.button(label="Reset", type="secondary")

with col2:
    b2 = st.button(label="Recommend", type="secondary")



try:
    if b1: 
        if tx1 == "":
            db.user_prefrences.append(random.choice(db.default_up))       
        else:
            db.user_prefrences.append(tx1)

    if b2:
        for s in db.user_prefrences: 
            uri = mm.accesbilty.find_uri(s)
            db.user_prefrences_uri.append(str(uri)[14:])

        with st.spinner('Get ready for your music...'):
            db.audio_features = mm.model.get_audio_features(db.user_prefrences_uri)
            db.similarity_matrix = mm.model.similarity_matrix(db.audio_features)
            db.recommendations = mm.model.recommend_song(db.similarity_matrix)    

        st.balloons()
        count = 1

        for recc in db.recommendations:
            txt_recommended_song += str(count) + ') ' + recc[0] + ' by ' + recc[1] + '. '
            count += 1 

        st.subheader("Recommended Tunes 🎤")
        st.text_area(label="txt2",value= txt_recommended_song,label_visibility="hidden")    

        #st.write(db.recommendations)

        txt_entered_song = " "


        db.audio_features.clear()
        db.similarity_matrix.clear()
        db.user_prefrences.clear()
        db.user_prefrences_uri.clear()
        db.recommendations.clear()

    if b3:
        txt_entered_song = " "


        db.audio_features.clear()
        db.similarity_matrix.clear()
        db.user_prefrences.clear()
        db.user_prefrences_uri.clear()
        db.recommendations.clear()                

except:
    
    styles = {'material-icons':{'color': 'red'},
          'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
          'notification-text': {'':''},
          'close-button':{'':''},
          'link':{'':''}}

    txt_entered_song = " "
    db.audio_features.clear()
    db.similarity_matrix.clear()
    db.user_prefrences.clear()
    db.recommendations.clear()

    custom_notification_box(icon='info', textDisplay='Opps an occured please try again 😅', externalLink='more info', url='#', styles=styles, key="foo")



for up in db.user_prefrences: 
    txt_entered_song += '-> ' + up + ' '

st.subheader("Entered Tunes 🔊")    
st.text_area(label="txt",value= txt_entered_song,label_visibility="hidden")


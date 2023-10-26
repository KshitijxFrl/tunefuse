import streamlit as st
import modelModule as mm 
import db

st.image('./logo_1.png')


# Side Bar (About Section)

st.sidebar.title("🔍 About")
st.sidebar.write(db.about_txt)

st.sidebar.subheader("🔵 Cosine Similarity")
st.sidebar.write(db.cosine_sim_txt)

st.sidebar.subheader("🟢 Spotify API")
st.sidebar.write(db.spoti_txt)

# Display Variables

txt_entered_song = ""
txt_recommended_song = ""


# App UI

st.subheader("Enter The Tunes You Like 🎶")
tx1 = st.text_input(label="Song Input", label_visibility= "hidden", placeholder="More Tunes Better the results")

col1, col2 = st.columns(2, gap="small")


# Coloumn Oriantaion For Buttons

with col1:
    b1 = st.button(label="ADD Song", type= "primary")

with col2:
    b2 = st.button(label="Recommend", type="secondary")




# Button Logic

if b1: 
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

    # Displaying Recommended Music

    for recc in db.recommendations: 
        txt_recommended_song += str(count) + ') ' + recc[0] + ' by ' + recc[1] + '. '
        count += 1  

    st.subheader("Recommended Tunes 🎤")
    st.text_area(label="txt2",value= txt_recommended_song,label_visibility="hidden")    


    txt_entered_song = " "


    # Reseting variables for the next user

    db.audio_features.clear()
    db.similarity_matrix.clear()
    db.user_prefrences.clear()
    db.recommendations.clear()

    



# Displaying Entered Music

for up in db.user_prefrences: 
    txt_entered_song += '-> ' + up + ' '

st.subheader("Entered Tunes 🔊")    
st.text_area(label="txt",value= txt_entered_song,label_visibility="hidden")


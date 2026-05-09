import streamlit as st

# CSS για την εμφάνιση της επικοινωνίας
st.markdown("""
    <style>
    .contact-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05); border-left: 8px solid #27ae60;
        margin-bottom: 20px;
        height: 250px;
    }
    .video-title {
        text-align: center; color: #27ae60; font-weight: bold; font-size: 24px; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='color: #27ae60;'>📞 Επικοινωνία & Υποστήριξη</h1>", unsafe_allow_html=True)
st.write("---")

# ΕΝΟΤΗΤΑ VIDEO: ΡΩΤΑ ΤΟΝ ΝΕΚΤΑΡΙΟ
st.markdown("<div class='video-title'>🎥 Ρώτα τον Νεκτάριο</div>", unsafe_allow_html=True)
# Αντικατάστησε το URL με το βίντεο που θέλεις να προβάλλεται
st.video("https://youtube.com") 

st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='contact-card'>
        <h3>👤 Τεχνική Υποστήριξη Smart Home</h3>
        <p><b>Υπεύθυνος:</b> Νεκτάριος Παπαδόπουλος</p>
        <p><b>Email:</b> <a href='mailto:kladouxos@geyer.gr'>kladouxos@geyer.gr</a></p>
        <p><b>Εξειδίκευση:</b> FIBARO, DALI, Z-Wave, KNX & Συστήματα GEYER</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='contact-card'>
        <h3>🏢 GEYER HELLAS Α.Ε.</h3>
        <p><b>Διεύθυνση:</b> 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p><b>Τηλεφωνικό Κέντρο:</b> 22620 31257</p>
        <p><b>Ωράριο:</b> Δευτέρα - Παρασκευή 08:00 - 16:00</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.page_link("main.py", label="⬅️ Επιστροφή στην Αρχική", icon="🏠")

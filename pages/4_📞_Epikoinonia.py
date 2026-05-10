import streamlit as st

# 1. Ρύθμιση σελίδας
st.set_page_config(page_title="Επικοινωνία - GEYER", layout="wide")

# 2. CSS για GEYER Green και Video Card
st.markdown("""
    <style>
    .main-title { color: #27ae60; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .video-card {
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1); border-top: 5px solid #27ae60;
        text-align: center; margin-bottom: 30px;
    }
    .contact-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05); border-left: 8px solid #27ae60;
        min-height: 220px; transition: transform 0.3s;
    }
    .info-label { color: #27ae60; font-weight: bold; }
    .play-button {
        background-color: #ff0000; color: white !important; padding: 12px 25px;
        text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block; margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📞 Επικοινωνία & Υποστήριξη</h1>", unsafe_allow_html=True)

# --- ΕΝΟΤΗΤΑ VIDEO: Η ΛΥΣΗ "VIDEO CARD" ---
# --- ΕΝΟΤΗΤΑ VIDEO: ΔΙΟΡΘΩΜΕΝΟ LINK ---
st.markdown("""
    <div class='video-card'>
        <h3 style='color: #27ae60;'>🎥 Ρώτα τον Νεκτάριο</h3>
        <p>Δείτε την εισαγωγή στη νέα σειρά τεχνικών λύσεων της GEYER.</p>
        <img src="https://youtube.com" style="width:100%; max-value:500px; border-radius:10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
        <br>
        <a href="https://youtube.com" target="_blank" class="play-button">▶ ΠΡΟΒΟΛΗ ΒΙΝΤΕΟ ΣΤΟ YOUTUBE</a>
    </div>
    """, unsafe_allow_html=True)


st.write("---")

# --- ΚΑΡΤΕΣ ΕΠΙΚΟΙΝΩΝΙΑΣ ---
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class='contact-card'>
        <h3 style='color: #1E3A8A;'>👤 Τεχνική Υποστήριξη</h3>
        <p><span class='info-label'>Υπεύθυνος:</span> Νεκτάριος Κλαδούχος</p>
        <p><span class='info-label'>Τηλέφωνο:</span> 6936803610</p>
        <p><span class='info-label'>Email:</span> <a href='mailto:kladouxos@geyer.gr' style='color:inherit; text-decoration:none;'>kladouxos@geyer.gr</a></p>
        <p><span class='info-label'>Ειδίκευση:</span> Smart Home Specialist & Technical Trainer</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='contact-card'>
        <h3 style='color: #1E3A8A;'>🏢 GEYER HELLAS Α.Ε.</h3>
        <p><span class='info-label'>📍 Διεύθυνση:</span> 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p><span class='info-label'>☎️ Τηλ. Κέντρο:</span> 22620 31257</p>
        <p><span class='info-label'>🕒 Ωράριο:</span> Δευτέρα - Παρασκευή 08:00 - 16:00</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Κουμπί επιστροφής
if st.button("🏠 ΕΠΙΣΤΡΟΦΗ ΣΤΗΝ ΑΡΧΙΚΗ"):
    st.switch_page("main.py")

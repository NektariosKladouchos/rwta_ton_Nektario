import streamlit as st

# CSS για πράσινο GEYER και σωστές κάρτες
st.markdown("""
    <style>
    .main-title { color: #27ae60; font-weight: bold; text-align: center; }
    .contact-card {
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05); border-left: 6px solid #27ae60;
        margin-bottom: 20px;
    }
    .info-label { color: #27ae60; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📞 Επικοινωνία & Υποστήριξη</h1>", unsafe_allow_html=True)

# --- ΕΝΟΤΗΤΑ VIDEO: ΡΩΤΑ ΤΟΝ ΝΕΚΤΑΡΙΟ ---
st.markdown("### 🎥 Ρώτα τον Νεκτάριο")
# Το link μετατράπηκε από shorts σε κανονικό watch link για να παίζει σίγουρα
st.video("https://youtube.com")

st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class='contact-card'>
        <h3>👤 Τεχνική Υποστήριξη</h3>
        <p><span class='info-label'>Υπεύθυνος:</span> Νεκτάριος Κλαδούχος</p>
        <p><span class='info-label'>Τηλέφωνο:</span> 6936803610</p>
        <p><span class='info-label'>Email:</span> <a href='mailto:kladouxos@geyer.gr' style='color:inherit; text-decoration:none;'>kladouxos@geyer.gr</a></p>
        <p><span class='info-label'>Ειδίκευση:</span> Smart Home Specialist</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='contact-card'>
        <h3>🏢 GEYER HELLAS Α.Ε.</h3>
        <p><span class='info-label'>📍 Διεύθυνση:</span> 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p><span class='info-label'>☎️ Τηλ. Κέντρο:</span> 22620 31257</p>
        <p><span class='info-label'>🕒 Ωράριο:</span> 08:00 - 16:00</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# ΔΙΟΡΘΩΣΗ: Χρήση του switch_page για εγγυημένη επιστροφή στην αρχική
if st.button("🏠 ΕΠΙΣΤΡΟΦΗ ΣΤΗΝ ΑΡΧΙΚΗ"):
    st.switch_page("main.py")

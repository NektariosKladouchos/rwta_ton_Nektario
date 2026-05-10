import streamlit as st

# CSS για επαγγελματική εμφάνιση
st.markdown("""
    <style>
    .main-title { color: #27ae60; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .contact-card {
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05); border-left: 6px solid #27ae60;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📞 Επικοινωνία & Υποστήριξη</h1>", unsafe_allow_html=True)

# --- ΤΕΣΤ 1: ΚΛΑΣΙΚΟ ΒΙΝΤΕΟ (Για να δούμε αν φταίει ο κώδικας) ---
st.subheader("🧪 Τέστ Λειτουργίας (Standard Video)")
st.video("https://youtube.com") 

st.write("---")

# --- ΤΕΣΤ 2: ΤΟ ΔΙΚΟ ΣΟΥ ΒΙΝΤΕΟ (Με Embed Link) ---
st.subheader("🎥 Ρώτα τον Νεκτάριο (Το δικό σου)")
# Δοκιμάζουμε την πιο "δυνατή" μορφή link
st.video("https://youtube.com")

st.write("---")

# --- ΚΑΡΤΕΣ ΕΠΙΚΟΙΝΩΝΙΑΣ ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div class='contact-card'>
        <h3>👤 Τεχνική Υποστήριξη</h3>
        <p><b>Υπεύθυνος:</b> Νεκτάριος Κλαδούχος</p>
        <p><b>Τηλέφωνο:</b> 6936803610</p>
        <p><b>Email:</b> kladouxos@geyer.gr</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='contact-card'>
        <h3>🏢 GEYER HELLAS Α.Ε.</h3>
        <p>📍 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p>☎️ Τηλ: 22620 31257</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("🏠 ΕΠΙΣΤΡΟΦΗ ΣΤΗΝ ΑΡΧΙΚΗ"):
    st.switch_page("main.py")

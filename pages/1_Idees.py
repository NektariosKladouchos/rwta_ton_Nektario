import streamlit as st
import base64

# Ρύθμιση σελίδας
st.markdown("<h1 style='color: #1E3A8A;'>💡 Τεχνική Εκπαίδευση & Λύσεις</h1>", unsafe_allow_html=True)
st.write("Οδηγός εγκατάστασης και λύσεις αυτοματισμού GEYER Smart Home.")
st.write("---")

# --- ΕΝΟΤΗΤΑ: ΠΑΡΟΥΣΙΑΣΗ PDF ---
st.markdown("### 📊 Παρουσίαση: Αυτοματοποίηση Φωτισμού")

try:
    with open("lighting_solutions.pdf", "rb") as f:
        pdf_bytes = f.read()
        
    # Κουμπί λήψης (Πάντα λειτουργικό)
    st.download_button(
        label="📥 Λήψη Παρουσίασης (PDF)",
        data=pdf_bytes,
        file_name="GEYER_Lighting_Solutions.pdf",
        mime="application/pdf"
    )

    # Προβολή PDF (Μέθοδος Base64)
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

except FileNotFoundError:
    st.warning("⚠️ Το αρχείο 'lighting_solutions.pdf' δεν βρέθηκε. Βεβαιωθείτε ότι το ανεβάσατε στο GitHub με αυτό ακριβώς το όνομα.")

st.write("---")

# --- ΒΗΜΑΤΑ ΕΚΠΑΙΔΕΥΣΗΣ (VIDEOS) ---
# Εδώ ακολουθούν τα βίντεο με st.video όπως στον προηγούμενο κώδικα...
st.markdown("### 🛠️ Βήμα 1: Πρώτη Σύνδεση & Setup (PC)")
st.video("https://youtube.com")

st.write("---")
st.markdown("### 📱 Βήμα 2: Σύνδεση από Κινητό / Tablet")
st.video("https://youtube.com")

st.write("---")
st.markdown("### 🌈 Εξειδικευμένες Λύσεις: LED Dimming")
st.video("https://youtube.com")

# --- ΕΠΙΣΤΡΟΦΗ ---
st.write("---")
st.page_link("main.py", label="⬅️ Επιστροφή στο Live Pricing", icon="📊")

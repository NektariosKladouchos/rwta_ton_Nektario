import streamlit as st
import base64

# Τίτλος Σελίδας
st.markdown("<h1 style='color: #1E3A8A;'>💡 Τεχνική Εκπαίδευση & Λύσεις</h1>", unsafe_allow_html=True)
st.write("---")

# --- ΕΝΟΤΗΤΑ: ΠΑΡΟΥΣΙΑΣΗ PDF ---
st.markdown("### 📊 Παρουσίαση: Αυτοματοποίηση Φωτισμού")

try:
    with open("lighting_solutions.pdf", "rb") as f:
        pdf_data = f.read()
        
    # Κουμπί Λήψης - Αυτό δουλεύει ΠΑΝΤΑ
    st.download_button(
        label="📥 Λήψη Παρουσίασης (PDF)",
        data=pdf_data,
        file_name="GEYER_Lighting_Solutions.pdf",
        mime="application/pdf"
    )

    # Preview PDF - Αν δεν το δείχνει ο browser, θα φαίνεται κενό (χρησιμοποιήστε το Download)
    base64_pdf = base64.b64encode(pdf_data).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

except FileNotFoundError:
    st.warning("⚠️ Το αρχείο 'lighting_solutions.pdf' δεν βρέθηκε στο GitHub.")

st.write("---")

# --- ΕΝΟΤΗΤΑ: VIDEOS (Με την πιο απλή μορφή link) ---

st.markdown("### 🛠️ Βήμα 1: Πρώτη Σύνδεση & Setup (PC)")
st.video("https://youtu.be")

st.write("---")

st.markdown("### 📱 Βήμα 2: Σύνδεση από Κινητό / Tablet")
st.video("https://youtu.be")

st.write("---")

st.markdown("### 🌈 Εξειδικευμένες Λύσεις: LED Dimming")
st.video("https://youtu.be")

st.write("---")
st.page_link("main.py", label="⬅️ Επιστροφή στο Live Pricing", icon="📊")

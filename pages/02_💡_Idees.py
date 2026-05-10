import streamlit as st

st.set_page_config(page_title="Ιδέες & Λύσεις - Geyer", page_icon="💡", layout="wide")

st.markdown("<h1 style='text-align: center; color: #28a745;'>Οικιακός & Επαγγελματικός Φωτισμός</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns(2)

with col1:
    # Χρησιμοποιούμε το τοπικό αρχείο που ανέβασες
    st.image("home_light.jpg", caption="Smart Οικιακός Φωτισμός", use_container_width=True)
    st.write("Δημιουργήστε ατμόσφαιρα στο σπίτι σας.")

with col2:
    # Χρησιμοποιούμε το τοπικό αρχείο που ανέβασες
    st.image("pro_light.jpg", caption="Επαγγελματικές Λύσεις", use_container_width=True)
    st.write("Αποδοτικός φωτισμός για επαγγελματικούς χώρους.")

st.write("---")

# Κουμπί για το PDF (Σιγουρέψου ότι το όνομα είναι σωστό στο GitHub)
try:
    with open("lighting_solutions.pdf", "rb") as f:
        st.download_button(
            label="📖 Ανοίξτε τον πλήρη Τεχνικό Κατάλογο (PDF)",
            data=f,
            file_name="Geyer_Lighting_Solutions.pdf",
            mime="application/pdf",
            use_container_width=True
        )
except:
    st.error("Το αρχείο PDF δεν βρέθηκε στο GitHub.")

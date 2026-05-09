import streamlit as st
import base64

# Ρύθμιση σελίδας
st.markdown("<h1 style='color: #1E3A8A;'>💡 Τεχνική Εκπαίδευση & Λύσεις</h1>", unsafe_allow_html=True)
st.write("Ολοκληρωμένος οδηγός για την εγκατάσταση και τις λύσεις αυτοματισμού GEYER Smart Home.")
st.write("---")

# --- ΕΝΟΤΗΤΑ: ΠΑΡΟΥΣΙΑΣΗ PDF ---
st.markdown("### 📊 Παρουσίαση: Αυτοματοποίηση Φωτισμού")
st.write("Λύσεις για οικιακό και επαγγελματικό φωτισμό (DALI, LED, Σενάρια).")

try:
    with open("lighting_solutions.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # Ενσωμάτωση PDF για απευθείας προβολή
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    # Κουμπί λήψης
    st.download_button(
        label="📥 Λήψη Παρουσίασης (PDF)",
        data=base64.b64decode(base64_pdf),
        file_name="GEYER_Lighting_Solutions.pdf",
        mime="application/pdf"
    )
except FileNotFoundError:
    st.warning("⚠️ Το αρχείο 'lighting_solutions.pdf' δεν βρέθηκε. Παρακαλώ ανεβάστε το στο GitHub (Add file -> Upload files).")

st.write("---")

# --- ΒΗΜΑ 1: SETUP ---
st.markdown("### 🛠️ Βήμα 1: Πρώτη Σύνδεση & Setup (PC)")
col1, col2 = st.columns([1.5, 1])
with col1:
    st.video("https://youtube.com")
with col2:
    st.info("""
    **Desktop Διαχείριση:**
    * Εντοπισμός IP στο δίκτυο.
    * Παραμετροποίηση συσκευών.
    * Ονοματοδοσία δωματίων.
    """)

st.write("---")

# --- ΒΗΜΑ 2: MOBILE APP ---
st.markdown("### 📱 Βήμα 2: Σύνδεση από Κινητό / Tablet")
col3, col4 = st.columns([1.5, 1])
with col3:
    st.video("https://youtube.com")
with col4:
    st.success("""
    **Mobile Έλεγχος:**
    * Απομακρυσμένη πρόσβαση.
    * Διαχείριση από τον τελικό χρήστη.
    * Ενεργοποίηση σεναρίων.
    """)

st.write("---")

# --- ΒΗΜΑ 3: ΤΕΧΝΙΚΕΣ ΛΥΣΕΙΣ ---
st.markdown("### 🌈 Εξειδικευμένες Λύσεις: LED Dimming")
col5, col6 = st.columns([1.5, 1])
with col5:
    st.video("https://youtube.com")
with col6:
    st.warning("""
    **Dimming με κοινό τροφοδοτικό:**
    * Χρήση RGBW Controller.
    * Έλεγχος μέσω απλού μπουτόν.
    * Ιδανικό για κρυφούς φωτισμούς.
    """)

# --- FOOTER ---
st.write("---")
st.page_link("main.py", label="⬅️ Επιστροφή στο Live Pricing", icon="📊")

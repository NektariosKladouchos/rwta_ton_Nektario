import streamlit as st

st.markdown("<h1 style='color: #1E3A8A;'>💡 Τεχνική Εκπαίδευση & Λύσεις</h1>", unsafe_allow_html=True)
st.write("Ολοκληρωμένος οδηγός για την εγκατάσταση και παραμετροποίηση του συστήματος GEYER Smart Home.")
st.write("---")

# --- ΒΗΜΑ 1: SETUP ---
st.markdown("### 🛠️ Βήμα 1: Πρώτη Σύνδεση & Setup (PC)")
col1, col2 = st.columns([1.5, 1])
with col1:
    st.video("https://youtube.com")
with col2:
    st.info("""
    **Desktop Διαχείριση:**
    * Εντοπισμός IP στην τοπική δίκτυο.
    * Πλήρες περιβάλλον παραμετροποίησης.
    * Ονοματοδοσία δωματίων και συσκευών.
    """)

st.write("---")

# --- ΒΗΜΑ 2: MOBILE APP ---
st.markdown("### 📱 Βήμα 2: Σύνδεση από Κινητό / Tablet")
col3, col4 = st.columns([1.5, 1])
with col3:
    st.video("https://www.youtube.com/watch?v=Z8UmoFfZcqY")
with col4:
    st.success("""
    **Mobile Έλεγχος:**
    * Σύνδεση μέσω Android ή iOS.
    * Απομακρυσμένη πρόσβαση στο Home Center.
    * Διαχείριση σεναρίων από τον τελικό χρήστη.
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
    * Χρήση FIBARO RGBW Controller.
    * Έλεγχος μέσω απλού μπουτόν πρίζας.
    * Ιδανικό για κρυφούς φωτισμούς και ατμόσφαιρα.
    """)

# --- FOOTER ---
st.write("---")
st.markdown("### 📊 Παρουσίαση: Λύσεις Αυτοματισμού Φωτισμού")
st.info("Φυλλομετρήστε την παρουσίαση για οικιακό και επαγγελματικό φωτισμό παρακάτω.")

# Ανάγνωση του αρχείου PDF (βεβαιώσου ότι το όνομα αρχείου είναι σωστό)
try:
    with open("lighting_solutions.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # Ενσωμάτωση του PDF μέσα σε iframe για προβολή
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    # Κουμπί για λήψη του αρχείου
    st.download_button(
        label="📥 Λήψη Παρουσίασης (PDF)",
        data=base64_pdf,
        file_name="GEYER_Lighting_Solutions.pdf",
        mime="application/pdf"
    )
except FileNotFoundError:
    st.warning("⚠️ Παρακαλώ ανεβάστε το αρχείο 'lighting_solutions.pdf' στο GitHub για να εμφανιστεί η παρουσίαση.")


st.write("---")
st.page_link("main.py", label="Επιστροφή στο Live Pricing", icon="📊")

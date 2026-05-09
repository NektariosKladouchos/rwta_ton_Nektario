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
st.page_link("main.py", label="Επιστροφή στο Live Pricing", icon="📊")

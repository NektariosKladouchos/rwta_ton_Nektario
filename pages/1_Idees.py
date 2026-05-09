import streamlit as st

# Ρύθμιση σελίδας (χωρίς set_page_config αν υπάρχει στο main)
st.markdown("<h1 style='color: #1E3A8A;'>💡 Τεχνικές Λύσεις & Ιδέες</h1>", unsafe_allow_html=True)
st.write("---")

# ΕΝΟΤΗΤΑ 1: DALI ΦΩΤΙΣΜΟΣ
with st.expander("🔌 Πρωτόκολλο DALI - Έλεγχος & Δυνατότητες", expanded=True):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("""
        **Τι προσφέρει η GEYER στο DALI:**
        * Ανεξάρτητος έλεγχος έως 64 διευθύνσεων ανά gateway.
        * Δυνατότητα δημιουργίας group χωρίς αλλαγή καλωδίωσης.
        * Feedback κατάστασης (αναφορά βλάβης φωτιστικού).
        """)
    with col2:
        # Εδώ μπορείς να βάλεις ένα YouTube Video για το DALI
        st.video("https://youtube.com") # Βάλε το σωστό link

st.write("---")

# ΕΝΟΤΗΤΑ 2: ΤΑΙΝΙΕΣ LED & ΕΙΔΙΚΟΙ ΑΥΤΟΜΑΤΙΣΜΟΙ
st.markdown("### 🌈 Ταινίες LED & Διακοσμητικός Φωτισμός")
col3, col4 = st.columns(2)
with col3:
    st.info("**Λύση Smart RGBW:** Έλεγχος χρωμάτων μέσω εφαρμογής και δημιουργία ατμόσφαιρας.")
    # Εδώ μπορείς να βάλεις μια εικόνα σχεδίου σύνδεσης
    # st.image("link_to_diagram.jpg", caption="Σχέδιο Σύνδεσης LED Controller")
with col4:
    st.success("**Dimming 1-10V:** Ιδανικό για μεγάλες γραμμές LED χωρίς τρεμόπαιγμα.")

st.write("---")

# ΕΝΟΤΗΤΑ 3: ΤΕΧΝΙΚΑ ΕΓΧΕΙΡΙΔΙΑ (DOWNLOADS)
st.markdown("### 📂 Τεχνική Βιβλιοθήκη & Σχέδια")
c1, c2, c3 = st.columns(3)
with c1:
    st.download_button("📕 Κατάλογος Rotal (PDF)", data="...", file_name="rotal.pdf")
with c2:
    st.link_button("🎥 Video Tutorials", "https://youtube.com")
with c3:
    st.link_button("🌐 Επίσημο Site", "https://geyer.gr")

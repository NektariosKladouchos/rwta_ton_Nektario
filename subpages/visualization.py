# subpages/visualization.py
import streamlit as st

def show():
    st.header("🖥️ Οπτικοποίηση Συστήματος")
    st.info("Δείτε σε πραγματικό χρόνο την κατάσταση του κτιρίου σας.")
    
    st.write("- **Άμεση Κατάσταση:** Δείτε ποια φώτα είναι αναμμένα.")
    st.write("- **Κεντρικός Έλεγχος:** Διαχειριστείτε τους αυτοματισμούς.")
    
    st.divider()
    st.subheader("📺 Δείτε το Σύστημα σε Λειτουργία")
    
    youtube_url = "https://www.youtube.com/watch?v=ckgDEu-wTXo" # Βάλτε το δικό σας Link
    st.video(youtube_url)
    
    st.link_button("🌐 Άνοιγμα του βίντεο στο YouTube", youtube_url)

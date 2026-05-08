import streamlit as st

st.markdown("# 💡 Ιδέες & Τεχνικές Λύσεις")
st.write("---")

st.markdown("### 🔌 Αυτοματισμός Φωτισμού DALI")
st.write("""
Το πρωτόκολλο DALI είναι η ιδανική λύση για επαγγελματικούς χώρους και μεγάλες κατοικίες. 
Προσφέρει απόλυτο έλεγχο ανά φωτιστικό και εύκολη ομαδοποίηση μέσω λογισμικού.
""")

# Εδώ μπορείς να βάλεις ένα Video από το YouTube της Geyer
st.video("https://youtube.com") # Αντικατάστησε με πραγματικό link

st.write("---")

st.markdown("### 🌈 Ταινίες LED & Dimming")
col1, col2 = st.columns(2)
with col1:
    st.info("**Λύση 1: Phase Cut Dimming**\nΙδανικό για retrofit εγκαταστάσεις με υφιστάμενη καλωδίωση.")
with col2:
    st.success("**Λύση 2: 1-10V / DALI Control**\nΓια γραμμική αυξομείωση χωρίς τρεμόπαιγμα (flicker-free).")

st.write("---")
st.markdown("### 📂 Τεχνικά Φυλλάδια")
st.link_button("📥 Κατεβάστε τον Οδηγό Rotal", "https://geyer.gr")

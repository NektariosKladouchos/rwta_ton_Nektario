import streamlit as st

st.set_page_config(page_title="Ιδέες & Λύσεις - Geyer", page_icon="💡", layout="wide")

st.markdown("<h1 style='text-align: center; color: #28a745;'>Οικιακός & Επαγγελματικός Φωτισμός</h1>", unsafe_allow_html=True)
st.write("---")

st.info("✨ **Ανακαλύψτε τις Λύσεις μας:** Περιηγηθείτε στις κορυφαίες προτάσεις φωτισμού της Geyer.")

# Εμφάνιση εικόνων (Εδώ μπορείς να βάλεις links από φωτογραφίες των προϊόντων σου)
# Σου βάζω μερικές ενδεικτικές εικόνες φωτισμού για να δεις πώς φαίνεται
col1, col2 = st.columns(2)

with col1:
    st.image("https://pexels.com", caption="Smart Οικιακός Φωτισμός")
    st.write("Δημιουργήστε ατμόσφαιρα στο σπίτι σας με σενάρια φωτισμού που προσαρμόζονται στις ανάγκες σας.")

with col2:
    st.image("https://pexels.com", caption="Επαγγελματικές Λύσεις")
    st.write("Αποδοτικός φωτισμός για γραφεία και καταστήματα με έμφαση στην εξοικονόμηση ενέργειας.")

st.write("---")

# Κουμπί για όποιον θέλει να δει ΟΛΟ τον κατάλογο
with open("lighting_solutions.pdf", "rb") as f:
    st.download_button(
        label="📖 Ανοίξτε τον πλήρη Τεχνικό Κατάλογο (PDF)",
        data=f,
        file_name="Geyer_Lighting_Solutions.pdf",
        mime="application/pdf",
        use_container_width=True
    )

st.success("💡 **Tip:** Ο σωστός φωτισμός μπορεί να μειώσει την κατανάλωση ενέργειας έως και 70%!")

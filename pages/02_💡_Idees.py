import streamlit as st
import base64

# Ρύθμιση σελίδας
st.set_page_config(page_title="Ιδέες & Λύσεις - Geyer", page_icon="💡", layout="wide")

# Τίτλος Ενότητας
st.markdown("<h1 style='text-align: center; color: #28a745;'>Οικιακός & Επαγγελματικός Φωτισμός</h1>", unsafe_allow_html=True)
st.write("---")

st.info("💡 **Πάρτε Ιδέες:** Ξεφυλλίστε τον παρακάτω κατάλογο για να δείτε λύσεις φωτισμού που αναβαθμίζουν κάθε χώρο.")

# Συνάρτηση για την εμφάνιση του PDF
def display_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        
        # Δημιουργία PDF Viewer σε iframe
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("⚠️ Το αρχείο PDF δεν βρέθηκε. Βεβαιωθείτε ότι το 'lighting_solutions.pdf' είναι στον κεντρικό φάκελο.")

# Εμφάνιση του PDF
display_pdf("lighting_solutions.pdf")

st.write("---")
st.markdown("### ✨ Γιατί να επιλέξετε Smart Φωτισμό;")
st.write("""
*   **Εξοικονόμηση Ενέργειας**: Φωτισμός μόνο όταν και όπου χρειάζεται.
*   **Ατμόσφαιρα**: Σενάρια φωτισμού για κάθε στιγμή της ημέρας.
*   **Ασφάλεια**: Αυτόματη ενεργοποίηση κατά την απουσία σας.
""")


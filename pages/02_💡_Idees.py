import streamlit as st
import base64

st.set_page_config(page_title="Ιδέες & Λύσεις - Geyer", page_icon="💡", layout="wide")

st.markdown("<h1 style='text-align: center; color: #28a745;'>Οικιακός & Επαγγελματικός Φωτισμός</h1>", unsafe_allow_html=True)
st.write("---")

# Ορισμός του σωστού ονόματος αρχείου
pdf_filename = "lighting_solutions.pdf"

try:
    with open(pdf_filename, "rb") as f:
        pdf_bytes = f.read()
    
    # 1. Κουμπί για άνοιγμα/κατέβασμα (Πάντα δουλεύει!)
    st.download_button(
        label="📥 Προβολή ή Κατέβασμα του Καταλόγου (PDF)",
        data=pdf_bytes,
        file_name=pdf_filename,
        mime="application/pdf",
        use_container_width=True
    )

    st.write("") # Κενό

    # 2. Προσπάθεια για ενσωματωμένη προβολή (Embed)
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

except FileNotFoundError:
    st.error(f"⚠️ Το αρχείο '{pdf_filename}' δεν βρέθηκε. Σιγουρευτείτε ότι το ανεβάσατε στο GitHub (έξω από το φάκελο pages).")

import streamlit as st
import urllib.parse

st.set_page_config(page_title="GEYER Portal", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>GEYER PORTAL</h1>", unsafe_allow_html=True)

tab_calc, tab_contact = st.tabs(["📊 LIVE PRICING", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    st.info("Εδώ θα επαναφέρουμε τον τιμοκατάλογο μόλις βεβαιωθούμε ότι ξεκόλλησε η 'Επικοινωνία'.")

with tab_contact:
    st.markdown("### 📨 Φόρμα Επικοινωνίας")
    
    # Χρησιμοποιούμε τα απλά πεδία του Streamlit
    c_name = st.text_input("Ονοματεπώνυμο:", placeholder="π.χ. Νεκτάριος")
    c_msg = st.text_area("Το μήνυμά σας:", placeholder="Γράψτε εδώ τι χρειάζεστε...")
    
    if st.button("🚀 ΠΡΟΕΤΟΙΜΑΣΙΑ ΑΠΟΣΤΟΛΗΣ"):
        if c_name and c_msg:
            # Στοιχεία email
            recipient = "nnerinos@yahoo.gr"
            subject = f"Ζήτηση από Portal - {c_name}"
            body = f"Αποστολέας: {c_name}\n\nΜήνυμα:\n{c_msg}"
            
            # Δημιουργία Mailto Link
            mailto_link = f"mailto:{recipient}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
            
            st.success("Το email είναι έτοιμο!")
            st.markdown(f"""
                <div style="text-align:center; margin-top:20px;">
                    <a href="{mailto_link}" style="background-color: #27ae60; color: white; padding: 15px 25px; text-decoration: none; border-radius: 5px; font-weight: bold; font-size: 18px; display: inline-block;">
                        📩 ΠΑΤΗΣΤΕ ΕΔΩ ΓΙΑ ΟΡΙΣΤΙΚΗ ΑΠΟΣΤΟΛΗ
                    </a>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Παρακαλώ συμπληρώστε Όνομα και Μήνυμα.")

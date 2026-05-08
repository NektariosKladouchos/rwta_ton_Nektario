import streamlit as st
import urllib.parse

st.set_page_config(page_title="GEYER Portal", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>GEYER PORTAL</h1>", unsafe_allow_html=True)

tab_calc, tab_contact = st.tabs(["📊 LIVE PRICING", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    st.info("Δοκιμή αποστολής στο προσωπικό email (Yahoo). Πηγαίνετε στο Tab 'ΕΠΙΚΟΙΝΩΝΙΑ'.")

with tab_contact:
    st.markdown("### 📨 Φόρμα Επικοινωνίας (Προς Yahoo)")
    
    # Είσοδος στοιχείων από τον χρήστη
    c_name = st.text_input("Το όνομά σας:", placeholder="π.χ. Νεκτάριος")
    c_msg = st.text_area("Το μήνυμά σας:", placeholder="Γράψτε εδώ το κείμενο της δοκιμής...")
    
    if st.button("🚀 ΔΗΜΙΟΥΡΓΙΑ EMAIL"):
        if c_name and c_msg:
            # Το email παραλήπτη είναι το προσωπικό σου Yahoo
            recipient = "nnerinos@yahoo.gr"
            subject = f"GEYER Portal Message - {c_name}"
            body = f"Αποστολέας: {c_name}\n\nΜήνυμα:\n{c_msg}"
            
            # Δημιουργία του Mailto Link
            mailto_link = f"mailto:{recipient}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
            
            st.success("Το email δημιουργήθηκε με επιτυχία!")
            st.markdown(f"""
                <div style="text-align:center; margin-top:20px;">
                    <a href="{mailto_link}" style="background-color: #27ae60; color: white; padding: 15px 25px; text-decoration: none; border-radius: 5px; font-weight: bold; font-size: 18px; display: inline-block;">
                        📩 ΠΑΤΗΣΤΕ ΕΔΩ ΓΙΑ ΑΠΟΣΤΟΛΗ ΣΤΟ YAHOO
                    </a>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Παρακαλώ συμπληρώστε όλα τα πεδία.")

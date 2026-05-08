import streamlit as st

st.set_page_config(page_title="GEYER Portal", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>GEYER PORTAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>ΔΟΚΙΜΗ ΦΟΡΜΑΣ ΕΠΙΚΟΙΝΩΝΙΑΣ</b></p>", unsafe_allow_html=True)

tab_calc, tab_contact = st.tabs(["📊 LIVE PRICING", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    st.info("Πηγαίνετε στο Tab 'ΕΠΙΚΟΙΝΩΝΙΑ' για να δείτε τη φόρμα.")

with tab_contact:
    st.markdown("### 📨 Φόρμα Επικοινωνίας")
    
    # Ο κώδικας της φόρμας απομονωμένος για να δουλέψει σωστά
    contact_form_html = """
    <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #ccc; font-family: sans-serif;">
        <form action="https://formsubmit.co" method="POST">
            <input type="hidden" name="_subject" value="Δοκιμαστικό Μήνυμα από Portal">
            
            <label style="font-weight:bold;">Το όνομά σας:</label><br>
            <input type="text" name="name" required style="width:100%; padding:10px; margin-top:5px; margin-bottom:15px; border-radius:5px; border:1px solid #ccc;"><br>
            
            <label style="font-weight:bold;">Το μήνυμά σας:</label><br>
            <textarea name="message" required style="width:100%; height:100px; padding:10px; margin-top:5px; margin-bottom:15px; border-radius:5px; border:1px solid #ccc;"></textarea>
            
            <input type="hidden" name="_captcha" value="false">
            <button type="submit" style="background-color: #27ae60; color: white; padding: 15px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 100%; font-size: 16px;">
                🚀 ΑΠΟΣΤΟΛΗ ΔΟΚΙΜΗΣ
            </button>
        </form>
    </div>
    """
    
    # Χρήση component για να "τρέξει" ο HTML κώδικας
    st.components.v1.html(contact_form_html, height=400)

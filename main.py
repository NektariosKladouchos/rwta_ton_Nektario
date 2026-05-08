import streamlit as st

st.set_page_config(page_title="GEYER Portal", layout="wide")

# --- CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-header { text-align: center; color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-header'><h1>GEYER PORTAL</h1><p><b>ΔΟΚΙΜΗ ΕΠΙΚΟΙΝΩΝΙΑΣ</b></p></div>", unsafe_allow_html=True)

tab_calc, tab_contact = st.tabs(["📊 LIVE PRICING", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    st.info("Αυτή η σελίδα είναι για υπολογισμούς. Πηγαίνετε στο Tab 'ΕΠΙΚΟΙΝΩΝΙΑ' για τη δοκιμή email.")
    st.text_input("Ονοματεπώνυμο (για το display)")

with tab_contact:
    st.markdown("### 📨 Φόρμα Επικοινωνίας")
    st.write("Συμπληρώστε τα στοιχεία σας για να δούμε αν λειτουργεί η αποστολή.")
    
    contact_form = f"""
    <form action="https://formsubmit.co" method="POST" style="background: white; padding: 20px; border-radius: 10px; border: 1px solid #ccc;">
        <input type="hidden" name="_subject" value="Δοκιμαστικό Μήνυμα από Portal">
        
        <label>Το όνομά σας:</label><br>
        <input type="text" name="name" required style="width:100%; padding:10px; margin-bottom:15px; border-radius:5px; border:1px solid #ccc;"><br>
        
        <label>Το μήνυμά σας:</label><br>
        <textarea name="message" required style="width:100%; height:100px; padding:10px; margin-bottom:15px; border-radius:5px; border:1px solid #ccc;"></textarea>
        
        <input type="hidden" name="_captcha" value="false">
        <button type="submit" style="background-color: #27ae60; color: white; padding: 15px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 100%;">
            🚀 ΑΠΟΣΤΟΛΗ ΔΟΚΙΜΗΣ
        </button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

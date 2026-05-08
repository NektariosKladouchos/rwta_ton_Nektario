import streamlit as st

st.set_page_config(page_title="GEYER Portal", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>GEYER PORTAL</h1>", unsafe_allow_html=True)

tab_calc, tab_contact = st.tabs(["📊 LIVE PRICING", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    st.info("Εδώ θα είναι ο τιμοκατάλογος. Πηγαίνετε στο Tab 'ΕΠΙΚΟΙΝΩΝΙΑ' για τη δοκιμή.")

with tab_contact:
    st.markdown("### 📨 Φόρμα Επικοινωνίας")
    st.write("Συμπληρώστε τα στοιχεία σας παρακάτω:")

    # Χρησιμοποιούμε st.form για να "δένει" τα πεδία μαζί
    with st.form("my_contact_form"):
        c_name = st.text_input("Το όνομά σας:")
        c_email = st.text_input("Το email σας:")
        c_msg = st.text_area("Το μήνυμά σας:")
        
        submit_button = st.form_submit_button("🚀 ΑΠΟΣΤΟΛΗ ΖΗΤΗΣΗΣ")

    if submit_button:
        if c_name and c_email and c_msg:
            # Εδώ φτιάχνουμε την κρυφή φόρμα που θα στείλει τα δεδομένα στο FormSubmit
            # Μόλις πατηθεί το κουμπί, θα γίνει η αποστολή
            import streamlit.components.v1 as components
            
            # Καθαρισμός κειμένου
            clean_msg = c_msg.replace("\n", " ")
            
            # Αυτό το κομμάτι κώδικα θα εκτελεστεί ΜΟΝΟ όταν πατηθεί το submit
            js_submit = f"""
                <form id="hidden_form" action="https://formsubmit.co" method="POST" style="display:none;">
                    <input type="hidden" name="name" value="{c_name}">
                    <input type="hidden" name="email" value="{c_email}">
                    <input type="hidden" name="message" value="{clean_msg}">
                    <input type="hidden" name="_captcha" value="false">
                </form>
                <script>
                    document.getElementById("hidden_form").submit();
                </script>
            """
            components.html(js_submit, height=0)
            st.success("Η αποστολή ξεκίνησε! Παρακαλώ περιμένετε...")
        else:
            st.warning("Παρακαλώ συμπληρώστε όλα τα πεδία.")

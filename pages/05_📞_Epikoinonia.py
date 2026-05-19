import streamlit as st

# 1. Ρύθμιση σελίδας
st.set_page_config(page_title="Επικοινωνία - GEYER", layout="wide")

# Οριστικό CSS για σκούρο πράσινο μενού και λευκά γράμματα ΜΟΝΟ στην αριστερή μπάρα
st.markdown(
    """
    <style>

        /* ============================
           SIDEBAR (ΠΡΑΣΙΝΟ + ΑΣΠΡΑ ΓΡΑΜΜΑΤΑ)
        ============================ */

        /* Φόντο αριστερής μπάρας */
        [data-testid="stSidebar"] {
            background-color: #0b3c26 !important;
        }

        /* Γράμματα και σύνδεσμοι αριστερής μπάρας */
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Εικονίδια αριστερής μπάρας */
        [data-testid="stSidebar"] svg {
            fill: white !important;
        }

        /* Κουμπί "<" που κλείνει το sidebar */
        button[kind="header"] svg {
            fill: white !important;
        }


        /* ============================
           INPUT FIELDS (ΑΣΠΡΑ ΚΟΥΤΙΑ + ΜΑΥΡΟ ΚΕΙΜΕΝΟ)
        ============================ */

        /* Κείμενο που γράφεις */
        input, textarea, .stTextInput input, .stTextArea textarea {
            color: black !important;
        }

        /* Placeholder text */
        input::placeholder,
        textarea::placeholder {
            color: #444 !important;
        }

    </style>
    """,
    unsafe_allow_html=True
)

  

# 2. CSS για GEYER Green
st.markdown("""
    <style>
    .main-title { color: #27ae60; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .video-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1); border-top: 5px solid #27ae60;
        text-align: center; margin-bottom: 30px;
    }
    .contact-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05); border-left: 8px solid #27ae60;
        min-height: 200px;
    }
    .info-label { color: #27ae60; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📞 Επικοινωνία & Υποστήριξη</h1>", unsafe_allow_html=True)

# --- ΕΝΟΤΗΤΑ VIDEO ---
st.markdown("<div class='video-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #27ae60;'>🎥 Ρώτα τον Νεκτάριο</h3>", unsafe_allow_html=True)
#st.write("Πατήστε το παρακάτω κουμπί για να δείτε το βίντεο στο YouTube:")
#st.video("https://www.youtube.com/shorts/Q2dzj4YCIy4")
 youtube_url ="https://www.youtube.com/watch?vQ2dzj4YCIy4="
    st.video(youtube_url)


# Χρησιμοποιούμε το st.link_button που είναι το πιο ασφαλές εργαλείο του Streamlit
#st.link_button("▶ ΠΡΟΒΟΛΗ ΒΙΝΤΕΟ (YouTube Shorts)","https://www.youtube.com/shorts/Q2dzj4YCIy4")

#st.markdown("</div>", unsafe_allow_html=True)

#st.write("---")

 

# --- ΚΑΡΤΕΣ ΕΠΙΚΟΙΝΩΝΙΑΣ ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div class='contact-card'>
        <h3 style='color: #1E3A8A;'>👤 Τεχνική Υποστήριξη</h3>
        <p><span class='info-label'>Υπεύθυνος:</span> Νεκτάριος Κλαδούχος</p>
        <p><span class='info-label'>Τηλέφωνο:</span> 6936803610</p>
        <p><span class='info-label'>Email:</span> kladouxos@geyer.gr</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='contact-card'>
        <h3>🏢 GEYER HELLAS Α.Ε.</h3>
        <p><span class='info-label'>📍 Διεύθυνση:</span> 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p><span class='info-label'>☎️ Τηλ. Κέντρο:</span> 22620 31257</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

if st.button("🏠 ΕΠΙΣΤΡΟΦΗ ΣΤΗΝ ΑΡΧΙΚΗ"):
    st.switch_page("main.py")

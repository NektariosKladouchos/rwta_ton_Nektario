import streamlit as st

# Ρύθμιση σελίδας: Το initial_sidebar_state="expanded" κρατάει το μενού ανοιχτό
st.set_page_config(
    page_title="GEYER Technical Portal", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# CSS για την Αρχική Σελίδα
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-title { text-align: center; color: #1E3A8A; font-weight: bold; }
    .welcome-card { 
        background-color: #ffffff; padding: 30px; border-radius: 15px; 
        box-shadow: 0px 4px 20px rgba(0,0,0,0.05); border-top: 5px solid #1E3A8A;
    }
    /* Διόρθωση για να φαίνεται καλύτερα το sidebar */
    [data-testid="stSidebar"] {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>GEYER TECHNICAL PORTAL</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([2, 1]) # Δίνουμε περισσότερο χώρο στο κείμενο

with col1:
    st.markdown("""
    <div class='welcome-card'>
        <h3>👋 Καλώς ήρθατε</h3>
        <p>Αυτή είναι η κεντρική πύλη τεχνικής υποστήριξης για τους συνεργάτες της <b>GEYER Hellas</b>.</p>
        <p>Εδώ θα βρείτε εξειδικευμένα εργαλεία για:</p>
        <ul>
            <li><b>Live Pricing:</b> Γρήγορη κοστολόγηση Smart Home.</li>
            <li><b>Τεχνική Βιβλιοθήκη:</b> Σχέδια και εγχειρίδια.</li>
            <li><b>Ιδέες & Λύσεις:</b> Παρουσιάσεις DALI, LED και αυτοματισμών.</li>
        </ul>
        <br>
        <p style='color: #1E3A8A;'><b>👈 Επιλέξτε μια ενότητα από το μενού στα αριστερά για να ξεκινήσετε.</b></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Χρήση σωστού URL για το λογότυπο
    st.image("https://geyer.gr", use_container_width=True)
    st.info("""
    **Υπεύθυνος Portal:**
    Νεκτάριος Παπαδόπουλος
    *Technical Support Specialist*
    """)

st.write("---")
st.caption("© 2024 Geyer Hellas - Smart Solutions Portal")

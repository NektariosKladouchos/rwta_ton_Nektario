import streamlit as st

# 1. Ρύθμιση Σελίδας
st.set_page_config(
    page_title="GEYER Technical Portal",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS με το Πράσινο της GEYER (#27ae60)
st.markdown("""
    <style>
    .main-title { text-align: center; color: #27ae60; font-size: 40px; font-weight: bold; }
    .stButton>button { 
        background-color: #27ae60; color: white; border-radius: 8px; border: none; height: 3em; width: 100%;
    }
    .stButton>button:hover { background-color: #219150; color: white; border: 1px solid white; }
    .feature-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #27ae60;
        text-align: center; height: 100%;
    }
    .contact-info { background-color: #f1f9f4; padding: 20px; border-radius: 10px; border-left: 5px solid #27ae60; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header & Logo
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    st.image("https://wikimedia.org", use_container_width=True)

st.markdown("<div class='main-title'>TECHNICAL PORTAL</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Καλώς ήρθατε στην πλατφόρμα τεχνικής υποστήριξης της GEYER HELLAS</p>", unsafe_allow_html=True)

st.write("---")

# 4. Πλέγμα Ενοτήτων (Εδώ προσθέτεις εύκολα νέα κουτιά)
c1, c2 = st.columns(2)

with c1:
    st.markdown("<div class='feature-card'><h3>📊 Live Pricing</h3><p>Διαδραστικός υπολογισμός για Smart Home της GEYER.</p></div>", unsafe_allow_html=True)
    if st.button("ΕΙΣΟΔΟΣ ΣΤΟ LIVE PRICING"):
        st.switch_page("pages/2_📊_Pricing.py")

with c2:
    st.markdown("<div class='feature-card'><h3>💡 Ιδέες & Λύσεις</h3><p>Video tutorials και προτάσεις αυτοματισμού.</p></div>", unsafe_allow_html=True)
    if st.button("ΔΕΙΤΕ ΤΙΣ ΙΔΕΕΣ"):
        st.switch_page("pages/1_Idees.py")

st.write("") # Κενό

c3, c4 = st.columns(2)

with c3:
    st.markdown("<div class='feature-card'><h3>📐 Τεχνικά Σχέδια</h3><p>Διαγράμματα σύνδεσης DALI, LED και HVAC.</p></div>", unsafe_allow_html=True)
    if st.button("ΑΝΟΙΓΜΑ ΣΧΕΔΙΩΝ"):
        # Θα φτιάξεις το αρχείο pages/3_📐_Sxedia.py
        st.info("Η ενότητα 'Σχέδια' ετοιμάζεται.")

with c4:
    st.markdown("<div class='feature-card'><h3>📞 Ρώτα τον Νεκτάριο </h3><p>Άμεση υποστήριξη και στοιχεία επικοινωνίας.</p></div>", unsafe_allow_html=True)
    if st.button("ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΜΑΖΙ ΜΑΣ"):
        # Θα φτιάξεις το αρχείο pages/4_📞_Epikoinonia.py
        st.info("Η ενότητα 'Επικοινωνία' ετοιμάζεται.")

st.write("---")

# 5. Footer Στοιχεία
st.markdown("<div class='contact-info'><b>Υπεύθυνος:</b> Νεκτάριος Παπαδόπουλος | <b>Email:</b> kladouxos@geyer.gr</div>", unsafe_allow_html=True)

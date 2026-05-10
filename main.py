import streamlit as st

# 1. Ρύθμιση Σελίδας
st.set_page_config(
    page_title="GEYER Technical Portal",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS για Επαγγελματική Εμφάνιση (Geyer Green)
st.markdown("""
    <style>
    .main-title { text-align: center; color: #27ae60; font-size: 40px; font-weight: bold; }
    .stButton>button { 
        background-color: #27ae60; color: white; border-radius: 8px; border: none; height: 3em; width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #219150; color: white; border: 1px solid white; }
    .feature-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #27ae60;
        text-align: center; height: 180px; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header & Logo
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    st.image("https://wikimedia.org", use_container_width=True)

st.markdown("<div class='main-title'>TECHNICAL PORTAL</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Καλώς ήρθατε στην πλατφόρμα τεχνικής υποστήριξης Smart Home</p>", unsafe_allow_html=True)

st.write("---")

# 4. Πλέγμα Ενοτήτων με τα 4 Κουμπιά
c1, c2 = st.columns(2)

with c1:
    st.markdown("<div class='feature-card'><h3>📊 Live Pricing</h3><p>Υπολογισμός υλικών και άμεση προσφορά Smart Home.</p></div>", unsafe_allow_html=True)
    if st.button("ΕΙΣΟΔΟΣ ΣΤΟ PRICING"):
        st.switch_page("pages/03_📊_Pricing.py")


with c2:
    st.markdown("<div class='feature-card'><h3>💡 Ιδέες & Λύσεις</h3><p>Video tutorials και προτάσεις αυτοματισμού.</p></div>", unsafe_allow_html=True)
    if st.button("ΔΕΙΤΕ ΤΙΣ ΙΔΕΕΣ"):
        st.switch_page("pages/02_💡_Idees.py")
st.write("") # Κενό ανάμεσα στις σειρές

c3, c4 = st.columns(2)

with c3:
    st.markdown("<div class='feature-card'><h3>📐 Τεχνικά Σχέδια</h3><p>Διαγράμματα σύνδεσης DALI, LED και HVAC.</p></div>", unsafe_allow_html=True)
    if st.button("ΑΝΟΙΓΜΑ ΣΧΕΔΙΩΝ"):
        # Εδώ θα βάλουμε το αρχείο pages/3_📐_Sxedia.py όταν το φτιάξεις
        st.info("Η ενότητα 'Σχέδια' ετοιμάζεται.")

with c4:
    st.markdown("<div class='feature-card'><h3>📞 Επικοινωνία</h3><p>Άμεση υποστήριξη και στοιχεία επικοινωνίας.</p></div>", unsafe_allow_html=True)
    if st.button("ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΜΑΖΙ ΜΑΣ"):
        st.switch_page("pages/05_📞_Epikoinonia.py")
st.write("---")
st.caption("© 2024 Geyer Portal - Υπεύθυνος: Νεκτάριος Κλαδούχος")

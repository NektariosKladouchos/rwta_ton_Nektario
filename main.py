import streamlit as st

# 1. Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Technical Portal", page_icon="⚡", layout="wide")

# 2. CSS για Πράσινο Μενού
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #1a4a2e !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Περιεχόμενο Μενού
st.sidebar.markdown("<h2 style='text-align: center; color: #28a745;'>GEYER</h2>", unsafe_allow_html=True)
st.sidebar.write("---")

# Εδώ συνεχίζει ο υπόλοιπος κώδικας σου (κουμπιά κλπ)


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

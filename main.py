import streamlit as st

# 1. Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Technical Portal", page_icon="⚡", layout="wide")

# 2. CSS για Πράσινο Μενού και Ομορφιά
st.markdown("""
    <style>
        /* Χρώμα στο πλευρικό μενού (Sidebar) */
        [data-testid="stSidebar"] {
            background-color: #1a4a2e; /* Σκούρο επαγγελματικό πράσινο */
        }
        /* Χρώμα κειμένων στο μενού */
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        /* Γραμμή διαχωρισμού */
        hr {
            border: 1px solid #28a745;
        }
    </style>
    """, unsafe_allow_html=True)

# 3. Εικόνα Σχετική με Τεχνικό Portal (Smart Home / Technology)
# Χρησιμοποιούμε μια όμορφη εικόνα από το Unsplash που φορτώνει πάντα
st.sidebar.image("https://unsplash.com", use_container_width=True)

st.sidebar.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <h2 style='color: #28a745; margin-bottom: 0;'>GEYER</h2>
        <p style='font-size: 1em; color: #e0e0e0;'>Technical Portal</p>
    </div>
    <hr>
    """, unsafe_allow_html=True)

st.sidebar.info("Καλώς ήρθατε στην πλατφόρμα τεχνικής υποστήριξης.")




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

import streamlit as st

# 1. Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Technical Portal", page_icon="⚡", layout="wide")

# 2. CSS για εμφάνιση (Πράσινο Sidebar & Στυλ)
st.markdown("""
    <style>
        /* Πράσινο φόντο στο Sidebar */
        [data-testid="stSidebar"] {
            background-color: #1a4a2e !important;
        }
        /* Λευκά γράμματα στο Sidebar */
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        /* Κρύβουμε το 'main' πάνω αριστερά */
        [data-testid="stSidebarNav"] li:first-child {
            display: none;
        }
        /* Στυλ για τους τίτλους των καρτών */
        .main-title {
            color: #28a745;
            text-align: center;
            font-family: sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)

# 3. ΠΛΕΥΡΙΚΟ ΜΕΝΟΥ (Sidebar)
# Φωτογραφία Smart Home
st.sidebar.image("https://gstatic.com", caption="Geyer Technical Portal", use_container_width=True)

st.sidebar.markdown("<h2 style='text-align: center;'>GEYER</h2>", unsafe_allow_html=True)
st.sidebar.write("---")
st.sidebar.info("Καλώς ήρθατε στο Technical Portal. Επιλέξτε ενότητα για να ξεκινήσετε.")

# 4. ΚΥΡΙΩΣ ΣΕΛΙΔΑ
st.markdown("<h1 class='main-title'>TECHNICAL PORTAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Πλατφόρμα τεχνικής υποστήριξης Smart Home - Υπεύθυνος: Νεκτάριος Κλαδούχος</p>", unsafe_allow_html=True)
st.write("---")

# Δημιουργία στηλών για τις κάρτες
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Live Pricing")
    st.write("Υπολογισμός υλικών και άμεση προσφορά Smart Home.")
    if st.button("ΕΙΣΟΔΟΣ ΣΤΟ PRICING", use_container_width=True):
        st.switch_page("pages/03_📊_Pricing.py")

    st.write("") # Κενό
    st.markdown("### 📐 Τεχνικά Σχέδια")
    st.write("Διαγράμματα σύνδεσης DALI, LED και HVAC.")
    if st.button("ΑΝΟΙΓΜΑ ΣΧΕΔΙΩΝ", use_container_width=True):
        # Εδώ βάλε το σωστό όνομα αρχείου αν έχεις σελίδα σχεδίων
        st.info("Η σελίδα σχεδίων ετοιμάζεται.")

with col2:
    st.markdown("### 💡 Ιδέες & Λύσεις")
    st.write("Video tutorials και προτάσεις αυτοματισμού.")
    if st.button("ΔΕΙΤΕ ΤΙΣ ΙΔΕΕΣ", use_container_width=True):
        st.switch_page("pages/02_💡_Idees.py")

    st.write("") # Κενό
    st.markdown("### 📞 Επικοινωνία")
    st.write("Άμεση υποστήριξη και στοιχεία επικοινωνίας.")
    if st.button("ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΜΑΖΙ ΜΑΣ", use_container_width=True):
        st.switch_page("pages/05_📞_Epikoinonia.py")

st.write("---")
st.caption("© 2024 Geyer Portal - Υπεύθυνος: Νεκτάριος Κλαδούχος")

import streamlit as st
import streamlit_analytics2 as analytics

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Geyer Technical Portal",
    page_icon="⚡",
    layout="wide"
)

# ---------------------------------------------------------
# ANALYTICS
# ---------------------------------------------------------
with analytics.track():
    st.title("Ρώτα τον Νεκτάριο")

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
CUSTOM_CSS = """
<style>
/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #1a4a2e !important;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Hide first nav item */
[data-testid="stSidebarNav"] li:first-child {
    display: none;
}

/* Main title */
.main-title {
    color: #28a745;
    text-align: center;
    font-family: sans-serif;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.image("home_light.jpg", caption="Geyer Technical Portal", use_container_width=True)
    st.markdown("<h2 style='text-align:center;'>GEYER</h2>", unsafe_allow_html=True)
    st.write("---")
    st.info("Καλώς ήρθατε στο Technical Portal. Επιλέξτε ενότητα για να ξεκινήσετε.")

# ---------------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------------
st.markdown("<h1 class='main-title'>TECHNICAL PORTAL</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:gray;'>"
    "Πλατφόρμα τεχνικής υποστήριξης Smart Home - Υπεύθυνος: Νεκτάριος Κλαδούχος"
    "</p>",
    unsafe_allow_html=True
)
st.write("---")

# ---------------------------------------------------------
# CONTENT SECTIONS
# ---------------------------------------------------------
col1, col2 = st.columns(2)

# -------- LEFT COLUMN --------
with col1:
    st.markdown("### 📊 Live Pricing")
    st.write("Υπολογισμός υλικών και άμεση προσφορά Smart Home.")
    if st.button("ΕΙΣΟΔΟΣ ΣΤΟ PRICING", use_container_width=True):
        st.switch_page("pages/03_📊_Pricing.py")

    st.markdown("### 📘 Τεχνικά Σχέδια")
    st.write("Διαγράμματα σύνδεσης DALI, LED και HVAC.")
    if st.button("ΑΝΟΙΓΜΑ ΣΧΕΔΙΩΝ", use_container_width=True):
       st.switch_page("06_📘_Σχέδια.py")


# -------- RIGHT COLUMN --------
with col2:
    st.markdown("### 💡 Ιδέες & Λύσεις")
    st.write("Video tutorials και προτάσεις αυτοματισμού.")
    if st.button("ΔΕΙΤΕ ΤΙΣ ΙΔΕΕΣ", use_container_width=True):
        st.switch_page("pages/02_💡_Idees.py")

    st.markdown("### 📞 Επικοινωνία")
    st.write("Άμεση υποστήριξη και στοιχεία επικοινωνίας.")
    if st.button("ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΜΑΖΙ ΜΑΣ", use_container_width=True):
        st.switch_page("pages/05_📞_Epikoinonia.py")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.write("---")
st.caption("© 2024 Geyer Portal - Υπεύθυνος: Νεκτάριος Κλαδούχος")

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
    st.markdown("<h1 class='main-title-ask'>Technical Portal</h1>", unsafe_allow_html=True)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
CUSTOM_CSS = """
<style>

/* Green GEYER title */
.main-title-ask {
    color: #28a745 !important;
    font-weight: 700;
    text-align: center;
    font-size: 38px;
    margin-top: -20px;
}

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

/* CARD STYLE */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    border: 2px solid #1a4a2e20;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
    transition: 0.2s ease-in-out;
}

.card:hover {
    border-color: #1a4a2e;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.12);
    transform: translateY(-3px);
}

/* Card titles */
.card h3 {
    color: #1a4a2e;
    margin-bottom: 8px;
}

/* Buttons */
button[kind="secondary"] {
    background-color: #1a4a2e !important;
    color: white !important;
    border-radius: 6px !important;
}

button[kind="secondary"]:hover {
    background-color: #145a32 !important;
}

</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.image("LOGO_GEYER.png", use_container_width=True)
    st.markdown("<h2 style='text-align:center;'>GEYER</h2>", unsafe_allow_html=True)
    st.write("---")
    st.info("Καλώς ήρθατε στο Technical Portal. Επιλέξτε ενότητα για να ξεκινήσετε.")

# ---------------------------------------------------------
# MAIN SUBTITLE
# ---------------------------------------------------------
st.markdown(
    "<p style='text-align:center; color:gray; margin-top:-10px;'>"
    "Πλατφόρμα τεχνικής υποστήριξης Smart Home - Υπεύθυνος: Νεκτάριος Κλαδούχος"
    "</p>",
    unsafe_allow_html=True
)
st.write("---")

# ---------------------------------------------------------
# CONTENT SECTIONS (WHITE MINIMAL CARDS)
# ---------------------------------------------------------
col1, col2 = st.columns(2)

# -------- LEFT COLUMN --------
with col1:

    # 1) Τι είναι το Technical Portal
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🏠 Τι είναι το Technical Portal")
        st.write("Μάθετε τι προσφέρει η πλατφόρμα και πώς μπορεί να σας βοηθήσει.")
        if st.button("ΜΑΘΕΤΕ ΠΕΡΙΣΣΟΤΕΡΑ", use_container_width=True):
            st.switch_page("pages/01_🏠_Τι είναι το Technical Portal.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # 2) Φτιάξε ΕΣΥ το κόστος σου
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📊 Φτιάξε ΕΣΥ το κόστος σου")
        st.write("Υπολογισμός υλικών και άμεση προσφορά Smart Home.")
        if st.button("ΕΙΣΟΔΟΣ ΣΤΟ PRICING", use_container_width=True):
            st.switch_page("pages/03_📊_Φτιάξε ΕΣΥ το κόστος σου.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # 3) Τεχνικά Σχέδια
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📘 Τεχνικά Σχέδια")
        st.write("Διαγράμματα σύνδεσης DALI, LED και HVAC.")
        if st.button("ΑΝΟΙΓΜΑ ΣΧΕΔΙΩΝ", use_container_width=True):
            st.switch_page("pages/06_📘_Σχέδια.py")
        st.markdown("</div>", unsafe_allow_html=True)

# -------- RIGHT COLUMN --------
with col2:

    # 4) Ιδέες & Λύσεις
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 💡 ΙΔΕΕΣ & ΛΥΣΕΙΣ")
        st.write("Video tutorials και προτάσεις αυτοματισμού.")
        if st.button("ΔΕΙΤΕ ΤΙΣ ΙΔΕΕΣ", use_container_width=True):
            st.switch_page("pages/02_💡_ΙΔΕΕΣ & ΛΥΣΕΙΣ.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # 5) Forum
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 💬 Forum")
        st.write("Συζητήσεις, απορίες και τεχνική κοινότητα.")
        if st.button("ΜΠΕΙΤΕ ΣΤΟ FORUM", use_container_width=True):
            st.switch_page("pages/04_💬_Forum.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # 6) Επικοινωνία
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📞 Επικοινωνία")
        st.write("Άμεση υποστήριξη και στοιχεία επικοινωνίας.")
        if st.button("ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΜΑΖΙ ΜΑΣ", use_container_width=True):
            st.switch_page("pages/05_📞_Επικοινωνία.py")
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.write("---")
st.caption("© 2024 Geyer Portal - Υπεύθυνος: Νεκτάριος Κλαδούχος")

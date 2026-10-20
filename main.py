import streamlit as st
from supabase import create_client, Client
import streamlit_analytics2 as analytics
import pandas as pd
import pytz

# ---------------------------------------------------------
# SUPABASE CONNECTION
# ---------------------------------------------------------
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------------------------------------------------
# LOG EVENT FUNCTION
# ---------------------------------------------------------
def log_event(page, event, user=None, extra=None):
    try:
        supabase.table("analytics").insert({
            "page": page,
            "event": event,
            "user_email": user,
            "extra": extra
        }).execute()
    except Exception as e:
        print("Analytics error:", e)

# ---------------------------------------------------------
# GLOBAL TIMEZONE CONVERSION (UTC → GREECE)
# ---------------------------------------------------------
def convert_utc_to_greece(df):
    if "timestamp" not in df.columns:
        return df

    greece = pytz.timezone("Europe/Athens")

    df["timestamp"] = (
        pd.to_datetime(df["timestamp"])
        .dt.tz_convert(greece)
    )

    return df

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Geyer Technical Portal",
    page_icon="⚡",
    layout="wide"
)

CUSTOM_CSS = """
<style>

/* =======================================================
   GLOBAL
======================================================= */

.main .block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stAppViewContainer"] {
    background: #f7f8fa;
}

/* =======================================================
   SIDEBAR
======================================================= */

[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e5e7eb;
    padding-top: 20px;
}

[data-testid="stSidebar"] * {
    color: #1f2937 !important;
}

[data-testid="stSidebar"] input {
    background: #ffffff !important;
    color: #111827 !important;
    border-radius: 10px !important;
}

/* =======================================================
   SIDEBAR NAV
======================================================= */

[data-testid="stSidebarNav"] a {
    border-radius: 10px;
    margin-bottom: 4px;
}

[data-testid="stSidebarNav"]::before {
    content: "GEYER SMART";
    display: block;
    padding: 15px 20px;
    margin-bottom: 10px;
    color: #008c95;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
}

[data-testid="stSidebarNav"] a:hover {
    background: rgba(0,140,149,0.08);
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(0,140,149,0.12);
    color: #008c95 !important;
    font-weight: 600;
}

/* =======================================================
   HERO
======================================================= */

.hero-section {
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 30px;
}

.hero-eyebrow {
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 12px;
    color: #008c95;
    font-weight: 700;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 64px;
    font-weight: 800;
    color: #1f2937;
    line-height: 1.05;
    margin-bottom: 16px;
}

.hero-subtitle {
    font-size: 20px;
    color: #6b7280;
    max-width: 700px;
    margin: auto;
    line-height: 1.6;
}

/* =======================================================
   TITLES
======================================================= */

h1, h2, h3 {
    color: #1f2937;
}

/* =======================================================
   BUTTONS
======================================================= */

.stButton > button {
    width: 100% !important;
    min-height: 54px !important;

    background: #006f77 !important;
    color: #ffffff !important;

    border: none !important;
    border-radius: 12px !important;

    font-size: 16px !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px !important;

    text-transform: uppercase !important;

    transition: 0.2s ease !important;

    box-shadow: 0 4px 12px rgba(0,111,119,.20);
}

.stButton > button:hover {
    background: #004f55 !important;
    color: #ffffff !important;
    transform: translateY(-2px);
}

/* FORCE WHITE TEXT */

.stButton > button,
.stButton > button span,
.stButton > button div,
.stButton > button p {
    color: #ffffff !important;
}

/* =======================================================
   DATAFRAMES
======================================================= */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

/* =======================================================
   ALERTS
======================================================= */

.stAlert {
    border-radius: 12px;
}

/* =======================================================
   FOOTER
======================================================= */

.footer {
    text-align: center;
    color: #6b7280;
    font-size: 13px;
    padding: 20px;
}

/* =======================================================
   DIVIDER
======================================================= */

hr {
    border: none;
    border-top: 1px solid #e5e7eb;
}

</style>
"""
/* =======================================================
   SIDEBAR NAVIGATION
======================================================= */

[data-testid="stSidebarNav"] a {
    border-radius: 10px;
    margin-bottom: 4px;
}

[data-testid="stSidebarNav"]::before {
    content: "GEYER SMART";
    display: block;
    padding: 15px 20px;
    margin-bottom: 10px;

    color: #008c95;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
}

[data-testid="stSidebarNav"] a:hover {
    background: rgba(0,140,149,0.08);
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(0,140,149,0.12);
    color: #008c95 !important;
    font-weight: 600;
}

/* =======================================================
   HERO
======================================================= */

.hero-section {
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 30px;
}

.hero-eyebrow {
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 12px;
    color: #008c95;
    font-weight: 700;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 64px;
    font-weight: 800;
    color: #1f2937;
    line-height: 1.05;
    margin-bottom: 16px;
}

.hero-subtitle {
    font-size: 20px;
    color: #6b7280;
    max-width: 700px;
    margin: auto;
    line-height: 1.6;
}

/* =======================================================
   CONTENT
======================================================= */

h1, h2, h3 {
    color: #1f2937;
}

p {
    color: #4b5563;
}

/* =======================================================
   BUTTONS
======================================================= */

.stButton > button {
    width: 100%;
    min-height: 54px;

    background: #008c95 !important;
    color: #ffffff !important;

    border: none !important;
    border-radius: 12px !important;

    font-size: 16px !important;
    font-weight: 700 !important;
    letter-spacing: 0.4px;

    box-shadow: 0 4px 12px rgba(0,140,149,0.20);

    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #006f77 !important;
    color: #ffffff !important;

    transform: translateY(-2px);

    box-shadow: 0 8px 20px rgba(0,111,119,0.30);
}

.stButton > button:hover {
    background: #006f77 !important;
    color: white !important;
    transform: translateY(-1px);
}

/* =======================================================
   DATAFRAMES
======================================================= */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

/* =======================================================
   FOOTER
======================================================= */

.footer {
    text-align: center;
    color: #6b7280;
    font-size: 13px;
    padding: 20px;
}

/* =======================================================
   DIVIDERS
======================================================= */

hr {
    border: none;
    border-top: 1px solid #e5e7eb;
}

/* =======================================================
   ALERTS
======================================================= */

.stAlert {
    border-radius: 12px;
}

</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
# ---------------------------------------------------------
# ANALYTICS — PAGE VISIT
# ---------------------------------------------------------
log_event("home", "visit")

with analytics.track():

    st.markdown(
        "<p style='text-align:center;color:#008c95;"
        "font-size:12px;font-weight:600;"
        "letter-spacing:3px;'>GEYER SMART</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 style='text-align:center;"
        "color:#1f2937;"
        "font-size:56px;'>Technical Portal</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;"
        "color:#6b7280;"
        "font-size:18px;'>"
        "Πλατφόρμα τεχνικής υποστήριξης Smart Home"
        "</p>",
        unsafe_allow_html=True
    )
# ---------------------------------------------------------
# ---------------------------------------------------------
# CONTENT SECTIONS
# ---------------------------------------------------------

col1, col2 = st.columns(2)

# -------- LEFT COLUMN --------
with col1:

    st.markdown("### 🏠 Τι είναι το Technical Portal")

    st.write(
        "Μάθετε τι προσφέρει η πλατφόρμα και πώς μπορεί να σας βοηθήσει."
    )

    if st.button(
        "ΜΑΘΕΤΕ ΠΕΡΙΣΣΟΤΕΡΑ",
        use_container_width=True
    ):
        log_event("home", "click_more_info")
        st.switch_page(
            "pages/01_🏠_Τι είναι το Technical Portal.py"
        )

    st.write("")

    st.markdown("### 📊 Φτιάξε ΕΣΥ το κόστος σου")

    st.write(
        "Διαδραστικός τιμοκατάλογος Υλικών."
    )

    if st.button(
        "ΕΙΣΟΔΟΣ ΣΤΟ PRICING",
        use_container_width=True
    ):
        log_event("home", "click_pricing")
        st.switch_page(
            "pages/03_📊_Φτιάξε ΕΣΥ το κόστος σου.py"
        )

    st.write("")

    st.markdown("### 📘 Τεχνικά Σχέδια")

    st.write(
        "Διαγράμματα σύνδεσης ανά κατηγορία αυτοματισμών."
    )

    if st.button(
        "ΑΝΟΙΓΜΑ ΣΧΕΔΙΩΝ",
        use_container_width=True
    ):
        log_event("home", "click_sxedia")
        st.switch_page(
            "pages/06_📘_Σχέδια.py"
        )

# -------- RIGHT COLUMN --------
with col2:

    st.markdown("### 💡 ΙΔΕΕΣ & ΛΥΣΕΙΣ")

    st.write(
        "Video tutorials και προτάσεις αυτοματισμού."
    )

    if st.button(
        "ΔΕΙΤΕ ΤΙΣ ΙΔΕΕΣ",
        use_container_width=True
    ):
        log_event("home", "click_idees")
        st.switch_page(
            "pages/02_💡_ΙΔΕΕΣ & ΛΥΣΕΙΣ.py"
        )

    st.write("")

    st.markdown("### 💬 Forum")

    st.write(
        "Συζητήσεις, απορίες και τεχνική κοινότητα."
    )

    if st.button(
        "ΜΠΕΙΤΕ ΣΤΟ FORUM",
        use_container_width=True
    ):
        log_event("home", "click_forum")
        st.switch_page(
            "pages/04_💬_Forum.py"
        )

    st.write("")

    st.markdown("### 📞 Επικοινωνία")

    st.write(
        "Άμεση υποστήριξη και στοιχεία επικοινωνίας."
    )

    if st.button(
        "ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΜΑΖΙ ΜΑΣ",
        use_container_width=True
    ):
        log_event("home", "click_contact")
        st.switch_page(
            "pages/05_📞_Επικοινωνία.py"
        )
# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.write("---")

st.markdown(
    """
    <div class="footer">
        © 2026 GEYER Smart Hellas | Technical Portal
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# ADMIN ANALYTICS (WITH GREECE TIME)
# ---------------------------------------------------------
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False
if st.session_state.is_admin:
    st.write("---")
    st.subheader("📊 Analytics Αρχικής Σελίδας (Admin Only)")

    try:
        result = supabase.table("analytics").select("*").eq("page", "home").order("id", desc=True).execute()

        if result.data and len(result.data) > 0:
            df = convert_utc_to_greece(pd.DataFrame(result.data))
            st.success(f"Βρέθηκαν {len(df)} events.")
            st.dataframe(df)
        else:
            st.info("Δεν υπάρχουν ακόμα δεδομένα για την Αρχική σελίδα.")
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης analytics: {e}")

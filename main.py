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

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
CUSTOM_CSS = """
<style>

.main .block-container{
    max-width:1400px;
    padding-top:2rem;
    padding-bottom:3rem;
}

[data-testid="stAppViewContainer"]{
    background:#f7f8fa;
}
[data-testid="stSidebar"] {

    background:#ffffff;

    border-right:1px solid #e5e7eb;

    padding-top:20px;
}
--[data-testid="stSidebar"]{
  -- background:#ffffff;
  --  border-right:1px solid #e5e7eb;
}

[data-testid="stSidebar"] *{
    color:#1f2937 !important;
}

[data-testid="stSidebar"] input{
    background:#ffffff !important;
    color:#111827 !important;
    border-radius:10px !important;
}
[data-testid="stSidebarNav"] a {

    border-radius:10px;

    margin-bottom:4px;
}
--[data-testid="stSidebarNav"] li:first-child a{
  --  font-size:0 !important;
}

[data-testid="stSidebarNav"]::before{
    content:"GEYER SMART";
    display:block;
    padding:15px 20px;
    font-size:14px;
    font-weight:700;
    letter-spacing:2px;
    color:#008c95;
}

.hero-section{
    text-align:center;
    padding:40px 20px 50px 20px;
}

.hero-eyebrow{
    text-transform:uppercase;
    letter-spacing:3px;
    font-size:12px;
    color:#7b8794;
    font-weight:600;
    margin-bottom:12px;
}

.hero-title{
    font-size:72px;
    font-weight:700;
    color:#1f2937;
    line-height:1.1;
    margin-bottom:12px;
}
.hero-section{
    padding:80px 20px;
}

.hero-subtitle{
    font-size:17px;
    color:#6b7280;
}

.card{
    background:#ffffff;
    padding:30px;
    border-radius:18px;
    border:1px solid #e5e7eb;
    min-height:220px;
    box-shadow:0 4px 12px rgba(0,0,0,.04);
    transition:all .25s ease;
}

.card:hover{
    transform:translateY(-4px);
    box-shadow:0 14px 28px rgba(0,0,0,.08);
    border-color:#008c95;
}

.card h3{
    color:#111827;
    margin-bottom:12px;
}
.stButton > button {

    background:#008c95 !important;

    color:white !important;

    border:none !important;

    border-radius:12px !important;

    height:48px !important;

    font-weight:600 !important;
}

.stButton > button:hover {

    background:#006f77 !important;
}
--.stButton button{
 --   width:100%;
 --   min-height:48px;
 --   background:#008c95;
 --   color:white;
 --   border:none;
  --  border-radius:12px;
 --   font-weight:600;
}

.stButton button:hover{
    background:#006f77;
    color:white;
}

.footer{
    text-align:center;
    color:#6b7280;
    font-size:13px;
    padding:20px;
}

</style>
"""
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
# MAIN SUBTITLE
# ---------------------------------------------------------

#st.write("---")

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
            log_event("home", "click_more_info")
            st.switch_page("pages/01_🏠_Τι είναι το Technical Portal.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # 2) Φτιάξε ΕΣΥ το κόστος σου
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📊 Φτιάξε ΕΣΥ το κόστος σου")
        st.write("Διαδραστικός τιμοκατάλογος Υλικών .")
        if st.button("ΕΙΣΟΔΟΣ ΣΤΟ PRICING", use_container_width=True):
            log_event("home", "click_pricing")
            st.switch_page("pages/03_📊_Φτιάξε ΕΣΥ το κόστος σου.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # 3) Τεχνικά Σχέδια
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📘 Τεχνικά Σχέδια")
        st.write("Διαγράμματα σύνδεσης ανά κατηγορία αυτοματισμών.")
        if st.button("ΑΝΟΙΓΜΑ ΣΧΕΔΙΩΝ", use_container_width=True):
            log_event("home", "click_sxedia")
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
            log_event("home", "click_idees")
            st.switch_page("pages/02_💡_ΙΔΕΕΣ & ΛΥΣΕΙΣ.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # 5) Forum
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 💬 Forum")
        st.write("Συζητήσεις, απορίες και τεχνική κοινότητα.")
        if st.button("ΜΠΕΙΤΕ ΣΤΟ FORUM", use_container_width=True):
            log_event("home", "click_forum")
            st.switch_page("pages/04_💬_Forum.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # 6) Επικοινωνία
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📞 Επικοινωνία")
        st.write("Άμεση υποστήριξη και στοιχεία επικοινωνίας.")
        if st.button("ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΜΑΖΙ ΜΑΣ", use_container_width=True):
            log_event("home", "click_contact")
            st.switch_page("pages/05_📞_Επικοινωνία.py")
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.write("---")
st.markdown("""
<div class="footer">
© 2026 GEYER Smart Hellas | Technical Portal
</div>
""", unsafe_allow_html=True)
# ---------------------------------------------------------
# GLOBAL ADMIN MODE
# ---------------------------------------------------------

if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False
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

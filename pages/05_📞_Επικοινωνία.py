import streamlit as st
import os
import json
import pandas as pd
import pytz
from supabase import create_client, Client

# ---------------------------------------------------------
# SUPABASE CONNECTION
# ---------------------------------------------------------
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_event(page, event, user=None, extra=None):
    try:
        supabase.table("analytics").insert({
            "page": page,
            "event": event,
            "user_email": user,
            "extra": extra
        }).execute()
    except:
        pass

def convert_utc_to_greece(ts):
    try:
        greece = pytz.timezone("Europe/Athens")
        return pd.to_datetime(ts).tz_convert(greece)
    except:
        return ts

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(page_title="Επικοινωνία - GEYER", layout="wide")

# ---------------------------------------------------------
# ADMIN LOGIN (όπως Forum & Σχέδια)
# ---------------------------------------------------------
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

st.sidebar.title("🔒 Admin Login")
admin_password = st.sidebar.text_input("Password", type="password")

if admin_password == "geyer123":
    st.session_state.is_admin = True

is_admin = st.session_state.is_admin

# ---------------------------------------------------------
# ADMIN BADGE
# ---------------------------------------------------------
if is_admin:
    st.markdown("""
        <div style="
            position: fixed;
            top: 15px;
            right: 20px;
            background-color: #0b3c26;
            color: white;
            padding: 8px 15px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
            z-index: 9999;
        ">
            🟢 Admin Mode ενεργό
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# COUNTERS FILE
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COUNTER_FILE = os.path.join(BASE_DIR, "counters.json")

def load_counters():
    if not os.path.exists(COUNTER_FILE):
        return {}
    with open(COUNTER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_counters(data):
    with open(COUNTER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# Count page visit
_c = load_counters()
_c["contact_total"] = _c.get("contact_total", 0) + 1
_c["contact_last_visit"] = st.session_state.get("username", "Χρήστης")
save_counters(_c)

# LOG VISIT
log_event("contact", "visit")

# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------
st.markdown(
    """
    <style>
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
.stApp {
    background-color: #f8fafc;
}
        input, textarea, .stTextInput input, .stTextArea textarea {
            color: black !important;
        }
        input::placeholder,
        textarea::placeholder {
            color: #444 !important;
        }
       div[data-testid="stAlert"]{
    background:#ffffff !important;
    border-top:5px solid #008c95 !important;
    border-radius:24px !important;
    color:#1f2937 !important;
    box-shadow:0 8px 24px rgba(0,0,0,.08) !important;
}
    </style>
    """,
    unsafe_allow_html=True
)

# GEYER GREEN CSS
st.markdown("""
    <style>
    .main-title { color: #008c95; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .video-card {
    background: #ffffff;
    padding: 30px;
    border-radius: 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,.08);
    border-top: 5px solid #008c95;
}
  .contact-card {
    background:#ffffff;
    padding:35px;
    border-radius:28px;
    box-shadow:0 12px 32px rgba(0,0,0,.08);
    border-top:5px solid #008c95;
    min-height:220px;
    text-align:center;
}

   .info-label {
    color: #008c95;
    font-weight: 700;
}
h3{
    text-align:center;
    color:#008c95 !important;
    letter-spacing:5px;
    font-size:12px !important;
}

h1{
    text-align:center !important;
}

p{
    text-align:center;
}
    </style>
    """, unsafe_allow_html=True)

st.markdown("### GEYER SMART")

st.title("📞 Επικοινωνία & Υποστήριξη")

st.caption(
    "Επικοινωνία με την ομάδα υποστήριξης GEYER Smart Home"
)

st.write("")
st.write("")
# ---------------------------------------------------------
# VIDEO SECTION
# ---------------------------------------------------------

st.markdown(
    "<h3 style='color:#008c95;'>🎥 Ρώτα τον Νεκτάριο</h3>",
    unsafe_allow_html=True
)

st.write("Δείτε το βίντεο απευθείας εδώ:")

st.video("https://www.youtube.com/embed/Q2dzj4YCIy4")

st.write("")
# ---------------------------------------------------------
# CONTACT CARDS
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.success("""
👤 ΤΕΧΝΙΚΗ ΥΠΟΣΤΗΡΙΞΗ

Υπεύθυνος:
Νεκτάριος Κλαδούχος

Τηλέφωνο:
6936803610

Email:
kladouxos@geyer.gr
""")

with col2:

    st.success("""
🏢 GEYER HELLAS Α.Ε.

📍 Διεύθυνση:
2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας

☎️ Τηλ. Κέντρο:
22620 31257
""")
# ---------------------------------------------------------
# HOME BUTTON
# ---------------------------------------------------------
if st.button("🏠 ΕΠΙΣΤΡΟΦΗ ΣΤΗΝ ΑΡΧΙΚΗ"):
    _c = load_counters()
    _c["contact_home_clicks"] = _c.get("contact_home_clicks", 0) + 1
    save_counters(_c)

    log_event("contact", "home_click")

    st.switch_page("main.py")

# ---------------------------------------------------------
# ADMIN ANALYTICS
# ---------------------------------------------------------
if is_admin:
    st.write("---")
    st.subheader("📊 Analytics Επικοινωνίας (Admin Only)")

    try:
        result = supabase.table("analytics").select("*").eq("page", "contact").order("id", desc=True).execute()

        if result.data:
            df = pd.DataFrame(result.data)
            df["timestamp"] = df["timestamp"].apply(convert_utc_to_greece)
            st.dataframe(df)
        else:
            st.info("Δεν υπάρχουν ακόμα δεδομένα.")
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης analytics: {e}")

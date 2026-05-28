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
            background-color: #0b3c26 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        [data-testid="stSidebar"] svg {
            fill: white !important;
        }
        input, textarea, .stTextInput input, .stTextArea textarea {
            color: black !important;
        }
        input::placeholder,
        textarea::placeholder {
            color: #444 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# GEYER GREEN CSS
st.markdown("""
    <style>
    .main-title { color: #27ae60; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .video-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1); border-top: 5px solid #27ae60;
        text-align: center; margin-bottom: 30px;
    }
    .contact-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05); border-left: 8px solid #27ae60;
        min-height: 200px;
    }
    .info-label { color: #27ae60; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📞 Επικοινωνία & Υποστήριξη</h1>", unsafe_allow_html=True)

# ---------------------------------------------------------
# VIDEO SECTION
# ---------------------------------------------------------
st.markdown("<div class='video-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #27ae60;'>🎥 Ρώτα τον Νεκτάριο</h3>", unsafe_allow_html=True)

st.write("Δείτε το βίντεο απευθείας εδώ:")

if st.button("▶️ Play Video"):
    log_event("contact", "video_play")

st.video("https://www.youtube.com/embed/Q2dzj4YCIy4")

st.markdown("</div>", unsafe_allow_html=True)
st.write("---")

# ---------------------------------------------------------
# CONTACT CARDS
# ---------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
    if st.button("👤 View Support Card", key="support_card"):
        log_event("contact", "open_card", extra="support")

    st.markdown(f"""
    <div class='contact-card'>
        <h3 style='color: #1E3A8A;'>👤 Τεχνική Υποστήριξη</h3>
        <p><span class='info-label'>Υπεύθυνος:</span> Νεκτάριος Κλαδούχος</p>
        <p><span class='info-label'>Τηλέφωνο:</span> 6936803610</p>
        <p><span class='info-label'>Email:</span> kladouxos@geyer.gr</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button("🏢 View Company Card", key="company_card"):
        log_event("contact", "open_card", extra="company")

    st.markdown("""
    <div class='contact-card'>
        <h3>🏢 GEYER HELLAS Α.Ε.</h3>
        <p><span class='info-label'>📍 Διεύθυνση:</span> 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p><span class='info-label'>☎️ Τηλ. Κέντρο:</span> 22620 31257</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

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

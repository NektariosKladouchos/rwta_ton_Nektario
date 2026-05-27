import streamlit as st
import os
import json

# 1. Ρύθμιση σελίδας
st.set_page_config(page_title="Επικοινωνία - GEYER", layout="wide")

# ---------------------------------------------------------
# GLOBAL ADMIN MODE (READ ONLY)
# ---------------------------------------------------------
is_admin = st.session_state.get("is_admin", False)

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
_c["contact_total"] = _c.get("contact_total", 0) - 10
_c["contact_last_visit"] = st.session_state.get("username", "Χρήστης")
save_counters(_c)

# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------
st.markdown(
    """
    <style>

        /* ============================
           SIDEBAR (ΠΡΑΣΙΝΟ + ΑΣΠΡΑ ΓΡΑΜΜΑΤΑ)
        ============================ */

        [data-testid="stSidebar"] {
            background-color: #0b3c26 !important;
        }

        [data-testid="stSidebar"] * {
            color: white !important;
        }

        [data-testid="stSidebar"] svg {
            fill: white !important;
        }

        button[kind="header"] svg {
            fill: white !important;
        }

        /* ============================
           INPUT FIELDS
        ============================ */

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

# 2. CSS για GEYER Green
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

# --- ΕΝΟΤΗΤΑ VIDEO ---
st.markdown("<div class='video-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #27ae60;'>🎥 Ρώτα τον Νεκτάριο</h3>", unsafe_allow_html=True)

st.write("Δείτε το βίντεο απευθείας εδώ:")

# Ενσωματωμένο YouTube Shorts
st.video("https://www.youtube.com/embed/Q2dzj4YCIy4")

st.markdown("</div>", unsafe_allow_html=True)
st.write("---")

# --- ΚΑΡΤΕΣ ΕΠΙΚΟΙΝΩΝΙΑΣ ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div class='contact-card'>
        <h3 style='color: #1E3A8A;'>👤 Τεχνική Υποστήριξη</h3>
        <p><span class='info-label'>Υπεύθυνος:</span> Νεκτάριος Κλαδούχος</p>
        <p><span class='info-label'>Τηλέφωνο:</span> 6936803610</p>
        <p><span class='info-label'>Email:</span> kladouxos@geyer.gr</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='contact-card'>
        <h3>🏢 GEYER HELLAS Α.Ε.</h3>
        <p><span class='info-label'>📍 Διεύθυνση:</span> 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p><span class='info-label'>☎️ Τηλ. Κέντρο:</span> 22620 31257</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Count button clicks
if st.button("🏠 ΕΠΙΣΤΡΟΦΗ ΣΤΗΝ ΑΡΧΙΚΗ"):
    _c = load_counters()
    _c["contact_home_clicks"] = _c.get("contact_home_clicks", 0) + 1
    save_counters(_c)
    st.switch_page("main.py")

# ---------------------------------------------------------
# ADMIN ANALYTICS (ONLY IF ADMIN)
# ---------------------------------------------------------
if is_admin:
    st.write("---")
    st.subheader("📊 Analytics Επικοινωνίας (Μόνο για Admin)")

    counters = load_counters()

    col1, col2, col3 = st.columns(3)
    col1.metric("📞 Συνολικές Επισκέψεις", counters.get("contact_total", 0))
    col2.metric("🏠 Επιστροφές στην Αρχική", counters.get("contact_home_clicks", 0))
    col3.metric("👤 Τελευταίος Επισκέπτης", counters.get("contact_last_visit", "—"))

    st.write("---")
    st.info("Τα analytics ενημερώνονται αυτόματα σε κάθε επίσκεψη και κάθε πάτημα κουμπιού.")

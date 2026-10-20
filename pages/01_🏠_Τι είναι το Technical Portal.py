import streamlit as st
from supabase import create_client, Client
import pandas as pd
import pytz

# ---------------------------------------------------------
# SUPABASE CONNECTION (ίδια ονόματα με main.py)
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
    page_title="Εισαγωγή - Geyer Portal",
    page_icon="🏠",
    layout="wide"
)

# ---------------------------------------------------------
# GLOBAL ADMIN MODE (READ ONLY)
# ---------------------------------------------------------
is_admin = st.session_state.get("is_admin", False)

# ---------------------------------------------------------
# CUSTOM CSS (GREEN SIDEBAR)
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #0b3c26 !important;
        }
        [data-testid="stSidebarNav"] span {
            color: white !important;
        }
        [data-testid="stSidebarNav"] svg {
            fill: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------

st.markdown(
    """
    <p style="
        text-align:center;
        color:#008c95;
        font-size:12px;
        font-weight:700;
        letter-spacing:3px;">
        GEYER SMART
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style="
        text-align:center;
        color:#1f2937;
        font-size:60px;
        font-weight:800;">
        Τι είναι το Technical Portal
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align:center;
        color:#6b7280;
        font-size:18px;">
        Η πλατφόρμα τεχνικής υποστήριξης και επαγγελματικής εξέλιξης
    </p>
    """,
    unsafe_allow_html=True
)

st.image(
    "subpages/pictures/Hero_Baner.png",
    use_container_width=True
)

st.markdown(
    "<div style='height:40px'></div>",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# ANALYTICS
# ---------------------------------------------------------

log_event("intro", "visit")

# ---------------------------------------------------------
# Ο ΣΚΟΠΟΣ ΜΑΣ
# ---------------------------------------------------------

st.markdown("## 🎯 Ο Σκοπός μας")

st.markdown(
    """
    <div style="
        background:white;
        padding:30px;
        border-radius:20px;
        border-left:5px solid #008c95;
        box-shadow:0 8px 24px rgba(0,0,0,.06);">

        Σε έναν κόσμο που εξελίσσεται ραγδαία, ο αυτοματισμός δεν είναι πλέον πολυτέλεια,
        αλλά το εργαλείο για έναν εξυπνότερο τρόπο ζωής.

        <br><br>

        Σκοπός αυτής της πλατφόρμας είναι να σας προσφέρει την τεχνική και πληροφοριακή
        υποστήριξη που χρειάζεστε για να δώσετε
        <strong>τεχνική ευφυΐα</strong> στους χώρους σας.

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# ΒΑΣΙΚΕΣ ΑΞΙΕΣ
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div style="
            background:white;
            padding:25px;
            border-radius:18px;
            text-align:center;
            box-shadow:0 6px 18px rgba(0,0,0,.05);">

            <div style="font-size:36px;">⚡</div>

            <h4 style="color:#1f2937;">
            Πιο Ενεργειακά & Αποδοτικά
            </h4>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="
            background:white;
            padding:25px;
            border-radius:18px;
            text-align:center;
            box-shadow:0 6px 18px rgba(0,0,0,.05);">

            <div style="font-size:36px;">🌱</div>

            <h4 style="color:#1f2937;">
            Πιο Βιώσιμα
            </h4>

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div style="
            background:white;
            padding:25px;
            border-radius:18px;
            text-align:center;
            box-shadow:0 6px 18px rgba(0,0,0,.05);">

            <div style="font-size:36px;">📊</div>

            <h4 style="color:#1f2937;">
            Πιο Διαχειρίσιμα
            </h4>

        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# ΤΙ ΘΑ ΒΡΕΙΤΕ ΕΔΩ
# ---------------------------------------------------------

st.markdown("## 🛠 Τι θα βρείτε εδώ")

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        <div style="
            background:white;
            padding:25px;
            border-radius:18px;
            box-shadow:0 6px 18px rgba(0,0,0,.05);">

        ✅ Παρουσίαση Έργων

        <br><br>

        ✅ Επίλυση Προβλημάτων

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div style="
            background:white;
            padding:25px;
            border-radius:18px;
            box-shadow:0 6px 18px rgba(0,0,0,.05);">

        ✅ Live Pricing System

        <br><br>

        ✅ Διαδραστική Επικοινωνία

        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# ΦΙΛΟΣΟΦΙΑ
# ---------------------------------------------------------

st.markdown(
    """
    <div style="
        background:#008c95;
        color:white;
        padding:30px;
        border-radius:20px;">

        <h3 style="color:white;margin-top:0;">
        💡 Η Φιλοσοφία μας
        </h3>

        Πιστεύω στη δύναμη της συνεργασίας.

        <br><br>

        Το site αυτό δεν είναι απλά μια σελίδα πληροφοριών,
        αλλά μια ζωντανή κοινότητα ανταλλαγής ιδεών.

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# FORUM
# ---------------------------------------------------------

st.markdown("## 💬 Η Κοινότητά μας")

st.markdown(
    """
    <div style="
        background:white;
        padding:30px;
        border-radius:20px;
        box-shadow:0 8px 24px rgba(0,0,0,.06);">

        Δημιουργούμε ένα Forum ανταλλαγής ιδεών για να βοηθήσω προσωπικά
        σε κάθε απαίτηση αυτοματισμού που σας ζητείται.

        <br><br>

        Σας προσκαλώ να γίνετε μέρος αυτής της προσπάθειας.

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="
        background:#e8f7f8;
        color:#006f77;
        text-align:center;
        padding:20px;
        border-radius:18px;
        font-size:20px;
        font-weight:700;">

        Βοήθα με να σε βοηθώ, να ανεβούμε το βουνό.

    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")
# ADMIN ANALYTICS (ONLY IF ADMIN)
# ---------------------------------------------------------
if is_admin:
    st.subheader("📊 Analytics Σελίδας Εισαγωγή (Admin Only)")

    try:
        result = supabase.table("analytics").select("*").eq("page", "intro").order("id", desc=True).execute()

        if result.data and len(result.data) > 0:
            df = convert_utc_to_greece(pd.DataFrame(result.data))
            st.success(f"Βρέθηκαν {len(df)} events.")
            st.dataframe(df)
        else:
            st.info("Δεν υπάρχουν ακόμα δεδομένα για τη σελίδα Εισαγωγή.")
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης analytics: {e}")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    """
    <div style="
        text-align:center;
        color:#6b7280;
        font-size:13px;
        padding:20px;">
        © 2026 GEYER Smart Hellas | Technical Portal
    </div>
    """,
    unsafe_allow_html=True
)

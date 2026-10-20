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
# CONTENT
# ---------------------------------------------------------

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("## 🎯 Ο Σκοπός μας")

    st.write(
        """
        Σε έναν κόσμο που εξελίσσεται ραγδαία, ο αυτοματισμός δεν αποτελεί πλέον
        πολυτέλεια αλλά εργαλείο για έναν εξυπνότερο και αποδοτικότερο τρόπο ζωής.

        Το GEYER Smart Technical Portal δημιουργήθηκε για να παρέχει τεχνική
        υποστήριξη, τεχνογνωσία και πρακτικές λύσεις σε επαγγελματίες του χώρου
        των αυτοματισμών και του Smart Home.

        Μέσα από την πλατφόρμα μπορείτε να αποκτήσετε πρόσβαση σε πληροφορίες,
        σχέδια, εκπαιδευτικό υλικό και εργαλεία που θα σας βοηθήσουν στην
        καθημερινή σας εργασία.
        """
    )

    st.markdown(
        "<div style='height:25px'></div>",
        unsafe_allow_html=True
    )

    st.markdown("## 🛠 Τι θα βρείτε εδώ")

    st.write(
        """
        ✅ Παρουσίαση έργων και εφαρμογών

        ✅ Τεχνικές λύσεις και troubleshooting

        ✅ Live Pricing System

        ✅ Τεχνικά σχέδια και διαγράμματα

        ✅ Forum συνεργατών

        ✅ Άμεση τεχνική υποστήριξη
        """
    )

with col2:

    st.info(
        """
### 💡 Η Φιλοσοφία μας

Το Technical Portal δεν είναι απλά μια πλατφόρμα πληροφοριών.

Είναι ένα σημείο συνάντησης συνεργατών,
ηλεκτρολόγων εγκαταστατών και επαγγελματιών
που μοιράζονται γνώση, εμπειρίες και λύσεις.

Στόχος μας είναι η συνεχής εξέλιξη και η
υποστήριξη κάθε συνεργάτη στην καθημερινή του εργασία.
"""
    )

st.write("---")

# ---------------------------------------------------------
# FORUM SECTION
# ---------------------------------------------------------

st.markdown("## 💬 Η Κοινότητά μας")

st.write(
    """
    Δημιουργούμε μία ενεργή κοινότητα ανταλλαγής γνώσεων,
    εμπειριών και τεχνικών λύσεων.

    Μέσα από το Forum μπορείτε να συζητήσετε απαιτήσεις έργων,
    να μοιραστείτε εμπειρίες από εγκαταστάσεις και να λάβετε
    βοήθεια από άλλους επαγγελματίες της κοινότητας.
    """
)

st.success(
    "Βοήθα με να σε βοηθώ, να ανεβούμε το βουνό."
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
st.caption("© 2024 Geyer Technical Portal | Σχεδιασμός & Υλοποίηση: Νεκτάριος Κλαδούχος")

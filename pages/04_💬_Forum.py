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
# PAGE TITLE
# ---------------------------------------------------------
st.markdown(
    "<h1 style='text-align: center; color: #28a745;'>"
    "Καλώς ήρθατε στο Geyer Technical Portal"
    "</h1>",
    unsafe_allow_html=True
)

st.write("---")

# ---------------------------------------------------------
# ANALYTICS — PAGE VISIT
# ---------------------------------------------------------
log_event("intro", "visit")

# ---------------------------------------------------------
# MAIN CONTENT
# ---------------------------------------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎯 Ο Σκοπός μας")
    st.write("""
    Σε έναν κόσμο που εξελίσσεται ραγδαία, ο αυτοματισμός δεν είναι πλέον πολυτέλεια, 
    αλλά το εργαλείο για έναν εξυπνότερο τρόπο ζωής. 
    
    Σκοπός αυτής της πλατφόρμας είναι να σας προσφέρει την τεχνική και πληροφοριακή 
    υποστήριξη που χρειάζεστε για να δώσετε **τεχνική ευφυΐα** στους χώρους σας.
    
    Εστιάζουμε σε λύσεις που κάνουν τα κτίρια:
    * **Πιο Ενεργειακά & Αποδοτικά**
    * **Πιο Βιώσιμα**
    * **Πιο Διαχειρίσιμα**
    """)

    st.markdown("### 🛠 Τι θα βρείτε εδώ")
    st.write("""
    * **Παρουσίαση Έργων**
    * **Επίλυση Προβλημάτων**
    * **Live Pricing System**
    * **Διαδραστική Επικοινωνία**
    """)

with col2:
    st.info("""
    **💡 Η Φιλοσοφία μας**
    Πιστεύω στη δύναμη της συνεργασίας. 
    Το site αυτό δεν είναι απλά μια σελίδα πληροφοριών, 
    αλλά μια ζωντανή κοινότητα ανταλλαγής ιδεών.
    """)

st.write("---")

# ---------------------------------------------------------
# FORUM SECTION
# ---------------------------------------------------------
st.markdown("### 💬 Η Κοινότητά μας (Forum)")
st.write("""
Δημιουργούμε ένα Forum ανταλλαγής ιδεών για να βοηθήσω προσωπικά 
σε κάθε απαίτηση αυτοματισμού που σας ζητείται. 
Σας προσκαλώ να γίνετε μέρος αυτής της προσπάθειας.
""")

st.success("### *«Βοήθα με να σε βοηθώ, να ανεβούμε το βουνό»*")

st.write("---")

# ---------------------------------------------------------
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

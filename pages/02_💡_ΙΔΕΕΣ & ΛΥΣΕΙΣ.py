import streamlit as st
import importlib
from supabase import create_client, Client

# ==================================================
# SUPABASE CONNECTION
# ==================================================
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ==================================================
# LOG EVENT FUNCTION
# ==================================================
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

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Ιδέες & Λύσεις",
    page_icon="💡",
    layout="wide"
)

# ==================================================
# GLOBAL ADMIN MODE (READ ONLY)
# ==================================================
is_admin = st.session_state.get("is_admin", False)

# ==================================================
# CUSTOM CSS
# ==================================================
st.markdown(
    """
    <style>
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #0b3c26 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Make sidebar text inputs readable */
        [data-testid="stSidebar"] input {
            color: black !important;
            background-color: white !important;
        }

        /* Title styling */
        .main-title {
            text-align: center;
            color: #28a745;
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }

        /* Selectbox spacing */
        .stSelectbox {
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# PAGE TITLE
# ==================================================
st.markdown("<h1 class='main-title'>💡 Ιδέες & Έξυπνες Λύσεις</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Επιλέξτε κατηγορία για να δείτε προτάσεις, λύσεις και παραδείγματα.</p>", unsafe_allow_html=True)

# ==================================================
# ANALYTICS — PAGE VISIT
# ==================================================
log_event("idees", "visit")

# ==================================================
# CATEGORIES
# ==================================================
categories = {
    "🏠 Ιδέες για Ενοικιαζόμενα": "rentals",
    "🏢 Ιδέες για Επαγγελματικό Φωτισμό": "prof_lighting",
    "🔥 Έξυπνη Θέρμανση & Ψύξη": "heating_cooling",
    "🚿 Ζεστά Νερά Χρήσης": "hot_water",
    "🖥️ Οπτικοποίηση Συστήματος": "visualization",
    "🎛️ Πρόγραμμα Κεντρικής Μονάδας": "central_unit",
    "🌡️ Θερμικές Ζώνες": "thermal_zones",
    "🌱 Πρόγραμμα Ποτίσματος": "irrigation",
    "🚨 Σενάρια με Ενσωμάτωση Συναγερμού": "alarm_scenarios",
    "⚡ Ενεργειακός Πίνακας": "energy_panel",
    "⏱️ Χρονικά Προγράμματα": "time_programs",
    "📶 Zwave": "zwave",
    "🛠️ Tips Εγκατάστασης": "installation_tips"
}

# ==================================================
# SELECT CATEGORY
# ==================================================
selected_category_name = st.selectbox(
    "🔍 Επιλέξτε Υποενότητα:",
    list(categories.keys())
)

# Log category selection
log_event("idees", "select_category", extra={"category": selected_category_name})

file_name = categories[selected_category_name]
st.divider()

# ==================================================
# LOAD SUBPAGE
# ==================================================
try:
    subpage = importlib.import_module(f"subpages.{file_name}")
    if hasattr(subpage, "show"):
        log_event("idees", "load_subpage", extra={"file": file_name})
        subpage.show()
    else:
        st.error(f"⚠️ Το αρχείο `subpages/{file_name}.py` δεν περιέχει συνάρτηση show().")
except ModuleNotFoundError:
    st.warning(f"⚠️ Το αρχείο `subpages/{file_name}.py` δεν έχει δημιουργηθεί ακόμα.")
except Exception as e:
    st.error(f"❌ Σφάλμα κατά τη φόρτωση της υποσελίδας: {e}")

# ==================================================
# ADMIN ANALYTICS (ONLY IF ADMIN)
# ==================================================
if is_admin:
    st.write("---")
    st.subheader("📊 Analytics (Μόνο για Admin)")

    try:
        result = supabase.table("analytics").select("*").eq("page", "idees").order("id", desc=True).execute()

        if result.data and len(result.data) > 0:
            st.success(f"Βρέθηκαν {len(result.data)} events.")
            st.dataframe(result.data)
        else:
            st.info("Δεν υπάρχουν ακόμα δεδομένα για την ενότητα Ιδέες & Λύσεις.")
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης analytics: {e}")

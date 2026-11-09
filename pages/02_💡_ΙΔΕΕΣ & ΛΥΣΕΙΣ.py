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

st.markdown("""
<styleΑφεντικό 💪, ορίστε το κομμάτι **διορθωμένο και καθαρό**, χωρίς `<br>`, ώστε το Hero να μοιάζει περισσότερο με το Technical Portal:

```python
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
st.markdown("""
<style>

.stApp{
    background-color:#f8fafc;
}

.info-text{
    background:linear-gradient(
        135deg,
        #00757c 0%,
        #00666d 100%
    );
    color:white !important;
    font-size:16px;
    line-height:1.8;
    padding:20px;
    border-radius:24px;
    box-shadow:0 8px 24px rgba(0,0,0,.08);
}

.info-text *{
    color:white !important;
*

[data-testid="stSidebar"]{
    b*ckground*#ffffff;
    border-right:1px soli* #e5e7eb;
    padding-top*20px;
}

[data-testid="stSidebar"]**{
    color:#1f2937 !important;
}*
[data-testid="stSidebar"] input{
*   background:#ffffff !important;
*   color:#111827 !important;
    b*rder-radius:10px !important;
}

h1*
    text-align:center !important;*}

h3*
    text-align:center !important;*    color:#6b7280 *important;
    font-weight:400 !im*ortant;
*   line-height:1.4*!important;
}

p{
*   text-align:center;
}

button[data-baseweb="tab"]{
    font-weight:*00 !important;
}

button[data-baseweb="tab"][aria-selected="true"]{
 *  color:#008c95 !important;
}

div*data-baseweb="tab-list"]{
    just*fy-content:center;
}

</style>
"""* unsafe_allow_html=True)

# ======*==================================*========
# HERO SECTION
# ========*==================================*======

st.title("Ιδέες & Έξυπνες *ύσεις")

st.markdown(
    """
    *## Προτάσεις, εφαρμογές και πρακτι*ά παραδείγματα

    ### Smart Home*&*Building Automation
    """
)

st.*rite("")
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
st.write("")
st.write("---")

st.caption(
    "© 2026 GEYER Smart Hellas | Ιδέες & Έξυπνες Λύσεις"
)
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

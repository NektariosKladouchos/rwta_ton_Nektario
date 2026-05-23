import streamlit as st
import importlib

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Ιδέες & Λύσεις",
    page_icon="💡",
    layout="wide"
)

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
# CATEGORIES
# ==================================================
categories = {
    "🏠 Ιδέες για Ενοικιαζόμενα": "rentals",
    "🏢 Ιδέες για Επαγγελματικό Φωτισμό": "prof_lighting",
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

file_name = categories[selected_category_name]
st.divider()

# ==================================================
# LOAD SUBPAGE
# ==================================================
try:
    subpage = importlib.import_module(f"subpages.{file_name}")
    if hasattr(subpage, "show"):
        subpage.show()
    else:
        st.error(f"⚠️ Το αρχείο `subpages/{file_name}.py` δεν περιέχει συνάρτηση show().")
except ModuleNotFoundError:
    st.warning(f"⚠️ Το αρχείο `subpages/{file_name}.py` δεν έχει δημιουργηθεί ακόμα.")
except Exception as e:
    st.error(f"❌ Σφάλμα κατά τη φόρτωση της υποσελίδας: {e}")

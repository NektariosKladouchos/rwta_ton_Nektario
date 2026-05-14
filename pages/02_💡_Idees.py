import streamlit as st
import importlib

# ==================================================
# SETTINGS
# ==================================================
st.set_page_config(
    page_title="Ιδέες & Λύσεις",
    page_icon="💡",
    layout="centered"
)

# Custom CSS για το πράσινο μενού
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] { background-color: #0b3c26 !important; }
        [data-testid="stSidebarNav"] span { color: white !important; }
        [data-testid="stSidebarNav"] svg { fill: white !important; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💡 Ιδέες & Έξυπνες Λύσεις")

# ==================================================
# ΔΙΑΔΡΑΣΤΙΚΟ ΜΕΝΟΥ (Όνομα Ενότητας : Όνομα Αρχείου Python)
# ==================================================
categories = {
    "🖥️ Οπτικοποίηση Συστήματος": "visualization",
    "🏠 Ιδέες για Ενοικιαζόμενα": "rentals",
    "🏢 Ιδέες για Επαγγελματικό Φωτισμό": "prof_lighting"
}

selected_category_name = st.selectbox(
    "🔍 Επιλέξτε Υποενότητα:",
    list(categories.keys())
)

file_name = categories[selected_category_name]
st.divider()

# ==================================================
# ΔΥΝΑΜΙΚΗ ΦΟΡΤΩΣΗ ΤΟΥ ΑΡΧΕΙΟΥ
# ==================================================
try:
    # Φορτώνει δυναμικά το αρχείο από τον φάκελο subpages
    subpage = importlib.import_module(f"subpages.{file_name}")
    # Εκτελεί τη συνάρτηση show() που γράψαμε μέσα στο αρχείο
    subpage.show()
except ModuleNotFoundError:
    st.warning(f"⚠️ Το αρχείο `subpages/{file_name}.py` δεν έχει δημιουργηθεί ακόμα.")
except Exception as e:
    st.error(f"❌ Σφάλμα κατά τη φόρτωση της υποσελίδας: {e}")

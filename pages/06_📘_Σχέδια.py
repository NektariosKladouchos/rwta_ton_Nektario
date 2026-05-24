import streamlit as st
import os

st.set_page_config(page_title="📘 Τεχνικά Σχέδια", page_icon="📘", layout="wide")

# ---------------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------------
st.title("📘 Τεχνικά Σχέδια")

st.write("---")

tab1, tab2, tab3 = st.tabs(["🔌 Σχέδια Σύνδεσης", "⚙️ Τρόποι Προγραμματισμού", "🎓 Μαθήματα"])

# ---------------------------------------------------------
# TAB 1 — ΣΧΕΔΙΑ ΣΥΝΔΕΣΗΣ
# ---------------------------------------------------------
with tab1:

    st.subheader("🔌 Σχέδια Σύνδεσης")

    # ΣΩΣΤΟ PATH ΓΙΑ ΤΟ ΠΕΡΙΒΑΛΛΟΝ ΣΟΥ
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SXEDIA_DIR = os.path.join(BASE_DIR, "subpages", "pictures", "sxedia")

    # DEBUG
    st.write("### 🐞 DEBUG INFO")
    st.write("📁 BASE_DIR:", BASE_DIR)
    st.write("📁 SXEDIA_DIR:", SXEDIA_DIR)

    categories = {
        "Φωτισμός": "fotismos",
        "Μοτέρ Σκίασης": "moter",
        "HVAC": "hvac",
        "Ζεστά Νερά": "znx",
        "Συναγερμός": "synagermos",
        "Αισθητήρες": "aisthitires",
        "Σενάρια": "senaria",
        "Μετρητές": "metrites",
        "Άλλα": "alla"
    }

    cat_choice = st.selectbox("Επιλέξτε κατηγορία σχεδίων:", list(categories.keys()))
    folder = os.path.join(SXEDIA_DIR, categories[cat_choice])

    # DEBUG
    st.write("📁 Selected folder:", folder)
    st.write("📁 Folder exists:", os.path.exists(folder))

    if os.path.exists(folder):
        st.write("📄 Files in folder:", os.listdir(folder))
    else:
        st.warning("⚠️ Ο φάκελος δεν υπάρχει ακόμα.")
        st.stop()

    files = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if not files:
        st.info("ℹ️ Δεν υπάρχουν σχέδια.")
        st.stop()

    choice = st.selectbox("Επιλέξτε σχέδιο:", files)
    img_path = os.path.join(folder, choice)

    st.image(img_path, use_container_width=True)

    st.markdown("### 📘 Τίτλος Σχεδίου")
    st.write(choice.replace(".png", "").replace(".jpg", "").replace("_", " ").title())

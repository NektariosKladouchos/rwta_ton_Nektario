import streamlit as st
import os
import pandas as pd
import pytz
from supabase import create_client, Client

# ==================================================
# SUPABASE CONNECTION
# ==================================================
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ==================================================
# LOG EVENT
# ==================================================
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

# ==================================================
# TIMEZONE CONVERSION (UTC → GREECE)
# ==================================================
def convert_utc_to_greece(ts):
    try:
        greece = pytz.timezone("Europe/Athens")
        return pd.to_datetime(ts).tz_convert(greece)
    except:
        return ts

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Τεχνικά Σχέδια",
    page_icon="📘",
    layout="wide"
)

# ==================================================
# ADMIN MODE
# ==================================================
is_admin = st.session_state.get("is_admin", False)

# ==================================================
# PAGE TITLE
# ==================================================
st.markdown(
    "<h1 style='text-align:center; color:#28a745;'>📘 Τεχνικά Σχέδια</h1>",
    unsafe_allow_html=True
)
st.write("---")

# LOG VISIT
log_event("sxedia", "visit")

# ==================================================
# PATHS
# ==================================================
BASE_DIR = os.path.dirname(__file__)
SXEDIA_DIR = os.path.join(BASE_DIR, "sxedia")

CATEGORIES = {
    "Φωτισμός": "fotismos",
    "Ρολά": "rola",
    "Συναγερμός": "synagermos"
}

# ==================================================
# LOAD FILES
# ==================================================
def load_designs(folder):
    path = os.path.join(SXEDIA_DIR, folder)
    if not os.path.exists(path):
        return []

    files = os.listdir(path)
    images = [f for f in files if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    designs = []
    for img in images:
        name = os.path.splitext(img)[0]
        txt_path = os.path.join(path, name + ".txt")

        description = "Δεν υπάρχει περιγραφή."
        if os.path.exists(txt_path):
            with open(txt_path, "r", encoding="utf-8") as f:
                description = f.read()

        designs.append({
            "image": os.path.join(path, img),
            "name": name,
            "description": description
        })

    return designs

# ==================================================
# TABS
# ==================================================
tabs = st.tabs(list(CATEGORIES.keys()))

for tab, (cat_name, folder) in zip(tabs, CATEGORIES.items()):
    with tab:
        st.markdown(f"### 📂 {cat_name}")

        designs = load_designs(folder)

        if not designs:
            st.info("Δεν υπάρχουν διαθέσιμα σχέδια.")
        else:
            for d in designs:
                with st.container(border=True):
                    st.markdown(f"### 🖼 {d['name']}")
                    st.image(d["image"], use_container_width=True)
                    st.markdown("#### 📄 Περιγραφή")
                    st.write(d["description"])
                    st.write("---")

# ==================================================
# ADMIN ANALYTICS
# ==================================================
if is_admin:
    st.write("---")
    st.subheader("📊 Analytics Σχεδίων (Admin Only)")

    try:
        result = supabase.table("analytics").select("*").eq("page", "sxedia").order("id", desc=True).execute()

        if result.data:
            df = pd.DataFrame(result.data)
            df["timestamp"] = df["timestamp"].apply(convert_utc_to_greece)
            st.dataframe(df)
        else:
            st.info("Δεν υπάρχουν ακόμα δεδομένα.")
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης analytics: {e}")

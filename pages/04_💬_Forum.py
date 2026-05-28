import streamlit as st
import pandas as pd
from datetime import datetime
from supabase import create_client, Client
import pytz

# ==================================================
# SETTINGS & INITIALIZATION
# ==================================================

st.set_page_config(
    page_title="Public Forum",
    page_icon="💬",
    layout="centered"
)

ADMIN_PASSWORD = "geyer123"

# CSS για λευκά γράμματα στο sidebar
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #0b3c26 !important;
        }
        [data-testid="stSidebarNav"] span,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: white !important;
        }
        [data-testid="stSidebarNav"] svg {
            fill: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# SUPABASE CONNECTION
# ==================================================
@st.cache_resource
def init_supabase() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)

supabase = init_supabase()

# ==================================================
# TIMEZONE CONVERSION (UTC → GREECE)
# ==================================================
def convert_to_greece_time(ts_str):
    try:
        utc_time = pd.to_datetime(ts_str).tz_localize("UTC")
        gr_tz = pytz.timezone("Europe/Athens")
        return utc_time.tz_convert(gr_tz).strftime("%d/%m/%Y %H:%M")
    except:
        return ts_str

# ==================================================
# LOAD DATA
# ==================================================
def load_data():
    try:
        response = supabase.table("forum_data").select("*").execute()
        df = pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης: {e}")
        return pd.DataFrame(columns=["id", "date", "name", "question", "answer"])

    if df.empty:
        return pd.DataFrame(columns=["id", "date", "name", "question", "answer"])

    df = df.fillna("")
    df["id"] = df["id"].astype(int)

    # Μετατροπή ώρας Ελλάδας
    df["date"] = df["date"].apply(convert_to_greece_time)

    return df

df = load_data()

# ==================================================
# TITLE
# ==================================================
st.title("💬 Public Forum")
st.write("Γράψε την ερώτησή σου και δες απαντήσεις από τον διαχειριστή.")

# ==================================================
# QUESTION FORM
# ==================================================
with st.expander("➕ Νέα Ερώτηση", expanded=False):
    with st.form("question_form", clear_on_submit=True):
        name = st.text_input("Όνομα")
        question = st.text_area("Ερώτηση", height=120)
        submit_question = st.form_submit_button("Υποβολή")

        if submit_question:
            if not name.strip():
                st.warning("Συμπλήρωσε όνομα.")
            elif not question.strip():
                st.warning("Συμπλήρωσε ερώτηση.")
            else:
                new_row = {
                    "date": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                    "name": str(name),
                    "question": str(question),
                    "answer": ""
                }
                supabase.table("forum_data").insert(new_row).execute()
                st.success("Η ερώτηση καταχωρήθηκε!")
                st.rerun()

# ==================================================
# QUESTIONS LIST
# ==================================================
st.divider()
st.subheader("📋 Ερωτήσεις")

df = load_data()

if len(df) == 0:
    st.info("Δεν υπάρχουν ακόμη ερωτήσεις.")
else:
    df_sorted = df.sort_values(by="id", ascending=False)
    for _, row in df_sorted.iterrows():
        with st.container(border=True):
            st.markdown(f"### ❓ {row['question']}")
            st.caption(f"👤 {row['name']} | 🕒 {row['date']}")

            if str(row["answer"]).strip() != "":
                st.success(f"✅ Απάντηση:\n\n{row['answer']}")

# ==================================================
# ADMIN PANEL
# ==================================================
st.sidebar.title("🔒 Admin Panel")
admin_password = st.sidebar.text_input("Password", type="password")

if admin_password == ADMIN_PASSWORD:
    st.sidebar.success("Επιτυχής σύνδεση")
    df = load_data()

    if len(df) > 0:
        selected_id = st.sidebar.selectbox("Επιλογή Question ID", df["id"].tolist())
        selected_row = df[df["id"] == int(selected_id)].iloc[0]

        st.sidebar.markdown("---")
        st.sidebar.write("### Ερώτηση")
        st.sidebar.info(selected_row["question"])

        answer_text = st.sidebar.text_area(
            "Απάντηση",
            value=str(selected_row["answer"]),
            height=180
        )

        # SAVE ANSWER
        if st.sidebar.button("💾 Αποθήκευση Απάντησης"):
            supabase.table("forum_data").update({"answer": str(answer_text)}).eq("id", int(selected_id)).execute()
            st.sidebar.success("Η απάντηση αποθηκεύτηκε!")
            st.rerun()

        st.sidebar.markdown("---")

        # DELETE QUESTION
        if st.sidebar.button("🗑️ Διαγραφή Ερώτησης"):
            supabase.table("forum_data").delete().eq("id", int(selected_id)).execute()
            st.sidebar.success("Η ερώτηση διαγράφηκε!")
            st.rerun()
    else:
        st.sidebar.info("Δεν υπάρχουν ερωτήσεις.")
else:
    st.sidebar.caption("Πρόσβαση μόνο διαχειριστή")

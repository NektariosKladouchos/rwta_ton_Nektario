import streamlit as st
import pandas as pd
from datetime import datetime
from supabase import create_client, Client

# ==================================================
# SETTINGS & INITIALIZATION
# ==================================================

st.set_page_config(
    page_title="Public Forum",
    page_icon="💬",
    layout="centered"
)

ADMIN_PASSWORD = "geyer123"

# CSS για να είναι όλα τα γράμματα λευκά και ευανάγνωστα στο μενού
st.markdown("""
<style>

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #0b3c26 !important;
        padding-top: 30px;
    }

    /* Sidebar text — WHITE */
    [data-testid="stSidebar"] * {
        color: white !important;
        font-weight: 500 !important;
    }

    /* Sidebar icons — WHITE */
    [data-testid="stSidebar"] svg {
        fill: white !important;
    }

    /* Collapse button "<" — WHITE */
    button[kind="header"] svg {
        fill: white !important;
    }

    /* Main background */
    .stApp {
        background-color: #f8f9fa !important;
    }

    /* Forum question card */
    .forum-card {
        background-color: white;
        border: 2px solid #0b3c26;
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 18px;
    }

    /* Answer box */
    .answer-box {
        background-color: #e8f4e8;
        border-left: 5px solid #0b3c26;
        padding: 12px;
        border-radius: 6px;
        margin-top: 10px;
    }

    /* Header */
    .main-header {
        text-align: center;
        margin-bottom: 20px;
    }
    .main-header h1 {
        color: #0b3c26;
        font-weight: 700;
    }

</style>
""", unsafe_allow_html=True)


# Σύνδεση με Supabase μέσω Secrets
@st.cache_resource
def init_supabase() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)

supabase = init_supabase()

# ==================================================
# FUNCTIONS
# ==================================================

def load_data():
    try:
        response = supabase.table("forum_data").select("*").execute()
        df = pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης: {e}")
        df = pd.DataFrame(columns=["id", "date", "name", "question", "answer"])
    
    if df.empty:
        df = pd.DataFrame(columns=["id", "date", "name", "question", "answer"])
    else:
        df = df.fillna("")
        df["id"] = df["id"].astype(int)
        
    return df

# ==================================================
# LOAD DATA
# ==================================================

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
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
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
        
        # Εδώ διορθώθηκε το .iloc[0] για να παίρνει σωστά τη γραμμή
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

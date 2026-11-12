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
    layout="wide"
)

ADMIN_PASSWORD = "geyer123"

# CSS για λευκά γράμματα στο sidebar
st.markdown(
    """
    <style>

    .stApp{
        background-color:#f8fafc;
    }

    /* SIDEBAR */

    [data-testid="stSidebar"]{
        background:#ffffff;
        border-right:1px solid #e5e7eb;
        padding-top:20px;
    }

    [data-testid="stSidebar"] *{
        color:#1f2937 !important;
    }

    [data-testid="stSidebar"] input{
        background:#ffffff !important;
        color:#111827 !important;
        border-radius:10px !important;
    }

    [data-testid="stSidebarNav"] svg{
        fill:#1f2937 !important;
    }

    /* HERO */

    h1{
        color:#1F2937 !important;
        font-size:42px !important;
        font-weight:800 !important;
        text-align:center !important;
    }

    h3{
        color:#64748B !important;
        font-size:18px !important;
        font-weight:400 !important;
        text-align:center !important;
        line-height:1.4 !important;
    }

    /* QUESTION CARDS */

    .question-card{
        background:#ffffff;
        padding:25px;
        border-radius:24px;
        box-shadow:0 8px 24px rgba(0,0,0,.08);
        border-left:5px solid #008c95;
        margin-bottom:10px;
    }

    /* ANSWER BOXES */

    div[data-testid="stAlert"]{
        background:linear-gradient(
            135deg,
            #00757c 0%,
            #00666d 100%
        ) !important;

        color:white !important;
        border:none !important;
        border-radius:24px !important;
        box-shadow:0 8px 24px rgba(0,0,0,.08) !important;
    }

    div[data-testid="stAlert"] *{
        color:white !important;
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
# LOG EVENT
# ==================================================
from subpages.analytics_utils import log_event
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
st.markdown(
    """
    <p style="
        text-align:center;
        color:#008C95;
        font-size:14px;
        font-weight:700;
        letter-spacing:5px;
        margin-bottom:10px;
    ">
        GEYER SMART
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")

st.title("💬 Forum Υποστήριξης")

st.markdown(
    """
    ### Ερωτήσεις, απαντήσεις και ανταλλαγή γνώσης

    ### για εγκαταστάτες και συνεργάτες GEYER Smart
    """
)

st.write("")
st.write("")

# --------------------------------------------------
# LOG PAGE VISIT
# --------------------------------------------------
log_event("forum", "visit")

# ==================================================
# QUESTION FORM
# ==================================================
with st.expander("✍️ Νέα Ερώτηση προς την Τεχνική Υποστήριξη", expanded=True):
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

                # LOG EVENT
                log_event("forum", "new_question", name)

                st.success("Η ερώτηση καταχωρήθηκε!")
                st.rerun()

# ==================================================
# QUESTIONS LIST
# ==================================================

st.divider()

search_term = st.text_input(
    "🔍 Αναζήτηση ερώτησης"
)

df = load_data()

if len(df) == 0:

    st.info("Δεν υπάρχουν ακόμη ερωτήσεις.")

else:

    df_sorted = df.sort_values(by="id", ascending=False)

    if search_term.strip():

        df_sorted = df_sorted[
            df_sorted["question"].str.contains(
                search_term,
                case=False,
                na=False
            )
        ]

    for _, row in df_sorted.iterrows():

        with st.container(border=True):

            st.subheader(f"❓ {row['question']}")

            st.caption(
                f"👤 {row['name']} | 🕒 {row['date']}"
            )

            if str(row["answer"]).strip() != "":

                st.markdown(
    f"""
    <div style="
        background:linear-gradient(
            135deg,
            #00757c 0%,
            #00666d 100%
        );
        color:white;
        padding:14px 20px;
        border-radius:24px;
        box-shadow:0 8px 24px rgba(0,0,0,.08);
        margin-top:8px;
        margin-bottom:10px;
    ">

    <strong>✅ Απάντηση</strong>

    <br>

    {row['answer']}

    </div>
    """,
    unsafe_allow_html=True
)
        st.write("")
# ==================================================
# ADMIN PANEL
# ==================================================
st.sidebar.markdown("### 🔒 Admin")
admin_password = st.sidebar.text_input("Password", type="password")

if admin_password == ADMIN_PASSWORD:
    st.session_state.is_admin = True
    st.sidebar.success("Επιτυχής σύνδεση")

    df = load_data()

    if len(df) > 0:
        selected_id = st.sidebar.selectbox("Επιλογή Question ID", df["id"].tolist())
        selected_row = df[df["id"] == int(selected_id)].iloc[0]

        st.sidebar.markdown("---")
        st.sidebar.write("### Ερώτηση")

        st.sidebar.markdown(
        f"""
        <div style="
        background:#00757c;
        color:white;
        padding:12px;
        border-radius:12px;
        text-align:left;
        font-weight:500;
        line-height:1.5;
        ">
        {selected_row["question"]}
    </div>
    """,
    unsafe_allow_html=True
)
        answer_text = st.sidebar.text_area(
            "Απάντηση",
            value=str(selected_row["answer"]),
            height=180
        )

        # SAVE ANSWER
        if st.sidebar.button("💾 Αποθήκευση Απάντησης"):
            supabase.table("forum_data").update({"answer": str(answer_text)}).eq("id", int(selected_id)).execute()

            # LOG EVENT
            log_event("forum", "new_answer", "admin")

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
# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.write("")
st.write("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#9ca3af;
        font-size:13px;
        padding:15px 0;
    ">
        © 2026 GEYER Smart Hellas | Forum Υποστήριξης
    </div>
    """,
    unsafe_allow_html=True
)
# ==================================================
# ADMIN ANALYTICS
# ==================================================
if st.session_state.get("is_admin", False):
    st.write("---")
    st.subheader("📊 Analytics Forum (Admin Only)")

    try:
        result = supabase.table("analytics").select("*").eq("page", "forum").order("id", desc=True).execute()

        if result.data:
            df_analytics = pd.DataFrame(result.data)
            df_analytics["timestamp"] = df_analytics["timestamp"].apply(convert_to_greece_time)
            st.dataframe(df_analytics)
        else:
            st.info("Δεν υπάρχουν ακόμα δεδομένα.")
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης analytics: {e}")

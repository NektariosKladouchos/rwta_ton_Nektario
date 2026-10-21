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
# GEYER THEME
# ---------------------------------------------------------


st.markdown(
    """
    <style>
   .geyer-card{
    background:#0B7F86;
    color:white;
    padding:22px;
    border-radius:18px;
    box-shadow:0 8px 24px rgba(0,0,0,.08);
    min-height:140px;
}

.geyer-card h4{
    color:white !important;
    margin-bottom:12px;
}

.geyer-card p{
    color:white !important;
    margin:0;
    line-height:1.7;
}

    [data-testid="stAppViewContainer"]{
        background:#f7f8fa;
    }


    .main .block-container{
        max-width:1400px;
        padding-top:2rem;
        padding-bottom:3rem;
    }
    /* NAVIGATION */

    [data-testid="stSidebarNav"] a{
        border-radius:10px;
        margin-bottom:4px;
    }

    [data-testid="stSidebarNav"]::before{
        content:"GEYER SMART";
        display:block;
        padding:15px 20px;

        color:#008c95;
        font-size:13px;
        font-weight:700;
        letter-spacing:3px;
    }

    [data-testid="stSidebarNav"] a:hover{
        background:rgba(0,140,149,0.08);
    }

    [data-testid="stSidebarNav"] a[aria-current="page"]{
        background:rgba(0,140,149,0.12);
        color:#008c95 !important;
        font-weight:600;
    }

    h1,h2,h3{
        color:#1f2937;
    }

div[data-baseweb="notification"]{
    background:#0B7F86 !important;
    border-left:4px solid #086D73 !important;
    border-radius:18px !important;
    box-shadow:0 8px 24px rgba(0,0,0,.08) !important;
}

div[data-baseweb="notification"] p,
div[data-baseweb="notification"] strong,
div[data-baseweb="notification"] span{
    color:white !important;
}


[data-testid="column"] {
    background:#E6F4F2;
    border-radius:18px;
    padding:20px;
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
}

[data-testid="stCaptionContainer"]{
    text-align:center;
}

[data-testid="stCaptionContainer"] p{
    color:#008C95 !important;
    font-weight:700 !important;
    letter-spacing:5px;
}

    </style>
    """,
    unsafe_allow_html=True
)
# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------

st.caption("GEYER SMART")

st.write("")

st.title("Τι είναι το Technical Portal")

st.markdown(
    """
    ### Το σημείο αναφοράς για τεχνική υποστήριξη,

    ### γνώση και συνεργασία στον κόσμο του Smart Home
    """
)

st.write("")
st.write("")
col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
⚡ Πιο Ενεργειακά

Εξοικονόμηση ενέργειας.
""")

with col2:
    st.success("""
🌱 Πιο Βιώσιμα

Λύσεις νέας γενιάς για σύγχρονα κτίρια.
""")

with col3:
    st.success("""
📊 Πιο Διαχειρίσιμα

Καλύτερος έλεγχος εγκαταστάσεων.
""")
st.write("")

# ---------------------------------------------------------
# ANALYTICS
# ---------------------------------------------------------


st.markdown(
    "<div style='height:50px'></div>",
    unsafe_allow_html=True
)

st.header("🎯 Ο Σκοπός μας")
st.write("")
st.markdown("""
Σε έναν κόσμο που εξελίσσεται ραγδαία, ο αυτοματισμός δεν αποτελεί πλέον πολυτέλεια αλλά ένα ουσιαστικό εργαλείο για έναν πιο αποδοτικό και έξυπνο τρόπο ζωής.

Η πλατφόρμα αυτή δημιουργήθηκε για να προσφέρει τεχνική γνώση, καθοδήγηση και πρακτική υποστήριξη, βοηθώντας επαγγελματίες και συνεργάτες να αξιοποιήσουν στο μέγιστο τις δυνατότητες του οικοσυστήματος GEYER Smart.
""")
st.write("")

# ---------------------------------------------------------
# ΤΙ ΘΑ ΒΡΕΙΤΕ ΕΔΩ
# ---------------------------------------------------------

st.header("🛠 Τι θα βρείτε εδώ")

st.write("")

col1, col2 = st.columns(2)

with col1:

    st.success("""
📁 **Παρουσίαση Έργων**

Παρουσίαση πραγματικών εφαρμογών και εγκαταστάσεων.
""")

    st.write("")

    st.success("""
🛠 **Επίλυση Προβλημάτων**

Τεχνικές λύσεις και troubleshooting εγκαταστάσεων.
""")

with col2:

    st.success("""
💰 **Live Pricing System**

Υπολογισμός κόστους και πληροφορίες προϊόντων.
""")

    st.write("")

    st.success("""
💬 **Διαδραστική Επικοινωνία**

Συνεργασία και ανταλλαγή τεχνογνωσίας.
""")

st.write("")
st.write("")
# ---------------------------------------------------------
# Η ΦΙΛΟΣΟΦΙΑ ΜΑΣ
# ---------------------------------------------------------

st.header("💡 Η Φιλοσοφία μας")

st.markdown("""
Πιστεύω στη δύναμη της συνεργασίας.

Το site αυτό δεν είναι απλά μια σελίδα πληροφοριών.

Είναι μια ζωντανή κοινότητα ανταλλαγής ιδεών, τεχνογνωσίας και εμπειριών, με στόχο τη συνεχή εξέλιξη και υποστήριξη των επαγγελματιών του χώρου.
""")

st.write("")
st.write("")

# ---------------------------------------------------------
# Η ΚΟΙΝΟΤΗΤΑ ΜΑΣ
# ---------------------------------------------------------

st.header("💬 Η Κοινότητά μας")

st.markdown("""
Ανταλλάσσουμε ιδέες, τεχνογνωσία και λύσεις, δημιουργώντας μια ενεργή κοινότητα επαγγελματιών Smart Home.

Σας προσκαλώ να γίνετε μέρος της.
""")

st.write("")
st.success(
    "🤝 Βοήθα με να σε βοηθώ, να ανεβούμε το βουνό."
)


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
            st.success("Δεν υπάρχουν ακόμα δεδομένα για τη σελίδα Εισαγωγή.")
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης analytics: {e}")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    "<div style='height:30px'></div>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="
        text-align:center;
        color:#6b7280;
        font-size:13px;
        padding:20px;">
        © 2026 GEYER Smart Hellas | Technical Portal
    </div>
    """,
    unsafe_allow_html=True
)

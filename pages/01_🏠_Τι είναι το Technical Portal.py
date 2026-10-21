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
    background:#ffffff !important;
    border-left:4px solid #008C95 !important;
    border-radius:20px !important;
    box-shadow:0 8px 24px rgba(0,0,0,.06) !important;
    padding:1rem !important;
}

div[data-baseweb="notification"] *{
    color:#1F2937 !important;
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
    st.info("""
⚡ **Τεχνική Υποστήριξη**

Άμεση πρόσβαση σε λύσεις, οδηγούς και troubleshooting.
""")

with col2:
    st.info("""
📚 **Τεχνογνωσία**

Γνώση, εμπειρία και βέλτιστες πρακτικές εγκατάστασης.
""")

with col3:
    st.info("""
🤝 **Συνεργασία**

Ανταλλαγή ιδεών και υποστήριξη από την κοινότητα.
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
col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
⚡ **Πιο Ενεργειακά**

Μείωση κατανάλωσης και βελτίωση απόδοσης.
""")

with col2:
    st.info("""
🌱 **Πιο Βιώσιμα**

Λύσεις νέας γενιάς για σύγχρονα κτίρια.
""")

with col3:
    st.info("""
📊 **Πιο Διαχειρίσιμα**

Καλύτερος έλεγχος εγκαταστάσεων.
""")
# ---------------------------------------------------------
# ΤΙ ΘΑ ΒΡΕΙΤΕ ΕΔΩ
# ---------------------------------------------------------

st.markdown("## 🛠 Τι θα βρείτε εδώ")

st.markdown(
    "<div style='height:15px'></div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="
            background:white;
            padding:20px;
            border-radius:16px;
            color:#008c95;
            font-size:20px;
            font-weight:700;
            margin-bottom:12px;
            border-left:6px solid #008c95;
            box-shadow:0 8px 24px rgba(0,0,0,.06);
        ">

        📁 Παρουσίαση Έργων

        Παρουσίαση πραγματικών εφαρμογών και εγκαταστάσεων.

        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<div style='height:20px'></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            background:white;
            padding:20px;
            border-radius:16px;
            color:#008c95;
            font-size:20px;
            font-weight:700;
            margin-bottom:12px;
            border-left:6px solid #008c95;
            box-shadow:0 8px 24px rgba(0,0,0,.06);
        ">

        🛠 Επίλυση Προβλημάτων

        Τεχνικές λύσεις και troubleshooting εγκαταστάσεων.

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="
            background:white;
            padding:20px;
            font-size:16px;
            color:#008c95;
            font-size:20px;
            font-weight:700;
            margin-bottom:12px;
            border-left:6px solid #008c95;
            box-shadow:0 8px 24px rgba(0,0,0,.06);
        ">

        💰 Live Pricing System

        Υπολογισμός κόστους και πληροφορίες προϊόντων.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<div style='height:20px'></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            background:white;
            padding:20px;
            border-radius:16px;
            color:#008c95;
            font-size:20px;
            font-weight:700;
            margin-bottom:12px;
            border-left:6px solid #008c95;
            box-shadow:0 8px 24px rgba(0,0,0,.06);
        ">

        💬 Διαδραστική Επικοινωνία

        Συνεργασία και ανταλλαγή τεχνογνωσίας.

        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    "<div style='height:40px'></div>",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Η ΦΙΛΟΣΟΦΙΑ ΜΑΣ
# ---------------------------------------------------------
st.markdown(
    """
    <div style="
        background:linear-gradient(
            135deg,
            #008c95 0%,
            #006f77 100%
        );
        color:white;
        font-size:18px;
        font-weight:700;
        margin-bottom:20px;
        padding:40px;
        border-radius:26px;
        box-shadow:0 12px 32px rgba(0,0,0,.10);
        line-height:1.9;
    ">

    <h3 style="color:white;margin-top:0;">
    💡 Η Φιλοσοφία μας
     </h3>
      Πιστεύω στη δύναμη της συνεργασίας.
      Το site αυτό δεν είναι απλά μια σελίδα πληροφοριών.
      Είναι μια ζωντανή κοινότητα ανταλλαγής ιδεών,
      τεχνογνωσίας και εμπειριών.

    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<div style='height:40px'></div>",
    unsafe_allow_html=True
)
# ---------------------------------------------------------
# Η ΚΟΙΝΟΤΗΤΑ ΜΑΣ
# ---------------------------------------------------------
st.markdown(
    """
    <div style="
        background:white;
        border-left:6px solid #008c95;
        padding:40px;
        border-radius:24px;
        box-shadow:0 12px 32px rgba(0,0,0,.08);
        color:#1f2937;
        font-size:12px;
        font-weight:700;
        margin-bottom:20px;
        line-height:2;
    ">

        💬 Η Κοινότητά μας
        Δημιουργούμε ένα Forum ανταλλαγής ιδεών για να βοηθήσω προσωπικάσε κάθε απαίτηση αυτοματισμού που σας ζητείται.
        Σας προσκαλώ να γίνετε μέρος αυτής της προσπάθειας.

    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<div style='height:40px'></div>",
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style="
        background:#e8f7f8;
        border-left:6px solid #008c95;
        color:#006f77;
        padding:20px;
        border-radius:18px;
        text-align:center;
        font-size:12px;
        font-weight:700;
    ">
        Βοήθα με να σε βοηθώ, να ανεβούμε το βουνό.
    </div>
        """,
        unsafe_allow_html=True
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
            st.info("Δεν υπάρχουν ακόμα δεδομένα για τη σελίδα Εισαγωγή.")
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

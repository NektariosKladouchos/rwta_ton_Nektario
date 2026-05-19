st.markdown(""")
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

    /* Input fields text color (FIX) */
    input, textarea, .stTextInput input, .stTextArea textarea {
        color: black !important;      /* Το κείμενο που γράφεις */
    }

    /* Placeholder text */
    input::placeholder,
    textarea::placeholder {
        color: #444 !important;       /* Σκούρο γκρι placeholder */
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

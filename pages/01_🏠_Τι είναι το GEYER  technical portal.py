import streamlit as st

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Εισαγωγή - Geyer Portal",
    page_icon="🏠",
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

        /* Hide Streamlit top bar if desired */
        header {visibility: hidden;}

        /* Main title */
        .main-title {
            text-align: center;
            color: #28a745;
            font-size: 40px;
            font-weight: 800;
            margin-bottom: 5px;
        }

        .subtitle {
            text-align: center;
            color: #777;
            font-size: 20px;
            margin-bottom: 25px;
        }

        /* Section titles */
        h3 {
            color: #28a745 !important;
            font-weight: 700 !important;
        }

        /* Philosophy box */
        .philosophy-box {
            background-color: #e8f5e9;
            padding: 18px;
            border-radius: 10px;
            border-left: 5px solid #28a745;
            margin-bottom: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# TITLES
# ==================================================
st.markdown("<h1 class='main-title'>Καλώς ήρθατε στο Geyer Technical Portal</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Με την υπογραφή του Νεκτάριου Κλαδούχου</p>", unsafe_allow_html=True)
st.write("---")

# ==================================================
# MAIN CONTENT
# ==================================================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎯 Ο Σκοπός μας")
    st.write("""
    Σε έναν κόσμο που εξελίσσεται ραγδαία, ο αυτοματισμός δεν είναι πλέον πολυτέλεια, αλλά το εργαλείο για έναν εξυπνότερο τρόπο ζωής.  
    Σκοπός αυτής της πλατφόρμας είναι να σας προσφέρει την τεχνική και πληροφοριακή υποστήριξη που χρειάζεστε για να δώσετε **τεχνική ευφυΐα** στους χώρους σας.

    Εστιάζουμε σε λύσεις που κάνουν τα κτίρια:
    - **Πιο Ενεργειακά & Αποδοτικά**  
    - **Πιο Βιώσιμα**  
    - **Πιο Διαχειρίσιμα**  
    """)

    st.markdown("### 🛠 Τι θα βρείτε εδώ")
    st.write("""
    - **Παρουσίαση Έργων**  
    - **Επίλυση Προβλημάτων**  
    - **Live Pricing System**  
    - **Διαδραστική Επικοινωνία**  
    """)

with col2:
    st.markdown("<div class='philosophy-box'>", unsafe_allow_html=True)
    st.markdown("**💡 Η Φιλοσοφία μας**")
    st.write("Πιστεύω στη δύναμη της συνεργασίας. Το site αυτό δεν είναι απλά μια σελίδα πληροφοριών, αλλά μια ζωντανή κοινότητα ανταλλαγής ιδεών.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Εικόνα από το έργο σου (όπως στο main.py)
    st.image("home_light.jpg", caption="Smart Living", use_container_width=True)

st.write("---")

# ==================================================
# COMMUNITY SECTION
# ==================================================
st.markdown("### 💬 Η Κοινότητά μας (Forum)")
st.write("""
Δημιουργούμε ένα Forum ανταλλαγής ιδεών για να βοηθήσω προσωπικά σε κάθε απαίτηση αυτοματισμού που σας ζητείται.  
Σας προσκαλώ να γίνετε μέρος αυτής της προσπάθειας.
""")

st.success("### *«Βοήθα με να σε βοηθώ, να ανεβούμε το βουνό»*")

st.write("---")
st.caption("© 2024 Geyer Technical Portal | Σχεδιασμός & Υλοποίηση: Νεκτάριος Κλαδούχος")

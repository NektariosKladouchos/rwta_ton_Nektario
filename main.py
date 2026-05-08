import streamlit as st

st.set_page_config(page_title="GEYER Portal", layout="wide", initial_sidebar_state="collapsed")

# CSS για να κρύψουμε το sidebar στην αρχική
st.markdown("<style>#MainMenu {visibility: hidden;} [data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>GEYER TECHNICAL PORTAL</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 👋 Καλώς ήρθατε")
    st.write("Αυτό είναι το επίσημο portal τεχνικής υποστήριξης της GEYER Hellas.")
    st.write("Χρησιμοποιήστε τον live υπολογιστή για άμεση κοστολόγηση υλικών Smart Home.")
    
    # ΚΟΥΜΠΙ ΠΟΥ ΣΤΕΛΝΕΙ ΣΤΟ PRICING
    st.page_link("pages/2_📊_Pricing.py", label="🚀 ΕΝΑΡΞΗ ΚΟΣΤΟΛΟΓΗΣΗΣ (LIVE PRICING)", icon="📊")

with col2:
    st.image("https://wikimedia.org", width=250)

st.write("---")
st.info("💡 Για τεχνικές λύσεις και ιδέες, χρησιμοποιήστε το μενού πλοήγησης.")

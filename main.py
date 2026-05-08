import streamlit as st

# ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ Η ΠΡΩΤΗ ΓΡΑΜΜΗ
st.image("https://cloudinary.com", width=250)


# 1. Sidebar - Εδώ θα εμφανιστούν αυτόματα οι σελίδες αν δεν έχουν σφάλμα
with st.sidebar:
    st.image("https://wikimedia.org", width=150)
    st.write("---")
    st.markdown("### 🛠️ Πλοήγηση")

# 2. Κεντρικό Περιεχόμενο
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>GEYER TECHNICAL PORTAL</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style='background-color: #ffffff; padding: 25px; border-radius: 15px; border-top: 5px solid #1E3A8A; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);'>
        <h3>👋 Καλώς ήρθατε</h3>
        <p>Αυτή είναι η κεντρική πύλη τεχνικής υποστήριξης για τους συνεργάτες της <b>GEYER Hellas</b>.</p>
        <p>Επιλέξτε μια ενότητα από το μενού στα αριστερά:</p>
        <ul>
            <li><b>📊 Pricing:</b> Για άμεση κοστολόγηση Smart Home.</li>
            <li><b>💡 Ιδέες:</b> Για τεχνικές λύσεις και παρουσιάσεις.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Σίγουρο Logo
    st.image("https://wikimedia.org", use_container_width=True)
    st.info("**Υπεύθυνος Portal:**\nΝεκτάριος Παπαδόπουλος")

st.write("---")
st.caption("© 2024 Geyer Hellas - Smart Solutions Portal")

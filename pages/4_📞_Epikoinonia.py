import streamlit as st

# Ρύθμιση σελίδας
st.set_page_config(page_title="Επικοινωνία - GEYER", layout="wide")

# CSS για την εμφάνιση
st.markdown("""
    <style>
    .main-title { color: #27ae60; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .contact-card {
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05); border-left: 6px solid #27ae60;
        margin-bottom: 20px;
    }
    .video-wrapper {
        position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;
        max-width: 100%; border-radius: 12px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    .video-wrapper iframe {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📞 Επικοινωνία & Υποστήριξη</h1>", unsafe_allow_html=True)

st.markdown("### 🎥 Ρώτα τον Νεκτάριο")

# Χρήση καθαρού HTML για το Video (Embed Method)
# Αυτός ο τρόπος "ξεγελάει" τους περιορισμούς του Streamlit
st.components.v1.html("""
    <div style="display: flex; justify-content: center;">
        <iframe width="560" height="315" 
            src="https://youtube.com" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen>
        </iframe>
    </div>
    """, height=350)

st.write("---")

# ΚΑΡΤΕΣ ΕΠΙΚΟΙΝΩΝΙΑΣ
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div class='contact-card'>
        <h3>👤 Τεχνική Υποστήριξη</h3>
        <p><b>Υπεύθυνος:</b> Νεκτάριος Κλαδούχος</p>
        <p><b>Τηλέφωνο:</b> 6936803610</p>
        <p><b>Email:</b> kladouxos@geyer.gr</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='contact-card'>
        <h3>🏢 GEYER HELLAS Α.Ε.</h3>
        <p>📍 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p>☎️ Τηλ: 22620 31257</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("🏠 ΕΠΙΣΤΡΟΦΗ ΣΤΗΝ ΑΡΧΙΚΗ"):
    st.switch_page("main.py")

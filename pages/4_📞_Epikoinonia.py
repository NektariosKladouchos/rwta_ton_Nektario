import streamlit as st

# Ρύθμιση σελίδας (Επιβάλλεται για να μη χαθεί το Sidebar)
st.set_page_config(page_title="Επικοινωνία - GEYER", layout="wide")

# CSS για επαγγελματική εμφάνιση και GEYER Green στυλ
st.markdown("""
    <style>
    .main-title { color: #27ae60; font-weight: bold; margin-bottom: 10px; text-align: center; }
    .video-container { 
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1); border-top: 5px solid #27ae60;
        margin-bottom: 30px; text-align: center;
    }
    .video-header {
        color: #27ae60; font-size: 24px; font-weight: bold; margin-bottom: 15px;
    }
    .contact-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05); border-left: 8px solid #27ae60;
        min-height: 250px; transition: transform 0.3s;
    }
    .contact-card:hover { transform: translateY(-5px); }
    .info-label { color: #27ae60; font-weight: bold; }
    /* Κεντράρισμα του iframe */
    .flex-center { display: flex; justify-content: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📞 Επικοινωνία & Υποστήριξη</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Είμαστε εδώ για να προσθέσουμε ψηφιακή εμπειρία στην έξυπνη εγκατάστασή σας.</p>", unsafe_allow_html=True)

# --- ΕΝΟΤΗΤΑ VIDEO: ΡΩΤΑ ΤΟΝ ΝΕΚΤΑΡΙΟ ---
st.markdown("<div class='video-container'>", unsafe_allow_html=True)
st.markdown("<div class='video-header'>🎥 Ρώτα τον Νεκτάριο</div>", unsafe_allow_html=True)

# Χρήση iframe για εγγυημένη αναπαραγωγή του YouTube Short
st.markdown("""
    <div class="flex-center">
        <iframe width="315" height="560" 
            src="https://youtube.com" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# --- ΚΑΡΤΕΣ ΕΠΙΚΟΙΝΩΝΙΑΣ ---
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class='contact-card'>
        <h3 style='color: #1E3A8A;'>👤 Τεχνική Υποστήριξη</h3>
        <p><span class='info-label'>Υπεύθυνος:</span> Νεκτάριος Κλαδούχος</p>
        <p><span class='info-label'>Τηλέφωνο:</span> 6936803610</p>
        <p><span class='info-label'>Email:</span> <a href='mailto:kladouxos@geyer.gr' style='color:inherit; text-decoration:none;'>kladouxos@geyer.gr</a></p>
        <p><span class='info-label'>Εξειδίκευση:</span> Smart Home Specialist & Technical Trainer</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='contact-card'>
        <h3 style='color: #1E3A8A;'>🏢 GEYER HELLAS Α.Ε.</h3>
        <p><span class='info-label'>📍 Διεύθυνση:</span> 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p><span class='info-label'>☎️ Τηλ. Κέντρο:</span> 22620 31257</p>
        <p><span class='info-label'>🕒 Ωράριο:</span> Δευτέρα - Παρασκευή 08:00 - 16:00</p>
        <p><span class='info-label'>🌐 Web:</span> <a href='https://geyer.gr' target='_blank' style='color:inherit; text-decoration:none;'>www.geyer.gr</a></p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Κουμπί επιστροφής στην αρχική σελίδα
st.page_link("main.py", label="⬅️ Επιστροφή στην Αρχική", icon="🏠")

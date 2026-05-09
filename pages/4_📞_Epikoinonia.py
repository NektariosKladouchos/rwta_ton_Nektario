import streamlit as st

# CSS για την εμφάνιση της επικοινωνίας
st.markdown("""
    <style>
    .contact-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05); border-left: 8px solid #27ae60;
        margin-bottom: 20px;
    }
    .wa-button {
        background-color: #25D366; color: white; padding: 12px 20px;
        text-decoration: none; border-radius: 8px; font-weight: bold;
        display: inline-block; text-align: center; width: 100%;
    }
    .call-button {
        background-color: #1E3A8A; color: white; padding: 12px 20px;
        text-decoration: none; border-radius: 8px; font-weight: bold;
        display: inline-block; text-align: center; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='color: #27ae60;'>📞 Επικοινωνία & Υποστήριξη</h1>", unsafe_allow_html=True)
st.write("Είμαστε δίπλα σας για οποιαδήποτε τεχνική διευκρίνιση ή βοήθεια στον προγραμματισμό.")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='contact-card'>
        <h3>👤 Τεχνική Υποστήριξη Smart Home</h3>
        <p><b>Υπεύθυνος:</b> Νεκτάριος Κλαδούχος</p>
        <p><b>Email:</b> <a href='mailto:kladouxos@geyer.gr'>kladouxos@geyer.gr</a></p>
        <p><b>Εξειδίκευση:</b> FIBARO, DALI, Z-Wave, Θυροτηλεόραση & Συστήματα Smart Solutions </p>
    </div>
    """, unsafe_allow_html=True)
    
    # WhatsApp Link - Άλλαξε το νούμερο με το δικό σου
    wa_link = "https://wa.me" 
    st.markdown(f'<a href="{wa_link}" class="wa-button">💬 Άμεσο Μήνυμα στο WhatsApp</a>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='contact-card'>
        <h3>🏢 GEYER HELLAS Α.Ε.</h3>
        <p><b>Διεύθυνση:</b> 2ο χλμ. Οδού Σχηματαρίου-Χαλκίδας</p>
        <p><b>Τηλεφωνικό Κέντρο:</b> 22620 31257</p>
        <p><b>Ωράριο:</b> Δευτέρα - Παρασκευή 08:00 - 16:00</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Τηλεφωνική Κλήση
    st.markdown('<a href="tel:+302262031257" class="call-button">📞 Κλήση στο Τεχνικό Τμήμα</a>', unsafe_allow_html=True)

st.write("---")

# Χάρτης Geyer (Προαιρετικό)
st.markdown("### 📍 Τοποθεσία")
st.info("GEYER HELLAS - Εργοστάσιο & Κεντρικά Γραφεία")
# Μπορείς να βάλεις συντεταγμένες αν θες χάρτη:
# st.map(...) 

st.write("---")
st.page_link("main.py", label="⬅️ Επιστροφή στην Αρχική", icon="🏠")


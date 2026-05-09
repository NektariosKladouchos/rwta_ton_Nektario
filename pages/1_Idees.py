import streamlit as st

# Ρύθμιση σελίδας
st.markdown("<h1 style='color: #1E3A8A;'>💡 Τεχνική Εκπαίδευση & Λύσεις</h1>", unsafe_allow_html=True)
st.write("Οδηγός εγκατάστασης και λύσεις αυτοματισμού GEYER Smart Home.")
st.write("---")

# --- ΕΝΟΤΗΤΑ: ΠΑΡΟΥΣΙΑΣΗ PDF ---
st.markdown("### 📊 Παρουσίαση: Αυτοματοποίηση Φωτισμού")
st.info("Εάν η προβολή δεν εμφανίζεται αυτόματα, χρησιμοποιήστε το κουμπί 'Λήψη' παρακάτω.")

# Απλό και σίγουρο κουμπί λήψης (αν το αρχείο υπάρχει στο GitHub)
try:
    with open("lighting_solutions.pdf", "rb") as f:
        st.download_button(
            label="📥 Λήψη Παρουσίασης (PDF)",
            data=f,
            file_name="GEYER_Lighting_Solutions.pdf",
            mime="application/pdf"
        )
    # Προβολή PDF μέσω iframe (πιο σταθερή μέθοδος)
    st.markdown('<iframe src="lighting_solutions.pdf" width="100%" height="500px"></iframe>', unsafe_allow_html=True)
except:
    st.warning("⚠️ Ανεβάστε το αρχείο 'lighting_solutions.pdf' στο GitHub για να ενεργοποιηθεί η λήψη.")

st.write("---")

# --- ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΣΤΑΘΕΡΟ EMBED YOUTUBE ---
def youtube_embed(url):
    video_id = url.split("v=")[-1].split("&")[0]
    embed_url = f"https://youtube.com{video_id}"
    st.markdown(f'<iframe width="100%" height="315" src="{embed_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)

# --- ΒΗΜΑ 1 ---
st.markdown("### 🛠️ Βήμα 1: Πρώτη Σύνδεση & Setup (PC)")
c1, c2 = st.columns([1.5, 1])
with c1:
    youtube_embed("https://youtube.com")
with c2:
    st.info("**Desktop Διαχείριση:**\n* Εντοπισμός IP\n* Παραμετροποίηση\n* Ονοματοδοσία")

st.write("---")

# --- ΒΗΜΑ 2 ---
st.markdown("### 📱 Βήμα 2: Σύνδεση από Κινητό / Tablet")
c3, c4 = st.columns([1.5, 1])
with c3:
    youtube_embed("https://youtube.com")
with c4:
    st.success("**Mobile Έλεγχος:**\n* Απομακρυσμένη πρόσβαση\n* Διαχείριση χρηστών")

st.write("---")

# --- ΒΗΜΑ 3 ---
st.markdown("### 🌈 Εξειδικευμένες Λύσεις: LED Dimming")
c5, c6 = st.columns([1.5, 1])
with c1: # Διόρθωση στήλης
    youtube_embed("https://youtube.com")
with c2: # Διόρθωση στήλης
    st.warning("**Dimming:**\n* Χρήση RGBW Controller\n* Έλεγχος μέσω μπουτόν")

# --- FOOTER ---
st.write("---")
st.page_link("main.py", label="⬅️ Επιστροφή στο Live Pricing", icon="📊")

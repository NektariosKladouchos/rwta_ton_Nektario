import streamlit as st
import os

# Το αρχείο αυτό βρίσκεται μέσα στο subpages/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PICTURES_DIR = os.path.join(BASE_DIR, "pictures")

def show():

    # ---------------------------------------------------------
    #  ΤΙΤΛΟΣ ΣΕΛΙΔΑΣ
    # ---------------------------------------------------------
    st.title("💡 Ιδέες για Επαγγελματικό Φωτισμό")
    st.write(
        "Premium λύσεις για επαγγελματικούς χώρους με Dimmer 220V, "
        "LED Strip, 0-10V, DALI & κεντρική διαχείριση."
    )

    st.divider()
    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 1 – Προβλήματα που λύνουμε
    # ---------------------------------------------------------
    st.header("❗ Προβλήματα στον Επαγγελματικό Φωτισμό")

    colA, colB = st.columns([1, 1])

    with colA:
        st.markdown("""
        - Δυσκολία τοπικού ελέγχου όταν υπάρχουν πολλές γραμμές φωτισμού.
        - Απουσία ομαδοποίησης γραμμών με δυνατότητα dimming.
        - Έλλειψη απομακρυσμένης διαχείρισης και κεντρικής οθόνης.
        - Περιορισμοί σε DALI drivers και μεγάλα μήκη LED strip.
        - Δεν μπορούν να δημιουργηθούν χρονοπρογράμματα dimming.
        - Μεγάλες μπουτονιέρες και ποτενσιόμετρα που δυσκολεύουν τον χειρισμό.
        """)

    with colB:
        st.image(
            "https://images.unsplash.com/photo-1524758631624-e2822e304c36",
            caption="Σύγχρονος επαγγελματικός χώρος",
            use_container_width=True
        )

    st.divider()

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 2 – Οι Λύσεις μας
    # ---------------------------------------------------------
    st.header("⚙️ Λύσεις για Επαγγελματικό Φωτισμό")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔌 Dimmer 220V")
        st.markdown("""
        - Dimming σε LED panel & PL μέχρι 200VA.
        - Ασύρματη ομαδοποίηση πολλών dimmers.
        - Ομοιόμορφο dimming σε όλες τις γραμμές.
        - Χειρισμός από ένα μπουτόν.
        """)
        st.image(
            "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
            caption="Ομοιόμορφος φωτισμός σε επαγγελματικό περιβάλλον",
            use_container_width=True
        )

        st.subheader("🎚️ Dimming LED Strip")
        st.markdown("""
        - Παράδειγμα με δική σου εικόνα από το project.
        - Μπορείς να αντικαταστήσεις οποιαδήποτε εικόνα έτσι.
        """)
        st.image(
            os.path.join(PICTURES_DIR, "09_SETTINGS_DEVICES.png"),
            caption="Δική σου εικόνα από το project (παράδειγμα)",
            use_container_width=True
        )

    with col2:
        st.subheader("🔵 Dimming 0-10V & 1-10V")
        st.markdown("""
        - Οδήγηση οποιουδήποτε driver 1-10V.
        - Τοπικός έλεγχος με μπουτόν.
        - Ασύρματη ομαδοποίηση πολλών drivers.
        - Μνήμη τελευταίας κατάστασης.
        """)
        st.image(
            "https://images.unsplash.com/photo-1520880867055-1e30d1cb001c",
            caption="Επαγγελματικός φωτισμός γραφείων με 0-10V",
            use_container_width=True
        )

        st.subheader("🟣 DALI Dimming")
        st.markdown("""
        - Έλεγχος DALI drivers (DT6).
        - Ομαδοποίηση και διευθυνσιοδότηση.
        - Τοπικός έλεγχος με μπουτόν.
        - Σύνδεση μέχρι 64 drivers στην ίδια γραμμή.
        """)
        st.image(
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b",
            caption="DALI φωτισμός σε retail χώρο",
            use_container_width=True
        )

    st.divider()

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 3 – Κεντρική Διαχείριση Φωτισμού
    # ---------------------------------------------------------
    st.header("🖥️ Κεντρική Οθόνη Διαχείρισης")

    colX, colY = st.columns([1, 1])

    with colX:
        st.markdown("""
        - Οπτικοποίηση όλων των γραμμών φωτισμού.
        - Ομαδοποίηση ανά κατηγορία.
        - Μεμονωμένος ή ομαδικός χειρισμός.
        - Χρονοπρογράμματα & profiles.
        """)

    with colY:
        st.image(
            "https://images.unsplash.com/photo-1558002038-1055907df827",
            caption="Κεντρική διαχείριση φωτισμού",
            use_container_width=True
        )

    st.divider()

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 4 – Πού εφαρμόζεται
    # ---------------------------------------------------------
    st.header("🏢 Πού εφαρμόζεται")

    st.markdown("""
    - Γραφεία & επαγγελματικοί χώροι.
    - Φαρμακεία & ιατρεία.
    - Εστιατόρια & καφετέριες.
    - Ξενοδοχεία & κοινόχρηστοι χώροι.
    - Πάρκα, πλατείες, γήπεδα & εξωτερικοί χώροι.
    - Μεγάλα καταστήματα με πολλές γραμμές φωτισμού.
    """)

    st.image(
        "https://images.unsplash.com/photo-1505842465776-3d90f616310d",
        caption="Εφαρμογές φωτισμού",
        use_container_width=True
    )

    st.divider()
      # ---------------------------------------------------------
    #  PREMIUM CSS PACK – Rounded + Shadow + Border + Fade‑in + Alignment
    # ---------------------------------------------------------
    st.markdown("""
    <style>

    /* Fade-in animation */
    .premium-img {
        opacity: 0;
        animation: fadeIn 0.8s ease forwards;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* Σταθερό ύψος εικόνας */
    .premium-img img {
        height: 260px !important;
        object-fit: cover !important;
        width: 100% !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 4px 18px rgba(0,0,0,0.35);
    }

    /* Σταθερό ύψος τίτλου */
    .gallery-title {
        height: 40px;
        display: flex;
        align-items: center;
        font-size: 20px;
        font-weight: 600;
        margin-top: 10px;
    }

    /* Σταθερό ύψος περιγραφής */
    .gallery-desc {
        height: 55px;
        font-size: 15px;
        color: #ccc;
        margin-bottom: 10px;
    }

    /* Σταθερό ύψος όλου του block */
    .gallery-block {
        min-height: 420px;
        margin-bottom: 20px;
    }

    /* Premium background */
    .gallery-section {
        background: linear-gradient(180deg, #0f0f0f 0%, #1a1a1a 100%);
        padding: 40px 25px;
        border-radius: 18px;
        margin-top: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.06);
    }

    </style>
    """, unsafe_allow_html=True)


    # ---------------------------------------------------------
    #  GALLERY – Screenshots Κεντρικής Μονάδας & App
    # ---------------------------------------------------------
    st.markdown("""
<style>

.premium-img {
    opacity: 0;
    animation: fadeIn 0.8s ease forwards;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Σταθερό ύψος εικόνας (μικρότερο για λιγότερα κενά) */
.premium-img img {
    height: 240px !important;
    object-fit: cover !important;
    width: 100% !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 4px 18px rgba(0,0,0,0.35);
}

/* Σταθερό ύψος τίτλου */
.gallery-title {
    height: 40px;
    display: flex;
    align-items: center;
    font-size: 20px;
    font-weight: 600;
    margin-top: 10px;
}

/* Σταθερό ύψος περιγραφής */
.gallery-desc {
    height: 55px;
    font-size: 15px;
    color: #ccc;
    margin-bottom: 10px;
}

/* Σταθερό ύψος όλου του block (μικρότερο για λιγότερα κενά) */
.gallery-block {
    min-height: 380px;
    margin-bottom: 20px;
}

/* Premium background */
.gallery-section {
    background: linear-gradient(180deg, #0f0f0f 0%, #1a1a1a 100%);
    padding: 40px 25px;
    border-radius: 18px;
    margin-top: 20px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.06);
}

</style>
""", unsafe_allow_html=True)

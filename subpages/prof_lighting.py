import streamlit as st
import os

# Το αρχείο αυτό είναι μέσα στο subpages/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PICTURES_DIR = os.path.join(BASE_DIR, "pictures")


def show():

    # ---------------------------------------------------------
    #  CSS ΓΙΑ ΤΕΛΕΙΑ ΕΥΘΥΓΡΑΜΜΙΣΗ
    # ---------------------------------------------------------
    st.markdown("""
    <style>
    /* Κάνει όλες τις στήλες να ξεκινούν από το ίδιο ύψος */
    [data-testid="column"] {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }

    /* Κεντράρισμα εικόνων */
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* Κεντράρισμα captions */
    .block-container p {
        text-align: center !important;
    }

    /* ----------- GALLERY FIX ----------- */

    .gallery-card {
        padding: 10px;
        border-radius: 8px;
        text-align: center;
    }

    .gallery-title {
        font-size: 18px;
        font-weight: 600;
        min-height: 45px; /* ίδιο ύψος για όλους */
    }

    .gallery-desc {
        font-size: 14px;
        color: #555;
        min-height: 60px; /* ίδιο ύψος για όλους */
    }

    .gallery-card img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    </style>
    """, unsafe_allow_html=True)

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
    #  ΕΝΟΤΗΤΑ 1 – Προβλήματα που λύνουμε (ΜΕ ΤΗ ΔΙΚΗ ΣΟΥ ΦΩΤΟ)
    # ---------------------------------------------------------
    st.header("❗ Προβλήματα στον Επαγγελματικό Φωτισμό")

    colA, colB = st.columns([1, 1], vertical_alignment="center")

    with colA:
        st.markdown("""
        - Πολλοί διακόπτες στον ίδιο τοίχο για πολλές γραμμές φωτισμού.
        - Μπερδεμένος χειρισμός και κακή εργονομία.
        - Απουσία ομαδοποίησης γραμμών με δυνατότητα dimming.
        - Έλλειψη απομακρυσμένης διαχείρισης και κεντρικής οθόνης.
        - Περιορισμοί σε DALI drivers και μεγάλα μήκη LED strip.
        - Δεν μπορούν να δημιουργηθούν χρονοπρογράμματα dimming.
        """)

    with colB:
        st.image(
            os.path.join(PICTURES_DIR, "προβλημα.jpg"),
            caption="Πολλοί διακόπτες στον ίδιο τοίχο → πολλές γραμμές φωτισμού → σύγχυση & κακή εργονομία",
            use_container_width=True
        )

    st.divider()

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 2 – Οι Λύσεις μας (ΜΕ ΤΕΛΕΙΑ ΕΥΘΥΓΡΑΜΜΙΣΗ)
    # ---------------------------------------------------------
    st.header("⚙️ Λύσεις για Επαγγελματικό Φωτισμό")

    col1, col2 = st.columns(2, vertical_alignment="top")

    # ---------------- LEFT COLUMN ----------------
    with col1:

        # DIMMER 220V
        st.subheader("🔌 Dimmer 220V")
        st.markdown("""
        - Dimming σε LED panel & PL μέχρι 200VA.
        - Ασύρματη ομαδοποίηση πολλών dimmers.
        - Ομοιόμορφο dimming σε όλες τις γραμμές.
        - Χειρισμός από ένα μπουτόν.
        """)
        st.image(
            os.path.join(PICTURES_DIR, "ligths_office_220v.png"),
            caption="Φωτισμός γραφείων με panel με dimming phase cut",
            use_container_width=True
        )

        # LED STRIP (ΕΥΘΥΓΡΑΜΜΙΣΜΕΝΟ)
        st.subheader("🎚️ Dimming LED Strip")
        st.markdown("""
        - Dimming με απλό τροφοδοτικό 12V/24V.
        - Ομαδοποίηση για πολλά μέτρα ταινίας.
        - RGB / RGBW / μονόχρωμη ταινία.
        - Ale retour με απλά μπουτόν.
        """)
        st.image(
            os.path.join(PICTURES_DIR, "ligths_room_RGBW.png"),
            caption="Dimming σε ταινίες Led μονόχρωμες, CCT, RGB, RGBW",
            use_container_width=True
        )

    # ---------------- RIGHT COLUMN ----------------
    with col2:

        # 0-10V / 1-10V
        st.subheader("🔵 Dimming 0-10V & 1-10V")
        st.markdown("""
        - Οδήγηση οποιουδήποτε driver 1-10V.
        - Τοπικός έλεγχος με μπουτόν.
        - Ασύρματη ομαδοποίηση πολλών drivers.
        - Μνήμη τελευταίας κατάστασης.
        """)
        st.image(
            os.path.join(PICTURES_DIR, "0-10v.png"),
            caption="Dimming φωτοσωλήνας ειδικής κατασκευής 1-10V",
            use_container_width=True
        )

        # DALI (ΕΥΘΥΓΡΑΜΜΙΣΜΕΝΟ)
        st.subheader("🟣 DALI Dimming")
        st.markdown("""
        - Έλεγχος DALI drivers (DT6).
        - Ομαδοποίηση και διευθυνσιοδότηση.
        - Τοπικός έλεγχος με μπουτόν.
        - Σύνδεση μέχρι 64 drivers στην ίδια γραμμή.
        """)
        st.image(
            os.path.join(PICTURES_DIR, "Dali_office.png"),
            caption="Dimming φωτισμός σε γραφεία με μέθοδο DALI 2 (DT6)",
            use_container_width=True
        )

    st.divider()

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 3 – Κεντρική Διαχείριση Φωτισμού
    # ---------------------------------------------------------
    st.header("🖥️ Κεντρική Οθόνη Διαχείρισης")

    colX, colY = st.columns([1, 1], vertical_alignment="center")

    with colX:
        st.markdown("""
        - Οπτικοποίηση όλων των γραμμών φωτισμού.
        - Ομαδοποίηση ανά κατηγορία (220V / LED Strip / DALI).
        - Μεμονωμένος ή ομαδικός χειρισμός.
        - Ταυτόχρονο dimming σε όλες τις ομάδες.
        - Χρονοπρογράμματα με profiles ανά ώρα/μέρα/συνθήκες.
        """)

    with colY:
        st.image(
            os.path.join(PICTURES_DIR, "kentrikh_othonh.png"),
            caption="Ομαδοποίηση και κεντρική διαχείριση με σενάρια dimming για όλα τα είδη φωτισμού",
            use_container_width=True
        )

    st.divider()

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 4 – Πού εφαρμόζεται (ΧΩΡΙΣ ΕΙΚΟΝΑ)
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

    st.divider()

    # ---------------------------------------------------------
    #  GALLERY – Screenshots Κεντρικής Μονάδας & App
    # ---------------------------------------------------------
    st.header("📱 Screenshots Κεντρικής Μονάδας ")
    st.write("Premium gallery με τέλεια ευθυγράμμιση σε desktop.")

    gallery_items = [
        ("37_Rooms.png", "Section & Rooms", "Τμήματα και χώροι."),
        ("36_συσκευές.png", "Devices", "Γραμμές φωτισμού μέσα στον κάθε χώρο."),
        ("44_κεντρικοί φωτισμοί.png", "Ομαδοποιήσεις Γραμμών Φωτισμού", "Ίδιες γραμμές που ελέγχονται από εικονική συσκευή."),
        ("36_σενάρια χρονικα 2.png", "Scenes", "Ομαδοποίηση φωτισμού με σενάριο."),
        ("34_ομαδοποίηση.png", "Ομαδοποίηση συσκευών", "Ρυθμίσεις συσκευών φωτισμού να λειτουργούν ως ομάδα."),
        ("31_profile.png", "Profiles", "Κλείδωμα ρυθμίσεων γραμμών ή ομάδων."),
        ("35_σενάρια χρονικα.png", "Scenes για Profiles", "Αλλαγή Profile με βάση ώρα ή συνθήκη."),
        ("32_Scenes.png", "Πίνακας σεναρίων", "Παραμετροποίηση ή απενεργοποίηση σεναρίων."),
        ("38_ιστορικό σεναρίων.png", "Ιστορικό", "Παρακολούθηση λειτουργίας σεναρίων."),
        ("33_Καταναλώσεις.png", "Energy", "Καταναλώσεις φωτισμού ανά χώρο."),
        ("42_on_off.png", "Λειτουργία ON/OFF", "Χειρισμός γραμμής φωτισμού με μέτρηση."),
        ("43_dimming.png", "Λειτουργία Dimming", "Dimming με μέτρηση κατανάλωσης εκτός DALI & 0-10V.")
    ]

    cols = st.columns(3)

    for i, (filename, title, desc) in enumerate(gallery_items):
        full_path = os.path.join(PICTURES_DIR, filename)

        with cols[i % 3]:
            st.markdown("<div class='gallery-card'>", unsafe_allow_html=True)

            st.image(full_path, use_container_width=True)

            st.markdown(f"<div class='gallery-title'>{title}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='gallery-desc'>{desc}</div>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

    st.caption("GEYER Hellas – Επαγγελματικές λύσεις φωτισμού με έξυπνη διαχείριση.")

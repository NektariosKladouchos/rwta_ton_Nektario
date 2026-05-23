import streamlit as st
import os

# Το αρχείο αυτό είναι μέσα στο subpages/
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
            os.path.join(PICTURES_DIR, "ligths_office_220v.png"),
            caption="Φωτισμός γραφείων με panel με dimming phase cut",
            use_container_width=True
        )

    st.divider()

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 2 – Οι Λύσεις μας (ΜΕ ΔΙΚΕΣ ΣΟΥ ΦΩΤΟΓΡΑΦΙΕΣ)
    # ---------------------------------------------------------
    st.header("⚙️ Λύσεις για Επαγγελματικό Φωτισμό")

    col1, col2 = st.columns(2)

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

        # LED STRIP
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

        # DALI
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

    colX, colY = st.columns([1, 1])

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
    #  ΕΝΟΤΗΤΑ 4 – Εφαρμογές σε Πραγματικούς Χώρους
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
        os.path.join(PICTURES_DIR, "ligths_office_220v.png"),
        caption="Εφαρμογές φωτισμού σε πραγματικούς επαγγελματικούς χώρους",
        use_container_width=True
    )

    st.divider()

    # ---------------------------------------------------------
    #  GALLERY – Screenshots Κεντρικής Μονάδας & App
    # ---------------------------------------------------------
    st.header("📱 Screenshots Κεντρικής Μονάδας & Mobile App")
    st.write("Premium gallery με απλή προβολή και επεξήγηση κάτω από κάθε εικόνα.")

    gallery_items = [
        ("01_Dashboard.png", "Dashboard", "Κεντρική οθόνη διαχείρισης."),
        ("03_history_Thermostat_IR.png", "Thermostat History", "Ιστορικό θερμοστάτη & εντολές."),
        ("04_history_scene open windows close AC.png", "Scene History", "Αυτόματη σκηνή: Παράθυρα ανοιχτά → Κλείσιμο AC."),
        ("05_SCENES.png", "Scenes", "Λίστα σκηνών & ενεργοποίηση."),
        ("09_SETTINGS_DEVICES.png", "Devices", "Ρυθμίσεις συσκευών & παραμετροποίηση."),
        ("10_SETTINGS_ROOMS.png", "Rooms", "Ομαδοποίηση δωματίων & διαχείριση."),
        ("11_SETTINGS_SCENES_1.png", "Scenes Setup 1", "Ρυθμίσεις σκηνών – Βήμα 1."),
        ("12_SETTINGS_SCENES_2.png", "Scenes Setup 2", "Ρυθμίσεις σκηνών – Βήμα 2."),
        ("13_SETTINGS_SCENES_3.png", "Scenes Setup 3", "Ρυθμίσεις σκηνών – Βήμα 3."),
        ("21_SETTINGS_GENERAL_LOCATION.png", "Location", "Ρυθμίσεις τοποθεσίας & ώρας."),
        ("23_SETTINGS_GENERAL_VARIABLES.png", "Variables", "Μεταβλητές συστήματος & automation."),
        ("33_SETTINGS_ALARM.png", "Alarm", "Ρυθμίσεις συστήματος συναγερμού.")
    ]

    cols = st.columns(3)

    for i, (filename, title, desc) in enumerate(gallery_items):
        full_path = os.path.join(PICTURES_DIR, filename)

        with cols[i % 3]:
            st.image(full_path, use_container_width=True)
            st.markdown(f"### {title}")
            st.markdown(desc)
            st.markdown("---")

    st.caption("GEYER Hellas – Επαγγελματικές λύσεις φωτισμού με έξυπνη διαχείριση.")

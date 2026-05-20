import streamlit as st
import base64
import os

# === ABSOLUTE PATH ΓΙΑ ΝΑ ΔΟΥΛΕΥΟΥΝ ΟΙ ΕΙΚΟΝΕΣ ΠΑΝΤΟΥ ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PICTURES_DIR = os.path.join(BASE_DIR, "pictures")

def load_image_base64(filename):
    full_path = os.path.join(PICTURES_DIR, filename)
    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def show():

    st.title("💡 Ιδέες για Επαγγελματικό Φωτισμό")
    st.write("Premium λύσεις για επαγγελματικούς χώρους με Dimmer 220V, LED Strip, 0-10V, DALI & κεντρική διαχείριση.")
    st.divider()
    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 1 – Προβλήματα που λύνουμε
    # ---------------------------------------------------------
    st.header("❗ Προβλήματα στον Επαγγελματικό Φωτισμό")

    colA, colB = st.columns([1,1])

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
        st.image("https://images.unsplash.com/photo-1504384308090-c894fdcc538d", use_container_width=True)

        st.subheader("🎚️ Dimming LED Strip")
        st.markdown("""
        - Dimming με απλό τροφοδοτικό 12V/24V.
        - Ομαδοποίηση για πολλά μέτρα ταινίας.
        - RGB / RGBW / μονόχρωμη ταινία.
        - Ale retour με απλά μπουτόν.
        """)
        st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c", use_container_width=True)

    with col2:
        st.subheader("🔵 Dimming 0-10V & 1-10V")
        st.markdown("""
        - Οδήγηση οποιουδήποτε driver 1-10V.
        - Τοπικός έλεγχος με μπουτόν.
        - Ασύρματη ομαδοποίηση πολλών drivers.
        - Μνήμη τελευταίας κατάστασης.
        """)
        st.image("https://images.unsplash.com/photo-1520880867055-1e30d1cb001c", use_container_width=True)

        st.subheader("🟣 DALI Dimming")
        st.markdown("""
        - Έλεγχος DALI drivers (DT6).
        - Ομαδοποίηση και διευθυνσιοδότηση.
        - Τοπικός έλεγχος με μπουτόν.
        - Σύνδεση μέχρι 64 drivers στην ίδια γραμμή.
        """)
        st.image("https://images.unsplash.com/photo-1582719478250-c89cae4dc85b", use_container_width=True)

    st.divider()

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ 3 – Κεντρική Διαχείριση
    # ---------------------------------------------------------
    st.header("🖥️ Κεντρική Οθόνη Διαχείρισης")

    colX, colY = st.columns([1,1])

    with colX:
        st.markdown("""
        - Οπτικοποίηση όλων των γραμμών φωτισμού.
        - Ομαδοποίηση ανά κατηγορία.
        - Μεμονωμένος ή ομαδικός χειρισμός.
        - Χρονοπρογράμματα & profiles.
        """)

    with colY:
        st.image("https://images.unsplash.com/photo-1558002038-1055907df827", use_container_width=True)

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

    st.image("https://images.unsplash.com/photo-1505842465776-3d90f616310d", use_container_width=True)

    st.divider()
    st.markdown("""
    <style>

    .dark-card {
        background: #111;
        border: 1px solid #222;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 0 18px rgba(0,0,0,0.45);
        transition: 0.25s ease;
        cursor: pointer;
    }

    .dark-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 0 28px rgba(0,0,0,0.65);
    }

    .dark-title {
        font-size: 18px;
        font-weight: 600;
        color: #fff;
        margin-top: 12px;
    }

    .dark-desc {
        font-size: 14px;
        color: #bbb;
        margin-top: 6px;
    }

    .lightbox {
        display: none;
        position: fixed;
        z-index: 9999;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.92);
        text-align: center;
        padding-top: 40px;
    }

    .lightbox:target {
        display: block;
    }

    .lightbox-close {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
    }

    .lightbox-content {
        position: relative;
        z-index: 2;
        max-width: 90%;
        margin: auto;
    }

    .lightbox-content img {
        width: 100%;
        max-width: 900px;
        border-radius: 12px;
    }

    .lightbox-text {
        color: white;
        margin-top: 20px;
        font-size: 18px;
        padding: 0 20px;
    }

    </style>
    """, unsafe_allow_html=True)
    st.header("📱 Screenshots Κεντρικής Μονάδας & Mobile App")
    st.write("Premium dark‑mode gallery με fullscreen προβολή και επεξηγηματικό κείμενο.")

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
        img_b64 = load_image_base64(filename)

        with cols[i % 3]:

            st.image(full_path, use_container_width=True)

            st.markdown(f"""
            <a href="#lightbox{i}">
                <div class="dark-card">
                    <img src="data:image/png;base64,{img_b64}" style="width:100%; border-radius:10px;">
                    <div class="dark-title">{title}</div>
                    <div class="dark-desc">{desc}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div id="lightbox{i}" class="lightbox">
                <a href="#" class="lightbox-close"></a>
                <div class="lightbox-content">
                    <img src="data:image/png;base64,{img_b64}">
                    <div class="lightbox-text">
                        <h2>{title}</h2>
                        <p>{desc}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.caption("GEYER Hellas – Επαγγελματικές λύσεις φωτισμού με έξυπνη διαχείριση.")

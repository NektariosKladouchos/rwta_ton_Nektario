import streamlit as st

def show():

    # ---------------------------------------------------------
    #  ΤΙΤΛΟΣ ΣΕΛΙΔΑΣ
    # ---------------------------------------------------------
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
            caption="Σύγχρονος επαγγελματικός χώρος με πολλαπλές γραμμές φωτισμού",
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
        - Dimming με απλό τροφοδοτικό 12V/24V.
        - Ομαδοποίηση για πολλά μέτρα ταινίας.
        - RGB / RGBW / μονόχρωμη ταινία.
        - Ale retour με απλά μπουτόν.
        """)
        st.image(
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
            caption="Premium LED strip φωτισμός σε επαγγελματικό χώρο",
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

    colX, colY = st.columns([1,1])

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
            "https://images.unsplash.com/photo-1558002038-1055907df827",
            caption="Κεντρική διαχείριση φωτισμού σε επαγγελματικό περιβάλλον",
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
        "https://images.unsplash.com/photo-1505842465776-3d90f616310d",
        caption="Εφαρμογές φωτισμού σε πραγματικούς επαγγελματικούς χώρους",
        use_container_width=True
    )

    st.divider()

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ – Premium Fullscreen Dark Gallery
    # ---------------------------------------------------------
    st.header("📱 Screenshots Κεντρικής Μονάδας & Mobile App")
    st.write("Παρουσίαση λειτουργιών της κεντρικής μονάδας και της εφαρμογής διαχείρισης κινητού, με premium dark‑mode αισθητική και fullscreen προβολή.")

    # CSS για fullscreen lightbox + dark cards
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
        padding-top: 40px;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.90);
        text-align: center;
    }

    .lightbox img {
        max-width: 90%;
        max-height: 90%;
        border-radius: 12px;
    }

    .lightbox:target {
        display: block;
    }

    </style>
    """, unsafe_allow_html=True)

    cols = st.columns(3)

    # Τυχαίες εικόνες από subpages/pictures/
    gallery_items = [
        {"img": "subpages/pictures/Dashboard.png", "title": "Dashboard", "desc": "Κεντρική οθόνη διαχείρισης."},
        {"img": "subpages/pictures/screen2.jpg", "title": "Groups", "desc": "Ομαδοποίηση φωτισμού."},
        {"img": "subpages/pictures/screen3.png", "title": "Schedules", "desc": "Χρονοπρογράμματα & profiles."},
        {"img": "subpages/pictures/screen4.jpg", "title": "Mobile Home", "desc": "Αρχική οθόνη εφαρμογής."},
        {"img": "subpages/pictures/screen5.png", "title": "Mobile Groups", "desc": "Έλεγχος ομάδων από κινητό."},
        {"img": "subpages/pictures/screen6.jpg", "title": "Scenes", "desc": "Σκηνές φωτισμού."}
    ]

    for i, item in enumerate(gallery_items):
        with cols[i % 3]:
            st.markdown(f"""
            <a href="#lightbox{i}">
                <div class="dark-card">
                    <img src="{item['img']}" style="width:100%; border-radius:10px;">
                    <div class="dark-title">{item['title']}</div>
                    <div class="dark-desc">{item['desc']}</div>
                </div>
            </a>

            <div id="lightbox{i}" class="lightbox" onclick="window.location='#'">
                <img src="{item['img']}">
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    st.caption("GEYER Hellas – Επαγγελματικές λύσεις φωτισμού με έξυπνη διαχείριση.")

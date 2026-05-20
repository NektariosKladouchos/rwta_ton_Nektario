import streamlit as st

def show():

    st.header("🖼️ Screenshots Κεντρικής Μονάδας & Mobile App")
    st.write("Premium dark‑mode gallery με fullscreen προβολή και επεξηγηματικό κείμενο.")

    # ---------------------------------------------------------
    #  CSS – FULLSCREEN LIGHTBOX (μένει όπως είναι)
    # ---------------------------------------------------------
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

    /* ----------- FULLSCREEN LIGHTBOX ----------- */
    .lightbox {
        display: none;
        position: fixed;
        z-index: 9999;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow-y: auto;
        background-color: rgba(0,0,0,0.92);
        text-align: center;
        padding: 40px 0;
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
        display: inline-block;
        max-width: 90%;
        margin: auto;
    }

    .lightbox-content img {
        width: 100%;
        max-width: 900px;
        border-radius: 12px;
        margin-bottom: 20px;
    }

    .lightbox-text {
        color: white;
        max-width: 900px;
        margin: auto;
        text-align: center;
        padding: 10px 20px;
    }

    .lightbox-text h2 {
        margin-bottom: 10px;
        font-size: 26px;
        font-weight: 700;
    }

    .lightbox-text p {
        font-size: 16px;
        color: #ccc;
        line-height: 1.5;
    }

    </style>
    """, unsafe_allow_html=True)
    # ---------------------------------------------------------
    #  GALLERY ITEMS (paths 100% σωστά)
    # ---------------------------------------------------------
    gallery_items = [
        {"img": "../pictures/UI_Dashboard.png", "title": "Dashboard", "desc": "Κεντρική οθόνη διαχείρισης."},
        {"img": "../pictures/UI_Thermostat.png", "title": "Thermostat", "desc": "Έλεγχος θερμοκρασίας και ιστορικό."},
        {"img": "../pictures/UI_Scenes.png", "title": "Scenes", "desc": "Διαχείριση και ενεργοποίηση σκηνών."},
        {"img": "../pictures/UI_Devices.png", "title": "Devices", "desc": "Λίστα συσκευών και παραμετροποίηση."},
        {"img": "../pictures/UI_Rooms.png", "title": "Rooms", "desc": "Ομαδοποίηση και διαχείριση δωματίων."},
        {"img": "../pictures/UI_Alarm.png", "title": "Alarm", "desc": "Σύστημα συναγερμού και ειδοποιήσεις."},
        {"img": "../pictures/UI_Favourites.png", "title": "Favourites", "desc": "Αγαπημένες λειτουργίες και shortcuts."},
        {"img": "../pictures/UI_Home.png", "title": "Home", "desc": "Αρχική οθόνη εφαρμογής."},
        {"img": "../pictures/UI_Settings.png", "title": "Settings", "desc": "Γενικές ρυθμίσεις συστήματος."},
        {"img": "../pictures/UI_Slideshow.png", "title": "Slideshow", "desc": "Προβολή εικόνων και πληροφοριών."},
        {"img": "../pictures/UI_Numbers.png", "title": "Numbers", "desc": "Αριθμητικές ενδείξεις και στατιστικά."},
        {"img": "../pictures/UI_Weather.png", "title": "Weather", "desc": "Καιρικές συνθήκες και πρόγνωση."}
    ]
    # ---------------------------------------------------------
    #  THUMBNAILS ΜΕ STREAMLIT (χωρίς HTML)
    # ---------------------------------------------------------
    cols = st.columns(3)

    for i, item in enumerate(gallery_items):
        with cols[i % 3]:

            # Thumbnail με Streamlit → 100% σταθερό
            st.image(item["img"], use_container_width=True)

            # Αόρατο click‑layer για να ανοίγει το fullscreen
            st.markdown(
                f'<a href="#lightbox{i}"><div style="margin-top:-40px; height:40px;"></div></a>',
                unsafe_allow_html=True
            )

            # FULLSCREEN LIGHTBOX (μένει όπως είναι)
            st.markdown(f"""
            <div id="lightbox{i}" class="lightbox">
                <a href="#" class="lightbox-close"></a>
                <div class="lightbox-content">
                    <img src="{item['img']}">
                    <div class="lightbox-text">
                        <h2>{item['title']}</h2>
                        <p>{item['desc']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.caption("GEYER Hellas – Επαγγελματικές λύσεις φωτισμού με έξυπνη διαχείριση.")

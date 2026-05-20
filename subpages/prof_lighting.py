import streamlit as st

def show():

    st.header("🖼️ Screenshots Κεντρικής Μονάδας & Mobile App")
    st.write("Premium dark‑mode gallery με fullscreen προβολή και επεξηγηματικό κείμενο.")

    # ---------------------------------------------------------
    #  PREMIUM CSS – FULLSCREEN LIGHTBOX
    # ---------------------------------------------------------
    st.markdown("""
    <style>

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
    #  GALLERY ITEMS — ΜΕ URLS (100% σταθερά)
    # ---------------------------------------------------------
    gallery_items = [
        {"img": "https://images.unsplash.com/photo-1524758631624-e2822e304c36", "title": "Dashboard", "desc": "Κεντρική οθόνη διαχείρισης."},
        {"img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d", "title": "Thermostat", "desc": "Έλεγχος θερμοκρασίας και ιστορικό."},
        {"img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c", "title": "Scenes", "desc": "Διαχείριση και ενεργοποίηση σκηνών."},
        {"img": "https://images.unsplash.com/photo-1520880867055-1e30d1cb001c", "title": "Devices", "desc": "Λίστα συσκευών και παραμετροποίηση."},
        {"img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b", "title": "Rooms", "desc": "Ομαδοποίηση και διαχείριση δωματίων."},
        {"img": "https://images.unsplash.com/photo-1558002038-1055907df827", "title": "Alarm", "desc": "Σύστημα συναγερμού και ειδοποιήσεις."},
        {"img": "https://images.unsplash.com/photo-1505842465776-3d90f616310d", "title": "Favourites", "desc": "Αγαπημένες λειτουργίες και shortcuts."}
    ]
    # ---------------------------------------------------------
    #  THUMBNAILS ΜΕ STREAMLIT + FULLSCREEN LIGHTBOX
    # ---------------------------------------------------------
    cols = st.columns(3)

    for i, item in enumerate(gallery_items):
        with cols[i % 3]:

            # Thumbnail με Streamlit → 100% σταθερό
            st.image(item["img"], use_container_width=True)

            # Αόρατο click‑layer για fullscreen
            st.markdown(
                f'<a href="#lightbox{i}"><div style="margin-top:-40px; height:40px;"></div></a>',
                unsafe_allow_html=True
            )

            # FULLSCREEN LIGHTBOX (με URL)
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

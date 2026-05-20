import streamlit as st

def show():
# ---------------------------------------------------------
#  ΕΝΟΤΗΤΑ – Premium Gallery Screenshots
# ---------------------------------------------------------
st.header("📱 Screenshots Κεντρικής Μονάδας & Mobile App")
st.write("Παρουσίαση λειτουργιών της κεντρικής μονάδας και της εφαρμογής διαχείρισης κινητού, με premium dark‑mode αισθητική.")

# CSS για Dark Mode Cards
st.markdown("""
<style>
.dark-card {
    background: #111;
    border: 1px solid #222;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 0 18px rgba(0,0,0,0.45);
    transition: 0.25s ease;
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
</style>
""", unsafe_allow_html=True)

# -----------------------------
#  GALLERY GRID (3 columns)
# -----------------------------
cols = st.columns(3)

# Βάλε εδώ τις εικόνες σου (PNG)
gallery_items = [
    {
        "img": "images/screens/dashboard.png",
        "title": "Κεντρική Οθόνη Διαχείρισης",
        "desc": "Πλήρης οπτικοποίηση όλων των γραμμών φωτισμού με real‑time ενημέρωση."
    },
    {
        "img": "images/screens/groups.png",
        "title": "Ομαδοποίηση Φωτισμού",
        "desc": "Δημιουργία ομάδων 220V / LED Strip / DALI με ταυτόχρονο dimming."
    },
    {
        "img": "images/screens/schedules.png",
        "title": "Χρονοπρογράμματα",
        "desc": "Profiles ανά ώρα/μέρα με αυτόματη ρύθμιση φωτεινότητας."
    },
    {
        "img": "images/screens/mobile_home.png",
        "title": "Αρχική Οθόνη Εφαρμογής",
        "desc": "Γρήγορη πρόσβαση σε όλες τις ομάδες φωτισμού από το κινητό."
    },
    {
        "img": "images/screens/mobile_group.png",
        "title": "Έλεγχος Ομάδων",
        "desc": "Άμεσο on/off και dimming για κάθε ομάδα φωτισμού."
    },
    {
        "img": "images/screens/mobile_scenes.png",
        "title": "Σκηνές Φωτισμού",
        "desc": "Προκαθορισμένες σκηνές για καφετέριες, γραφεία, ξενοδοχεία."
    }
]

# Render gallery
for i, item in enumerate(gallery_items):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="dark-card">
            <img src="{item['img']}" style="width:100%; border-radius:10px;">
            <div class="dark-title">{item['title']}</div>
            <div class="dark-desc">{item['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    #  ΕΝΟΤΗΤΑ – Premium Gallery Screenshots
    # ---------------------------------------------------------
    st.header("📱 Screenshots Κεντρικής Μονάδας & Mobile App")
    st.write("Παρουσίαση λειτουργιών της κεντρικής μονάδας και της εφαρμογής διαχείρισης κινητού, με premium dark‑mode αισθητική.")

    # CSS για Dark Mode Cards
    st.markdown("""
    <style>
    .dark-card {
        background: #111;
        border: 1px solid #222;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 0 18px rgba(0,0,0,0.45);
        transition: 0.25s ease;
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
    </style>
    """, unsafe_allow_html=True)

    # -----------------------------
    #  GALLERY GRID (3 columns)
    # -----------------------------
    cols = st.columns(3)

    # Βάλε εδώ τις εικόνες σου (PNG)
    gallery_items = [
        {
            "img": "images/screens/dashboard.png",
            "title": "Κεντρική Οθόνη Διαχείρισης",
            "desc": "Πλήρης οπτικοποίηση όλων των γραμμών φωτισμού με real‑time ενημέρωση."
        },
        {
            "img": "images/screens/groups.png",
            "title": "Ομαδοποίηση Φωτισμού",
            "desc": "Δημιουργία ομάδων 220V / LED Strip / DALI με ταυτόχρονο dimming."
        },
        {
            "img": "images/screens/schedules.png",
            "title": "Χρονοπρογράμματα",
            "desc": "Profiles ανά ώρα/μέρα με αυτόματη ρύθμιση φωτεινότητας."
        },
        {
            "img": "images/screens/mobile_home.png",
            "title": "Αρχική Οθόνη Εφαρμογής",
            "desc": "Γρήγορη πρόσβαση σε όλες τις ομάδες φωτισμού από το κινητό."
        },
        {
            "img": "images/screens/mobile_group.png",
            "title": "Έλεγχος Ομάδων",
            "desc": "Άμεσο on/off και dimming για κάθε ομάδα φωτισμού."
        },
        {
            "img": "images/screens/mobile_scenes.png",
            "title": "Σκηνές Φωτισμού",
            "desc": "Προκαθορισμένες σκηνές για καφετέριες, γραφεία, ξενοδοχεία."
        }
    ]

    # Render gallery
    for i, item in enumerate(gallery_items):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="dark-card">
                <img src="{item['img']}" style="width:100%; border-radius:10px;">
                <div class="dark-title">{item['title']}</div>
                <div class="dark-desc">{item['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

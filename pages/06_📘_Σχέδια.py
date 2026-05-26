import streamlit as st
import os
import json

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="📘 Τεχνικά Σχέδια",
    page_icon="📘",
    layout="wide"
)

# ---------------------------------------------------------
# ADMIN MODE WITH PASSWORD (GLOBAL)
# ---------------------------------------------------------
if "admin" not in st.session_state:
    st.session_state.admin = False

with st.sidebar:
    st.write("### 🔐 Admin Login")
    pwd = st.text_input("Κωδικός Admin", type="password")
    if st.button("Είσοδος"):
        if pwd == "1234":   # ΒΑΛΕ ΤΟΝ ΔΙΚΟ ΣΟΥ ΚΩΔΙΚΟ
            st.session_state.admin = True
            st.success("Επιτυχής είσοδος Admin!")
        else:
            st.error("Λάθος κωδικός.")

is_admin = st.session_state.admin

# ---------------------------------------------------------
# ADMIN BADGE
# ---------------------------------------------------------
if is_admin:
    st.markdown("""
        <div style="
            position: fixed;
            top: 15px;
            right: 20px;
            background-color: #0b3c26;
            color: white;
            padding: 8px 15px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
            z-index: 9999;
        ">
            🟢 Admin Mode ενεργό
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# PREMIUM GREEN SIDEBAR CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #0b3c26 !important;
    }
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] a {
        color: white !important;
    }
    [data-testid="stSidebar"] svg {
        fill: white !important;
    }
    button[kind="header"] svg {
        fill: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------------
st.title("📘 Τεχνικά Σχέδια")
st.write("""
Καλώς ήρθατε στην ενότητα Τεχνικών Σχεδίων.  
Εδώ θα βρείτε οργανωμένα παραδείγματα, αναλύσεις και οδηγίες για:
- Διαγράμματα ηλεκτρολογικών συνδέσεων  
- Για κάθε είδος αυτοματισμού  
- HVAC αυτοματισμούς  
- Παραδείγματα προγραμματισμού  
- Εκπαιδευτικό υλικό  
""")

st.write("---")

# ---------------------------------------------------------
# PATHS
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SXEDIA_DIR = os.path.join(BASE_DIR, "sxedia")
PROGRAMMING_DIR = os.path.join(BASE_DIR, "programming")
LESSONS_DIR = os.path.join(BASE_DIR, "lessons")

# ---------------------------------------------------------
# GLOBAL COUNTERS
# ---------------------------------------------------------
COUNTER_FILE = os.path.join(BASE_DIR, "counters.json")

def load_counters():
    if not os.path.exists(COUNTER_FILE):
        return {}
    with open(COUNTER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_counters(data):
    with open(COUNTER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# καταγραφή εισόδου στη σελίδα
_c = load_counters()
_c["sxedia_total"] = _c.get("sxedia_total", 0) + 1
save_counters(_c)

# ---------------------------------------------------------
# TXT HELPERS
# ---------------------------------------------------------
def load_txt_sections(txt_path, sections):
    data = {key: "" for key in sections}
    if not os.path.exists(txt_path):
        return data

    section = None
    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            low = line.strip().lower()
            if low in [f"[{s}]" for s in sections]:
                section = low.strip("[]")
                continue
            if section:
                data[section] += line + "\n"
    return data

def load_sxedio_txt(txt_path):
    return load_txt_sections(txt_path, ["title", "description", "electrician", "customer"])

def load_lesson_or_program_txt(txt_path):
    return load_txt_sections(txt_path, ["title", "description", "video"])

# ---------------------------------------------------------
# SCREENSHOT LOADER
# ---------------------------------------------------------
def load_screenshots(folder):
    if not os.path.exists(folder):
        return []

    valid_ext = (".png", ".jpg", ".jpeg")
    images = [
        f for f in os.listdir(folder)
        if f.lower().endswith(valid_ext) and not f.startswith(".")
    ]

    if not images:
        return []

    images = sorted(images)
    items = []

    for img in images:
        base, _ = os.path.splitext(img)
        img_path = os.path.join(folder, img)
        txt_path = os.path.join(folder, base + ".txt")

        if not os.path.exists(txt_path):
            continue

        try:
            with open(txt_path, "r", encoding="utf-8") as f:
                caption = f.read().strip()
        except:
            caption = ""

        items.append({"img": img_path, "caption": caption})

    return items

# ---------------------------------------------------------
# CAROUSEL
# ---------------------------------------------------------
def render_carousel(title, items, key_prefix):
    if not items:
        return

    st.markdown(f"#### {title}")

    if len(items) == 1:
        st.image(items[0]["img"], use_container_width=True)
        if items[0]["caption"]:
            st.caption(items[0]["caption"])
        st.write("---")
        return

    idx = st.slider(
        "Επιλέξτε screenshot",
        min_value=1,
        max_value=len(items),
        value=1,
        key=f"{key_prefix}_slider"
    )

    item = items[idx - 1]
    st.image(item["img"], use_container_width=True)
    if item["caption"]:
        st.caption(item["caption"])
    st.write("---")

# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "🔌 Σχέδια Σύνδεσης",
    "⚙️ Τρόποι Προγραμματισμού",
    "🎓 Μαθήματα"
])

# ---------------------------------------------------------
# TAB 1
# ---------------------------------------------------------
with tab1:
    _c = load_counters()
    _c["sxedia_sxedia"] = _c.get("sxedia_sxedia", 0) + 1
    save_counters(_c)

    st.subheader("🔌 Σχέδια Σύνδεσης")

    categories = {
        "Φωτισμός": "fotismos",
        "Μοτέρ Σκίασης": "moter_skiasis",
        "HVAC": "hvac",
        "Ζεστά Νερά": "znx",
        "Συναγερμός": "synagermos",
        "Αισθητήρες": "aisthitires",
        "Σενάρια": "senaria",
        "Μετρητές": "metrites",
        "Άλλα": "alla"
    }

    cat_choice = st.selectbox("Επιλέξτε κατηγορία σχεδίων:", list(categories.keys()))
    folder = os.path.join(SXEDIA_DIR, categories[cat_choice])

    st.write("---")

    if not os.path.exists(folder):
        st.warning("⚠️ Ο φάκελος δεν υπάρχει ακόμα.")
        files = []
    else:
        files = [
            f for f in os.listdir(folder)
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]

    if files:
        choice = st.selectbox("Επιλέξτε σχέδιο:", files)
        img_path = os.path.join(folder, choice)

        st.image(img_path, use_container_width=True)

        txt_name = choice.rsplit(".", 1)[0] + ".txt"
        txt_path = os.path.join(folder, txt_name)
        info = load_sxedio_txt(txt_path)

        clean_title = choice.rsplit(".", 1)[0].replace("_", " ").title()

        st.markdown("### 📘 Τίτλος Σχεδίου")
        st.write(info["title"] if info["title"] else clean_title)

        st.markdown("### 📝 Γρήγορη Επεξήγηση")
        st.write(info["description"] if info["description"] else "Δεν υπάρχει περιγραφή.")

        st.markdown("### ⚠️ Τι πρέπει να προσέξει ο ηλεκτρολόγος")
        st.write(info["electrician"] if info["electrician"] else "Δεν υπάρχουν παρατηρήσεις.")

        st.markdown("### ⭐ Τι κερδίζει ο πελάτης")
        st.write(info["customer"] if info["customer"] else "Δεν υπάρχουν οφέλη.")
    else:
        st.info("ℹ️ Δεν υπάρχουν σχέδια για αυτή την κατηγορία.")

# ---------------------------------------------------------
# TAB 2
# ---------------------------------------------------------
with tab2:
    _c = load_counters()
    _c["sxedia_programming"] = _c.get("sxedia_programming", 0) + 1
    save_counters(_c)

    st.subheader("⚙️ Τρόποι Προγραμματισμού")

    if not os.path.exists(PROGRAMMING_DIR):
        st.info("ℹ️ Δεν υπάρχει φάκελος 'programming'.")
        entries = []
    else:
        entries = [
            d for d in os.listdir(PROGRAMMING_DIR)
            if os.path.isdir(os.path.join(PROGRAMMING_DIR, d))
        ]
        entries = sorted(entries)

    if entries:
        choice_prog = st.selectbox(
            "Επιλέξτε διαδικασία:",
            entries,
            format_func=lambda x: x.replace("_", " ").title()
        )

        prog_folder = os.path.join(PROGRAMMING_DIR, choice_prog)
        main_txt = os.path.join(prog_folder, f"{choice_prog}.txt")
        data = load_lesson_or_program_txt(main_txt)

        st.markdown("### 📘 Τίτλος Διαδικασίας")
        st.write(data["title"] if data["title"] else choice_prog.replace("_", " ").title())

        st.markdown("### 📝 Περιγραφή")
        st.write(data["description"] if data["description"] else "Δεν υπάρχει περιγραφή.")

        video_url = data["video"].strip()
        if video_url:
            st.markdown("### 🎬 Βίντεο YouTube")
            st.video(video_url)

        st.write("---")

        mobile_folder = os.path.join(prog_folder, "mobile")
        pc_folder = os.path.join(prog_folder, "pc")

        mobile_items = load_screenshots(mobile_folder)
        pc_items = load_screenshots(pc_folder)

        if mobile_items:
            render_carousel("📱 Screens από κινητό", mobile_items, key_prefix=f"{choice_prog}_mobile")

        if pc_items:
            render_carousel("💻 Screens από υπολογιστή", pc_items, key_prefix=f"{choice_prog}_pc")

    else:
        st.info("ℹ️ Δεν υπάρχουν διαδικασίες προγραμματισμού.")

# ---------------------------------------------------------
# TAB 3
# ---------------------------------------------------------
with tab3:
    _c = load_counters()
    _c["sxedia_lessons"] = _c.get("sxedia_lessons", 0) + 1
    save_counters(_c)

    st.subheader("🎓 Μαθήματα")

    if not os.path.exists(LESSONS_DIR):
        st.info("ℹ️ Δεν υπάρχει φάκελος 'lessons'.")
        entries = []
    else:
        entries = [
            d for d in os.listdir(LESSONS_DIR)
            if os.path.isdir(os.path.join(LESSONS_DIR, d))
        ]
        entries = sorted(entries)

    if entries:
        choice_lesson = st.selectbox(
            "Επιλέξτε μάθημα:",
            entries,
            format_func=lambda x: x.replace("_", " ").title()
        )

        lesson_folder = os.path.join(LESSONS_DIR, choice_lesson)
        main_txt = os.path.join(lesson_folder, f"{choice_lesson}.txt")
        data = load_lesson_or_program_txt(main_txt)

        st.markdown("### 📘 Τίτλος Μαθήματος")
        st.write(data["title"] if data["title"] else choice_lesson.replace("_", " ").title())

        st.markdown("### 📝 Περιγραφή")
        st.write(data["description"] if data["description"] else "Δεν υπάρχει περιγραφή.")

        video_url = data["video"].strip()
        if video_url:
            st.markdown("### 🎬 Βίντεο YouTube")
            st.video(video_url)

        st.write("---")

        mobile_folder = os.path.join(lesson_folder, "mobile")
        pc_folder = os.path.join(lesson_folder, "pc")

        mobile_items = load_screenshots(mobile_folder)
        pc_items = load_screenshots(pc_folder)

        if mobile_items:
            render_carousel("📱 Screens από κινητό", mobile_items, key_prefix=f"{choice_lesson}_mobile")

        if pc_items:
            render_carousel("💻 Screens από υπολογιστή", pc_items, key_prefix=f"{choice_lesson}_pc")

    else:
        st.info("ℹ️ Δεν υπάρχουν μαθήματα.")

# ---------------------------------------------------------
# ADMIN‑ONLY ANALYTICS (ΕΞΩ ΑΠΟ ΤΑ TABS)
# ---------------------------------------------------------
if is_admin:
    st.write("---")
    st.subheader("📊 Συνολικά Analytics (Μόνο για Admin)")

    counters = load_counters()

    st.write("### Προβολές ανά ενότητα")
    st.bar_chart({
        "Ενότητα": [
            "Σχέδια Σύνδεσης",
            "Τρόποι Προγραμματισμού",
            "Μαθήματα"
        ],
        "Προβολές": [
            counters.get("sxedia_sxedia", 0),
            counters.get("sxedia_programming", 0),
            counters.get("sxedia_lessons", 0)
        ]
    })

    st.write("### Σύνολο επισκέψεων σελίδας")
    st.metric("Συνολικές προβολές", counters.get("sxedia_total", 0))

import streamlit as st
import os
import json
import pandas as pd
import pytz
from supabase import create_client, Client

# ---------------------------------------------------------
# SUPABASE CONNECTION
# ---------------------------------------------------------
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_event(page, event, user=None, extra=None):
    try:
        supabase.table("analytics").insert({
            "page": page,
            "event": event,
            "user_email": user,
            "extra": extra
        }).execute()
    except:
        pass

def convert_utc_to_greece(ts):
    try:
        greece = pytz.timezone("Europe/Athens")
        return pd.to_datetime(ts).tz_convert(greece)
    except:
        return ts

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="📘 Τεχνικά Σχέδια",
    page_icon="📘",
    layout="wide"
)

# ---------------------------------------------------------
# ADMIN CHECK
# ---------------------------------------------------------
try:
    user_email = st.experimental_user.email
except:
    user_email = None

admin_emails = [
    "kladouxos@geyer.gr",
    "nektarioskladouchos@gmail.com"
]

is_admin = (user_email in admin_emails)

# ---------------------------------------------------------
# ADMIN BADGE
# ---------------------------------------------------------
if is_admin:
    st.markdown(f"""
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
            🟢 Admin Mode ενεργό<br>
            <span style="font-size:12px; opacity:0.8;">{user_email}</span>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# PREMIUM SIDEBAR CSS
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
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------------
st.title("📘 Τεχνικά Σχέδια")
st.write("""
Καλώς ήρθατε στην ενότητα Τεχνικών Σχεδίων.  
Εδώ θα βρείτε οργανωμένα παραδείγματα, αναλύσεις και οδηγίες.
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
# COUNTERS
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
# TAB 1 — ΣΧΕΔΙΑ ΣΥΝΔΕΣΗΣ
# ---------------------------------------------------------
with tab1:
    log_event("sxedia", "open_tab", extra="sxedia_syndesis")

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
    log_event("sxedia", "open_category", extra=cat_choice)

    folder = os.path.join(SXEDIA_DIR, categories[cat_choice])

    st.write("---")

    if not os.path.exists(folder):
        st.warning("⚠️ Ο φάκελος δεν υπάρχει ακόμα.")
        st.stop()

    files = [
        f for f in os.listdir(folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    if not files:
        st.info("ℹ️ Δεν υπάρχουν σχέδια.")
        st.stop()

    choice = st.selectbox("Επιλέξτε σχέδιο:", files)
    log_event("sxedia", "open_design", extra=choice)

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

# ---------------------------------------------------------
# TAB 2 — ΤΡΟΠΟΙ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ
# ---------------------------------------------------------
with tab2:
    log_event("sxedia", "open_tab", extra="programming")

    _c = load_counters()
    _c["sxedia_programming"] = _c.get("sxedia_programming", 0) + 1
    save_counters(_c)

    st.subheader("⚙️ Τρόποι Προγραμματισμού")

    if not os.path.exists(PROGRAMMING_DIR):
        st.info("ℹ️ Δεν υπάρχει φάκελος 'programming'.")
    else:
        entries = [
            d for d in os.listdir(PROGRAMMING_DIR)
            if os.path.isdir(os.path.join(PROGRAMMING_DIR, d))
        ]
        entries = sorted(entries)

        if not entries:
            st.info("ℹ️ Δεν υπάρχουν διαδικασίες.")
        else:
            choice_prog = st.selectbox(
                "Επιλέξτε διαδικασία:",
                entries,
                format_func=lambda x: x.replace("_", " ").title()
            )

            log_event("sxedia", "open_programming", extra=choice_prog)

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

# ---------------------------------------------------------
# TAB 3 — ΜΑΘΗΜΑΤΑ
# ---------------------------------------------------------
with tab3:
    log_event("sxedia", "open_tab", extra="lessons")

    _c = load_counters()
    _c["sxedia_lessons"] = _c.get("sxedia_lessons", 0) + 1
    save_counters(_c)

    st.subheader("🎓 Μαθήματα")

    if not os.path.exists(LESSONS_DIR):
        st.info("ℹ️ Δεν υπάρχει φάκελος 'lessons'.")
    else:
        entries = [
            d for d in os.listdir(LESSONS_DIR)
            if os.path.isdir(os.path.join(LESSONS_DIR, d))
        ]
        entries = sorted(entries)

        if not entries:
            st.info("ℹ️ Δεν υπάρχουν μαθήματα.")
        else:
            choice_lesson = st.selectbox(
                "Επιλέξτε μάθημα:",
                entries,
                format_func=lambda x: x.replace("_", " ").title()
            )

            log_event("sxedia", "open_lesson", extra=choice_lesson)

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

# ---------------------------------------------------------
# ADMIN ANALYTICS
# ---------------------------------------------------------
if is_admin:
    st.write("---")
    st.subheader("📊 Analytics Σχεδίων (Admin Only)")

    try:
        result = supabase.table("analytics").select("*").eq("page", "sxedia").order("id", desc=True).execute()

        if result.data:
            df = pd.DataFrame(result.data)
            df["timestamp"] = df["timestamp"].apply(convert_utc_to_greece)
            st.dataframe(df)
        else:
            st.info("Δεν υπάρχουν ακόμα δεδομένα.")
    except Exception as e:
        st.error(f"Σφάλμα φόρτωσης analytics: {e}")

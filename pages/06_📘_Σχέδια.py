import streamlit as st
import os

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="📘 Τεχνικά Σχέδια",
    page_icon="📘",
    layout="wide"
)

# ---------------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------------
st.title("📘 Τεχνικά Σχέδια")
st.write("""
Καλώς ήρθατε στην ενότητα Τεχνικών Σχεδίων.  
Εδώ θα βρείτε οργανωμένα παραδείγματα, αναλύσεις και οδηγίες για:
- Συνδέσεις DALI  
- Συνδέσεις LED & Drivers  
- HVAC αυτοματισμούς  
- Παραδείγματα προγραμματισμού  
- Εκπαιδευτικό υλικό  
""")

st.write("---")

# ---------------------------------------------------------
# ΒΑΣΙΚΑ PATHS
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SXEDIA_DIR = os.path.join(BASE_DIR, "sxedia")
PROGRAMMING_DIR = os.path.join(BASE_DIR, "programming")
LESSONS_DIR = os.path.join(BASE_DIR, "lessons")

# ---------------------------------------------------------
# HELPERS ΓΙΑ TXT
# ---------------------------------------------------------
def load_txt_sections(txt_path, sections):
    """Γενική συνάρτηση: διαβάζει .txt με [sections] και επιστρέφει dict."""
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
# ΑΛΕΞΙΣΦΑΙΡΟ LOADER ΓΙΑ SCREENSHOTS
# ---------------------------------------------------------
def load_screenshots(folder):
    """
    Αλεξίσφαιρη φόρτωση screenshots:
    - Δέχεται .png, .jpg, .jpeg (όλα lowercase)
    - Αγνοεί κεφαλαία (.PNG)
    - Αγνοεί κρυφά αρχεία
    - Αγνοεί αρχεία χωρίς αντίστοιχο .txt
    - Δεν κρασάρει ποτέ
    """
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
# ΑΛΕΞΙΣΦΑΙΡΟ CAROUSEL
# ---------------------------------------------------------
def render_carousel(title, items, key_prefix):
    """
    Αλεξίσφαιρο carousel:
    - Αν δεν υπάρχουν εικόνες → δεν εμφανίζει slider
    - Αν υπάρχει 1 εικόνα → δεν εμφανίζει slider
    - Αν υπάρχουν πολλές → slider κανονικά
    """
    if not items or len(items) == 0:
        return  # ΜΗΝ εμφανίσεις τίποτα

    st.markdown(f"#### {title}")

    # ΜΟΝΟ ΜΙΑ ΕΙΚΟΝΑ → χωρίς slider
    if len(items) == 1:
        st.image(items[0]["img"], use_container_width=True)
        if items[0]["caption"]:
            st.caption(items[0]["caption"])
        st.write("---")
        return

    # ΠΕΡΙΣΣΟΤΕΡΕΣ ΑΠΟ 1 → slider
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
    st.subheader("🔌 Σχέδια Σύνδεσης")

    categories = {
        "Φωτισμός": "fotismos",
        "Μοτέρ Σκίασης": "moter",
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
        st.warning("⚠️ Ο φάκελος δεν υπάρχει ακόμα. Δημιουργήστε τον και προσθέστε PNG/JPG σχέδια.")
        st.stop()

    files = [
        f for f in os.listdir(folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    if len(files) == 0:
        st.info("ℹ️ Δεν υπάρχουν ακόμα σχέδια σε αυτή την κατηγορία.")
        st.stop()

    choice = st.selectbox("Επιλέξτε σχέδιο:", files)
    img_path = os.path.join(folder, choice)

    st.image(img_path, use_container_width=True)

    # TXT για το συγκεκριμένο σχέδιο
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
    st.subheader("⚙️ Τρόποι Προγραμματισμού")

    if not os.path.exists(PROGRAMMING_DIR):
        st.info("ℹ️ Δεν έχει δημιουργηθεί ακόμα ο φάκελος 'programming'.")
    else:
        entries = [
            d for d in os.listdir(PROGRAMMING_DIR)
            if os.path.isdir(os.path.join(PROGRAMMING_DIR, d))
        ]
        entries = sorted(entries)

        if not entries:
            st.info("ℹ️ Δεν υπάρχουν ακόμα διαδικασίες προγραμματισμού.")
        else:
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

# ---------------------------------------------------------
# TAB 3 — ΜΑΘΗΜΑΤΑ
# ---------------------------------------------------------
with tab3:
    st.subheader("🎓 Μαθήματα")

    if not os.path.exists(LESSONS_DIR):
        st.info("ℹ️ Δεν έχει δημιουργηθεί ακόμα ο φάκελος 'lessons'.")
    else:
        entries = [
            d for d in os.listdir(LESSONS_DIR)
            if os.path.isdir(os.path.join(LESSONS_DIR, d))
        ]
        entries = sorted(entries)

        if not entries:
            st.info("ℹ️ Δεν υπάρχουν ακόμα μαθήματα.")
        else:
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

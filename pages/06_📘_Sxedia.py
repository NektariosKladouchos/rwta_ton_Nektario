import streamlit as st
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PICTURES_DIR = os.path.join(BASE_DIR, "subpages", "pictures")

# ---------------------------------------------------------
# PATHS
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PICTURES_DIR = os.path.join(BASE_DIR, "..", "subpages", "pictures")


def show():

    # ---------------------------------------------------------
    # TITLE & INTRO
    # ---------------------------------------------------------
    st.title("📘 Τεχνικά Σχέδια")

    st.write("""
    Η ενότητα αυτή έχει δημιουργηθεί για ηλεκτρολόγους και τεχνικούς που χρειάζονται 
    άμεση πρόσβαση σε διαγράμματα σύνδεσης, τρόπους προγραμματισμού και εκπαιδευτικό υλικό.
    Όλα τα σχέδια είναι διαθέσιμα σε μορφή PNG/JPG ώστε να ανοίγουν άμεσα από κινητό.
    """)

    st.info(
        "💡 Επιλέξτε υποκατηγορία και στη συνέχεια διαλέξτε το σχέδιο ή μάθημα που σας ενδιαφέρει "
        "από το αναδυόμενο μενού."
    )

    # ---------------------------------------------------------
    # PREMIUM CSS ΓΙΑ ΕΙΚΟΝΕΣ
    # ---------------------------------------------------------
    st.markdown(
        """
        <style>
        .tech-img {
            opacity: 0;
            animation: fadeIn 0.6s ease forwards;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .tech-img img {
            border-radius: 14px !important;
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 4px 18px rgba(0,0,0,0.35);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ---------------------------------------------------------
    # TABS
    # ---------------------------------------------------------
    tab1, tab2, tab3 = st.tabs(
        ["🔌 Σχέδια Σύνδεσης", "⚙️ Τρόποι Προγραμματισμού", "🎓 Μαθήματα"]
    )

    # ---------------------------------------------------------
    # TAB 1 — ΣΧΕΔΙΑ ΣΥΝΔΕΣΗΣ
    # ---------------------------------------------------------
    with tab1:
        st.subheader("🔌 Σχέδια Σύνδεσης")

        st.write(
            "Εδώ θα βρείτε διαγράμματα συνδεσμολογίας για dimmer, LED, DALI, θερμοστάτες κ.ά. "
            "Κάθε σχέδιο συνοδεύεται από σύντομη ανάλυση και τα βασικά οφέλη."
        )

        connection_options = {
            "Σύνδεση Dimmer 220V με φωτιστικό": {
                "file": "dimmer_220v.png",  # βάλε το πραγματικό όνομα αρχείου
                "analysis": "Σύνδεση dimmer 220V με ένα ή περισσότερα φωτιστικά LED/PL.",
                "benefits": [
                    "Ομαλό dimming χωρίς τρεμόπαιγμα.",
                    "Απλή καλωδίωση με φάση/ουδέτερο.",
                    "Ιδανικό για αναβάθμιση υπάρχουσας εγκατάστασης.",
                ],
            },
            "Σύνδεση LED Strip 24V με controller": {
                "file": "ledstrip_24v.png",
                "analysis": "Σύνδεση ταινίας LED 24V με τροφοδοτικό και controller.",
                "benefits": [
                    "Ασφαλής χαμηλή τάση 24V.",
                    "Δυνατότητα μεγάλου μήκους ταινίας.",
                    "Σταθερή λειτουργία και ομαλό dimming.",
                ],
            },
            "Σύνδεση DALI DT6 με κεντρική μονάδα": {
                "file": "dali_dt6.png",
                "analysis": "Σύνδεση DALI driver DT6 με κεντρικό controller/σύστημα.",
                "benefits": [
                    "Ακριβής έλεγχος φωτισμού ανά φωτιστικό.",
                    "Ομαδοποίηση και σενάρια φωτισμού.",
                    "Επαγγελματική λύση για μεγάλες εγκαταστάσεις.",
                ],
            },
        }

        choice_conn = st.selectbox(
            "Επιλέξτε σχέδιο σύνδεσης:", list(connection_options.keys())
        )

        data_conn = connection_options[choice_conn]
        img_path_conn = os.path.join(PICTURES_DIR, data_conn["file"])

        st.markdown('<div class="tech-img">', unsafe_allow_html=True)
        st.image(img_path_conn, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### 📘 Ανάλυση")
        st.write(data_conn["analysis"])

        st.markdown("### ⭐ Τι κερδίζεις")
        for b in data_conn["benefits"]:
            st.write(f"- {b}")

    # ---------------------------------------------------------
    # TAB 2 — ΤΡΟΠΟΙ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ
    # ---------------------------------------------------------
    with tab2:
        st.subheader("⚙️ Τρόποι Προγραμματισμού")

        st.write(
            "Παραδείγματα προγραμματισμού μέσα από την εφαρμογή και πώς εμφανίζονται "
            "στο κινητό ή στον υπολογιστή."
        )

        prog_options = {
            "Δημιουργία σκηνής φωτισμού": {
                "file": "scene_programming.png",
                "analysis": "Παράδειγμα δημιουργίας σκηνής φωτισμού από την εφαρμογή.",
                "steps": [
                    "Επιλογή των γραμμών φωτισμού που θα συμμετέχουν.",
                    "Ορισμός επιπέδου φωτισμού για κάθε γραμμή.",
                    "Αποθήκευση σκηνής με όνομα (π.χ. 'Βραδινή ατμόσφαιρα').",
                    "Έλεγχος σκηνής από κινητό ή κεντρική οθόνη.",
                ],
            },
            "Ρύθμιση χρονοπρογράμματος": {
                "file": "schedule_programming.png",
                "analysis": "Παράδειγμα ρύθμισης χρονοπρογράμματος για αυτόματο άναμμα/σβήσιμο.",
                "steps": [
                    "Επιλογή ημέρας ή ομάδας ημερών.",
                    "Ορισμός ώρας έναρξης και λήξης.",
                    "Επιλογή σκηνής ή γραμμής φωτισμού.",
                    "Ενεργοποίηση/απενεργοποίηση του χρονοπρογράμματος.",
                ],
            },
        }

        choice_prog = st.selectbox(
            "Επιλέξτε διαδικασία προγραμματισμού:", list(prog_options.keys())
        )

        data_prog = prog_options[choice_prog]
        img_path_prog = os.path.join(PICTURES_DIR, data_prog["file"])

        st.markdown('<div class="tech-img">', unsafe_allow_html=True)
        st.image(img_path_prog, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### 📘 Ανάλυση")
        st.write(data_prog["analysis"])

        st.markdown("### 🧩 Βήματα")
        for step in data_prog["steps"]:
            st.write(f"- {step}")

    # ---------------------------------------------------------
    # TAB 3 — ΜΑΘΗΜΑΤΑ
    # ---------------------------------------------------------
    with tab3:
        st.subheader("🎓 Μαθήματα")

        st.write(
            "Εκπαιδευτικά παραδείγματα, διαγράμματα και υλικό που βοηθά στην κατανόηση "
            "των βασικών εννοιών και καλών πρακτικών."
        )

        lessons = {
            "Μάθημα 1 — Τι είναι το 0-10V": {
                "file": "lesson_0_10v.png",
                "desc": "Εισαγωγή στο 0-10V, πού χρησιμοποιείται και πώς επηρεάζει το dimming.",
            },
            "Μάθημα 2 — Ομαδοποίηση LED Strip": {
                "file": "lesson_ledstrip.png",
                "desc": "Παράδειγμα ομαδοποίησης πολλών LED strip σε μία σκηνή.",
            },
            "Μάθημα 3 — Ρύθμιση χρονοπρογράμματος": {
                "file": "lesson_schedule.png",
                "desc": "Αναλυτικό παράδειγμα ρύθμισης χρονοπρογράμματος για εξοικονόμηση ενέργειας.",
            },
        }

        choice_lesson = st.selectbox(
            "Επιλέξτε μάθημα:", list(lessons.keys())
        )

        data_lesson = lessons[choice_lesson]
        img_path_lesson = os.path.join(PICTURES_DIR, data_lesson["file"])

        st.markdown('<div class="tech-img">', unsafe_allow_html=True)
        st.image(img_path_lesson, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### 📘 Περιγραφή")
        st.write(data_lesson["desc"])

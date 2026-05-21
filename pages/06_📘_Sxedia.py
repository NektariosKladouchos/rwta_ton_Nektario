import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PICTURES_DIR = os.path.join(BASE_DIR, "pictures")

def show():

    st.title("📘 Τεχνικά Σχέδια")
    st.write("""
    Η ενότητα αυτή έχει δημιουργηθεί για ηλεκτρολόγους και τεχνικούς που χρειάζονται 
    άμεση πρόσβαση σε διαγράμματα σύνδεσης, τρόπους προγραμματισμού και εκπαιδευτικό υλικό.
    Όλα τα σχέδια είναι διαθέσιμα σε μορφή PNG/JPG ώστε να ανοίγουν άμεσα από κινητό.
    """)

    st.divider()

    tab1, tab2, tab3 = st.tabs([
        "🔌 Σχέδια Σύνδεσης",
        "⚙️ Τρόποι Προγραμματισμού",
        "🎓 Μαθήματα"
    ])

    # ---------------------------------------------------------
    #  TAB 1 — ΣΧΕΔΙΑ ΣΥΝΔΕΣΗΣ
    # ---------------------------------------------------------
    with tab1:

        st.subheader("🔌 Σχέδια Σύνδεσης")

        options = {
            "Σύνδεση Dimmer 220V": {
                "file": "dimmer_220v.png",
                "analysis": "Σύνδεση dimmer 220V με LED panel ή PL.",
                "benefits": [
                    "Ομαλό dimming",
                    "Απλή καλωδίωση",
                    "Συμβατότητα με LED panel",
                    "Μικρότερη κατανάλωση"
                ]
            },
            "Σύνδεση LED Strip 24V": {
                "file": "ledstrip_24v.png",
                "analysis": "Σύνδεση LED strip 24V με τροφοδοτικό και controller.",
                "benefits": [
                    "Σταθερή λειτουργία",
                    "Μεγάλο μήκος ταινίας",
                    "Ομαλό dimming",
                    "Ασφαλής χαμηλή τάση"
                ]
            },
            "Σύνδεση DALI DT6": {
                "file": "dali_dt6.png",
                "analysis": "Σύνδεση DALI driver DT6 με κεντρικό controller.",
                "benefits": [
                    "Ακριβής έλεγχος φωτισμού",
                    "Ομαδοποίηση",
                    "Διευθυνσιοδότηση",
                    "Επαγγελματική εγκατάσταση"
                ]
            }
        }

        choice = st.selectbox("Επιλέξτε σχέδιο:", list(options.keys()))

        data = options[choice]
        img_path = os.path.join(PICTURES_DIR, data["file"])

        st.image(img_path, use_container_width=True)

        st.markdown(f"### 📘 Ανάλυση")
        st.write(data["analysis"])

        st.markdown("### ⭐ Τι κερδίζεις")
        for b in data["benefits"]:
            st.write(f"- {b}")

    # ---------------------------------------------------------
    #  TAB 2 — ΤΡΟΠΟΙ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ
    # ---------------------------------------------------------
    with tab2:

        st.subheader("⚙️ Τρόποι Προγραμματισμού")

        prog_options = {
            "Δημιουργία Σκηνής": {
                "file": "scene_programming.png",
                "analysis": "Πώς δημιουργούμε σκηνή από την εφαρμογή.",
                "steps": [
                    "Επιλογή συσκευών",
                    "Ορισμός επιπέδων φωτισμού",
                    "Αποθήκευση σκηνής",
                    "Έλεγχος από κινητό"
                ]
            },
            "Χρονοπρογράμματα": {
                "file": "schedule_programming.png",
                "analysis": "Προγραμματισμός ενεργειών με βάση την ώρα.",
                "steps": [
                    "Επιλογή ημέρας",
                    "Ορισμός ώρας",
                    "Επιλογή ενέργειας",
                    "Ενεργοποίηση προγράμματος"
                ]
            }
        }

        choice2 = st.selectbox("Επιλέξτε διαδικασία:", list(prog_options.keys()))

        data2 = prog_options[choice2]
        img_path2 = os.path.join(PICTURES_DIR, data2["file"])

        st.image(img_path2, use_container_width=True)

        st.markdown("### 📘 Ανάλυση")
        st.write(data2["analysis"])

        st.markdown("### 🧩 Βήματα")
        for s in data2["steps"]:
            st.write(f"- {s}")

    # ---------------------------------------------------------
    #  TAB 3 — ΜΑΘΗΜΑΤΑ
    # ---------------------------------------------------------
    with tab3:

        st.subheader("🎓 Μαθήματα")

        lessons = {
            "Μάθημα 1 — Τι είναι το 0-10V": {
                "file": "lesson_0_10v.png",
                "desc": "Εισαγωγή στο πρωτόκολλο 0-10V και πώς λειτουργεί."
            },
            "Μάθημα 2 — Ομαδοποίηση LED Strip": {
                "file": "lesson_ledstrip.png",
                "desc": "Πώς κάνουμε ομαδοποίηση πολλών LED strip."
            },
            "Μάθημα 3 — Ρύθμιση Χρονοπρογράμματος": {
                "file": "lesson_schedule.png",
                "desc": "Πώς ρυθμίζουμε χρονοπρόγραμμα από την εφαρμογή."
            }
        }

        choice3 = st.selectbox("Επιλέξτε μάθημα:", list(lessons.keys()))

        data3 = lessons[choice3]
        img_path3 = os.path.join(PICTURES_DIR, data3["file"])

        st.image(img_path3, use_container_width=True)

        st.markdown("### 📘 Περιγραφή")
        st.write(data3["desc"])

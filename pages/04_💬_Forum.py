# pages/04_💬_Forum.py

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==================================================
# SETTINGS
# ==================================================

st.set_page_config(
    page_title="Public Forum",
    page_icon="💬",
    layout="centered"
)

CSV_FILE = "forum_data.csv"
ADMIN_PASSWORD = "geyer123"

# ==================================================
# CREATE CSV IF NOT EXISTS
# ==================================================

if not os.path.exists(CSV_FILE):

    empty_df = pd.DataFrame(columns=[
        "id",
        "date",
        "name",
        "question",
        "answer"
    ])

    empty_df.to_csv(CSV_FILE, index=False)

# ==================================================
# FUNCTIONS
# ==================================================

def load_data():

    try:

        df = pd.read_csv(
            CSV_FILE,
            dtype=str
        )

    except Exception:

        df = pd.DataFrame(columns=[
            "id",
            "date",
            "name",
            "question",
            "answer"
        ])

    # Αν είναι άδειο
    if df.empty:

        df = pd.DataFrame(columns=[
            "id",
            "date",
            "name",
            "question",
            "answer"
        ])

    # Συμπλήρωση κενών
    df = df.fillna("")

    # Μετατροπή ID σε integer
    if "id" in df.columns:

        df["id"] = pd.to_numeric(
            df["id"],
            errors="coerce"
        ).fillna(0).astype(int)

    return df


def save_data(df):

    df.to_csv(
        CSV_FILE,
        index=False
    )

# ==================================================
# LOAD DATA
# ==================================================

df = load_data()

# ==================================================
# TITLE
# ==================================================

st.title("💬 Public Forum")

st.write(
    "Γράψε την ερώτησή σου και δες απαντήσεις από τον διαχειριστή."
)

# ==================================================
# QUESTION FORM
# ==================================================

with st.expander("➕ Νέα Ερώτηση", expanded=False):

    with st.form("question_form", clear_on_submit=True):

        name = st.text_input("Όνομα")

        question = st.text_area(
            "Ερώτηση",
            height=120
        )

        submit_question = st.form_submit_button("Υποβολή")

        if submit_question:

            if not name.strip():

                st.warning("Συμπλήρωσε όνομα.")

            elif not question.strip():

                st.warning("Συμπλήρωσε ερώτηση.")

            else:

                # νέο ID
                if len(df) == 0:
                    new_id = 1
                else:
                    new_id = int(df["id"].max()) + 1

                # νέα εγγραφή
                new_row = pd.DataFrame([{
                    "id": new_id,
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "name": str(name),
                    "question": str(question),
                    "answer": ""
                }])

                # προσθήκη
                df = pd.concat(
                    [df, new_row],
                    ignore_index=True
                )

                # αποθήκευση
                save_data(df)

                st.success("Η ερώτηση καταχωρήθηκε!")

                st.rerun()

# ==================================================
# QUESTIONS LIST
# ==================================================

st.divider()

st.subheader("📋 Ερωτήσεις")

df = load_data()

if len(df) == 0:

    st.info("Δεν υπάρχουν ακόμη ερωτήσεις.")

else:

    # newest first
    df = df.sort_values(
        by="id",
        ascending=False
    )

    for _, row in df.iterrows():

        with st.container(border=True):

            st.markdown(f"### ❓ {row['question']}")

            st.caption(
                f"👤 {row['name']} | 🕒 {row['date']}"
            )

            # απάντηση
            if str(row["answer"]).strip() != "":

                st.success(
                    f"✅ Απάντηση:\n\n{row['answer']}"
                )

# ==================================================
# ADMIN PANEL
# ==================================================

st.sidebar.title("🔒 Admin Panel")

admin_password = st.sidebar.text_input(
    "Password",
    type="password"
)

# ==================================================
# ADMIN ACCESS
# ==================================================

if admin_password == ADMIN_PASSWORD:

    st.sidebar.success("Επιτυχής σύνδεση")

    df = load_data()

    if len(df) > 0:

        # επιλογή ερώτησης
        selected_id = st.sidebar.selectbox(
            "Επιλογή Question ID",
            df["id"].tolist()
        )

        # επιλεγμένη γραμμή
        selected_row = df[
            df["id"] == int(selected_id)
        ].iloc[0]

        st.sidebar.markdown("---")

        st.sidebar.write("### Ερώτηση")

        st.sidebar.info(
            selected_row["question"]
        )

        # answer box
        answer_text = st.sidebar.text_area(
            "Απάντηση",
            value=str(selected_row["answer"]),
            height=180
        )

        # SAVE ANSWER
        if st.sidebar.button("💾 Αποθήκευση Απάντησης"):

            df.loc[
                df["id"] == int(selected_id),
                "answer"
            ] = str(answer_text)

            save_data(df)

            st.sidebar.success(
                "Η απάντηση αποθηκεύτηκε!"
            )

            st.rerun()

        st.sidebar.markdown("---")

        # DELETE QUESTION
        if st.sidebar.button("🗑️ Διαγραφή Ερώτησης"):

            df = df[
                df["id"] != int(selected_id)
            ]

            save_data(df)

            st.sidebar.success(
                "Η ερώτηση διαγράφηκε!"
            )

            st.rerun()

    else:

        st.sidebar.info(
            "Δεν υπάρχουν ερωτήσεις."
        )

else:

    st.sidebar.caption(
        "Πρόσβαση μόνο διαχειριστή"
    )

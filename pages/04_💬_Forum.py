# pages/Forum.py

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# =========================
# CONFIG
# =========================

st.set_page_config(page_title="Public Forum", page_icon="💬")

CSV_FILE = "forum_data.csv"
ADMIN_PASSWORD = "geyer123"

# =========================
# CREATE CSV IF NOT EXISTS
# =========================

if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=[
        "id",
        "date",
        "name",
        "question",
        "answer"
    ])
    df.to_csv(CSV_FILE, index=False)

# =========================
# LOAD DATA
# =========================

def load_data():
    return pd.read_csv(CSV_FILE)

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

df = load_data()

# =========================
# TITLE
# =========================

st.title("💬 Public Forum")

st.write("Κάνε την ερώτησή σου και δες απαντήσεις από την κοινότητα ή τον διαχειριστή.")

# =========================
# QUESTION FORM
# =========================

with st.expander("➕ Κάνε νέα ερώτηση", expanded=False):

    with st.form("question_form", clear_on_submit=True):

        name = st.text_input("Το όνομά σου")
        question = st.text_area("Η ερώτησή σου")

        submit = st.form_submit_button("Υποβολή")

        if submit:

            if name.strip() == "" or question.strip() == "":
                st.warning("Συμπλήρωσε όνομα και ερώτηση.")
            else:

                new_id = 1

                if len(df) > 0:
                    new_id = int(df["id"].max()) + 1

                new_row = {
                    "id": new_id,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "name": name,
                    "question": question,
                    "answer": ""
                }

                df = pd.concat(
                    [df, pd.DataFrame([new_row])],
                    ignore_index=True
                )

                save_data(df)

                st.success("Η ερώτηση καταχωρήθηκε!")

                st.rerun()

# =========================
# DISPLAY QUESTIONS
# =========================

st.subheader("📋 Ερωτήσεις")

df = load_data()

if len(df) == 0:

    st.info("Δεν υπάρχουν ακόμα ερωτήσεις.")

else:

    df = df.sort_values(by="id", ascending=False)

    for _, row in df.iterrows():

        with st.container(border=True):

            st.markdown(f"### ❓ {row['question']}")

            st.caption(
                f"Από: {row['name']} • {row['date']}"
            )

            if pd.notna(row["answer"]) and str(row["answer"]).strip() != "":

                st.success(f"✅ Απάντηση: {row['answer']}")

# =========================
# ADMIN PANEL
# =========================

st.sidebar.title("🔒 Admin")

admin_pass = st.sidebar.text_input(
    "Password",
    type="password"
)

if admin_pass == ADMIN_PASSWORD:

    st.sidebar.success("Συνδέθηκε ο διαχειριστής")

    df = load_data()

    if len(df) > 0:

        question_ids = df["id"].tolist()

        selected_id = st.sidebar.selectbox(
            "Επιλογή ερώτησης",
            question_ids
        )

        selected_row = df[df["id"] == selected_id].iloc[0]

        st.sidebar.markdown("### Ερώτηση")
        st.sidebar.write(selected_row["question"])

        answer_text = st.sidebar.text_area(
            "Απάντηση",
            value="" if pd.isna(selected_row["answer"]) else selected_row["answer"],
            height=150
        )

        if st.sidebar.button("💾 Αποθήκευση απάντησης"):

            df.loc[df["id"] == selected_id, "answer"] = answer_text

            save_data(df)

            st.sidebar.success("Η απάντηση αποθηκεύτηκε!")

            st.rerun()

        st.sidebar.divider()

        if st.sidebar.button("🗑️ Διαγραφή ερώτησης"):

            df = df[df["id"] != selected_id]

            save_data(df)

            st.sidebar.success("Η ερώτηση διαγράφηκε!")

            st.rerun()

else:

    st.sidebar.info("Μόνο για διαχειριστή")

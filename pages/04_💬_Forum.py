import streamlit as st
import pandas as pd

# 1. Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# 2. Το "μαγικό" link από τη Δημοσίευση στον Ιστό
# Χρησιμοποιούμε το link που τελειώνει σε pub?output=csv
sheet_url = "https://google.com"

st.title("💬 Forum Τεχνικής Υποστήριξης")
st.markdown("---")

st.subheader("Πρόσφατες Συζητήσεις")

# 3. Διάβασμα Δεδομένων
try:
    # Διαβάζουμε το CSV link
    df = pd.read_csv(sheet_url)
    
    # Καθαρίζουμε τα ονόματα των στηλών
    df.columns = df.columns.str.strip()
    
    if not df.empty:
        for index, row in df.iterrows():
            # Σιγουρευόμαστε ότι υπάρχει ερώτηση στη γραμμή
            if pd.notna(row.iloc[2]): 
                with st.container():
                    st.markdown(f"**👤 {row.iloc[1]}** | 📅 {row.iloc[0]}")
                    st.info(f"❓ {row.iloc[2]}")
                    
                    apantisi = row.iloc[3]
                    if pd.notna(apantisi) and str(apantisi).strip() != "":
                        st.success(f"✅ **Απάντηση:** {apantisi}")
                    else:
                        st.warning("🕒 *Αναμένεται απάντηση από τον Νεκτάριο...*")
                    st.write("---")
    else:
        st.write("Δεν υπάρχουν ακόμα συζητήσεις.")

except Exception as e:
    st.error("⚠️ Σύνδεση σε αναμονή... Παρακαλώ κάντε Refresh στη σελίδα.")

# 4. ΠΕΡΙΟΧΗ ΔΙΑΧΕΙΡΙΣΗΣ
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")
if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες!")
    # Το link για να ανοίγεις εσύ το Excel και να γράφεις
    edit_link = "https://google.com"
    st.sidebar.markdown(f"[👉 ΑΝΟΙΓΜΑ EXCEL]({edit_link})")

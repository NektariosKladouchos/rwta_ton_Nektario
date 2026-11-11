from supabase import create_client
import streamlit as st

SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def log_event(page, event, user=None, extra=None):

    # Μην καταγράφεις Admin ενέργειες
    if st.session_state.get("is_admin", False):
        return

    try:
        supabase.table("analytics").insert({
            "page": page,
            "event": event,
            "user_email": user,
            "extra": extra
        }).execute()

    except Exception:
        pass

import json
import re
from io import BytesIO
from pathlib import Path
from typing import List, Optional

import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

# --- PAGE STYLING ---
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
    .st-emotion-cache-wfksaw {

    justify-content: center !important;
}
.e16n7gab0{
    flex-direction: row !important;
}

.sme-header-time{
text-align:end !important;}
.st-emotion-cache-r3ry0f{
gap:1rem !important;}

.sme-header-date {
    font-size: 1rem !important;
  
    }
    .sme-header-center {
    
    font-size: 1rem !important;
    
    }
.sme-header-time {
    
    font-size: 1rem !important;
   
    }
.sme-header-center .sme-name {
    font-weight: 700;

}
    .st-emotion-cache-tn0cau {
  
    gap: 0.75rem !important;; 
    
}
/* Common style for all four buttons */
.st-key-nav_prev button[data-testid="stBaseButton-secondary"],
.st-key-nav_next button[data-testid="stBaseButton-secondary"],
.st-key-nav_save button[data-testid="stBaseButton-secondary"],
.st-key-nav_logout button[data-testid="stBaseButton-secondary"] {
  width: 100px;                 /* same width for all */
  height: 36px;                 /* moderate compact height */
  font-size: 14px;
  border-radius: 6px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

/* Individual color schemes */
.st-key-nav_prev button[data-testid="stBaseButton-secondary"] {
  background-color: #b0b0b0 !important;
  color: #000 !important;
}
.st-key-nav_prev button[data-testid="stBaseButton-secondary"]:hover {
  background-color: #8c8c8c !important;
  color: #fff !important;
}

.st-key-nav_next button[data-testid="stBaseButton-secondary"] {
  background-color: #007bff !important;
  color: #fff !important;
}
.st-key-nav_next button[data-testid="stBaseButton-secondary"]:hover {
  background-color: #0056b3 !important;
}

.st-key-nav_save button[data-testid="stBaseButton-secondary"] {
  background-color: #28a745 !important;
  color: #fff !important;
}
.st-key-nav_save button[data-testid="stBaseButton-secondary"]:hover {
  background-color: #1e7e34 !important;
}

.st-key-nav_logout button[data-testid="stBaseButton-secondary"] {
  background-color: #dc3545 !important;
  color: #fff !important;
}
.st-key-nav_logout button[data-testid="stBaseButton-secondary"]:hover {
  background-color: #a71d2a !important;
}

.stAppHeader{
display:none !important:}



    header, footer { display: none !important; }
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
    body { overflow-x: hidden; }
    .main { margin-top: 0 !important; margin-bottom: 0 !important; }
    .tight-label {
        font-size: 0.85em !important;
        font-weight: 500 !important;
        line-height: 1.08;
        margin-bottom: -0.34em !important;
        margin-top: -0.51em !important;
        padding-bottom: 0 !important;
        padding-top: 0 !important;
    }
    .stTextArea {
        margin-top: -0.44em !important;
        margin-bottom: -0.55em !important;
    }

    textarea[data-baseweb="textarea"] {
        min-height: 44px !important;
        font-size: 0.98em !important;
    }
    .stTextArea label { display: none !important; }
    .cw-40-fixed {
        height: 40vh !important;
        min-height: 40vh !important;
        max-height: 40vh !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        font-size: 1.035em !important;
        line-height: 1.14 !important;
        margin: 0 !important;
        padding: 0 0.09em 0.28em 0.09em !important;
        overflow-y: auto;
        overflow-x: hidden;
        box-sizing: border-box;
        background: none;
    }
    .cw-40-fixed strong { font-weight: 600 !important; }
.nav-id {
        font-weight: 600;
        color: #1f2937;
        white-space: nowrap;
    }
    .nav-rows {
        font-weight: 600;
        color: #111827;
        text-align: center;
        white-space: nowrap;
    }
    .nav-save-btn .stButton > button {
        padding: 0.35rem 0.75rem !important;
        font-size: 0.78rem !important;
        border-radius: 8px !important;
    }
    .nav-save-btn .stDownloadButton > button {
        width: 40px !important;
        height: 36px !important;
        border-radius: 8px !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 1rem !important;
        background: #f3f4f6 !important;
        color: #1f2937 !important;
        border: 1px solid #d1d5db !important;
    }
    .nav-save-btn .stDownloadButton > button:hover {
        background: #e5e7eb !important;
        border-color: #9ca3af !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- DATA SOURCES & CONSTANTS ---
DATA_DIR = Path(__file__).resolve().parent
DEFAULT_QUESTION_FILE = DATA_DIR / "bl_bio_bot_unit_4_chap_9_the_tissues_qb.xlsx"
SME_CREDENTIALS_FILE = DATA_DIR / "SME_Data.xlsx"
SESSION_STORAGE_DIR = DATA_DIR / "user_sessions"
TAMIL_QUESTION_COL = "கேள்வி"
TAMIL_OPTIONS_COL = "விருப்பங்கள் "
TAMIL_ANSWER_COL = "பதில் "
TAMIL_EXPLANATION_COL = "விளக்கம் "
ENGLISH_QUESTION_COL = "question "
ENGLISH_OPTIONS_COL = "questionOptions"
ENGLISH_ANSWER_COL = "answers "
ENGLISH_EXPLANATION_COL = "explanation"
ROW_ID_COL = "_id"
def load_dataframe(source) -> Optional[pd.DataFrame]:
    """Read an Excel source into a dataframe, handling errors gracefully."""
    try:
        df = pd.read_excel(source)
    except FileNotFoundError:
        st.warning(f"File '{source}' not found.")
        return None
    except ValueError as exc:
        st.warning(f"Unable to read Excel file '{getattr(source, 'name', source)}': {exc}")
        return None
    except Exception as exc:  # noqa: BLE001
        st.warning(f"Unexpected error while reading '{getattr(source, 'name', source)}': {exc}")
        return None

    if df.empty:
        st.warning(f"Excel file '{getattr(source, 'name', source)}' is empty.")
        return None

    return df.fillna("")


def parse_tamil_options(raw_value) -> List[str]:
    """Split the Tamil options string into individual choices."""
    if not raw_value:
        return ["", "", "", ""]

    parts = [part.strip() for part in str(raw_value).split("|") if part.strip()]
    cleaned: List[str] = []

    for part in parts:
        candidate = part
        for delimiter in (")", ".", ":"):
            if delimiter in candidate and candidate.index(delimiter) < 3:
                candidate = candidate.split(delimiter, 1)[1]
                break
        cleaned.append(candidate.strip())

    while len(cleaned) < 4:
        cleaned.append("")
    return cleaned[:4]


def set_dataset(
    df: pd.DataFrame,
    source_name: str,
    *,
    source_size: Optional[int] = None,
    source_type: str = "upload",
) -> None:
    """Store the active dataframe in session state."""
    st.session_state.pop("download_ready", None)
    st.session_state.pop("download_bytes", None)
    st.session_state.pop("last_save_message", None)
    st.session_state.pop("last_save_error", None)
    st.session_state["question_df"] = df
    st.session_state["question_total"] = len(df)
    st.session_state["question_source"] = source_name
    st.session_state["question_source_size"] = source_size
    st.session_state["question_index"] = 0
    st.session_state["question_source_type"] = source_type


def format_size(size_bytes: Optional[int]) -> str:
    """Return a human-friendly size string."""
    if not size_bytes:
        return ""
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    return f"{size_bytes / 1024:.1f} KB"


def sanitize_filename_component(value: Optional[str]) -> str:
    """Return a filesystem-safe component derived from the provided value."""
    if not value:
        return "user"
    cleaned = re.sub(r"[^0-9A-Za-z]+", "_", value)
    cleaned = cleaned.strip("_")
    return cleaned or "user"


def build_download_filename(source_name: Optional[str], username: Optional[str]) -> str:
    """Construct the download filename with the required suffix."""
    base_name = Path(source_name or "questions").stem or "questions"
    safe_base = sanitize_filename_component(base_name)
    safe_user = sanitize_filename_component(username or "")
    return f"{safe_base}_edited_{safe_user}.xlsx"


def dataframe_to_excel_bytes(df: pd.DataFrame) -> bytes:
    """Serialize the dataframe to an Excel binary stream."""
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    buffer.seek(0)
    return buffer.getvalue()


def get_user_storage_paths(user_identifier: Optional[str]) -> tuple[Optional[Path], Optional[Path]]:
    """Return workbook and metadata storage paths for a given user."""
    if not user_identifier:
        return None, None
    SESSION_STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    safe_user = sanitize_filename_component(user_identifier)
    workbook_path = SESSION_STORAGE_DIR / f"{safe_user}_workspace.xlsx"
    metadata_path = SESSION_STORAGE_DIR / f"{safe_user}_metadata.json"
    return workbook_path, metadata_path


def persist_user_progress(current_index: int) -> None:
    """Persist the current workbook and index for the active SME."""
    df = st.session_state.get("question_df")
    user_identifier = st.session_state.get("sme_email")
    if df is None or not user_identifier:
        return

    workbook_path, metadata_path = get_user_storage_paths(user_identifier)
    if workbook_path is None or metadata_path is None:
        return

    try:
        workbook_path.write_bytes(dataframe_to_excel_bytes(df))
        metadata = {
            "current_index": int(current_index),
            "source_name": st.session_state.get("question_source"),
            "saved_at": pd.Timestamp.now().isoformat(),
        }
        metadata_path.write_text(json.dumps(metadata))
    except Exception as exc:  # noqa: BLE001
        st.session_state["last_save_error"] = f"Unable to persist session: {exc}"


def load_saved_progress() -> None:
    """Restore the SME's last saved progress if it exists."""
    if st.session_state.get("resume_checked"):
        return
    if st.session_state.get("question_df") is not None:
        st.session_state["resume_checked"] = True
        return
    user_identifier = st.session_state.get("sme_email")
    if not user_identifier:
        return

    workbook_path, metadata_path = get_user_storage_paths(user_identifier)
    if not workbook_path or not workbook_path.exists() or not metadata_path or not metadata_path.exists():
        st.session_state["resume_checked"] = True
        return

    try:
        metadata = json.loads(metadata_path.read_text())
    except Exception:  # noqa: BLE001
        metadata = {}

    df = load_dataframe(workbook_path)
    if df is None:
        st.session_state["resume_checked"] = True
        return

    source_name = metadata.get("source_name") or workbook_path.name
    set_dataset(
        df,
        source_name,
        source_size=workbook_path.stat().st_size if workbook_path.exists() else None,
        source_type="resume",
    )
    saved_index = metadata.get("current_index", 0)
    st.session_state["question_index"] = max(0, min(saved_index, len(df) - 1))
    try:
        st.session_state["download_bytes"] = workbook_path.read_bytes()
        st.session_state["download_ready"] = True
    except Exception:  # noqa: BLE001
        st.session_state.pop("download_bytes", None)
        st.session_state["download_ready"] = False
    st.session_state["resume_checked"] = True
    st.session_state["resume_loaded"] = True


def apply_current_row_edits(
    question_df: Optional[pd.DataFrame],
    current_index: int,
    question_key: str,
    option_widget_keys: List[str],
    explanation_key: str,
) -> bool:
    """Persist the current widget inputs back into the dataframe."""
    if question_df is None or question_df.empty:
        return False
    if current_index < 0 or current_index >= len(question_df):
        return False

    row_idx = question_df.index[current_index]
    new_question = st.session_state.get(question_key, "")
    new_explanation = st.session_state.get(explanation_key, "")
    new_options = [st.session_state.get(key, "") for key in option_widget_keys]
    joined_options = " | ".join(option.strip() for option in new_options if option.strip())

    changed = False
    if question_df.at[row_idx, TAMIL_QUESTION_COL] != new_question:
        changed = True
    if question_df.at[row_idx, TAMIL_OPTIONS_COL] != joined_options:
        changed = True
    if question_df.at[row_idx, TAMIL_EXPLANATION_COL] != new_explanation:
        changed = True

    question_df.at[row_idx, TAMIL_QUESTION_COL] = new_question
    question_df.at[row_idx, TAMIL_OPTIONS_COL] = joined_options
    question_df.at[row_idx, TAMIL_EXPLANATION_COL] = new_explanation
    st.session_state["question_df"] = question_df
    return changed


def style_file_uploaders(configs: List[dict]) -> None:
    """Adjust the file uploader appearance for each configured dropzone."""
    css_parts = [
        "<style>",
        "section[data-testid='stFileUploader'] div[data-testid='stFileUploaderDropzone'] small,"
        " section[data-testid='stFileUploader'] span[data-testid='stFileUploaderFileName'],"
        " section[data-testid='stFileUploader'] span[data-testid='stFileUploaderFileSize'],"
        " section[data-testid='stFileUploader'] div[data-testid='stFileUploaderInstructions'],"
        " section[data-testid='stFileUploader'] div[data-testid='stFileUploaderDropzone'] div[aria-live='polite']"
        " {display:none!important;}",
    ]

    for idx, cfg in enumerate(configs, start=1):
        placeholder = cfg.get("placeholder", "")
        filename = cfg.get("filename")
        size_bytes = cfg.get("size")
        selector = cfg.get("selector")

        if not selector:
            selector = f"section[data-testid='stFileUploader']:nth-of-type({idx})"

        if filename:
            size_text = format_size(size_bytes)
            text = f"{filename} {size_text}".strip()
        else:
            text = placeholder

        if not text:
            continue

        content_json = json.dumps(text)
        css_parts.extend(
            [
                f"{selector} div[data-testid='stFileUploaderDropzone'] {{"
                "position:relative; display:flex!important; align-items:center!important;"
                " justify-content:flex-end!important; padding:0.55rem 1.2rem!important;"
                " min-height:64px!important; border-radius:16px!important;"
                "}}",
                f"{selector} div[data-testid='stFileUploaderDropzone'] button {{margin-left:auto!important;}}",
                f"{selector} div[data-testid='stFileUploaderDropzone']::before {{content:{content_json};"
                " position:absolute; top:50%; left:1.2rem; transform:translateY(-50%);"
                " font-weight:600; color:#1f2c44;}}",
            ]
        )

    css_parts.append("</style>")
    st.markdown("\n".join(css_parts), unsafe_allow_html=True)


def safe_rerun() -> None:
    """Trigger a Streamlit rerun across supported versions."""
    rerun_fn = getattr(st, "rerun", None)
    if callable(rerun_fn):
        rerun_fn()
        return
    exp_rerun = getattr(st, "experimental_rerun", None)
    if callable(exp_rerun):
        exp_rerun()


@st.cache_data
def load_sme_credentials(path: Path) -> Optional[pd.DataFrame]:
    """Load the SME credentials workbook."""
    if not path.exists():
        return None
    try:
        df = pd.read_excel(path, header=1).fillna("")
    except Exception:  # noqa: BLE001
        return None
    required_columns = {"Email", "Password"}
    if not required_columns.issubset({col.strip() for col in df.columns}):
        return None
    return df


def require_login() -> None:
    """Render the login screen until the user authenticates."""
    if st.session_state.get("authenticated"):
        return

    credentials_df = load_sme_credentials(SME_CREDENTIALS_FILE)
    if credentials_df is None or credentials_df.empty:
        st.error(
            "SME credentials file is missing or invalid. "
            "Please ensure 'SME_Data.xlsx' exists with 'Email' and 'Password' columns."
        )
        st.stop()

    st.markdown(
        """
        <style>
        div[data-testid="stForm"] {
            max-width: 430px;
            margin: 10vh auto 6vh;
            position: relative;
            padding: 0 1.2rem;
        }
        div[data-testid="stForm"]::before,
        div[data-testid="stForm"]::after {
            content: "";
            position: absolute;
            inset: auto;
            border-radius: 999px;
            filter: blur(80px);
            opacity: 0.6;
            z-index: -1;
            pointer-events: none;
        }
        div[data-testid="stForm"]::before {
            top: -14vh;
            left: 10%;
            width: 320px;
            height: 320px;
            background: rgba(99, 102, 241, 0.22);
        }
        div[data-testid="stForm"]::after {
            bottom: -18vh;
            right: 6%;
            width: 280px;
            height: 280px;
            background: rgba(244, 114, 182, 0.24);
        }
        div[data-testid="stForm"] > form {
            background: rgba(255, 255, 255, 0.96);
            padding: 2.9rem 2.7rem 2.5rem;
            border-radius: 28px;
            box-shadow: 0 30px 70px rgba(15, 23, 42, 0.14);
            border: 1px solid rgba(148, 163, 184, 0.18);
            position: relative;
            overflow: hidden;
            z-index: 1;
        }
        div[data-testid="stForm"] > form::before {
            content: "";
            position: absolute;
            inset: -140px -180px auto -180px;
            height: 280px;
            background: radial-gradient(circle at center, rgba(99, 102, 241, 0.24), rgba(59, 130, 246, 0));
            z-index: 0;
            filter: blur(4px);
            pointer-events: none;
        }
        div[data-testid="stForm"] > form > div {
            position: relative;
            z-index: 1;
        }
        div[data-testid="stForm"] .login-logo {
            width: 86px;
            height: 86px;
            margin: 0 auto 1.5rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #eef2ff, #dbeafe);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            letter-spacing: 0.08em;
            color: #3730a3;
            font-size: 1rem;
            box-shadow: 0 16px 36px rgba(79, 70, 229, 0.2);
        }
        div[data-testid="stForm"] .login-title {
            text-align: center;
            font-size: 1.6rem;
            font-weight: 700;
            color: #111827;
            margin-bottom: 0.35rem;
        }
        div[data-testid="stForm"] .login-subtitle {
            text-align: center;
            font-size: 0.96rem;
            color: #64748b;
            margin-bottom: 2.3rem;
        }
        div[data-testid="stForm"] .stTextInput {
            margin-bottom: 1.35rem;
        }
        div[data-testid="stForm"] .stTextInput label {
            font-weight: 600;
            font-size: 0.79rem;
            color: #1f2937;
            margin-bottom: 0.45rem;
        }
        div[data-testid="stForm"] .stTextInput > div > div {
            border-radius: 14px;
            border: 1px solid #e2e8f0;
            background: #f8fafc;
            box-shadow: inset 0 1px 0 rgba(148, 163, 184, 0.18);
            transition: all 0.2s ease;
        }
        div[data-testid="stForm"] .stTextInput > div > div:hover {
            border-color: #cbd5f5;
        }
        div[data-testid="stForm"] .stTextInput > div > div:focus-within {
            border-color: #6366f1;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.18);
        }
        div[data-testid="stForm"] input {
            padding: 0.72rem 1rem;
            font-size: 0.92rem;
            color: #0f172a;
            background: transparent;
        }
        div[data-testid="stForm"] .stFormSubmitButton {
            margin-top: 0.4rem;
        }
        div[data-testid="stForm"] .stFormSubmitButton button {
            width: 100%;
            height: 2.85rem;
            border-radius: 14px;
            background: linear-gradient(135deg, #4f46e5, #6366f1);
            color: #fff;
            font-weight: 600;
            font-size: 0.96rem;
            border: none;
            box-shadow: 0 14px 36px rgba(99, 102, 241, 0.34);
            transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
        }
        div[data-testid="stForm"] .stFormSubmitButton button:hover {
            transform: translateY(-1px);
            background: linear-gradient(135deg, #4338ca, #4f46e5);
            box-shadow: 0 18px 42px rgba(79, 70, 229, 0.32);
        }
        div[data-testid="stForm"] .stAlert {
            border-radius: 12px;
        }
        @media (max-width: 640px) {
            div[data-testid="stForm"] {
                margin: 7vh auto 4vh;
                padding: 0 0.4rem;
            }
            div[data-testid="stForm"] > form {
                padding: 2.4rem 1.9rem 2.2rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.form("sme_login_form", clear_on_submit=False):
        st.markdown(
            """
            <div class="login-logo">LOGO</div>
            <h3 class="login-title">SME Workspace</h3>
            <p class="login-subtitle">Sign in with your SME account to continue.</p>
            """,
            unsafe_allow_html=True,
        )

        email = st.text_input("Email", placeholder="name@example.com")
        password = st.text_input("Password", placeholder="Enter your password", type="password")
        submitted = st.form_submit_button("Sign In", use_container_width=True)

    if submitted:
        if not email or not password:
            st.error("Email and password are required.")
        else:
            normalized = email.strip().lower()
            normalized_emails = credentials_df["Email"].astype(str).str.strip().str.lower()
            match = credentials_df[normalized_emails == normalized]

            if match.empty:
                st.error("Invalid email or password.")
            else:
                record = match.iloc[0]
                expected_password = str(record.get("Password", "")).strip()
                if password.strip() != expected_password:
                    st.error("Invalid email or password.")
                else:
                    email_value = record.get("Email", "").strip()
                    st.session_state["authenticated"] = True
                    st.session_state["sme_email"] = email_value
                    st.session_state["sme_display_name"] = (
                        record.get("SME Name") or record.get("SME Name ", "") or email_value
                    )
                    st.session_state["sme_record"] = record.to_dict()
                    safe_rerun()

    st.stop()


require_login()

# --- HEADER BAR WITH SME INFO ---
def format_tamil_date(now: pd.Timestamp) -> str:
    """Generate formatted Tamil/Gregorian date display placeholder."""
    # Placeholder Tamil date; adjust logic if proper calendar conversion is needed.
    tamil_date = "புரட்டாசி 30"
    gregorian = now.strftime("%Y %b %d")
    return f"{tamil_date} / {gregorian}"


def render_header():
    now = pd.Timestamp.now()
    formatted_date = format_tamil_date(now)
    time_str = now.strftime("%I : %M : %S %p").lstrip("0")
    sme_name = st.session_state.get("sme_display_name", "SME")

    st.markdown(
        """
        <style>
        .sme-header-wrapper {
            padding: 0;
            margin: 0 0 1rem 0;
            background: transparent;
            box-shadow: none;
        }
        .sme-header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            flex-wrap: nowrap;
        }
        .sme-header-date {
            font-size: 0.8rem;
            font-weight: 600;
            color: #1f2937;
            white-space: nowrap;
            flex-shrink: 0;
        }
        .sme-header-center {
            flex: 1;
            text-align: center;
            font-size: 0.8rem;
            font-weight: 500;
            color: #374151;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            min-width: 0;
        }
        .sme-header-center .sme-name {
            font-weight: 700;
            color: #111827;
        }
        .sme-header-time {
            font-size: 0.8rem;
            font-weight: 600;
            color: #1f2937;
            white-space: nowrap;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='sme-header-wrapper'><div class='sme-header-content'>", unsafe_allow_html=True)

    cols = st.columns([1.8, 3.2, 1.2], gap="small")

    with cols[0]:
        st.markdown(f"<div class='sme-header-date'>{formatted_date}</div>", unsafe_allow_html=True)

    with cols[1]:
        st.markdown(
            f"<div class='sme-header-center'>Subject Matter Expert (SME) Panel for "
            f"<span class='sme-name'>{sme_name}</span></div>",
            unsafe_allow_html=True,
        )

    with cols[2]:
        st.markdown(f"<div class='sme-header-time'>{time_str}</div>", unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)


render_header()

load_saved_progress()

# --- INITIAL DATA LOAD ---
col_questionnaire, col_glossary = st.columns(2, gap="large")
with col_questionnaire:
    st.markdown('<div class="tight-label" style="margin-top:0.2em;">Upload Lesson File</div>', unsafe_allow_html=True)
    questionnaire_file = st.file_uploader(
        "questionnaire-dropzone",
        type="xlsx",
        label_visibility="collapsed",
        key="questionnaire_file",
    )
with col_glossary:
    st.markdown('<div class="tight-label" style="margin-top:0.2em;">Upload Glossary File</div>', unsafe_allow_html=True)
    glossary_file = st.file_uploader(
        "glossary-dropzone",
        type="xlsx",
        label_visibility="collapsed",
        key="glossary_file",
    )

if questionnaire_file is not None:
    source_changed = st.session_state.get("question_source") != questionnaire_file.name or st.session_state.get(
        "question_source_type"
    ) != "upload"
    if source_changed:
        uploaded_df = load_dataframe(questionnaire_file)
        if uploaded_df is not None:
            set_dataset(
                uploaded_df,
                questionnaire_file.name,
                source_size=getattr(questionnaire_file, "size", None),
                source_type="upload",
            )
else:
    if (
        st.session_state.get("question_df") is None
        and st.session_state.get("question_source_type") != "default"
    ):
        if DEFAULT_QUESTION_FILE.exists():
            default_df = load_dataframe(DEFAULT_QUESTION_FILE)
            if default_df is not None:
                set_dataset(
                    default_df,
                    DEFAULT_QUESTION_FILE.name,
                    source_size=DEFAULT_QUESTION_FILE.stat().st_size,
                    source_type="default",
                )
        else:
            st.info("Default question bank was not found. Please upload an Excel file to continue.")

if glossary_file is not None:
    st.session_state["glossary_source"] = glossary_file.name
    st.session_state["glossary_size"] = getattr(glossary_file, "size", None)

style_file_uploaders(
    [
        {
            "filename": st.session_state.get("question_source"),
            "size": st.session_state.get("question_source_size"),
            "placeholder": "Upload Questionnaire",
            "selector": "section[aria-label='questionnaire-dropzone']",
        },
        {
            "filename": st.session_state.get("glossary_source"),
            "size": st.session_state.get("glossary_size"),
            "placeholder": "Upload Glossary",
            "selector": "section[aria-label='glossary-dropzone']",
        },
    ]
)

question_df: Optional[pd.DataFrame] = st.session_state.get("question_df")

if question_df is None:
    st.stop()

total_rows = st.session_state.get("question_total", len(question_df))
current_index = min(st.session_state.get("question_index", 0), total_rows - 1)
st.session_state["question_index"] = current_index  # Clamp in case data size changed.

# --- NAVIGATION CONTROLS ---
nav_container = st.container()
row = question_df.iloc[current_index]
row_id = str(row.get(ROW_ID_COL, "") or "")
rows_label = f"({current_index + 1} of {total_rows} rows)"
option_suffixes = ["A", "B", "C", "D"]
question_key = f"tamil_question_{current_index}"
explanation_key = f"tamil_explanation_{current_index}"
option_widget_keys = [f"tamil_option_{suffix}_{current_index}" for suffix in option_suffixes]

tamil_question_default = str(row.get(TAMIL_QUESTION_COL, ""))
tamil_options_default = parse_tamil_options(row.get(TAMIL_OPTIONS_COL, ""))
tamil_explanation_default = str(row.get(TAMIL_EXPLANATION_COL, row.get("விளக்கம்", "")))

editable_defaults = {
    question_key: tamil_question_default,
    explanation_key: tamil_explanation_default,
}
for widget_key, opt_value in zip(option_widget_keys, tamil_options_default):
    editable_defaults[widget_key] = opt_value

for key, default in editable_defaults.items():
    st.session_state.setdefault(key, default)


# --- EDITABLE BLOCK (TAMIL) ---
st.markdown('<div class="tight-label">கேள்வி</div>', unsafe_allow_html=True)
st.text_area(
    "",
    value=st.session_state.get(question_key, editable_defaults[question_key]),
    key=question_key,
    height=52,
    label_visibility="collapsed",
)

st.markdown('<div class="tight-label">விருப்பங்கள்</div>', unsafe_allow_html=True)
opt_cols_row1 = st.columns(2, gap="small")
opt_cols_row2 = st.columns(2, gap="small")
for col, widget_key in zip(opt_cols_row1 + opt_cols_row2, option_widget_keys):
    with col:
        st.text_area(
            "",
            value=st.session_state.get(widget_key, editable_defaults[widget_key]),
            key=widget_key,
            height=40,
            label_visibility="collapsed",
        )

st.markdown('<div class="tight-label">விளக்கம்</div>', unsafe_allow_html=True)
st.text_area(
    "",
    value=st.session_state.get(explanation_key, editable_defaults[explanation_key]),
    key=explanation_key,
    height=175,
    label_visibility="collapsed",
)

current_values = {key: st.session_state.get(key, "") for key in editable_defaults}
has_unsaved_changes = any(current_values[key] != editable_defaults[key] for key in editable_defaults)
if has_unsaved_changes:
    st.session_state["download_ready"] = False

download_bytes = st.session_state.get("download_bytes")
download_ready = bool(st.session_state.get("download_ready")) and bool(download_bytes)

download_filename = ""
if download_ready:
    download_filename = build_download_filename(
        st.session_state.get("question_source"),
        st.session_state.get("sme_display_name") or st.session_state.get("sme_email"),
    )

with nav_container:
    cols = st.columns([1.3, 1.8, 0.9, 0.9, 0.9, 0.9], gap="small")

    with cols[0]:
        st.markdown(f"<div class='nav-id'>ID {row_id}</div>", unsafe_allow_html=True)

    with cols[1]:
        st.markdown(f"<div class='nav-rows'>{rows_label}</div>", unsafe_allow_html=True)

    with cols[2]:
        prev_clicked = st.button(
            "Back",
            use_container_width=True,
            disabled=current_index <= 0,
            key="nav_prev",
        )

    with cols[3]:
        next_clicked = st.button(
            "Next",
            use_container_width=True,
            disabled=current_index >= total_rows - 1,
            key="nav_next",
        )

    with cols[4]:
        st.markdown("<div class='nav-save-btn'>", unsafe_allow_html=True)
        inner_cols = st.columns([1.0, 0.35], gap="small")
        with inner_cols[0]:
            save_clicked = st.button("Save", key="nav_save", disabled=not has_unsaved_changes)
        with inner_cols[1]:
            if download_ready and download_bytes:
                st.download_button(
                    "⬇️",
                    data=download_bytes,
                    file_name=download_filename,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key="nav_download",
                    help="Download updated Excel file",
                )
            else:
                st.markdown("<div style='height:0px;'></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with cols[5]:
        st.markdown("<div class='nav-save-btn'>", unsafe_allow_html=True)
        logout_clicked = st.button("Logout", key="nav_logout")
        st.markdown("</div>", unsafe_allow_html=True)

if 'prev_clicked' not in locals():
    prev_clicked = False
if 'next_clicked' not in locals():
    next_clicked = False
if 'save_clicked' not in locals():
    save_clicked = False
if 'logout_clicked' not in locals():
    logout_clicked = False

if prev_clicked:
    st.session_state["question_index"] = max(0, current_index - 1)
    safe_rerun()

if next_clicked:
    st.session_state["question_index"] = min(total_rows - 1, current_index + 1)
    safe_rerun()

if save_clicked and has_unsaved_changes:
    apply_current_row_edits(question_df, current_index, question_key, option_widget_keys, explanation_key)
    st.session_state["nav_last_save"] = pd.Timestamp.now().isoformat()
    try:
        st.session_state["download_bytes"] = dataframe_to_excel_bytes(st.session_state["question_df"])
        st.session_state["download_ready"] = True
        st.session_state["last_save_message"] = "Changes saved successfully."
        st.session_state.pop("last_save_error", None)
        persist_user_progress(current_index)
    except Exception as exc:  # noqa: BLE001
        st.session_state["last_save_error"] = f"Unable to prepare download: {exc}"
        st.session_state["download_ready"] = False
        st.session_state.pop("download_bytes", None)
    safe_rerun()

if logout_clicked:
    apply_current_row_edits(question_df, current_index, question_key, option_widget_keys, explanation_key)
    persist_user_progress(st.session_state.get("question_index", 0))
    st.session_state.clear()
    st.session_state["authenticated"] = False
    safe_rerun()

save_message = st.session_state.pop("last_save_message", None)
if save_message:
    st.markdown(
        """
        <style>
        .save-banner {
            position: fixed;
            top: 12px;
            left: 50%;
            transform: translateX(-50%);
            background: #ecfdf5;
            color: #047857;
            padding: 0.55rem 1.45rem;
            border-radius: 999px;
            box-shadow: 0 18px 36px rgba(16, 185, 129, 0.22);
            font-weight: 600;
            z-index: 2000;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(f"<div class='save-banner'>{save_message}</div>", unsafe_allow_html=True)

save_error = st.session_state.pop("last_save_error", None)
if save_error:
    st.error(save_error)


# --- DATA EXTRACTION FOR CURRENT ROW ---
tamil_question = st.session_state.get(question_key, editable_defaults[question_key])
tamil_options = [st.session_state.get(key, editable_defaults[key]) for key in option_widget_keys]
tamil_answer = str(row.get(TAMIL_ANSWER_COL, ""))
tamil_explanation = st.session_state.get(explanation_key, editable_defaults[explanation_key])
english_question = str(row.get(ENGLISH_QUESTION_COL, ""))
english_options = str(row.get(ENGLISH_OPTIONS_COL, ""))
english_answer = str(row.get(ENGLISH_ANSWER_COL, ""))
english_explanation = str(row.get(ENGLISH_EXPLANATION_COL, ""))

# --- DIVIDER ---
st.markdown(
    '<hr style="height:1.3px;border:none;background:#666;margin:0;padding:0;">',
    unsafe_allow_html=True,
)

# --- REFERENCE BLOCK (READ-ONLY) ---
st.markdown(
    f"""
    <div class="cw-40-fixed">
        <div><b>தமிழ்</b></div>
        <div><strong>கேள்வி:</strong> {tamil_question}</div>
        <div><strong>விருப்பங்கள்:</strong> {row.get(TAMIL_OPTIONS_COL, "")}</div>
        <div><strong>பதில்:</strong> {tamil_answer}</div>
        <div><strong>விளக்கம்:</strong> {tamil_explanation}</div>
        <div style="height:0.13em"></div>
        <div><b>English</b></div>
        <div><strong>Question:</strong> {english_question}</div>
        <div><strong>Options:</strong> {english_options}</div>
        <div><strong>Answer:</strong> {english_answer}</div>
        <div><strong>Explanation:</strong> {english_explanation}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

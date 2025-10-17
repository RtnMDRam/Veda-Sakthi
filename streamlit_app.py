import json
from pathlib import Path
from typing import List, Optional

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

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
.e196pkbe3{
height:70px !important;}
.sme-header-time{
text-align:end !important;}
.st-emotion-cache-r3ry0f{
gap:1rem !important;}

.sme-header-date {
    font-size: 1rem !important;
     color: #fff !important;
    }
    .sme-header-center {
    
    font-size: 1rem !important;
     color: #fff !important;
    }
.sme-header-time {
    
    font-size: 1rem !important;
     color: #fff !important;
    }
.sme-header-center .sme-name {
    font-weight: 700;
     color: #fff !important;
}
    .st-emotion-cache-18kf3ut .e196pkbe3{
    background: #03A9F4 !important;;
    color: #fff !important;
    border-radius: 12px;
    padding: 3px 21px;
    }

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

    .fullscreen-btn {
        padding: 0.35rem 0.9rem !important;
        border-radius: 10px !important;
        border: 1px solid #d1d5db !important;
        background: #ffffff !important;
        color: #0f172a !important;
        font-weight: 600 !important;
        font-size: 0.78rem !important;
        cursor: pointer;
    }
    .fullscreen-btn:hover {
        background: #f8fafc !important;
        border-color: #cbd5f5 !important;
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
    </style>
    """,
    unsafe_allow_html=True,
)

# --- DATA SOURCES & CONSTANTS ---
DATA_DIR = Path(__file__).resolve().parent
DEFAULT_QUESTION_FILE = DATA_DIR / "bl_bio_bot_unit_4_chap_9_the_tissues_qb.xlsx"
SME_CREDENTIALS_FILE = DATA_DIR / "SME_Data.xlsx"
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
        .login-wrapper {
            max-width: 420px;
            margin: 10vh auto 4vh;
            padding: 2.5rem 2.4rem 2.2rem;
            border-radius: 22px;
            background: #ffffff;
            box-shadow: 0 20px 45px rgba(15, 23, 42, 0.12);
        }
        .login-logo {
            width: 92px;
            height: 92px;
            margin: 0 auto 1.6rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #eef2ff, #e0e7ff);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            letter-spacing: 0.08em;
            color: #3730a3;
            font-size: 1.05rem;
        }
        .login-wrapper h3 {
            text-align: center;
            margin-bottom: 0.35rem;
        }
        .login-wrapper p {
            text-align: center;
            margin-bottom: 1.6rem;
            color: #64748b;
            font-size: 0.93rem;
        }
        .login-wrapper [data-testid="baseButton-primary"] button,
        .login-wrapper [data-testid="baseButton-secondary"] button {
            width: 100%;
            padding: 0.65rem 0;
            font-weight: 600;
            border-radius: 10px;
            background: #4338ca;
            border: none;
        }
        .login-wrapper .stTextInput input {
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.markdown("<div class='login-wrapper'>", unsafe_allow_html=True)
        st.markdown("<div class='login-logo'>LOGO</div>", unsafe_allow_html=True)
        st.markdown("<h3>SME Workspace</h3>", unsafe_allow_html=True)
        st.markdown("<p>Sign in with your SME account to continue.</p>", unsafe_allow_html=True)

        with st.form("sme_login_form", clear_on_submit=False):
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

        st.markdown("</div>", unsafe_allow_html=True)

    st.stop()


require_login()

# --- HEADER BAR WITH SME INFO ---
def format_tamil_date(now: pd.Timestamp) -> str:
    """Generate formatted Tamil/Gregorian date display placeholder."""
    # Placeholder Tamil date; adjust logic if proper calendar conversion is needed.
    tamil_date = "புரட்டாசி 30"
    gregorian = now.strftime("%Y %b %d")
    return f"{tamil_date} / {gregorian}"


def render_fullscreen_toggle():
    """Render a button that lets the user enter/exit browser fullscreen."""
    components.html(
        """
        <div style="display:flex;justify-content:flex-end;align-items:center;height:100%;">
            <button class="fullscreen-btn" onclick="if (!document.fullscreenElement) {document.documentElement.requestFullscreen();} else {document.exitFullscreen();}">
                Full Screen
            </button>
        </div>
        """,
        height=50,
    )


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
        .sme-header-right {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-shrink: 0;
        }
        .sme-header-time {
            font-size: 0.8rem;
            font-weight: 600;
            color: #1f2937;
            white-space: nowrap;
        }
        .sme-header-button-container {
            display: inline-block;
        }
        .sme-header-button-container .stButton {
            display: inline-block;
        }
        .sme-header-button-container .stButton > button {
            border-radius: 8px;
            font-weight: 600;
            padding: 0.4rem 1rem !important;
            font-size: 0.8rem !important;
            background: #ffffff !important;
            color: #111827 !important;
            border: 1px solid #d1d5db !important;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            white-space: nowrap;
            min-height: unset !important;
            height: auto !important;
        }
        .sme-header-button-container .stButton > button:hover {
            background: #f9fafb !important;
            border-color: #9ca3af !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='sme-header-wrapper'><div class='sme-header-content'>", unsafe_allow_html=True)

    cols = st.columns([1.8, 3.2, 1.2, 1.4], gap="small")

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

    with cols[3]:
        render_fullscreen_toggle()

    st.markdown("</div></div>", unsafe_allow_html=True)


render_header()

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
    if st.session_state.get("question_source_type") != "default":
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
row = question_df.iloc[current_index]
row_id = str(row.get(ROW_ID_COL, "") or "")
rows_label = f"({current_index + 1} of {total_rows} rows)"

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
    save_clicked = st.button("Save", key="nav_save")
    st.markdown("</div>", unsafe_allow_html=True)

with cols[5]:
    st.markdown("<div class='nav-save-btn'>", unsafe_allow_html=True)
    logout_clicked = st.button("Logout", key="nav_logout")
    st.markdown("</div>", unsafe_allow_html=True)

if prev_clicked:
    st.session_state["question_index"] = max(0, current_index - 1)
    safe_rerun()

if next_clicked:
    st.session_state["question_index"] = min(total_rows - 1, current_index + 1)
    safe_rerun()

if save_clicked:
    st.session_state["nav_last_save"] = pd.Timestamp.now().isoformat()

if logout_clicked:
    st.session_state.clear()
    safe_rerun()

current_index = st.session_state["question_index"]
row = question_df.iloc[current_index]
row_id = str(row.get(ROW_ID_COL, "") or "")



# --- DATA EXTRACTION FOR CURRENT ROW ---
tamil_question = str(row.get(TAMIL_QUESTION_COL, ""))
tamil_options = parse_tamil_options(row.get(TAMIL_OPTIONS_COL, ""))
tamil_answer = str(row.get(TAMIL_ANSWER_COL, ""))
tamil_explanation = str(row.get(TAMIL_EXPLANATION_COL, row.get("விளக்கம்", "")))
english_question = str(row.get(ENGLISH_QUESTION_COL, ""))
english_options = str(row.get(ENGLISH_OPTIONS_COL, ""))
english_answer = str(row.get(ENGLISH_ANSWER_COL, ""))
english_explanation = str(row.get(ENGLISH_EXPLANATION_COL, ""))

# --- EDITABLE BLOCK (TAMIL) ---
st.markdown('<div class="tight-label">கேள்வி</div>', unsafe_allow_html=True)
st.text_area(
    "",
    value=tamil_question,
    key=f"tamil_question_{current_index}",
    height=52,
    label_visibility="collapsed",
)

st.markdown('<div class="tight-label">விருப்பங்கள்</div>', unsafe_allow_html=True)
opt_cols_row1 = st.columns(2, gap="small")
opt_cols_row2 = st.columns(2, gap="small")
option_keys = ["A", "B", "C", "D"]

for col, opt_value, key_suffix in zip(
    opt_cols_row1 + opt_cols_row2,
    tamil_options,
    option_keys,
):
    with col:
        st.text_area(
            "",
            value=opt_value,
            key=f"tamil_option_{key_suffix}_{current_index}",
            height=40,
            label_visibility="collapsed",
        )

st.markdown('<div class="tight-label">விளக்கம்</div>', unsafe_allow_html=True)
st.text_area(
    "",
    value=tamil_explanation,
    key=f"tamil_explanation_{current_index}",
    height=175,
    label_visibility="collapsed",
)

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

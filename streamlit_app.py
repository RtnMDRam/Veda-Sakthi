from pathlib import Path
from typing import List, Optional

import pandas as pd
import streamlit as st

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
    header, footer { display: none !important; }
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
    .editable-vh45 {
        height: 45vh !important;
        min-height: 45vh !important;
        max-height: 45vh !important;
        overflow-y: auto;
        overflow-x: hidden;
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
        box-sizing: border-box;
        background: none;
    }
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
    </style>
    """,
    unsafe_allow_html=True,
)

# --- DATA SOURCES & CONSTANTS ---
DATA_DIR = Path(__file__).resolve().parent
DEFAULT_QUESTION_FILE = DATA_DIR / "bl_bio_bot_unit_4_chap_9_the_tissues_qb.xlsx"
TAMIL_QUESTION_COL = "கேள்வி"
TAMIL_OPTIONS_COL = "விருப்பங்கள் "
TAMIL_ANSWER_COL = "பதில் "
TAMIL_EXPLANATION_COL = "விளக்கம் "
ENGLISH_QUESTION_COL = "question "
ENGLISH_OPTIONS_COL = "questionOptions"
ENGLISH_ANSWER_COL = "answers "
ENGLISH_EXPLANATION_COL = "explanation"
ROW_ID_COL = "_id"
GLOSSARY_COLUMNS = ["Glossary", "glossary", "Glossary "]


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


def pick_first_available(row: pd.Series, keys: List[str]) -> str:
    """Fetch the first non-empty value for any of the provided column keys."""
    for key in keys:
        value = row.get(key, "")
        if value:
            return str(value)
    return ""


def set_dataset(df: pd.DataFrame, source_name: str) -> None:
    """Store the active dataframe in session state."""
    st.session_state["question_df"] = df
    st.session_state["question_total"] = len(df)
    st.session_state["question_source"] = source_name
    st.session_state["question_index"] = 0


# --- INITIAL DATA LOAD ---
uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    uploaded_df = load_dataframe(uploaded_file)
    if uploaded_df is not None:
        set_dataset(uploaded_df, uploaded_file.name)
else:
    if "question_df" not in st.session_state:
        if DEFAULT_QUESTION_FILE.exists():
            default_df = load_dataframe(DEFAULT_QUESTION_FILE)
            if default_df is not None:
                set_dataset(default_df, DEFAULT_QUESTION_FILE.name)
        else:
            st.info("Default question bank was not found. Please upload an Excel file to continue.")

question_df: Optional[pd.DataFrame] = st.session_state.get("question_df")

if question_df is None:
    st.stop()

total_rows = st.session_state.get("question_total", len(question_df))
current_index = min(st.session_state.get("question_index", 0), total_rows - 1)
st.session_state["question_index"] = current_index  # Clamp in case data size changed.

# --- NAVIGATION CONTROLS ---
col_prev, col_info, col_next = st.columns([1, 2.4, 1])
with col_prev:
    prev_clicked = st.button("Previous", use_container_width=True, disabled=current_index <= 0)
with col_next:
    next_clicked = st.button(
        "Next",
        use_container_width=True,
        disabled=current_index >= total_rows - 1,
    )

if prev_clicked:
    st.session_state["question_index"] = max(0, current_index - 1)
    st.experimental_rerun()

if next_clicked:
    st.session_state["question_index"] = min(total_rows - 1, current_index + 1)
    st.experimental_rerun()

current_index = st.session_state["question_index"]
row = question_df.iloc[current_index]
row_id = str(row.get(ROW_ID_COL, "") or "")

with col_info:
    st.markdown(
        f"<div style='text-align:center;font-weight:600;'>"
        f"({current_index + 1} of {total_rows} rows) - ID {row_id}"
        f"</div>",
        unsafe_allow_html=True,
    )

st.caption(f"Active question bank: {st.session_state.get('question_source', 'Unknown source')}")

# --- DATA EXTRACTION FOR CURRENT ROW ---
tamil_question = str(row.get(TAMIL_QUESTION_COL, ""))
tamil_options = parse_tamil_options(row.get(TAMIL_OPTIONS_COL, ""))
tamil_answer = str(row.get(TAMIL_ANSWER_COL, ""))
tamil_explanation = str(row.get(TAMIL_EXPLANATION_COL, row.get("விளக்கம்", "")))
tamil_glossary = pick_first_available(row, GLOSSARY_COLUMNS)

english_question = str(row.get(ENGLISH_QUESTION_COL, ""))
english_options = str(row.get(ENGLISH_OPTIONS_COL, ""))
english_answer = str(row.get(ENGLISH_ANSWER_COL, ""))
english_explanation = str(row.get(ENGLISH_EXPLANATION_COL, ""))

# --- EDITABLE BLOCK (TAMIL) ---
st.markdown('<div class="editable-vh45">', unsafe_allow_html=True)
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

glossary_col, answer_col = st.columns(2, gap="small")
with glossary_col:
    st.markdown('<div class="tight-label">Glossary</div>', unsafe_allow_html=True)
    st.text_area(
        "",
        value=tamil_glossary,
        key=f"tamil_glossary_{current_index}",
        height=40,
        label_visibility="collapsed",
    )
with answer_col:
    st.markdown('<div class="tight-label">Answer</div>', unsafe_allow_html=True)
    st.text_area(
        "",
        value=tamil_answer,
        key=f"tamil_answer_{current_index}",
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
st.markdown("</div>", unsafe_allow_html=True)

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

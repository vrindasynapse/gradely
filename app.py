
import pickle
import html
from datetime import datetime

import pandas as pd
import streamlit as st

# =========================================================
# GR ADELY — STUDENT PERFORMANCE INTELLIGENCE
# =========================================================

st.set_page_config(
    page_title="Gradely | Academic Intelligence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- DESIGN SYSTEM ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --bg: #0B0D16;
    --panel: #141725;
    --card: #191D30;
    --card2: #20243A;
    --border: #2B3049;
    --lavender: #BDB0FF;
    --purple: #9684F5;
    --white: #F5F3FF;
    --muted: #A5A9C4;
    --green: #83D9B0;
    --gold: #E8CA8A;
}

.stApp {
    background: var(--bg);
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(11,13,22,0.96);
}

[data-testid="stToolbar"] {
    right: 1rem;
}

.block-container {
    max-width: 1200px;
    padding: 2rem 2rem 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

h1, h2, h3, h4, p, label {
    color: var(--white);
}

h1, h2 {
    font-family: 'Playfair Display', serif !important;
}

.stMarkdown, .stCaption {
    color: var(--white);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #101321;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * {
    color: var(--white);
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: var(--muted);
}

/* Branding */
.brand {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 700;
    letter-spacing: -1.5px;
    color: var(--white);
}

.brand-star {
    color: var(--lavender);
}

.brand-sub {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 3px;
    color: var(--lavender);
    margin-top: 2px;
}

.topline {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
}

.pill {
    display: inline-block;
    border: 1px solid #41405F;
    background: #211F37;
    color: var(--lavender);
    border-radius: 30px;
    padding: 7px 12px;
    font-size: 0.75rem;
    font-weight: 600;
}

/* Hero */
.hero {
    margin: 1.7rem 0;
    padding: 2.5rem;
    border-radius: 24px;
    border: 1px solid #373655;
    background: linear-gradient(130deg, #292746 0%, #1C2037 55%, #151928 100%);
}

.eyebrow {
    font-size: 0.7rem;
    letter-spacing: 2.5px;
    font-weight: 700;
    color: var(--lavender);
    margin-bottom: 1rem;
}

.hero h1 {
    font-size: clamp(2.1rem, 5vw, 3.4rem);
    line-height: 1.12;
    margin: 0 0 1rem 0;
}

.hero p {
    max-width: 680px;
    color: #D0D1E5;
    font-size: 0.98rem;
    line-height: 1.8;
    margin: 0;
}

.section-label {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--lavender);
    margin-bottom: 5px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    margin-bottom: 5px;
}

.section-desc {
    color: var(--muted);
    font-size: 0.9rem;
    margin-bottom: 1.3rem;
}

/* Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--panel) !important;
    border: 1px solid var(--border) !important;
    border-radius: 18px !important;
    padding: 1.15rem !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] h3 {
    font-size: 1.1rem !important;
}

div[data-testid="stMetric"] {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.2rem;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: var(--muted) !important;
}

[data-testid="stMetricValue"] {
    color: var(--white) !important;
}

[data-testid="stMetricDelta"] {
    color: var(--green) !important;
}

/* Form labels */
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label,
[data-testid="stSlider"] label,
[data-testid="stSlider"] label p {
    color: var(--white) !important;
}

[data-testid="stSlider"] [data-testid="stThumbValue"] {
    color: var(--lavender) !important;
}

/* Inputs */
.stNumberInput input,
.stTextInput input {
    background: var(--card2) !important;
    color: var(--white) !important;
    border-color: var(--border) !important;
    border-radius: 10px !important;
}

[data-baseweb="select"] > div {
    background: var(--card2) !important;
    border-color: var(--border) !important;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    border-radius: 11px;
    min-height: 2.8rem;
    font-weight: 600;
    border: 1px solid var(--border);
    background: var(--card2);
    color: var(--white) !important;
    transition: 0.2s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    border-color: var(--lavender);
    color: var(--lavender) !important;
}

.stButton > button[kind="primary"] {
    background: var(--lavender) !important;
    border-color: var(--lavender) !important;
    color: #151326 !important;
}

.stButton > button[kind="primary"] p {
    color: #151326 !important;
}

/* Notice */
div[data-testid="stAlert"] {
    background: #191D30 !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
}

div[data-testid="stAlert"] p,
div[data-testid="stAlert"] span {
    color: #E5E2F8 !important;
}

/* Custom result cards */
.result-card {
    background: linear-gradient(145deg, #1B2035, #141725);
    border: 1px solid #343752;
    border-radius: 19px;
    padding: 1.5rem;
    min-height: 175px;
    height: 100%;
}

.result-label {
    color: var(--muted);
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 1.4px;
}

.result-number {
    font-size: 2.8rem;
    line-height: 1.3;
    font-weight: 700;
    color: var(--white);
    margin-top: 0.6rem;
}

.result-number span {
    font-size: 1rem;
    color: var(--muted);
}

.result-category {
    color: var(--lavender);
    font-size: 1.8rem;
    font-weight: 700;
    margin-top: 1rem;
}

.result-note {
    color: var(--muted);
    font-size: 0.86rem;
    line-height: 1.6;
    margin-top: 0.5rem;
}

.track {
    height: 8px;
    border-radius: 20px;
    background: #30334B;
    overflow: hidden;
    margin-top: 1.2rem;
}

.fill {
    height: 100%;
    background: linear-gradient(90deg, #8271E2, #C7BBFF);
    border-radius: 20px;
}

/* Insight bars */
.insight-card {
    padding: 1.1rem 1.2rem;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    margin-bottom: 0.7rem;
}

.insight-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
}

.insight-name {
    color: var(--white);
    font-size: 0.9rem;
    font-weight: 600;
}

.insight-value {
    color: var(--lavender);
    font-size: 0.95rem;
    font-weight: 700;
}

.insight-track {
    height: 6px;
    background: #30334B;
    border-radius: 20px;
    margin-top: 0.8rem;
    overflow: hidden;
}

.insight-fill {
    height: 100%;
    background: var(--purple);
    border-radius: 20px;
}

/* Footer */
.footer {
    border-top: 1px solid var(--border);
    margin-top: 3rem;
    padding-top: 1.5rem;
    text-align: center;
    color: var(--muted);
    font-size: 0.82rem;
    line-height: 1.9;
}

.footer strong {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    color: var(--lavender);
}

hr {
    border-color: var(--border);
}

@media (max-width: 700px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }
    .hero {
        padding: 1.5rem;
    }
    .brand {
        font-size: 2rem;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- LOAD TRAINED MODEL ----------------

@st.cache_resource
def load_model():
    with open("student_model.pkl", "rb") as file:
        return pickle.load(file)

try:
    model = load_model()
except FileNotFoundError:
    st.error("The trained model was not found. Run python train_model.py first.")
    st.stop()
except Exception as error:
    st.error(f"Could not load the model: {error}")
    st.stop()


# ---------------- SESSION STATE ----------------

if "gradely_history" not in st.session_state:
    st.session_state.gradely_history = []

if "gradely_latest" not in st.session_state:
    st.session_state.gradely_latest = None


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown(
        '<div class="brand" style="font-size:2rem;">Gradely '
        '<span class="brand-star">✦</span></div>',
        unsafe_allow_html=True
    )
    st.caption("STUDENT PERFORMANCE INTELLIGENCE")

    st.divider()
    st.markdown("### Your workspace")
    page = st.radio(
        "Navigate",
        ["Performance Predictor", "Prediction History", "About Gradely"],
        label_visibility="collapsed"
    )

    st.divider()
    st.markdown("#### Model overview")
    st.markdown("**Algorithm**")
    st.caption("Linear Regression")
    st.markdown("**Input features**")
    st.caption("4 academic indicators")
    st.markdown("**Output**")
    st.caption("Estimated marks out of 100")

    st.divider()
    st.caption("Every effort, a step forward.")


# ---------------- HEADER ----------------

st.markdown("""
<div class="topline">
    <div>
        <div class="brand">Gradely <span class="brand-star">✦</span></div>
        <div class="brand-sub">STUDENT PERFORMANCE INTELLIGENCE</div>
    </div>
    <div class="pill">ACADEMIC INSIGHTS</div>
</div>

<div class="hero">
    <div class="eyebrow">YOUR LEARNING JOURNEY, REIMAGINED</div>
    <h1>Every effort,<br>a step forward.</h1>
    <p>
        Understand your academic profile, explore your learning habits,
        and discover a model-generated estimate of your performance.
        Every small step is part of a bigger journey.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# PAGE 1 — PERFORMANCE PREDICTOR
# =========================================================

if page == "Performance Predictor":

    st.markdown("""
    <div class="section-label">01 — STUDENT PROFILE</div>
    <div class="section-title">Academic overview</div>
    <div class="section-desc">
    Enter your academic averages and learning habits below.
    </div>
    """, unsafe_allow_html=True)

    with st.form("gradely_prediction_form"):

        left, right = st.columns(2, gap="medium")

        with left:
            with st.container(border=True):
                st.markdown("### 📚 Learning habits")

                study_hours = st.slider(
                    "Daily study hours",
                    min_value=0.0,
                    max_value=8.0,
                    value=3.0,
                    step=0.5,
                    help="Average number of hours you study each day."
                )

                attendance = st.slider(
                    "Attendance percentage",
                    min_value=40,
                    max_value=100,
                    value=80,
                    help="Your overall attendance percentage."
                )

        with right:
            with st.container(border=True):
                st.markdown("### ✍️ Academic record")

                previous_marks = st.slider(
                    "Previous exam marks — average of all subjects",
                    min_value=0,
                    max_value=100,
                    value=65,
                    help=(
                        "Enter the average percentage across all subjects "
                        "in your previous exams."
                    )
                )

                assignment_score = st.slider(
                    "Assignment marks — average of all assignments",
                    min_value=0,
                    max_value=100,
                    value=70,
                    help=(
                        "Enter the average percentage across all assignments "
                        "you have completed."
                    )
                )

        st.write("")
        submitted = st.form_submit_button(
            "✦  Estimate my performance",
            type="primary",
            use_container_width=True
        )

    if submitted:
        student = pd.DataFrame([{
            "study_hours": study_hours,
            "attendance": attendance,
            "previous_marks": previous_marks,
            "assignment_score": assignment_score
        }])

        prediction = float(model.predict(student)[0])
        prediction = max(0.0, min(100.0, prediction))

        if prediction >= 75:
            category = "High"
            message = (
                "Your inputs indicate a stronger estimated score. "
                "Continue practising consistently."
            )
        elif prediction >= 50:
            category = "Moderate"
            message = (
                "A steady routine, revision, and practice may help "
                "support your academic progress."
            )
        else:
            category = "Developing"
            message = (
                "Consider setting manageable study goals and asking "
                "for support in topics you find difficult."
            )

        # Avoid recording duplicate submissions of the same profile
        profile = {
            "study_hours": study_hours,
            "attendance": attendance,
            "previous_marks": previous_marks,
            "assignment_score": assignment_score
        }

        record = {
            "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
            **profile,
            "prediction": round(prediction, 2),
            "category": category
        }

        st.session_state.gradely_latest = record
        st.session_state.gradely_history.append(record)

    result = st.session_state.gradely_latest

    if result is not None:
        st.write("")
        st.markdown("""
        <div class="section-label">02 — PREDICTION RESULTS</div>
        <div class="section-title">Your performance outlook</div>
        <div class="section-desc">
        Review your estimated score and academic profile.
        </div>
        """, unsafe_allow_html=True)

        score_col, category_col = st.columns(2, gap="medium")

        score = result["prediction"]
        safe_category = html.escape(result["category"])

        if score >= 75:
            result_message = "Keep building on your current study habits."
        elif score >= 50:
            result_message = "Consistent revision and practice may help."
        else:
            result_message = "Build a steady routine and seek support when needed."

        with score_col:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">ESTIMATED MARKS</div>
                <div class="result-number">
                    {score:.1f}<span> / 100</span>
                </div>
                <div class="track">
                    <div class="fill" style="width:{score}%;"></div>
                </div>
                <div class="result-note">Model-generated estimate</div>
            </div>
            """, unsafe_allow_html=True)

        with category_col:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">PERFORMANCE CATEGORY</div>
                <div class="result-category">{safe_category}</div>
                <div class="result-note">
                    {html.escape(result_message)}
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.markdown("""
        <div class="section-label">03 — ACADEMIC INSIGHTS</div>
        <div class="section-title">Your learning snapshot</div>
        <div class="section-desc">
        A visual summary of the values you entered.
        </div>
        """, unsafe_allow_html=True)

        # Summary metric cards
        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric("Study hours/day", f"{result['study_hours']:.1f} h")
        with m2:
            st.metric("Attendance", f"{result['attendance']}%")
        with m3:
            st.metric("Exam average", f"{result['previous_marks']}%")
        with m4:
            st.metric("Assignment average", f"{result['assignment_score']}%")

        # Horizontal custom bars
        factors = [
            ("Attendance", result["attendance"]),
            ("Previous exam average", result["previous_marks"]),
            ("Assignment average", result["assignment_score"])
        ]

        for name, value in factors:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-row">
                    <div class="insight-name">{name}</div>
                    <div class="insight-value">{value}%</div>
                </div>
                <div class="insight-track">
                    <div class="insight-fill" style="width:{value}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Study suggestions based on entered profile
        st.markdown("""
        <div class="section-label">04 — NEXT STEPS</div>
        <div class="section-title">Suggestions for your journey</div>
        """, unsafe_allow_html=True)

        suggestions = []

        if result["study_hours"] < 2:
            suggestions.append(
                "Try scheduling a consistent daily study session, "
                "starting with a manageable goal."
            )
        else:
            suggestions.append(
                "Keep your study routine consistent and include short "
                "revision sessions."
            )

        if result["attendance"] < 75:
            suggestions.append(
                "Review your attendance pattern and try to attend "
                "classes more regularly where possible."
            )

        if result["previous_marks"] < 60:
            suggestions.append(
                "Identify difficult subjects and practise questions "
                "from those topics."
            )

        if result["assignment_score"] < 60:
            suggestions.append(
                "Review assignment feedback and break upcoming work "
                "into smaller tasks."
            )

        if not suggestions:
            suggestions.append(
                "Maintain your habits, practise past questions, and "
                "make time for regular revision."
            )

        for index, suggestion in enumerate(suggestions, start=1):
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-row">
                    <div class="insight-value">0{index}</div>
                    <div style="flex:1;color:#E5E3F5;line-height:1.7;">
                        {html.escape(suggestion)}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Downloadable report
        report = pd.DataFrame([{
            "Generated at": result["time"],
            "Study hours per day": result["study_hours"],
            "Attendance (%)": result["attendance"],
            "Previous exam average (%)": result["previous_marks"],
            "Assignment average (%)": result["assignment_score"],
            "Estimated marks": result["prediction"],
            "Performance category": result["category"]
        }])

        st.download_button(
            "↓  Download prediction report (CSV)",
            data=report.to_csv(index=False).encode("utf-8"),
            file_name="gradely_prediction_report.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.caption(
            "Interpretation note: this is an educational model trained "
            "on synthetic data. The estimates and categories are illustrative, "
            "not validated forecasts of real academic performance."
        )


# =========================================================
# PAGE 2 — PREDICTION HISTORY
# =========================================================

elif page == "Prediction History":

    st.markdown("""
    <div class="section-label">YOUR WORKSPACE</div>
    <div class="section-title">Prediction history</div>
    <div class="section-desc">
    Review estimates generated during this browser session.
    </div>
    """, unsafe_allow_html=True)

    history = st.session_state.gradely_history

    if history:
        history_df = pd.DataFrame(history)

        h1, h2, h3 = st.columns(3)

        with h1:
            st.metric("Predictions", len(history_df))

        with h2:
            st.metric(
                "Average estimated marks",
                f"{history_df['prediction'].mean():.1f}"
            )

        with h3:
            st.metric(
                "Latest estimate",
                f"{history_df.iloc[-1]['prediction']:.1f}"
            )

        st.write("")
        st.markdown("### Recent predictions")

        display_df = history_df.rename(columns={
            "time": "Date & time",
            "study_hours": "Study hours",
            "attendance": "Attendance %",
            "previous_marks": "Exam average %",
            "assignment_score": "Assignment average %",
            "prediction": "Estimated marks",
            "category": "Category"
        })

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "↓  Download complete history (CSV)",
            data=history_df.to_csv(index=False).encode("utf-8"),
            file_name="gradely_prediction_history.csv",
            mime="text/csv",
            use_container_width=True
        )

        if len(history_df) >= 2:
            st.markdown("### Estimated score across predictions")

            chart_df = history_df[["prediction"]].copy()
            chart_df.index = range(1, len(chart_df) + 1)
            chart_df.index.name = "Prediction number"
            chart_df = chart_df.rename(
                columns={"prediction": "Estimated marks"}
            )

            st.line_chart(chart_df)

        if st.button("Clear session history"):
            st.session_state.gradely_history = []
            st.session_state.gradely_latest = None
            st.rerun()

    else:
        st.info(
            "No predictions yet. Open Performance Predictor and "
            "generate your first estimate to see it here."
        )


# =========================================================
# PAGE 3 — ABOUT
# =========================================================

elif page == "About Gradely":

    st.markdown("""
    <div class="section-label">PROJECT OVERVIEW</div>
    <div class="section-title">About Gradely</div>
    <div class="section-desc">
    A student performance estimation application built with Python.
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("### The idea")
        st.write(
            "Gradely explores how study habits and academic indicators "
            "can be used by a machine-learning model to estimate a student's "
            "marks. It provides an interactive interface for experimenting "
            "with different input values."
        )

    st.write("")

    a, b = st.columns(2, gap="medium")

    with a:
        with st.container(border=True):
            st.markdown("### ⚙️ Technology stack")
            st.markdown("""
            - **Python** — core programming language
            - **Pandas** — tabular data handling
            - **NumPy** — numerical operations
            - **Scikit-learn** — machine learning
            - **Streamlit** — interactive web interface
            """)

    with b:
        with st.container(border=True):
            st.markdown("### 🧠 Machine-learning workflow")
            st.markdown("""
            1. Generate a sample student dataset
            2. Separate input features and target marks
            3. Split data into training and testing sets
            4. Train a Linear Regression model
            5. Evaluate with MAE and R-squared
            6. Save the model for application use
            """)

    st.write("")

    with st.container(border=True):
        st.markdown("### 📊 Model information")
        st.write(
            "The current model is trained on synthetic sample data created "
            "by train_model.py. Its evaluation scores describe performance "
            "on that generated dataset, not on real student records."
        )
        st.write(
            "**Input features:** study hours, attendance, previous exam "
            "average, assignment average."
        )
        st.write(
            "**Target:** generated final marks on a 0–100 scale."
        )
        st.write(
            "**Algorithm:** Linear Regression."
        )

        st.warning(
            "For real-world use, Gradely would need a representative, "
            "appropriately collected real student dataset, validation, "
            "and fairness and privacy checks."
        )


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    <strong>Gradely ✦</strong><br>
    Every effort, a step forward.<br>
    Made for learning, progress, and possibility.
</div>
""", unsafe_allow_html=True)



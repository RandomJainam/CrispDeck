import streamlit as st
import pandas as pd
import os

from backend.agents.extraction_agent import ExtractionAgent
from backend.agents.concept_agent import ConceptAgent
from backend.agents.generation_agent import GenerationAgent
from backend.agents.validation_agent import ValidationAgent
from backend.agents.coverage_agent import CoverageAgent

from backend.services.apkg_service import create_apkg

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="CrispDeck",
    page_icon="📚",
    layout="wide"
)

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "cards" not in st.session_state:
    st.session_state.cards = None

if "concepts" not in st.session_state:
    st.session_state.concepts = None

if "csv_data" not in st.session_state:
    st.session_state.csv_data = None

if "apkg_path" not in st.session_state:
    st.session_state.apkg_path = None

if "filename" not in st.session_state:
    st.session_state.filename = None

if "coverage_report" not in st.session_state:
    st.session_state.coverage_report = None

# -----------------------------------
# UI
# -----------------------------------

st.title("📚 CrispDeck")

st.subheader(
    "Agentic AI Deck Generator"
)

st.markdown("---")

uploaded_files = st.file_uploader(
    "Upload Files",
    type=["pdf", "pptx", "docx"],
    accept_multiple_files=True
)

# -----------------------------------
# FILE PROCESSING
# -----------------------------------

if uploaded_files:

    if len(uploaded_files) > 5:

        st.error(
            "Maximum 5 files allowed."
        )

        st.stop()

    os.makedirs(
        "backend/uploads",
        exist_ok=True
    )

    saved_files = []

    for uploaded_file in uploaded_files:

        file_path = os.path.join(
            "backend/uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:

            f.write(
                uploaded_file.getbuffer()
            )

        saved_files.append(
            file_path
        )

    st.success(
        f"{len(saved_files)} file(s) uploaded successfully."
    )
    syllabus_file = st.selectbox(
        "Select Syllabus File",
         [file.name for file in uploaded_files]
    )
    if st.button("🚀 Generate Deck"):

        try:

            with st.spinner(
                "Running AI Agents..."
            ):

                extractor = ExtractionAgent()

                syllabus_text = ""

                study_material_text = ""

                # -----------------------
                # EXTRACT FILE CONTENT
                # -----------------------

                for file_path in saved_files:
                    text = extractor.run(
                     file_path
                    )
    
                    filename = os.path.basename(
                        file_path
                        ).lower()
    
                    if filename == syllabus_file.lower():
                        syllabus_text += (
                            text + "\n\n"
                            )
                    else:
                        study_material_text += (
                            text + "\n\n"
                     )
                # -----------------------
                # COVERAGE ANALYSIS
                # -----------------------

                coverage_agent = CoverageAgent()

                coverage_report = coverage_agent.run(
                    syllabus_text,
                    study_material_text
                )

                st.write("syllabus lenghth:", len(syllabus_text))
                st.write("study material lenghth:", len(study_material_text))
                st.write("raw coverage report:", coverage_report)

                st.session_state.coverage_report = (
                    coverage_report
                )

                # -----------------------
                # FLASHCARD GENERATION
                # -----------------------

                concept_agent = ConceptAgent()

                generation_agent = GenerationAgent()

                validation_agent = ValidationAgent()

                concepts = concept_agent.run(
                    study_material_text
                )

                flashcards = generation_agent.run(
                    concepts
                )

                cards = validation_agent.run(
                    flashcards
                )

                # -----------------------
                # SAVE SESSION
                # -----------------------

                st.session_state.cards = cards

                st.session_state.concepts = concepts

                # CSV

                df = pd.DataFrame(cards)

                st.session_state.csv_data = (
                    df.to_csv(index=False)
                )

                # APKG

                apkg_path = create_apkg(
                    cards
                )

                st.session_state.apkg_path = (
                    apkg_path
                )

            st.success(
                f"Generated {len(cards)} Flashcards"
            )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )

# -----------------------------------
# DISPLAY RESULTS
# -----------------------------------

if st.session_state.cards:

    cards = st.session_state.cards

    st.markdown("---")

    # -----------------------
    # COVERAGE REPORT
    # -----------------------

    if st.session_state.coverage_report:

        st.header(
            "📊 Coverage Report"
        )

        for item in st.session_state.coverage_report:

            topic = item.get(
                "topic",
                "Unknown"
            )

            status = item.get(
                "status",
                "Unknown"
            )

            if status.lower() == "covered":

                st.success(
                    f"{topic} - Covered"
                )

            elif status.lower() == "partial":

                st.warning(
                    f"{topic} - Partial"
                )

            else:

                st.error(
                    f"{topic} - Missing"
                )

    # -----------------------
    # FLASHCARDS
    # -----------------------

    st.header(
        "📖 Generated Flashcards"
    )

    for i, card in enumerate(
        cards,
        start=1
    ):

        with st.expander(
            f"Card {i}"
        ):

            st.markdown(
                f"### Q: {card['question']}"
            )

            st.markdown(
                f"**A:** {card['answer']}"
            )

    st.markdown("---")

    # -----------------------
    # EXPORTS
    # -----------------------

    st.header(
        "📦 Export"
    )

    if st.session_state.csv_data:

        st.download_button(
            label="📥 Download CSV",
            data=st.session_state.csv_data,
            file_name="crispdeck_flashcards.csv",
            mime="text/csv"
        )

    if st.session_state.apkg_path:

        with open(
            st.session_state.apkg_path,
            "rb"
        ) as f:

            st.download_button(
                label="📚 Download APKG",
                data=f,
                file_name="crispdeck.apkg",
                mime="application/octet-stream"
            )
import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel
from typing import List, Optional

from langchain_mistralai import ChatMistralAI

# -----------------------------
# Load Environment
# -----------------------------

load_dotenv()

# -----------------------------
# Model
# -----------------------------

model = ChatMistralAI(
    model="mistral-small-2506"
)

# -----------------------------
# Pydantic Model
# -----------------------------

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(
    pydantic_object=Movie
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract movie information from the paragraph.

{format_instructions}
"""
        ),
        (
            "human",
            "{paragraph}"
        )
    ]
)

# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Information Extractor")

st.write(
    "Paste a movie paragraph and extract structured information using AI."
)

paragraph = st.text_area(
    "Movie Paragraph",
    height=220,
    placeholder="Paste your movie paragraph here..."
)

if st.button("🚀 Extract Movie Information", use_container_width=True):

    if paragraph.strip() == "":
        st.warning("Please enter a movie paragraph.")
        st.stop()

    with st.spinner("Extracting information..."):

        final_prompt = prompt.invoke(
            {
                "paragraph": paragraph,
                "format_instructions": parser.get_format_instructions()
            }
        )

        response = model.invoke(final_prompt)

        movie_data = parser.parse(response.content)

    st.success("Extraction Complete!")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🎬 Basic Information")

        st.info(f"**Title:** {movie_data.title}")

        st.info(f"**Release Year:** {movie_data.release_year}")

        st.info(f"**Director:** {movie_data.director}")

        st.info(f"**Rating:** ⭐ {movie_data.rating}")

    with col2:

        st.subheader("🎭 Genre")

        st.write(", ".join(movie_data.genre))

        st.subheader("👥 Cast")

        for actor in movie_data.cast:
            st.write("•", actor)

    st.subheader("📝 Summary")

    st.write(movie_data.summary)
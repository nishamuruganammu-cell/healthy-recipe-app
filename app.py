import streamlit as st
import pandas as pd

st.title("🍎 Healthy Recipe Recommendation App")
st.write("Find healthy recipes based on nutrition and rating!")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("epi_r.csv")
    return df

df = load_data()

st.subheader("🔍 Dataset Preview")
st.dataframe(df.head())

# -----------------------------
# USER FILTERS
# -----------------------------

st.subheader("📌 Filter Recipes")

min_rating = st.slider("Minimum Rating", 0.0, 5.0, 3.5, 0.1)
max_calories = st.slider("Maximum Calories", 50, 2000, 500)
max_fat = st.slider("Maximum Fat (g)", 0, 200, 20)
max_sodium = st.slider("Maximum Sodium (mg)", 0, 3000, 800)

# -----------------------------
# APPLY FILTERS
# -----------------------------

filtered = df[
    (df["rating"] >= min_rating) &
    (df["calories"] <= max_calories) &
    (df["fat"] <= max_fat) &
    (df["sodium"] <= max_sodium)
]

# -----------------------------
# SHOW RESULTS
# -----------------------------

st.subheader("🥗 Recommended Healthy Recipes")
st.write(f"Filters applied: rating ≥ {min_rating}, calories ≤ {max_calories}, fat ≤ {max_fat}, sodium ≤ {max_sodium}")

st.dataframe(
    filtered[["title", "rating", "calories", "protein", "fat", "sodium"]]
    .sort_values("rating", ascending=False)
)

st.write("📊 Total recipes found:", len(filtered))

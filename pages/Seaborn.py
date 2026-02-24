import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as
import time
if st.button("Back to Home"):
    st.switch_page("main.py")

#Animationa
st.set_page_config(page_title="StudyNest", layout="wide")

logo_path = "StudyNest_logo.png"   # apna logo file yaha rakho

st.markdown("""
<style>

/* 🌊 Professional Animated Background */
.stApp {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1e3c72);
    background-size: 300% 300%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* 🖼️ Floating Logo */
.logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 40px;
    animation: float 4s ease-in-out infinite;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-15px);}
    100% {transform: translateY(0px);}
}

/* ✨ Title */
.fade-text {
    text-align: center;
    font-size: 48px;
    color: #ffffff;
    animation: fadeIn 2.5s ease-in;
    margin-top: 20px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #dcdcdc;
    margin-bottom: 40px;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# 🖼️ Logo
st.markdown(f"""
<img src="file:///{logo_path}" class="logo" width="260">
""", unsafe_allow_html=True)

# ✨ Text
st.markdown('<h1 class="fade-text">Welcome to StudyNest</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Learn • Practice • Grow with Interactive Notes</p>', unsafe_allow_html=True)



#banner ...........
st.markdown("""
<style>
.top-banner {
    background: linear-gradient(to right, #6a11cb, #2575fc);
    padding: 10px;
    text-align: center;
    color: white;
    font-size: 22px;
    font-weight: bold;
    border-radius: 5px;
}
</style>

<div class="top-banner">
 📘 Welcome to StudyNest
</div>
""", unsafe_allow_html=True)

#sidebar.........




st.set_page_config(page_title="Seaborn Full Course", layout="wide")

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

st.markdown("<h1 style='text-align:center;color:cyan;'>📊 Seaborn Full Course Dashboard</h1>", unsafe_allow_html=True)

# ---------- SIDEBAR (ANCHOR MENU ONLY) ----------
st.sidebar.markdown("""
## 📋 Topics Menu
- [Introduction](#intro)
- [Table of Contents](#tab)
- [Categorical Plots](#cat)
- [Univariate Plots](#uni)
- [Bivariate Plots](#bi)
- [Multivariate Plots](#multi)
- [Matrix Plots](#matrix)
- [Dashboard](#dashboard)
- [Practice](#practice)
- [About Author](#about)
""", unsafe_allow_html=True)

# ---------- INTRO ----------
st.markdown("<a id='intro'></a>",unsafe_allow_html=True)
st.markdown("<h2 id='intro'>📘 Introduction</h2>", unsafe_allow_html=True)
st.write("""
Seaborn is a Python data visualization library based on Matplotlib.
It provides beautiful statistical graphics and works directly with Pandas DataFrames.
""")
st.markdown("<h4 style='color : pink'>Installation:</h4>",unsafe_allow_html=True)
st.code("pip install seaborn")
st.markdown("<h4 style='color : pink'>Importing libraries</h4>",unsafe_allow_html=True)
st.code("""import seaborn as sns
import matplotlib.pyplot as plt""")
st.markdown("<h4 style='color : pink'>Built-in datasets</h4>",unsafe_allow_html=True)
st.text("""Seaborn has some built-in datasets like :
        tips
        iris
        flights
        titanic
        diamonds etc........""")
st.markdown("<h4 style='color : pink'>Loading datasets</h4>",unsafe_allow_html=True)
st.code("sns.load_dataset()")
st.markdown("<h4 style='color : pink'>Example</h4>",unsafe_allow_html=True)
st.code("""
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
""")
st.markdown("<h4 style='color : pink'>Output</h4>",unsafe_allow_html=True)
df = sns.load_dataset("tips")
st.dataframe(df.head())



# ---------- TABLE OF CONTENTS ----------
st.markdown("<h2 id='tab'>📑 Table of Contents</h2>", unsafe_allow_html=True)

data = [
    # Categorical & Numerical
    ["sns.countplot()", "sns.barplot()", "Pie Chart", "sns.histplot()"],
    ["sns.kdeplot()", "sns.distplot()", "sns.rugplot()", "sns.boxplot()"],
    ["sns.violinplot()", "", "", ""],

    # Bivariate (Numerical vs Numerical)
    ["sns.scatterplot()", "sns.lineplot()", "sns.regplot()", "sns.jointplot()"],
    ["hexbin plot", "", "", ""],

    # Categorical vs Numerical
    ["sns.boxplot()", "sns.violinplot()", "sns.stripplot()", "sns.swarmplot()"],
    ["sns.pointplot()", "sns.barplot(hue)", "", ""],

    # Categorical vs Categorical
    ["sns.countplot(hue)", "Heatmap (cross-tab)", "", ""],

    # Multivariate
    ["hue parameter", "size parameter", "style parameter", "sns.pairplot()"],
    ["sns.FacetGrid()", "sns.relplot()", "sns.catplot()", "sns.displot()"],

    # Statistical Visualization
    ["Mean", "Median", "Confidence Interval", "Error Bars"],
    ["Estimator functions", "Bootstrapping", "Distribution comparison", "Correlation visualization"],

    # Advanced Plots
    ["sns.heatmap()", "sns.clustermap()", "Pairwise relationships", "Time series visualization"],
    ["Multiple subplots", "Log scale plots", "", ""],

    # Customization & Styling
    ["Figure size", "Titles & labels", "Legends", "Axis formatting"],
    ["deep palette", "muted palette", "bright palette", "pastel palette"],
    ["dark palette", "colorblind palette", "Custom palettes", "Markers & line styles"],
    ["whitegrid", "darkgrid", "ticks", ""],

    # Themes & Context
    ["sns.set_style()", "sns.set_context()", "Figure aesthetics", "Font scaling"],

    # Faceting & Subplots
    ["FacetGrid", "Row faceting", "Column faceting", "Sharing axes"],

    # Real Datasets
    ["Iris dataset", "Titanic dataset", "Flights dataset", "Diamonds dataset"],
    ["EDA", "", "", ""],

    # Integration with Matplotlib
    ["Mix seaborn & matplotlib", "Custom annotations", "plt.savefig()", "Export images"]
]

df = pd.DataFrame(data, columns=["Column 1", "Column 2", "Column 3", "Column 4"])

st.dataframe(df, use_container_width=True)

# ---------- CATEGORICAL ----------
st.markdown("<h2 id='cat'>📊 Categorical Plots (Count Plot)</h2>", unsafe_allow_html=True)
st.code("sns.countplot(x='day', data=tips)")
plt.figure(figsize=(5,4))
sns.countplot(x="day", data=tips)
st.pyplot(plt)

# ---------- UNIVARIATE ----------
st.markdown("<h2 id='uni'>📈 Univariate Plots (Histogram)</h2>", unsafe_allow_html=True)
st.code("sns.histplot(tips['total_bill'], kde=True)")
plt.figure(figsize=(5,4))
sns.histplot(tips["total_bill"], kde=True)
st.pyplot(plt)

st.markdown("<h3>KDE Plot</h3>", unsafe_allow_html=True)
st.code("sns.kdeplot(tips['total_bill'], fill=True)")
plt.figure(figsize=(5,4))
sns.kdeplot(tips["total_bill"], fill=True)
st.pyplot(plt)

# ---------- BIVARIATE ----------
st.markdown("<h2 id='bi'>🔹 Bivariate Plots (Scatter Plot)</h2>", unsafe_allow_html=True)
st.code("sns.scatterplot(x='total_bill', y='tip', data=tips)")
plt.figure(figsize=(5,4))
sns.scatterplot(x="total_bill", y="tip", data=tips)
st.pyplot(plt)

st.markdown("<h3>Regression Plot</h3>", unsafe_allow_html=True)
plt.figure(figsize=(5,4))
sns.regplot(x="total_bill", y="tip", data=tips)
st.pyplot(plt)

# ---------- MULTIVARIATE ----------
st.markdown("<h2 id='multi'>📍 Multivariate Plot (Point Plot)</h2>", unsafe_allow_html=True)
st.code("sns.pointplot(x='day', y='total_bill', data=tips)")
plt.figure(figsize=(5,4))
sns.pointplot(x="day", y="total_bill", data=tips)
st.pyplot(plt)

# ---------- MATRIX ----------
st.markdown("<h2 id='matrix'>🔥 Matrix Plot (Heatmap)</h2>", unsafe_allow_html=True)
st.code("sns.heatmap(tips.corr(numeric_only=True), annot=True)")
plt.figure(figsize=(5,4))
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap="coolwarm")
st.pyplot(plt)

st.markdown("<h3>Pair Plot</h3>", unsafe_allow_html=True)
st.pyplot(sns.pairplot(iris))

# ---------- DASHBOARD ----------
st.markdown("<h2 id='dashboard'>📊 Dashboard Section</h2>", unsafe_allow_html=True)
st.write("This section can be used to combine multiple plots into one dashboard.")

# ---------- PRACTICE ----------
st.markdown("<h2 id='practice'>✍ Practice</h2>", unsafe_allow_html=True)
st.write("""
1. Create a histogram of tips  
2. Create a boxplot of total_bill vs day  
3. Create a heatmap of correlations  
""")

# ---------- ABOUT ----------
st.markdown("<h2 id='about'>👨‍💻 About Author</h2>", unsafe_allow_html=True)

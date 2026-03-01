import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
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

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Seaborn Full Course", layout="wide")

# Load datasets
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")

st.markdown("<h1 style='text-align:center;color:cyan;'> Seaborn Full Course</h1>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("""
## 📋 Topics Menu
- [Introduction](#intro)
- [Table of Contents](#toc)

### Categorical
- [Count Plot](#countplot)
- [Bar Plot](#barplot)
- [Box Plot](#boxplot)
- [Violin Plot](#violinplot)
- [Strip Plot](#stripplot)
- [Swarm Plot](#swarmplot)

### Univariate
- [Histogram](#histogram)
- [KDE Plot](#kdeplot)
- [Rug Plot](#rugplot)
- [Dist Plot](#distplot)

### Bivariate
- [Scatter Plot](#scatter)
- [Regression Plot](#regression)
- [Line Plot](#lineplot)
- [Joint Plot](#jointplot)
- [Hexbin Plot](#hexbin)

### Multivariate
- [Point Plot](#pointplot)
- [Pair Plot](#pairplot)

### Advanced
- [Heatmap](#heatmap)
- [Clustermap](#clustermap)
- [Styling & Themes](#style)
- [Faceting](#facet)
- [Datasets](#datasets)
- [Practice](#practice)
- [About](#about)
""", unsafe_allow_html=True)

# ---------------- INTRO ----------------
st.markdown("<h2 id='intro'>📘 Introduction</h2>", unsafe_allow_html=True)
st.write("Seaborn is a Python data visualization library based on Matplotlib. It provides beautiful statistical graphics and works directly with Pandas DataFrames..")
st.subheader("Installation")
st.code("pip install seaborn")
st.subheader("Import Libraries") 
st.code("""import seaborn as sns
         import matplotlib.pyplot as plt""")
st.subheader("Built-in datasets") 
st.text(""" - tips
         - iris
         - flights 
         - titanic 
         - diamonds""")
st.subheader("Load Dataset")
st.code("tips = sns.load_dataset('tips')")
st.subheader("Example")
st.code("""import seaborn as sns
         import matplotlib as plt
         df=sns.load_dataset('tips')
         df.head()""")
tips=sns.load_dataset('tips')
st.dataframe(tips.head())
# ---------------- TOC ----------------
st.markdown("<h2 id='toc'>📑 Table of Contents</h2>", unsafe_allow_html=True)
st.write("Use sidebar or links above to navigate topics.")

# ---------------- COUNT ----------------
st.markdown("<h2 id='countplot'>📊 Count Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.countplot(x="day", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- BAR ----------------
st.markdown("<h2 id='barplot'>📊 Bar Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.barplot(x="day", y="total_bill", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- BOX ----------------
st.markdown("<h2 id='boxplot'>📦 Box Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.boxplot(x="day", y="total_bill", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- VIOLIN ----------------
st.markdown("<h2 id='violinplot'>🎻 Violin Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.violinplot(x="day", y="total_bill", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- STRIP ----------------
st.markdown("<h2 id='stripplot'>📍 Strip Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.stripplot(x="day", y="total_bill", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- SWARM ----------------
st.markdown("<h2 id='swarmplot'>🐝 Swarm Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.swarmplot(x="day", y="total_bill", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- HIST ----------------
st.markdown("<h2 id='histogram'>📈 Histogram</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.histplot(tips["total_bill"], kde=True)
st.pyplot(plt); plt.clf()

# ---------------- KDE ----------------
st.markdown("<h2 id='kdeplot'>📈 KDE Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.kdeplot(tips["total_bill"], fill=True)
st.pyplot(plt); plt.clf()

# ---------------- RUG ----------------
st.markdown("<h2 id='rugplot'>📏 Rug Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.rugplot(tips["total_bill"])
st.pyplot(plt); plt.clf()

# ---------------- DIST ----------------
st.markdown("<h2 id='distplot'>📉 Dist Plot (Deprecated)</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.histplot(tips["total_bill"])
st.pyplot(plt); plt.clf()

# ---------------- SCATTER ----------------
st.markdown("<h2 id='scatter'>🔹 Scatter Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.scatterplot(x="total_bill", y="tip", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- REG ----------------
st.markdown("<h2 id='regression'>📉 Regression Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.regplot(x="total_bill", y="tip", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- LINE ----------------
st.markdown("<h2 id='lineplot'>📈 Line Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.lineplot(x="size", y="total_bill", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- JOINT ----------------
st.markdown("<h2 id='jointplot'>🔗 Joint Plot</h2>", unsafe_allow_html=True)
fig = sns.jointplot(x="total_bill", y="tip", data=tips)
st.pyplot(fig.fig)

# ---------------- HEXBIN ----------------
st.markdown("<h2 id='hexbin'>⬢ Hexbin Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
plt.hexbin(tips["total_bill"], tips["tip"], gridsize=20, cmap="Blues")
st.pyplot(plt); plt.clf()

# ---------------- POINT ----------------
st.markdown("<h2 id='pointplot'>🌐 Point Plot</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.pointplot(x="day", y="total_bill", data=tips)
st.pyplot(plt); plt.clf()

# ---------------- PAIR ----------------
st.markdown("<h2 id='pairplot'>🌸 Pair Plot</h2>", unsafe_allow_html=True)
fig = sns.pairplot(iris)
st.pyplot(fig)

# ---------------- HEATMAP ----------------
st.markdown("<h2 id='heatmap'>🔥 Heatmap</h2>", unsafe_allow_html=True)
plt.figure(figsize=(4,3))
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap="coolwarm")
st.pyplot(plt); plt.clf()

# ---------------- CLUSTER ----------------
st.markdown("<h2 id='clustermap'>🧩 Clustermap</h2>", unsafe_allow_html=True)
cluster = sns.clustermap(tips.corr(numeric_only=True))
st.pyplot(cluster.fig)

# ---------------- STYLE ----------------
st.markdown("<h2 id='style'>🎨 Styling & Themes</h2>", unsafe_allow_html=True)
st.code("""
sns.set_style("whitegrid")
sns.set_context("talk")
sns.color_palette("colorblind")
""")

# ---------------- FACET ----------------
st.markdown("<h2 id='facet'>🧩 Faceting</h2>", unsafe_allow_html=True)
g = sns.FacetGrid(tips, col="sex", row="time")
g.map(sns.histplot, "total_bill")
st.pyplot(g.fig)

# ---------------- DATASETS ----------------
st.markdown("<h2 id='datasets'>📂 Real Datasets</h2>", unsafe_allow_html=True)
st.dataframe(titanic.head())

# ---------------- PRACTICE ----------------
st.markdown("<h2 id='practice'>✍ Practice</h2>", unsafe_allow_html=True)
st.write("Try creating your own plots using tips and titanic datasets.")

# ---------------- ABOUT ----------------
st.markdown("<h2 id='about'>👨‍💻 About</h2>", unsafe_allow_html=True)
st.write("This is a complete Seaborn Learning Dashboard.")
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

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Seaborn ", layout="wide")

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
flights = sns.load_dataset("flights")
diamonds = sns.load_dataset("diamonds")

st.markdown("<h1 style='text-align:center;color:cyan;'> Seaborn </h1>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("""
## 📋 Topics Menu
- [Introduction](#intro)
- [Table of Contents](#toc)

### Plots
- [Count Plot](#countplot)
- [Bar Plot](#barplot)
- [Histogram](#histogram)
- [KDE Plot](#kdeplot)
- [Scatter Plot](#scatter)
- [Regression Plot](#regression)
- [Point Plot](#pointplot)
- [Heatmap](#heatmap)
- [Pair Plot](#pairplot)

### Advanced
- [Styling & Themes](#style)
- [Faceting & Subplots](#facet)
- [Real Datasets](#datasets)

- [Practice](#practice)
- [About](#about)
""", unsafe_allow_html=True)

# ---------------- INTRO ----------------
st.markdown("<h2 id='intro'>📘 Introduction</h2>", unsafe_allow_html=True)
st.write("""
Seaborn is a Python data visualization library based on Matplotlib.
It provides beautiful statistical graphics and works directly with Pandas DataFrames.
""")

st.subheader("Installation")
st.code("pip install seaborn")

st.subheader("Import Libraries")
st.code("""import seaborn as sns
import matplotlib.pyplot as plt""")

st.subheader("Built-in datasets")
st.text("""
        - tips
        - iris
        - flights
        - titanic
        - diamonds""")

st.subheader("Load Dataset")
st.code("tips = sns.load_dataset('tips')")
st.subheader("Example")
st.code("""import seaborn as sns
        import matplotlib.pyplot as plt
        df=sns.load_dataset('tips')
        df.head()""")
st.dataframe(tips.head())

# ---------------- TABLE OF CONTENTS ----------------
st.markdown("<h2 id='toc'>📑 Table of Contents</h2>", unsafe_allow_html=True)
st.markdown("""
### 📊 Categorical Plots
- [Count Plot](#countplot)
- [Bar Plot](#barplot)
- [ Box Plot](#boxplot)
- [violin Plot](#violinplot)
- [strip Plot](#stripplot)
- [swarm Plot](#swarmplot)
- [point Plot](#pointplot)
### 📈 Distribution Plots (Univariate / Bivariate)
- [Histogram](#histogram)
- [KDE Plot](#kdeplot)
- [dist Plot](#distplot)
- [rug Plot](#rugplot)

### 🔹 Relational Plots (Relationship between variables)
- [Scatter Plot](#scatter)
- [Rel Plot](#rel)
- [line Plot](#lineplot)

### 🌐 Multivariate / Joint Plots
- [Pair Plot](#pairplot)
- [joint plot](#jointplot)

### 🔥 Matrix Plots
- [Heatmap](#heatmap)
- [clustermap]](#cluster)

### 🎨 Styling & Themes
- [Styling & Themes](#style)

### 🧩 Faceting & Subplots
- [Faceting](#facet)

### 📂 Real Datasets
- [Datasets](#datasets)
""", unsafe_allow_html=True)
#===================Categorical Plot=================

st.markdown("<h4 style='text-align:center; color:cyan;'>📊 COUNT PLOT IN SEABORN</h4>", unsafe_allow_html=True)

st.text("Used when one variable is categorical.")
# ---------------- COUNT PLOT ----------------


# Page Config
st.set_page_config(page_title="Count Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>COUNT PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Count Plot** is used to show the **number of observations in each categorical variable**.  
It displays the frequency of categories using bars.

Example:
- Number of males and females
- Count of customers per day
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Count plot works only on **categorical data**
- Y-axis shows **count**
- X-axis shows **categories**
- It does NOT work on continuous numerical data directly
""")


# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE ----------------
st.markdown("<h4 style='color:yellow;'> Example (One categorical variable)</h4>", unsafe_allow_html=True)
st.code("""import seaborn as sns
        import matplotlib.pyplot as plt
        df=sns.load_dataset('tips')
        sns.countplot(x="day", data=df, palette="Set2")
        plt.title("Count Plot of Days", color="blue")
        plt.xlabel("Day")
        plt.ylabel("Count")""")
    
if st.button("Run",key="1"):
   fig, ax = plt.subplots(figsize=(6,4))
   sns.countplot(x="day", data=tips, palette="Set2",ax=ax)
   ax.set_title("Count Plot of Days", color="blue")
   ax.set_xlabel("Day")
   ax.set_ylabel("Count")
   st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'>Count Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can add another categorical variable.
Example: Day vs Gender
""")
st.code("""import seaborn as sns
        import matplotlib.pyplot as plt
        df=sns.load_dataset('tips')
        sns.countplot(x="day",hue="sex", data=df, palette="Set1")
        plt.title("Count Plot of Days", color="purple")
        plt.xlabel("Day")
        plt.ylabel("Count")
        plt.show()""")
if st.button("Run",key="2"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.countplot(x="day", hue="sex", data=tips, palette="Set1", ax=ax2)
    ax2.set_title("Count of Days by Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Count Plot with Three Variables (Facet / catplot)</h4>", unsafe_allow_html=True)
st.markdown("""
Count plot works mainly with:
- 1 variable (x)
- 2 variables (x + hue)

For 3 variables, use **catplot()** with col or row.
""")
st.code("""import seaborn as sns
        import matplotlib.pyplot as plt
        df=sns.load_dataset('tips')
        sns.catplot(x="day",hue="sex",col="smoker", data=df,kind="count", palette="Set3")
        plt.title("Count Plot of Days", color="purple")
        plt.xlabel("Day")
        plt.ylabel("Count")
        plt.show()""")
if st.button("Run",key="3"):
   g = sns.catplot(x="day", hue="sex", col="smoker", data=tips, kind="count", palette="Set3")
   st.pyplot(g)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Count Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Continuous numerical data (like salary, age)  
❌ Too many categories (100+ unique values)  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **palette** → change colors  
- **hue** → add second variable  
- **order** → arrange categories  
- **dodge** → side by side bars  
- **orient** → horizontal plot  
- **saturation** → color intensity  
""")

# Example with keywords
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Count Plot Example</h3>", unsafe_allow_html=True)
st.code("""import seaborn as sns
        import matplotlib.pyplot as plt
        df=sns.load_dataset('tips')
        sns.catplot(x="day",hue="sex", data=df, palette="coolwarm",order=["Thur","Fri","Sat","Sun"],saturation=0.8)
        plt.title("Count Plot of Days", color="purple")
        plt.xlabel("Day")
        plt.ylabel("Count")
        plt.show()""")
fig3, ax3 = plt.subplots(figsize=(6,4))
sns.countplot(
    x="day",
    hue="sex",
    data=tips,
    palette="coolwarm",
    order=["Thur","Fri","Sat","Sun"],
    saturation=0.8,
    ax=ax3
)
if st.button("Run",key="4"):
    ax3.set_title("Stylish Count Plot", color="red")
    st.pyplot(fig3)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'>8️⃣ Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Count Plot shows frequency of categories  
✔ Works with categorical variables  
✔ Supports 1 variable (x)  
✔ Supports 2 variables (x + hue)  
✔ 3 variables using catplot  
✔ Can be customized using palette, order, hue, saturation  
""")
# ---------------- BAR PLOT ----------------
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bar Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>BAR PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Bar Plot** is used to show the **average (mean) value of a numerical variable for each category**.

It represents the relationship between:
- One categorical variable (x-axis)
- One numerical variable (y-axis)

Example:
- Average bill amount per day
- Average salary per department
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Bar plot works with **categorical + numerical data**
- X-axis → categorical variable
- Y-axis → numerical variable (mean by default)
- It shows **central tendency (mean)**, not count
- It can also show confidence interval (CI)
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One categorical & one numerical variable)</h4>", unsafe_allow_html=True)
st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.barplot(x="day", y="total_bill", data=df, palette="Set2")
plt.title("Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()""")

if st.button("Run", key="5"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x="day", y="total_bill", data=tips, palette="Set2", ax=ax)
    ax.set_title("Average Total Bill by Day", color="blue")
    ax.set_xlabel("Day")
    ax.set_ylabel("Average Total Bill")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Bar Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare one more categorical variable.

Example: Average bill by Day and Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.barplot(x="day", y="total_bill", hue="sex", data=df, palette="Set1")
plt.title("Average Bill by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()""")

if st.button("Run", key="6"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.barplot(x="day", y="total_bill", hue="sex", data=tips, palette="Set1", ax=ax2)
    ax2.set_title("Average Bill by Day and Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Bar Plot with Three Variables (Facet / catplot)</h4>", unsafe_allow_html=True)
st.markdown("""
Bar plot mainly works with:
- 1 categorical + 1 numerical
- 2 categorical (using hue)

For 3 variables, use **catplot()** with col or row.
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.catplot(x="day", y="total_bill", hue="sex", col="smoker",
            data=df, kind="bar", palette="Set3")
plt.show()""")

if st.button("Run", key="7"):
    g = sns.catplot(x="day", y="total_bill", hue="sex", col="smoker",
                    data=tips, kind="bar", palette="Set3")
    st.pyplot(g)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Bar Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Only categorical data without numerical values  
❌ Continuous numerical data without grouping  
❌ Too many categories (100+ unique values)  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **palette** → change colors  
- **hue** → add second categorical variable  
- **order** → arrange categories  
- **ci** → confidence interval (remove with ci=None)  
- **estimator** → change mean to median or sum  
- **orient** → horizontal bar plot  
- **saturation** → color intensity  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Bar Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.barplot(x="day", y="total_bill", hue="sex",
            data=df,
            palette="coolwarm",
            order=["Thur","Fri","Sat","Sun"],
            ci=None,
            saturation=0.8)
plt.title("Stylish Bar Plot")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()""")

fig3, ax3 = plt.subplots(figsize=(6,4))
sns.barplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    palette="coolwarm",
    order=["Thur","Fri","Sat","Sun"],
    ci=None,
    saturation=0.8,
    ax=ax3
)

if st.button("Run", key="8"):
    ax3.set_title("Stylish Bar Plot", color="red")
    st.pyplot(fig3)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Bar Plot shows **average (mean) of numerical values** for each category  
✔ Works with categorical + numerical variables  
✔ Supports 1 categorical + 1 numerical  
✔ Supports 2 categorical using hue  
✔ 3 variables using catplot  
✔ Can be customized using palette, order, hue, ci, estimator, saturation  
""")
#-------
# -----------BOX PLOT------------------------
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Box Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>BOX PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Box Plot** (also called Box-and-Whisker Plot) is used to show the **distribution of numerical data**
through **quartiles**, **median**, and **outliers**.

It helps us understand:
- Spread of data
- Central value (median)
- Presence of outliers
""")

# ---------------- THEORY / NOTES ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Box plot works with **numerical data**
- Shows **minimum, Q1, median, Q3, maximum**
- Detects **outliers**
- Very useful for comparing distributions
- Can compare data across categories
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE NUMERICAL VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One Numerical Variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.boxplot(y="total_bill", data=df)
plt.title("Box Plot of Total Bill")
plt.ylabel("Total Bill")
plt.show()""")

if st.button("Run", key="9"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(y="total_bill", data=tips, ax=ax)
    ax.set_title("Box Plot of Total Bill", color="blue")
    ax.set_ylabel("Total Bill")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Box Plot with Two Variables (Categorical + Numerical)</h4>", unsafe_allow_html=True)
st.markdown("""
Using one categorical and one numerical variable.

Example: Total bill by Day
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.boxplot(x="day", y="total_bill", data=df, palette="Set2")
plt.title("Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()""")

if st.button("Run", key="10"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.boxplot(x="day", y="total_bill", data=tips, palette="Set2", ax=ax2)
    ax2.set_title("Total Bill by Day", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Box Plot with Two Categorical Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare another categorical variable.

Example: Total bill by Day and Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.boxplot(x="day", y="total_bill", hue="sex", data=df, palette="Set1")
plt.title("Total Bill by Day and Gender")
plt.show()""")

if st.button("Run", key="11"):
    fig3, ax3 = plt.subplots(figsize=(6,4))
    sns.boxplot(x="day", y="total_bill", hue="sex", data=tips, palette="Set1", ax=ax3)
    ax3.set_title("Total Bill by Day and Gender", color="darkgreen")
    st.pyplot(fig3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Box Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Only categorical data  
❌ Very small datasets  
❌ Data without numerical values  
❌ When exact values are required instead of distribution  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **palette** → change colors  
- **hue** → add another categorical variable  
- **orient** → horizontal or vertical box  
- **width** → width of boxes  
- **showfliers** → show/hide outliers  
- **linewidth** → border thickness  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Box Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.boxplot(x="day", y="total_bill", hue="sex",
            data=df,
            palette="coolwarm",
            showfliers=True,
            linewidth=2)
plt.title("Stylish Box Plot")
plt.show()""")

fig4, ax4 = plt.subplots(figsize=(6,4))
sns.boxplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    palette="coolwarm",
    showfliers=True,
    linewidth=2,
    ax=ax4
)

if st.button("Run", key="12"):
    ax4.set_title("Stylish Box Plot", color="red")
    st.pyplot(fig4)
# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Box Plot shows data distribution using quartiles  
✔ Works with numerical data  
✔ Can compare across categories  
✔ Detects outliers easily  
✔ Supports categorical comparison using hue  
✔ Highly customizable using palette, hue, linewidth, showfliers  
""")
#------------------violin plot---------------------
st.set_page_config(page_title="Violin Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>VIOLIN PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Violin Plot** is used to show the **distribution of numerical data** and its **probability density**.

It combines features of:
- Box Plot (median & quartiles)
- KDE Plot (density shape)

Example:
- Distribution of total bill
- Salary distribution by department
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Violin plot works with **numerical data**
- Shows data distribution and density
- Helps compare distributions across categories
- X-axis → categorical variable (optional)
- Y-axis → numerical variable
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One numerical variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.violinplot(y="total_bill", data=df, palette="Set2")
plt.title("Violin Plot of Total Bill")
plt.ylabel("Total Bill")
plt.show()""")

if st.button("Run", key="13"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.violinplot(y="total_bill", data=tips, palette="Set2", ax=ax)
    ax.set_title("Violin Plot of Total Bill", color="blue")
    ax.set_ylabel("Total Bill")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Violin Plot with Two Variables</h4>", unsafe_allow_html=True)
st.markdown("""
Using a categorical variable on X-axis, we can compare distributions.

Example: Total Bill by Day
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.violinplot(x="day", y="total_bill", data=df, palette="Set1")
plt.title("Violin Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()""")

if st.button("Run", key="14"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.violinplot(x="day", y="total_bill", data=tips, palette="Set1", ax=ax2)
    ax2.set_title("Violin Plot of Total Bill by Day", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Violin Plot with Three Variables (Using Hue / catplot)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- X-axis → category
- Y-axis → numerical
- Hue → another category
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.catplot(x="day", y="total_bill", hue="sex",
            col="smoker", data=df,
            kind="violin", palette="Set3")
plt.show()""")

if st.button("Run", key="15"):
    g = sns.catplot(x="day", y="total_bill", hue="sex",
                    col="smoker", data=tips,
                    kind="violin", palette="Set3")
    st.pyplot(g)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Violin Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Only categorical data without numerical values  
❌ Very small dataset  
❌ Text / string data  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **palette** → change colors  
- **hue** → add second categorical variable  
- **order** → arrange categories  
- **orient** → horizontal violin plot  
- **split** → split violin by hue  
- **inner** → show box/points inside violin  
- **linewidth** → border thickness  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Violin Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.violinplot(x="day", y="total_bill", hue="sex",
            data=df,
            palette="coolwarm",
            split=True,
            inner="quartile",
            order=["Thur","Fri","Sat","Sun"])
plt.title("Stylish Violin Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()""")

fig3, ax3 = plt.subplots(figsize=(6,4))
sns.violinplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    palette="coolwarm",
    split=True,
    inner="quartile",
    order=["Thur","Fri","Sat","Sun"],
    ax=ax3
)

if st.button("Run", key="16"):
    ax3.set_title("Stylish Violin Plot", color="red")
    st.pyplot(fig3)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Violin Plot shows data distribution and density  
✔ Works with numerical data  
✔ Supports 1 numerical variable  
✔ Supports 1 categorical + 1 numerical  
✔ Supports 3 variables using hue and catplot  
✔ Can be customized using palette, order, hue, split, inner, linewidth  
""")
#-------------strip plot--------------
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Strip Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>STRIP PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Strip Plot** is used to show **individual data points** of a numerical variable across categories.

It is useful for visualizing:
- Data distribution
- Spread of values
- Overlapping points (with jitter)

Example:
- Total bill values for each day
- Marks of students in different classes
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Strip plot works with **numerical + categorical data**
- Each dot represents one observation
- It is similar to scatter plot but for categorical axis
- Overlapping points can be separated using **jitter**
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One categorical & one numerical variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.stripplot(x="day", y="total_bill", data=df, palette="Set2")
plt.title("Strip Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()""")

if st.button("Run", key="17"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.stripplot(x="day", y="total_bill", data=tips, palette="Set2", ax=ax)
    ax.set_title("Strip Plot of Total Bill by Day", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Strip Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare another categorical variable.

Example: Total Bill by Day and Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.stripplot(x="day", y="total_bill", hue="sex", data=df, palette="Set1", jitter=True)
plt.title("Strip Plot by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()""")

if st.button("Run", key="18"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.stripplot(x="day", y="total_bill", hue="sex", data=tips, palette="Set1", jitter=True, ax=ax2)
    ax2.set_title("Strip Plot by Day and Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Strip Plot with Three Variables (Using catplot)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- X-axis → category
- Y-axis → numerical
- Hue → another category
- Facet by col or row
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.catplot(x="day", y="total_bill", hue="sex",
            col="smoker", data=df,
            kind="strip", palette="Set3", jitter=True)
plt.show()""")

if st.button("Run", key="19"):
    g = sns.catplot(x="day", y="total_bill", hue="sex",
                    col="smoker", data=tips,
                    kind="strip", palette="Set3", jitter=True)
    st.pyplot(g)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Strip Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Very large dataset (too many points overlap)  
❌ Only categorical data without numerical values  
❌ Text / string data  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **palette** → change colors  
- **hue** → add second categorical variable  
- **jitter** → separate overlapping points  
- **dodge** → separate hue categories side by side  
- **size** → size of points  
- **alpha** → transparency  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Strip Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.stripplot(x="day", y="total_bill", hue="sex",
            data=df,
            palette="coolwarm",
            jitter=True,
            dodge=True,
            size=6,
            alpha=0.7)
plt.title("Stylish Strip Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()""")

fig3, ax3 = plt.subplots(figsize=(6,4))
sns.stripplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    palette="coolwarm",
    jitter=True,
    dodge=True,
    size=6,
    alpha=0.7,
    ax=ax3
)

if st.button("Run", key="20"):
    ax3.set_title("Stylish Strip Plot", color="red")
    st.pyplot(fig3)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Strip Plot shows individual data points  
✔ Works with categorical + numerical data  
✔ Supports 1 categorical + 1 numerical  
✔ Supports 2 categorical using hue  
✔ Supports 3 variables using catplot  
✔ Can be customized using palette, hue, jitter, dodge, size, alpha  
""")
#-------------------swarm plot==========

st.set_page_config(page_title="Swarm Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>SWARM PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Swarm Plot** is used to show **individual data points** of a numerical variable across categories
without overlapping points.

It is similar to Strip Plot but points are **adjusted automatically** so they do not overlap.

Example:
- Total bill values for each day
- Marks of students in different classes
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Swarm plot works with **numerical + categorical data**
- Each dot represents one observation
- Points never overlap (unlike strip plot)
- Useful to see exact distribution of values
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One categorical & one numerical variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.swarmplot(x="day", y="total_bill", data=df, palette="Set2")
plt.title("Swarm Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()""")

if st.button("Run", key="21"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.swarmplot(x="day", y="total_bill", data=tips, palette="Set2", ax=ax)
    ax.set_title("Swarm Plot of Total Bill by Day", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Swarm Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare another categorical variable.

Example: Total Bill by Day and Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.swarmplot(x="day", y="total_bill", hue="sex", data=df, palette="Set1")
plt.title("Swarm Plot by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()""")

if st.button("Run", key="22"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips, palette="Set1", ax=ax2)
    ax2.set_title("Swarm Plot by Day and Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Swarm Plot with Three Variables (Using catplot)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- X-axis → category
- Y-axis → numerical
- Hue → another category
- Facet by col or row
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.catplot(x="day", y="total_bill", hue="sex",
            col="smoker", data=df,
            kind="swarm", palette="Set3")
plt.show()""")

if st.button("Run", key="23"):
    g = sns.catplot(x="day", y="total_bill", hue="sex",
                    col="smoker", data=tips,
                    kind="swarm", palette="Set3")
    st.pyplot(g)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Swarm Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Very large dataset (too many points → slow & cluttered)  
❌ Only categorical data without numerical values  
❌ Text / string data  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **palette** → change colors  
- **hue** → add second categorical variable  
- **dodge** → separate hue categories side by side  
- **size** → size of points  
- **alpha** → transparency  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Swarm Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.swarmplot(x="day", y="total_bill", hue="sex",
            data=df,
            palette="coolwarm",
            dodge=True,
            size=6,
            alpha=0.7)
plt.title("Stylish Swarm Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()""")

fig3, ax3 = plt.subplots(figsize=(6,4))
sns.swarmplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    palette="coolwarm",
    dodge=True,
    size=6,
    alpha=0.7,
    ax=ax3
)

if st.button("Run", key="24"):
    ax3.set_title("Stylish Swarm Plot", color="red")
    st.pyplot(fig3)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Swarm Plot shows individual data points clearly  
✔ Works with categorical + numerical data  
✔ Supports 1 categorical + 1 numerical  
✔ Supports 2 categorical using hue  
✔ Supports 3 variables using catplot  
✔ Can be customized using palette, hue, dodge, size, alpha  
""")
#---------------point plot-----------------

st.set_page_config(page_title="Point Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>POINT PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Point Plot** is used to show the **mean (or another estimator)** of a numerical variable 
for different categories using points instead of bars.

It also shows **confidence intervals (CI)** by default.

Example:
- Average bill per day
- Average marks per class
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Point plot works with **categorical + numerical data**
- X-axis → categorical variable
- Y-axis → numerical variable (mean by default)
- Shows trends and comparisons between categories
- CI lines show uncertainty in data
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One categorical & one numerical variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.pointplot(x="day", y="total_bill", data=df, palette="Set2")
plt.title("Point Plot of Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()""")

if st.button("Run", key="25"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.pointplot(x="day", y="total_bill", data=tips, palette="Set2", ax=ax)
    ax.set_title("Point Plot of Average Total Bill by Day", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Point Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare another categorical variable.

Example: Average bill by Day and Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.pointplot(x="day", y="total_bill", hue="sex", data=df, palette="Set1")
plt.title("Point Plot by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()""")

if st.button("Run", key="26"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.pointplot(x="day", y="total_bill", hue="sex", data=tips, palette="Set1", ax=ax2)
    ax2.set_title("Point Plot by Day and Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Point Plot with Three Variables (Using catplot)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- X-axis → category
- Y-axis → numerical
- Hue → another category
- Facet by col or row
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.catplot(x="day", y="total_bill", hue="sex",
            col="smoker", data=df,
            kind="point", palette="Set3")
plt.show()""")

if st.button("Run", key="27"):
    g = sns.catplot(x="day", y="total_bill", hue="sex",
                    col="smoker", data=tips,
                    kind="point", palette="Set3")
    st.pyplot(g)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Point Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Only categorical data without numerical values  
❌ Very small dataset  
❌ Text / string data  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **palette** → change colors  
- **hue** → add second categorical variable  
- **order** → arrange categories  
- **ci** → confidence interval (use ci=None to remove)  
- **estimator** → change mean to median or sum  
- **markers** → change point style  
- **linestyles** → change line style  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Point Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.pointplot(x="day", y="total_bill", hue="sex",
            data=df,
            palette="coolwarm",
            order=["Thur","Fri","Sat","Sun"],
            ci=None,
            markers=["o","s"],
            linestyles=["-","--"])
plt.title("Stylish Point Plot")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()""")

fig3, ax3 = plt.subplots(figsize=(6,4))
sns.pointplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    palette="coolwarm",
    order=["Thur","Fri","Sat","Sun"],
    ci=None,
    markers=["o","s"],
    linestyles=["-","--"],
    ax=ax3
)

if st.button("Run", key="28"):
    ax3.set_title("Stylish Point Plot", color="red")
    st.pyplot(fig3)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Point Plot shows mean (or estimator) values  
✔ Works with categorical + numerical data  
✔ Supports 1 categorical + 1 numerical  
✔ Supports 2 categorical using hue  
✔ Supports 3 variables using catplot  
✔ Can be customized using palette, hue, order, ci, estimator, markers, linestyles  
""")


# ---------------- HISTOGRAM ----------------
st.markdown("<h2 id='histogram'>📈 Histogram</h2>", unsafe_allow_html=True)
st.code("sns.histplot(tips['total_bill'], kde=True)")
plt.figure(figsize=(5,4))
sns.histplot(tips["total_bill"], kde=True)
st.pyplot(plt)
plt.clf()

# ---------------- KDE ----------------
st.markdown("<h2 id='kdeplot'>📈 KDE Plot</h2>", unsafe_allow_html=True)
st.code("sns.kdeplot(tips['total_bill'], fill=True)")
plt.figure(figsize=(5,4))
sns.kdeplot(tips["total_bill"], fill=True)
st.pyplot(plt)
plt.clf()

# ---------------- SCATTER ----------------
st.markdown("<h2 id='scatter'>🔹 Scatter Plot</h2>", unsafe_allow_html=True)
st.code("sns.scatterplot(x='total_bill', y='tip', data=tips)")
plt.figure(figsize=(5,4))
sns.scatterplot(x="total_bill", y="tip", data=tips)
st.pyplot(plt)
plt.clf()

# ---------------- REGRESSION ----------------
st.markdown("<h2 id='regression'>📉 Regression Plot</h2>", unsafe_allow_html=True)
st.code("sns.regplot(x='total_bill', y='tip', data=tips)")
plt.figure(figsize=(5,4))
sns.regplot(x="total_bill", y="tip", data=tips)
st.pyplot(plt)
plt.clf()

# ---------------- POINT PLOT ----------------
st.markdown("<h2 id='pointplot'>🌐 Point Plot</h2>", unsafe_allow_html=True)
st.code("sns.pointplot(x='day', y='total_bill', data=tips)")
plt.figure(figsize=(5,4))
sns.pointplot(x="day", y="total_bill", data=tips)
st.pyplot(plt)
plt.clf()

# ---------------- HEATMAP ----------------
st.markdown("<h2 id='heatmap'>🔥 Heatmap</h2>", unsafe_allow_html=True)
st.code("sns.heatmap(tips.corr(numeric_only=True), annot=True)")
plt.figure(figsize=(5,4))
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap="coolwarm")
st.pyplot(plt)
plt.clf()

# ---------------- PAIRPLOT ----------------
st.markdown("<h2 id='pairplot'>🌸 Pair Plot</h2>", unsafe_allow_html=True)
fig = sns.pairplot(iris)
st.pyplot(fig)

# ---------------- STYLING & THEMES ----------------
st.markdown("<h2 id='style'>🎨 Styling & Themes</h2>", unsafe_allow_html=True)
st.code("""
sns.set_style("whitegrid")
sns.set_context("notebook")
sns.color_palette("deep")
""")
st.write("""
Styles: whitegrid, darkgrid, ticks  
Contexts: notebook, talk, poster  
Palettes: deep, muted, bright, pastel, dark, colorblind
""")

# ---------------- FACETING ----------------
st.markdown("<h2 id='facet'>🧩 Faceting & Subplots</h2>", unsafe_allow_html=True)
st.code("""
sns.FacetGrid(tips, col="sex", row="time").map(sns.histplot, "total_bill")
""")
g = sns.FacetGrid(tips, col="sex", row="time")
g.map(sns.histplot, "total_bill")
st.pyplot(g.fig)

# ---------------- DATASETS ----------------
st.markdown("<h2 id='datasets'>📂 Real Datasets</h2>", unsafe_allow_html=True)
st.write("""
Common datasets used in Seaborn:
- tips
- iris
- titanic
- flights
- diamonds
""")

st.dataframe(titanic.head())

# ---------------- PRACTICE ----------------
st.markdown("<h2 id='practice'>✍ Practice</h2>", unsafe_allow_html=True)
st.write("""
1. Create a histogram of tips  
2. Create a boxplot of total_bill vs day  
3. Create a heatmap of correlations  
4. Try FacetGrid with titanic dataset  
""")

# ---------------- ABOUT ----------------
st.markdown("<h2 id='about'>👨‍💻 About Author</h2>", unsafe_allow_html=True)
st.write("This Seaborn learning dashboard is created for educational purposes.")
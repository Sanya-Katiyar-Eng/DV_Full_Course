import streamlit as st
import seaborn as sns
st.set_page_config(page_title="StudyNest", layout="wide")

# ---------------- BACK BUTTON ----------------
if st.button("⬅ Back to Home"):
    st.switch_page("main.py")

# ---------------- CSS STYLE ----------------
st.markdown("""
<style>

/* 🌑 Professional Dark Background */
.stApp {
    background-color: #0f172a;   /* Deep Navy Professional Color */
}

/* ✨ Title */
.fade-text {
    text-align: center;
    font-size: 48px;
    color: #FFD700;
    animation: fadeIn 2s ease-in;
    margin-top: 40px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #e5e7eb;
    margin-bottom: 40px;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Banner */
.top-banner {
    background: #FFD700;
    padding: 12px;
    text-align: center;
    color: black;
    font-size: 22px;
    font-weight: bold;
    border-radius: 8px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TEXT ----------------
st.markdown('<h1 class="fade-text">Welcome to StudyNest</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Learn • Practice • Grow with Interactive Notes</p>', unsafe_allow_html=True)

# ---------------- BANNER ----------------
st.markdown("""
<div class="top-banner">
✨ 📘 Welcome to StudyNest – Your Smart Learning Hub ✨
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
## 📊 Categorical Plots
- [Count Plot](#countplot)
- [Bar Plot](#barplot)
- [ Box Plot](#boxplot)
- [ Boxen Plot](#boxenplot)
- [violin Plot](#violinplot)
- [strip Plot](#stripplot)
- [swarm Plot](#swarmplot)
- [point Plot](#pointplot)
### 📈 Distribution Plots (Univariate / Bivariate)
- [Histogram](#histogram)
- [KDE Plot](#kdeplot)
- [dist Plot](#distplot)
- [rug Plot](#rugplot)
- [ecdfplot](#ecd)

### Regression & Trend 
- [reg plot](#reg)
- [lm plot](#lmplot)


### 🔹 Relational Plots (Relationship between variables)
- [Scatter Plot](#scatter)
- [line Plot](#lineplot)

### 🌐 Multivariate / Joint Plots
- [Pair Plot](#pairplot)
- [joint plot](#jointplot)

### 🔥 Matrix Plots
- [Heatmap](#heatmap)
- [clustermap](#cluster)
### Time Series / Statistical Estimation
- [line plot](#lineplot)
- [point Plot](#pointplot)   

### 🎨 Styling & Themes
- [Styling & Themes](#style)


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
- [ Boxen Plot](#boxenplot)
- [violin Plot](#violinplot)
- [strip Plot](#stripplot)
- [swarm Plot](#swarmplot)
- [point Plot](#pointplot)
### 📈 Distribution Plots (Univariate / Bivariate)
- [Histogram](#histogram)
- [KDE Plot](#kdeplot)
- [dist Plot](#distplot)
- [rug Plot](#rugplot)
- [ecdfplot](#ecd)

### Regression & Trend 
- [reg plot](#reg)
- [lm plot](#lmplot)


### 🔹 Relational Plots (Relationship between variables)
- [Scatter Plot](#scatter)
- [line Plot](#lineplot)

### 🌐 Multivariate / Joint Plots
- [Pair Plot](#pairplot)
- [joint plot](#jointplot)

### 🔥 Matrix Plots
- [Heatmap](#heatmap)
- [clustermap](#cluster)
### Time Series / Statistical Estimation
- [line plot](#lineplot)
- [point Plot](#pointplot)   

### 🎨 Styling & Themes
- [Styling & Themes](#style)

""", unsafe_allow_html=True)
#===================Categorical Plot=================


st.markdown("<h4 style='text-align:center; color:cyan;'>📊 COUNT PLOT IN SEABORN</h4>", unsafe_allow_html=True)

st.text("Used when one variable is categorical.")
# ---------------- COUNT PLOT ----------------
st.markdown("<h2 id='countplot'>📊 Count Plot</h2>", unsafe_allow_html=True)

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
st.markdown("<h2 id='barplot'>📊 Bar Plot</h2>", unsafe_allow_html=True)


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
st.markdown("<h2 id='boxplot'>📊 Box Plot</h2>", unsafe_allow_html=True)






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
st.markdown("<h2 id='violinplot'>📊 Violin Plot</h2>", unsafe_allow_html=True)
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
st.markdown("<h2 id='stripplot'>📊 Strip Plot</h2>", unsafe_allow_html=True)
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
st.markdown("<h2 id='swarmplot'>📊 Swarm Plot</h2>", unsafe_allow_html=True)
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
st.markdown("<h2 id='pointplot'>📊 Point Plot</h2>", unsafe_allow_html=True)
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
st.markdown("<h2 style='color:yellow;'>Distribution Plot  </h2>", unsafe_allow_html=True)
#----------------Distribution plot================
st.text("""A Distribution Plot shows how data is spread (distributed) over values.
It helps us understand:

Data ka pattern kaisa hai

Values zyada kahan hain

Data symmetric hai ya skewed

Outliers hain ya nahi
        
Common Types of Distribution Plots in Seaborn

Histogram (histplot)

Bars ke through frequency show karta hai

Example: height, marks, salary distribution

KDE Plot (kdeplot)

Smooth curve version of histogram

Probability density show karta hai

Rug Plot (rugplot)

Small ticks show karta hai each data point ke liye

Distplot (old)

Histogram + KDE together (now deprecated)  """)

# ---------------- HISTOGRAM ----------------
st.markdown("<h2 id='histogram'>📈 Histogram</h2>", unsafe_allow_html=True)
st.set_page_config(page_title="Histogram - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>HISTOGRAM</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Histogram** is used to show the **distribution of a numerical variable** by dividing data into bins
and counting how many values fall into each bin.

It helps us understand:
- Data spread  
- Shape of data (normal, skewed, uniform)  
- Frequency of values  

Example:
- Distribution of total bill  
- Distribution of student marks  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Histogram works only with **numerical data**
- X-axis → value ranges (bins)
- Y-axis → frequency (count)
- It does NOT work with categorical data
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One numerical variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.histplot(x="total_bill", data=df, bins=10, kde=False)
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()""")

if st.button("Run", key="29"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(x="total_bill", data=tips, bins=10, kde=False, ax=ax)
    ax.set_title("Histogram of Total Bill", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Histogram with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare distributions of another categorical variable.

Example: Distribution of Total Bill by Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.histplot(x="total_bill", hue="sex", data=df, bins=10, palette="Set1")
plt.title("Histogram of Total Bill by Gender")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()""")

if st.button("Run", key="30"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.histplot(x="total_bill", hue="sex", data=tips, bins=10, palette="Set1", ax=ax2)
    ax2.set_title("Histogram by Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Histogram with Three Variables (Using Facet / displot)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- Numerical variable → x
- Categorical variable → hue
- Another categorical → col or row
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.displot(x="total_bill", hue="sex", col="smoker",
            data=df, bins=10, kind="hist", palette="Set3")
plt.show()""")

if st.button("Run", key="31"):
    g = sns.displot(x="total_bill", hue="sex", col="smoker",
                    data=tips, bins=10, kind="hist", palette="Set3")
    st.pyplot(g)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Histogram Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical data  
❌ Text / string data  
❌ Very small dataset  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **bins** → number of bars  
- **hue** → compare categories  
- **kde** → show density curve  
- **palette** → change colors  
- **stat** → count, probability, density  
- **element** → bars, step, poly  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Histogram Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.histplot(x="total_bill", hue="sex",
            data=df,
            bins=15,
            kde=True,
            palette="coolwarm",
            stat="density",
            element="step")
plt.title("Stylish Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.show()""")

fig3, ax3 = plt.subplots(figsize=(6,4))
sns.histplot(
    x="total_bill",
    hue="sex",
    data=tips,
    bins=15,
    kde=True,
    palette="coolwarm",
    stat="density",
    element="step",
    ax=ax3
)

if st.button("Run", key="32"):
    ax3.set_title("Stylish Histogram", color="red")
    st.pyplot(fig3)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Histogram shows distribution of numerical data  
✔ Works with numerical variables only  
✔ Supports 1 numerical variable  
✔ Supports 2 variables using hue  
✔ Supports 3 variables using displot  
✔ Can be customized using bins, hue, kde, palette, stat, element  
""")

# ---------------- KDE ----------------
st.markdown("<h2 id='kdeplot'>📈 KDE Plot</h2>", unsafe_allow_html=True)
st.markdown("<h2 id='kdeplot'>📈 KDE Plot</h2>", unsafe_allow_html=True)
st.set_page_config(page_title="KDE Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>KDE PLOT (Kernel Density Estimation)</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **KDE Plot** is used to show the **probability density distribution** of a numerical variable
using a smooth curve instead of bars (like histogram).

It helps us understand:
- Shape of data  
- Data spread  
- Peaks and valleys  
- Data distribution (normal or skewed)
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- KDE works only with **numerical data**
- It is a smooth version of histogram
- X-axis → data values
- Y-axis → density (not count)
- KDE is not suitable for very small datasets
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One numerical variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.kdeplot(x="total_bill", data=df, fill=True)
plt.title("KDE Plot of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.show()""")

if st.button("Run", key="33"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.kdeplot(x="total_bill", data=tips, fill=True, ax=ax)
    ax.set_title("KDE Plot of Total Bill", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> KDE Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare density of another categorical variable.

Example: Distribution of Total Bill by Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.kdeplot(x="total_bill", hue="sex", data=df, fill=True, palette="Set1")
plt.title("KDE Plot by Gender")
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.show()""")

if st.button("Run", key="34"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.kdeplot(x="total_bill", hue="sex", data=tips, fill=True, palette="Set1", ax=ax2)
    ax2.set_title("KDE Plot by Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> KDE Plot with Three Variables (Facet Plot)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- Numerical → x
- Categorical → hue
- Another categorical → col or row
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.displot(x="total_bill", hue="sex", col="smoker",
            data=df, kind="kde", fill=True, palette="Set3")
plt.show()""")

if st.button("Run", key="35"):
    g = sns.displot(x="total_bill", hue="sex", col="smoker",
                    data=tips, kind="kde", fill=True, palette="Set3")
    st.pyplot(g)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When KDE Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical data  
❌ Very small dataset  
❌ Discrete values with few unique numbers  
❌ Data with many outliers  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **fill** → fill area under curve  
- **hue** → compare categories  
- **bw_adjust** → control smoothness  
- **palette** → change colors  
- **common_norm** → normalize densities  
- **cut** → control curve length  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish KDE Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.kdeplot(x="total_bill", hue="sex",
            data=df,
            fill=True,
            bw_adjust=0.5,
            palette="coolwarm",
            cut=0)
plt.title("Stylish KDE Plot")
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.show()""")

fig3, ax3 = plt.subplots(figsize=(6,4))
sns.kdeplot(
    x="total_bill",
    hue="sex",
    data=tips,
    fill=True,
    bw_adjust=0.5,
    palette="coolwarm",
    cut=0,
    ax=ax3
)

if st.button("Run", key="36"):
    ax3.set_title("Stylish KDE Plot", color="red")
    st.pyplot(fig3)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ KDE Plot shows probability density distribution  
✔ Works only with numerical data  
✔ Smooth curve version of histogram  
✔ Supports 1 variable  
✔ Supports 2 variables using hue  
✔ Supports 3 variables using displot  
✔ Can be customized using fill, bw_adjust, palette, cut  
""")
#=================dist===========================
st.markdown("<h2 id='distplot'>📈 Dist Plot</h2>", unsafe_allow_html=True)

st.set_page_config(page_title="Dist Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>DIST PLOT (Distribution Plot)</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Dist Plot** is used to show the **distribution of a numerical variable**.
It combines:
- Histogram (bars)
- KDE curve (smooth line)

It helps us understand:
- Data spread  
- Shape of data  
- Skewness  
- Normal distribution  
- Outliers  
""")

# ---------------- IMPORTANT NOTE ----------------
st.markdown("<h2 style='color:orange;'> Important Note (Very Valuable)</h2>", unsafe_allow_html=True)
st.markdown("""
⚠️ **distplot() is deprecated in new Seaborn versions**  
Instead of `sns.distplot()` use:
- `sns.histplot()`  
- `sns.kdeplot()`  
- `sns.displot()`  

But concept of Dist Plot = Histogram + KDE (still very important).
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Dist plot works only with **numerical data**
- X-axis → data values  
- Y-axis → frequency / density  
- Shows overall data distribution  
- Best for univariate analysis  
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (BASIC DIST PLOT) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One numerical variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.histplot(df["total_bill"], kde=True)
plt.title("Dist Plot of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Count")
plt.show()""")

if st.button("Run", key="37"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(tips["total_bill"], kde=True, ax=ax)
    ax.set_title("Dist Plot of Total Bill", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Dist Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare distributions of another categorical variable.

Example: Distribution of Total Bill by Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.histplot(x="total_bill", hue="sex", data=df, kde=True, palette="Set1")
plt.title("Dist Plot by Gender")
plt.show()""")

if st.button("Run", key="a"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.histplot(x="total_bill", hue="sex", data=tips, kde=True, palette="Set1", ax=ax2)
    ax2.set_title("Dist Plot by Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Dist Plot with Three Variables (Facet)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- x → numerical  
- hue → categorical  
- col / row → categorical  

Example: Total Bill by Gender and Smoker
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.displot(x="total_bill", hue="sex", col="smoker",
            data=df, kde=True)
plt.show()""")

if st.button("Run", key="38"):
    g3 = sns.displot(x="total_bill", hue="sex", col="smoker", data=tips, kde=True)
    st.pyplot(g3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Dist Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical data  
❌ Very small dataset  
❌ Discrete values with few unique numbers  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (Very Valuable)</h3>", unsafe_allow_html=True)

st.markdown("""
- **bins** → number of bars  
- **kde** → show smooth curve  
- **stat** → count or density  
- **hue** → compare categories  
- **palette** → change colors  
- **element** → bars / step / poly  
- **alpha** → transparency  
- **common_norm** → normalize multiple plots  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Dist Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.histplot(x="total_bill", hue="sex",
             data=df,
             bins=20,
             kde=True,
             stat="density",
             palette="coolwarm",
             alpha=0.7)
plt.title("Stylish Dist Plot")
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.show()""")

fig4, ax4 = plt.subplots(figsize=(6,4))
sns.histplot(
    x="total_bill",
    hue="sex",
    data=tips,
    bins=20,
    kde=True,
    stat="density",
    palette="coolwarm",
    alpha=0.7,
    ax=ax4
)

if st.button("Run", key="39"):
    ax4.set_title("Stylish Dist Plot", color="red")
    st.pyplot(fig4)

# ---------------- EXTRA VALUABLE CONCEPT ----------------
st.markdown("<h2 style='color:orange;'> Extra Valuable Concept</h2>", unsafe_allow_html=True)
st.markdown("""
📌 Dist Plot = Histogram + KDE  

Histogram answers:  
- How many values fall in each range  

KDE answers:  
- Smooth probability distribution  

Used in:
- Data cleaning  
- Checking normality  
- Feature engineering  
- Machine learning preprocessing  
""")

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Dist Plot shows distribution of numerical data  
✔ Combination of histogram + KDE  
✔ Works only with numerical variables  
✔ Supports 1 variable  
✔ Supports 2 variables using hue  
✔ Supports 3 variables using displot  
✔ Very important for data analysis & ML  
✔ Can be customized using bins, kde, stat, palette  
""")
#=================rug=========
st.markdown("<h2 id='rugplot'>📈 Rug Plot</h2>", unsafe_allow_html=True)


st.set_page_config(page_title="Rug Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>RUG PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Rug Plot** is used to display **individual data points** along an axis.
It shows the **distribution of data** using small vertical (or horizontal) lines.

It is mainly used with:
- Histogram  
- KDE Plot  
to show exact data positions.
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Rug plot works only with **numerical data**
- Each small line represents **one data point**
- X-axis → data values  
- Y-axis → usually not meaningful  
- Best used with KDE or Histogram  
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One numerical variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.rugplot(x="total_bill", data=df)
plt.title("Rug Plot of Total Bill")
plt.xlabel("Total Bill")
plt.show()""")

if st.button("Run", key="40"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.rugplot(x="total_bill", data=tips, ax=ax)
    ax.set_title("Rug Plot of Total Bill", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Rug Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare distribution by another categorical variable.

Example: Total Bill by Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.rugplot(x="total_bill", hue="sex", data=df, palette="Set1")
plt.title("Rug Plot by Gender")
plt.xlabel("Total Bill")
plt.show()""")

if st.button("Run", key="41"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.rugplot(x="total_bill", hue="sex", data=tips, palette="Set1", ax=ax2)
    ax2.set_title("Rug Plot by Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Rug Plot with Three Variables (Facet Plot)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- Numerical → x  
- Categorical → hue  
- Another categorical → col or row  
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.displot(x="total_bill", hue="sex", col="smoker",
            data=df, kind="rug", palette="Set3")
plt.show()""")

if st.button("Run", key="42"):
    g = sns.displot(x="total_bill", hue="sex", col="smoker",
                    data=tips, kind="hist", palette="Set3")
    st.pyplot(g)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Rug Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical data  
❌ Very large dataset (overlapping lines)  
❌ Hard to read alone without KDE/Histogram  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **height** → size of rug lines  
- **hue** → add second variable  
- **palette** → change colors  
- **alpha** → transparency  
- **expand_margins** → spacing  
- **clip_on** → control drawing area  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Rug Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.rugplot(x="total_bill", hue="sex",
            data=df,
            height=0.1,
            alpha=0.6,
            palette="coolwarm")
plt.title("Stylish Rug Plot")
plt.xlabel("Total Bill")
plt.show()""")

fig3, ax3 = plt.subplots(figsize=(6,4))
sns.rugplot(
    x="total_bill",
    hue="sex",
    data=tips,
    height=0.1,
    alpha=0.6,
    palette="coolwarm",
    ax=ax3
)

if st.button("Run", key="43"):
    ax3.set_title("Stylish Rug Plot", color="red")
    st.pyplot(fig3)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Rug Plot shows individual data points  
✔ Works only with numerical data  
✔ Best used with KDE or Histogram  
✔ Supports 1 variable  
✔ Supports 2 variables using hue  
✔ Supports 3 variables using displot  
✔ Can be customized using height, alpha, palette  
""")
#=======================ecdf============
st.markdown("<h2 id='ecd'>📈 ECDF Plot</h2>", unsafe_allow_html=True)

st.set_page_config(page_title="ECDF Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>ECDF PLOT (Empirical Cumulative Distribution Function)</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
An **ECDF Plot** shows the **cumulative distribution of data**.
It tells us the proportion (percentage) of data points that are **less than or equal to a value**.

It helps us understand:
- Data spread  
- Percentiles  
- Probability  
- Comparison between groups  
""")

# ---------------- IMPORTANT NOTE ----------------
st.markdown("<h2 style='color:orange;'> Important Note (Very Valuable)</h2>", unsafe_allow_html=True)
st.markdown("""
⚠️ ECDF is an alternative to Histogram & KDE.
It is more precise because:
- No binning problem  
- Shows exact cumulative probability  
- Very useful in statistics & ML  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- ECDF works only with **numerical data**
- X-axis → data values  
- Y-axis → cumulative probability (0 to 1)  
- Best for univariate and bivariate analysis  
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (One numerical variable)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.ecdfplot(x="total_bill", data=df)
plt.title("ECDF Plot of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Proportion")
plt.show()""")

if st.button("Run", key="44"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.ecdfplot(x="total_bill", data=tips, ax=ax)
    ax.set_title("ECDF Plot of Total Bill", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> ECDF Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare cumulative distributions.

Example: Total Bill by Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.ecdfplot(x="total_bill", hue="sex", data=df, palette="Set1")
plt.title("ECDF Plot by Gender")
plt.show()""")

if st.button("Run", key="b"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.ecdfplot(x="total_bill", hue="sex", data=tips, palette="Set1", ax=ax2)
    ax2.set_title("ECDF Plot by Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> ECDF Plot with Three Variables (Facet)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- x → numerical  
- hue → categorical  
- col / row → categorical  

Example: Total Bill by Gender and Smoker
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.displot(x="total_bill", hue="sex", col="smoker",
            data=df, kind="ecdf")
plt.show()""")

if st.button("Run", key="45"):
    g3 = sns.displot(x="total_bill", hue="sex", col="smoker",
                     data=tips, kind="ecdf")
    st.pyplot(g3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When ECDF Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical data  
❌ Very small dataset  
❌ Discrete values with very few unique points  
❌ Time series data directly  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (Very Valuable)</h3>", unsafe_allow_html=True)

st.markdown("""
- **hue** → compare categories  
- **stat** → proportion or count  
- **complementary** → show 1-ECDF  
- **palette** → change colors  
- **linewidth** → line thickness  
- **alpha** → transparency  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish ECDF Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.ecdfplot(x="total_bill", hue="sex",
             data=df,
             stat="proportion",
             palette="coolwarm",
             linewidth=2)
plt.title("Stylish ECDF Plot")
plt.xlabel("Total Bill")
plt.ylabel("Proportion")
plt.show()""")

fig4, ax4 = plt.subplots(figsize=(6,4))
sns.ecdfplot(
    x="total_bill",
    hue="sex",
    data=tips,
    stat="proportion",
    palette="coolwarm",
    linewidth=2,
    ax=ax4
)

if st.button("Run", key="46"):
    ax4.set_title("Stylish ECDF Plot", color="red")
    st.pyplot(fig4)

# ---------------- EXTRA VALUABLE CONCEPT ----------------
st.markdown("<h2 style='color:orange;'> Extra Valuable Concept</h2>", unsafe_allow_html=True)
st.markdown("""
📌 ECDF answers questions like:
- What % of data is less than X?
- What is the median value?
- What is the 90th percentile?

Used in:
- Statistics  
- Data analysis  
- Machine learning  
- Comparing distributions  

Better than histogram when:
- You want exact cumulative probability  
- You want to avoid bin size confusion  
""")

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ ECDF Plot shows cumulative distribution  
✔ Works only with numerical data  
✔ No binning problem like histogram  
✔ Supports 1 variable  
✔ Supports 2 variables using hue  
✔ Supports 3 variables using displot  
✔ Very important for statistics & ML  
✔ Can be customized using stat, palette, linewidth  
""")





#===================reg plot

st.title("📈 Regression & Trend")

# ---------------- Definition ----------------
st.subheader("📌 Definition")
st.markdown("""
**Trend:**  
Trend shows the overall direction of data (increase, decrease, or constant).

**Regression:**  
Regression is a statistical method that shows the relationship between two variables and draws a best-fit line to predict future values.
""")

# ---------------- Key Points ----------------
st.subheader("📝 Key Points")
st.markdown("""
- Trend shows the pattern of data over time.
- Regression explains the relationship between variables.
- Trend can be positive, negative, or no trend.
- Regression uses a line or curve to represent data.
- Used for prediction and analysis.
""")

#reg plot


st.set_page_config(page_title="Regression Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>REGRESSION PLOT (REGPLOT)</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Regression Plot (regplot)** is used to show the **relationship between two numerical variables**
along with a **best-fit regression line**.

It helps us understand:
- Trend  
- Correlation  
- Prediction pattern  
- Relationship strength  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Regression plot works only with **numerical data**
- X-axis → independent variable  
- Y-axis → dependent variable  
- Shows scatter points + regression line  
- Best for bivariate analysis  
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (BASIC REGRESSION PLOT) ----------------
st.markdown("<h4 style='color:yellow;'> Example (Two numerical variables)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.regplot(x="total_bill", y="tip", data=df)
plt.title("Regression Plot of Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()""")

if st.button("Run", key="47"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.regplot(x="total_bill", y="tip", data=tips, ax=ax)
    ax.set_title("Regression Plot of Total Bill vs Tip", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES (COMPARISON STYLE) ----------------
st.markdown("<h4 style='color:yellow;'> Regression Plot with Category (Using Hue Concept)</h4>", unsafe_allow_html=True)
st.markdown("""
regplot does not directly support **hue**.
To compare categories, we draw multiple regplots separately.

Example: Total Bill vs Tip by Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.regplot(x="total_bill", y="tip", data=df[df["sex"]=="Male"], label="Male")
sns.regplot(x="total_bill", y="tip", data=df[df["sex"]=="Female"], label="Female")
plt.legend()
plt.show()""")

if st.button("Run", key="48"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.regplot(x="total_bill", y="tip", data=tips[tips["sex"]=="Male"], ax=ax2, label="Male")
    sns.regplot(x="total_bill", y="tip", data=tips[tips["sex"]=="Female"], ax=ax2, label="Female")
    ax2.legend()
    ax2.set_title("Regression Plot by Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Regression Plot with Three Variables (Facet Grid)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- x → numerical  
- y → numerical  
- col or row → categorical  

Example: Total Bill vs Tip by Smoker and Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

g = sns.lmplot(x="total_bill", y="tip", col="smoker", row="sex", data=df)
plt.show()""")

if st.button("Run", key="49"):
    g3 = sns.lmplot(x="total_bill", y="tip", col="smoker", row="sex", data=tips)
    st.pyplot(g3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Regression Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical vs categorical data  
❌ Only one variable  
❌ Non-linear relationship (without polynomial)  
❌ Very small datasets  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **ci** → confidence interval  
- **scatter** → show/hide points  
- **line_kws** → customize regression line  
- **order** → polynomial regression  
- **truncate** → limit line range  
- **color** → line color  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Regression Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.regplot(x="total_bill", y="tip",
            data=df,
            order=2,
            ci=95,
            scatter_kws={"alpha":0.6},
            line_kws={"color":"red"})
plt.title("Stylish Regression Plot")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()""")

fig4, ax4 = plt.subplots(figsize=(6,4))
sns.regplot(
    x="total_bill", y="tip",
    data=tips,
    order=2,
    ci=95,
    scatter_kws={"alpha":0.6},
    line_kws={"color":"red"},
    ax=ax4
)

if st.button("Run", key="50"):
    ax4.set_title("Stylish Regression Plot", color="red")
    st.pyplot(fig4)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Regression Plot shows relationship with best-fit line  
✔ Works only with numerical data  
✔ Best for bivariate analysis  
✔ Supports 2 variables (x & y)  
✔ Supports 3 variables using lmplot / FacetGrid  
✔ Can be customized using ci, order, line_kws  
""")
#lm plot

st.set_page_config(page_title="LM Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>LM PLOT (Linear Model Plot)</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
**LM Plot (Linear Model Plot)** is used to show the **relationship between two numerical variables**
along with a **regression line (best fit line)**.

It helps to understand:
- Trend  
- Correlation  
- Prediction  
- Pattern between variables  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- LM Plot is a combination of:
  - Scatter Plot  
  - Regression Line  
- It is used for **bivariate analysis**
- Supports grouping using **hue**
- Supports faceting using **row** and **col**
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (TWO VARIABLES) ----------------
st.markdown("<h4 style='color:yellow;'> Example (Two numerical variables)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.lmplot(x="total_bill", y="tip", data=df)
plt.title("LM Plot of Total Bill vs Tip")
plt.show()""")

if st.button("Run", key="51"):
    g1 = sns.lmplot(x="total_bill", y="tip", data=tips)
    st.pyplot(g1)

# ---------------- TWO VARIABLES WITH HUE ----------------
st.markdown("<h4 style='color:yellow;'> LM Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare regression lines for different categories.
Example: Tip vs Total Bill by Gender
""")

st.code("""sns.lmplot(x="total_bill", y="tip", hue="sex", data=df)""")

if st.button("Run", key="52"):
    g2 = sns.lmplot(x="total_bill", y="tip", hue="sex", data=tips, palette="Set1")
    st.pyplot(g2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> LM Plot with Three Variables (Facet)</h4>", unsafe_allow_html=True)
st.markdown("""
Three variables:
- x → numerical  
- y → numerical  
- col / row → categorical  

Example: Tip vs Total Bill by Smoker & Gender
""")

st.code("""sns.lmplot(x="total_bill", y="tip",
           hue="sex", col="smoker", data=df)""")

if st.button("Run", key="c"):
    g3 = sns.lmplot(x="total_bill", y="tip",
                    hue="sex", col="smoker",
                    data=tips)
    st.pyplot(g3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When LM Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical data only  
❌ Single variable only  
❌ Very small dataset  
❌ Non-numerical x or y values  
❌ Time series without numeric trend  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (Very Valuable)</h3>", unsafe_allow_html=True)
st.markdown("""
- **hue** → group comparison  
- **col / row** → faceting  
- **markers** → different point shapes  
- **palette** → change colors  
- **ci** → confidence interval  
- **scatter_kws** → control scatter style  
- **line_kws** → control line style  
- **order** → polynomial regression  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish LM Plot Example</h3>", unsafe_allow_html=True)

st.code("""sns.lmplot(x="total_bill", y="tip", hue="sex",
           data=df,
           markers=["o","s"],
           palette="coolwarm",
           ci=95,
           scatter_kws={'alpha':0.6},
           line_kws={'linewidth':2})""")

if st.button("Run", key="54"):
    g4 = sns.lmplot(
        x="total_bill", y="tip",
        hue="sex",
        data=tips,
        markers=["o","s"],
        palette="coolwarm",
        ci=95,
        scatter_kws={'alpha':0.6},
        line_kws={'linewidth':2}
    )
    st.pyplot(g4)

# ---------------- EXTRA VALUABLE CONCEPT ----------------
st.markdown("<h2 style='color:orange;'> Extra Valuable Concept</h2>", unsafe_allow_html=True)
st.markdown("""
📌 LM Plot is useful for:
- Trend analysis  
- Prediction  
- Correlation study  
- Machine Learning (linear regression visualization)  

Difference:
- **regplot()** → single plot  
- **lmplot()** → supports faceting (row & col)  

Polynomial regression:
Use `order=2` or `order=3`
""")

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ LM Plot shows scatter + regression line  
✔ Used for two numerical variables  
✔ Supports hue for grouping  
✔ Supports row & col for multiple plots  
✔ Helps understand trends & correlation  
✔ Customizable with palette, markers, ci  
✔ Very important for data analysis & ML  
""")










#relational plot



st.title("📊 Relational Plot")

# ---------------- Definition ----------------
st.subheader("📌 Definition")
st.markdown("""
**Relational Plot** is used to show the relationship between two or more numerical variables.
It helps us understand how one variable changes with respect to another variable using plots like scatter plot and line plot.
""")

# ---------------- Key Points ----------------
st.subheader("📝 Key Points")
st.markdown("""
- Shows relationship between variables.
- Mostly used for bivariate and multivariate analysis.
- Supports scatter plot and line plot.
- Can use hue, size, and style for more variables.
- Helps in trend and pattern analysis.
""")


# ---------------- SCATTER ----------------
st.markdown("<h2 id='scatter'>🔹 Scatter Plot</h2>", unsafe_allow_html=True)
st.set_page_config(page_title="Scatter Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>SCATTER PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Scatter Plot** is used to show the **relationship between two numerical variables**.
Each point represents one observation in the dataset.

It helps us to understand:
- Correlation  
- Pattern  
- Trend  
- Outliers  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Scatter plot works only with **numerical data**
- X-axis → one numerical variable  
- Y-axis → another numerical variable  
- Each dot = one data record  
- Best for checking relationship between variables  
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (ONE VS ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (Two numerical variables)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Scatter Plot of Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()""")

if st.button("Run", key="55"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(x="total_bill", y="tip", data=tips, ax=ax)
    ax.set_title("Scatter Plot of Total Bill vs Tip", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Scatter Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare another categorical variable.

Example: Total Bill vs Tip by Gender
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df, palette="Set1")
plt.title("Scatter Plot by Gender")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()""")

if st.button("Run", key="56"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips, palette="Set1", ax=ax2)
    ax2.set_title("Scatter Plot by Gender", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Scatter Plot with Three Variables (Hue + Size / Facet)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- x → numerical  
- y → numerical  
- hue or size → categorical  
- col or row → facet  
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.scatterplot(x="total_bill", y="tip",
                hue="sex", size="smoker",
                data=df, palette="Set2")
plt.show()""")

if st.button("Run", key="57"):
    fig3, ax3 = plt.subplots(figsize=(6,4))
    sns.scatterplot(x="total_bill", y="tip",
                    hue="sex", size="smoker",
                    data=tips, palette="Set2", ax=ax3)
    ax3.set_title("Scatter Plot with Three Variables", color="green")
    st.pyplot(fig3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Scatter Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical vs categorical data  
❌ Too many overlapping points (overplotting)  
❌ Very large dataset without transparency  
❌ One variable only (needs at least two)  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **hue** → add categorical variable  
- **size** → change point size  
- **style** → change marker style  
- **palette** → change colors  
- **alpha** → transparency  
- **marker** → change shape  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Scatter Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.scatterplot(x="total_bill", y="tip",
                hue="sex",
                style="smoker",
                size="size",
                palette="coolwarm",
                alpha=0.7)
plt.title("Stylish Scatter Plot")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()""")

fig4, ax4 = plt.subplots(figsize=(6,4))
sns.scatterplot(
    x="total_bill", y="tip",
    hue="sex",
    style="smoker",
    size="size",
    palette="coolwarm",
    alpha=0.7,
    data=tips,
    ax=ax4
)

if st.button("Run", key="58"):
    ax4.set_title("Stylish Scatter Plot", color="red")
    st.pyplot(fig4)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Scatter Plot shows relationship between two numerical variables  
✔ Works only with numerical data  
✔ Supports 2 variables (x & y)  
✔ Supports 3 variables using hue, size, style  
✔ Helps find correlation and outliers  
✔ Can be customized using palette, alpha, marker, size  
""")


#==================line plot-------------------
st.markdown("<h2 id='lineplot'>🔹 Line Plot</h2>", unsafe_allow_html=True)

st.set_page_config(page_title="Line Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>LINE PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Line Plot** is used to show the **trend or change of data over time or sequence**.
It connects data points with a line.

It helps to understand:
- Trend  
- Pattern  
- Increase or decrease  
- Comparison between groups  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Line plot works with **numerical data**
- X-axis → time or sequence  
- Y-axis → numerical values  
- Best for time series data  
- Shows continuous trend  
""")

# Load dataset
fmri = sns.load_dataset("fmri")

# ---------------- EXAMPLE (ONE VARIABLE) ----------------
st.markdown("<h4 style='color:yellow;'> Example (Basic Line Plot)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('fmri')
sns.lineplot(x="timepoint", y="signal", data=df)
plt.title("Line Plot of Signal over Time")
plt.xlabel("Timepoint")
plt.ylabel("Signal")
plt.show()""")

if st.button("Run", key="59"):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.lineplot(x="timepoint", y="signal", data=fmri, ax=ax)
    ax.set_title("Line Plot of Signal over Time", color="blue")
    st.pyplot(fig)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Line Plot with Two Variables (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can compare trends of another categorical variable.

Example: Time vs Signal by Event
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('fmri')
sns.lineplot(x="timepoint", y="signal", hue="event", data=df, palette="Set1")
plt.title("Line Plot by Event")
plt.xlabel("Timepoint")
plt.ylabel("Signal")
plt.show()""")

if st.button("Run", key="60"):
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.lineplot(x="timepoint", y="signal", hue="event", data=fmri, palette="Set1", ax=ax2)
    ax2.set_title("Line Plot by Event", color="purple")
    st.pyplot(fig2)

# ---------------- THREE VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Line Plot with Three Variables (Hue + Style / Facet)</h4>", unsafe_allow_html=True)
st.markdown("""
For three variables:
- x → numerical / time  
- y → numerical  
- hue → categorical  
- style or col → another categorical  
""")

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('fmri')
sns.lineplot(x="timepoint", y="signal",
             hue="event", style="region",
             data=df, palette="Set2")
plt.show()""")

if st.button("Run", key="61"):
    fig3, ax3 = plt.subplots(figsize=(6,4))
    sns.lineplot(x="timepoint", y="signal",
                 hue="event", style="region",
                 data=fmri, palette="Set2", ax=ax3)
    ax3.set_title("Line Plot with Three Variables", color="green")
    st.pyplot(fig3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Line Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical vs categorical data  
❌ Very noisy data without smoothing  
❌ One variable only (needs x and y)  
❌ Discrete unrelated data  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (To Make Plot Interesting)</h3>", unsafe_allow_html=True)

st.markdown("""
- **hue** → add category  
- **style** → line style  
- **size** → line thickness  
- **palette** → change colors  
- **markers** → show points  
- **dashes** → dashed lines  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Line Plot Example</h3>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('fmri')
sns.lineplot(x="timepoint", y="signal",
             hue="event",
             style="region",
             markers=True,
             dashes=False,
             palette="coolwarm")
plt.title("Stylish Line Plot")
plt.xlabel("Timepoint")
plt.ylabel("Signal")
plt.show()""")

fig4, ax4 = plt.subplots(figsize=(6,4))
sns.lineplot(
    x="timepoint", y="signal",
    hue="event",
    style="region",
    markers=True,
    dashes=False,
    palette="coolwarm",
    data=fmri,
    ax=ax4
)

if st.button("Run", key="62"):
    ax4.set_title("Stylish Line Plot", color="red")
    st.pyplot(fig4)

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Line Plot shows trend over time  
✔ Works with numerical data  
✔ Best for time series  
✔ Supports 2 variables (x & y)  
✔ Supports 3 variables using hue & style  
✔ Can be customized using palette, markers, dashes  
""")


st.title("📊 Multivariate / Joint Plots")

# ---------------- Definition ----------------
st.subheader("📌 Definition")
st.markdown("""
**Multivariate Plot:**  
Multivariate plots are used to visualize the relationship between more than two variables at the same time.

**Joint Plot:**  
Joint plot is a special type of multivariate plot that shows:
- Relationship between two variables (center plot)
- Distribution of each variable (side histograms or KDE plots)
""")

# ---------------- Key Points ----------------
st.subheader("📝 Key Points")
st.markdown("""
- Multivariate plots handle more than two variables.
- Joint plot combines scatter plot and distribution plot.
- Shows correlation and distribution together.
- Useful for detailed data analysis.
- Supports regression, KDE, and hex plots.
""")
st.markdown("<h2 id='pairplot'>🌐 Pair Plot</h2>", unsafe_allow_html=True)

st.set_page_config(page_title="Pair Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>PAIR PLOT (Pairwise Plot)</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Pair Plot** is used to show the **pairwise relationship between multiple numerical variables**
in a dataset.

It creates:
- Scatter plots between every pair of variables  
- Histogram or KDE on the diagonal  

Pair Plot helps to understand:
- Correlation  
- Distribution  
- Patterns  
- Outliers  
- Relationships between many variables at once  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Pair Plot works mainly on **numerical data**
- Diagonal shows:
  - Histogram (default)  
  - or KDE plot  
- Off-diagonal shows:
  - Scatter plots  
- Used for **multivariate analysis**
- Very useful in:
  - Data Analysis  
  - Machine Learning (EDA)  
""")

# Load dataset
iris = sns.load_dataset("iris")

# ---------------- EXAMPLE ----------------
st.markdown("<h4 style='color:yellow;'> Example (Multiple numerical variables)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('iris')

sns.pairplot(df)
plt.show()""")

if st.button("Run", key="63"):
    g1 = sns.pairplot(iris)
    st.pyplot(g1)

# ---------------- TWO VARIABLES ----------------
st.markdown("<h4 style='color:yellow;'> Pair Plot with Two Variables (Using vars)</h4>", unsafe_allow_html=True)
st.markdown("""
We can select only two variables using **vars** parameter.
""")

st.code("""sns.pairplot(df, vars=["sepal_length","sepal_width"])""")

if st.button("Run", key="64"):
    g2 = sns.pairplot(iris, vars=["sepal_length","sepal_width"])
    st.pyplot(g2)

# ---------------- MULTIPLE VARIABLES WITH HUE ----------------
st.markdown("<h4 style='color:yellow;'> Pair Plot with Category (Using Hue)</h4>", unsafe_allow_html=True)
st.markdown("""
Using **hue**, we can color points by category.
Example: Species of flowers
""")

st.code("""sns.pairplot(df, hue="species")""")

if st.button("Run", key="66"):
    g3 = sns.pairplot(iris, hue="species")
    st.pyplot(g3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Pair Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Very large dataset (slow & cluttered)  
❌ Too many variables (10+ columns)  
❌ Only categorical data  
❌ Time series data  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (Very Valuable)</h3>", unsafe_allow_html=True)
st.markdown("""
- **hue** → group by category  
- **vars** → select specific columns  
- **kind** → scatter or reg  
- **diag_kind** → hist or kde  
- **palette** → change colors  
- **markers** → change point shape  
- **corner=True** → show half matrix  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Pair Plot Example</h3>", unsafe_allow_html=True)

st.code("""sns.pairplot(df,
             hue="species",
             palette="coolwarm",
             diag_kind="kde",
             markers=["o","s","D"],
             corner=True)""")

if st.button("Run", key="65"):
    g4 = sns.pairplot(
        iris,
        hue="species",
        palette="coolwarm",
        diag_kind="kde",
        markers=["o","s","D"],
        corner=True
    )
    st.pyplot(g4)

# ---------------- EXTRA VALUABLE CONCEPT ----------------
st.markdown("<h2 style='color:orange;'> Extra Valuable Concept</h2>", unsafe_allow_html=True)
st.markdown("""
📌 Pair Plot is mainly used in:
- Exploratory Data Analysis (EDA)  
- Feature selection  
- Checking correlation  
- Detecting clusters  
- Finding outliers  

Difference:
- **pairplot()** → simple function  
- **PairGrid()** → advanced customization  

Pair Plot shows:
✔ Linear relationships  
✔ Clusters  
✔ Distribution  
✔ Correlation  
""")

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Pair Plot shows relationship between many variables  
✔ Diagonal shows distribution  
✔ Off-diagonal shows scatter plots  
✔ Supports hue for categories  
✔ Useful for EDA & ML  
✔ Customizable with vars, palette, diag_kind  
✔ Helps detect correlation and outliers  
""")


#joint plot-------------------
st.markdown("<h2 id='jointplot'>🌐 Joint Plot</h2>", unsafe_allow_html=True)
import matplotlib.pyplot as plt

st.set_page_config(page_title="Joint Plot - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>JOINT PLOT</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Joint Plot** is used to show the **relationship between two numerical variables**
along with their **individual distributions**.

It combines:
- Scatter / Hex / KDE / Regression plot (center)
- Histogram or KDE on X-axis (top)
- Histogram or KDE on Y-axis (right)

It helps to understand:
- Relationship  
- Correlation  
- Distribution  
- Outliers  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Joint plot works only with **two numerical variables**
- Center plot shows relationship
- Side plots show distributions
- Used in **bivariate analysis**
- Very useful in Exploratory Data Analysis (EDA)
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE (SCATTER) ----------------
st.markdown("<h4 style='color:yellow;'> Example (Default Scatter Joint Plot)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.jointplot(x="total_bill", y="tip", data=df)
plt.show()""")

if st.button("Run", key="67"):
    g1 = sns.jointplot(x="total_bill", y="tip", data=tips)
    st.pyplot(g1)




# ---------------- REGRESSION JOINT PLOT ----------------
st.markdown("<h4 style='color:yellow;'> Joint Plot using Regression</h4>", unsafe_allow_html=True)

st.code("""sns.jointplot(x="total_bill", y="tip", data=df, kind="reg")""")

if st.button("Run", key="69"):
    g4 = sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
    st.pyplot(g4)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Joint Plot Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Categorical data only  
❌ More than two variables  
❌ Very large dataset (slow)  
❌ Time series data  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (Very Valuable)</h3>", unsafe_allow_html=True)
st.markdown("""
- **kind** → scatter, kde, hex, reg  
- **color** → change color  
- **palette** → color scheme  
- **height** → size of plot  
- **ratio** → size of marginal plots  
- **space** → gap between plots  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Joint Plot Example</h3>", unsafe_allow_html=True)

st.code("""sns.jointplot(x="total_bill", y="tip",
           data=df,
           kind="reg",
           color="purple",
           height=7,
           ratio=3,
           space=0.2)""")

if st.button("Run", key="68"):
    g5 = sns.jointplot(
        x="total_bill", y="tip",
        data=tips,
        kind="reg",
        color="purple",
        height=7,
        ratio=3,
        space=0.2
    )
    st.pyplot(g5)

# ---------------- EXTRA VALUABLE CONCEPT ----------------
st.markdown("<h2 style='color:orange;'> Extra Valuable Concept</h2>", unsafe_allow_html=True)
st.markdown("""
📌 Joint Plot is used to:
- Study correlation  
- Detect outliers  
- See joint distribution  
- Understand data shape  

Difference:
- **jointplot()** → easy and quick  
- **JointGrid()** → advanced customization  

Kinds:
✔ scatter  
✔ kde  
✔ hex  
✔ reg  
""")

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Joint plot shows relationship + distributions  
✔ Works with two numerical variables  
✔ Used in bivariate analysis  
✔ Supports scatter, kde, hex, reg  
✔ Useful for EDA and statistics  
✔ Customizable using kind, color, height  
""")

st.title("📊 Matrix Plot (Pair Plot)")

# ---------------- Definition ----------------
st.subheader("📌 Definition")
st.markdown("""
**Matrix Plot** (also called Pair Plot) is used to visualize relationships between multiple numerical variables at once.
It creates a grid (matrix) of plots where:
- Diagonal plots show distribution of each variable.
- Off-diagonal plots show relationship between two variables.
""")

# ---------------- Key Points ----------------
st.subheader("📝 Key Points")
st.markdown("""
- Used for multivariate data analysis.
- Shows correlation between variables.
- Diagonal shows histogram or KDE plots.
- Off-diagonal shows scatter plots.
- Helpful to detect patterns and outliers.
""")

# Load dataset
data = sns.load_dataset("iris")

# ---------------- Matrix Plot Example ----------------
st.subheader("📍 Example: Matrix (Pair) Plot")

sns.pairplot(data, hue="species")
st.pyplot(plt.gcf())

# ---------------- Short Definition ----------------
st.subheader("✨ Short Definition")
st.markdown("""
Matrix plot displays pairwise relationships and distributions of multiple variables in a grid format.
""")

#==============heatmap===========
st.markdown("<h2 id='heatmap'>🔥 Heatmap</h2>", unsafe_allow_html=True)

st.set_page_config(page_title="Heatmap - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>HEATMAP</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Heatmap** is a graphical representation of data where values are shown as **colors**.

It is mainly used to display:
- Correlation between variables  
- Intensity of values  
- Patterns and relationships  

Darker / brighter colors represent higher or lower values.
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Heatmap works on **numerical matrix data**
- Colors represent magnitude of values  
- Very useful for:
  - Correlation analysis  
  - Feature comparison  
  - Pattern detection  
- Used in **EDA (Exploratory Data Analysis)**
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE ----------------
st.markdown("<h4 style='color:yellow;'> Example (Simple Heatmap)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(5,5)
sns.heatmap(data)
plt.show()""")

if st.button("Run", key="72"):
    data = np.random.rand(5,5)
    fig, ax = plt.subplots(figsize=(5,4))
    sns.heatmap(data, ax=ax)
    ax.set_title("Simple Heatmap", color="blue")
    st.pyplot(fig)

# ---------------- CORRELATION HEATMAP ----------------
st.markdown("<h4 style='color:yellow;'> Correlation Heatmap</h4>", unsafe_allow_html=True)
st.markdown("""
Used to show correlation between numerical variables.
""")

st.code("""corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")""")

if st.button("Run", key="73"):
    corr = tips.corr(numeric_only=True)
    fig2, ax2 = plt.subplots(figsize=(6,5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
    ax2.set_title("Correlation Heatmap", color="purple")
    st.pyplot(fig2)

# ---------------- HEATMAP WITH CATEGORIES ----------------
st.markdown("<h4 style='color:yellow;'> Heatmap with Categorical Pivot Table</h4>", unsafe_allow_html=True)
st.markdown("""
We can create heatmap using pivot table (grouped data).
Example: Day vs Time with average tip.
""")

st.code("""pivot = df.pivot_table(values="tip", index="day", columns="time")
sns.heatmap(pivot, annot=True, cmap="YlGnBu")""")

if st.button("Run", key="74"):
    pivot = tips.pivot_table(values="tip", index="day", columns="time")
    fig3, ax3 = plt.subplots(figsize=(6,4))
    sns.heatmap(pivot, annot=True, cmap="YlGnBu", ax=ax3)
    ax3.set_title("Heatmap using Pivot Table", color="green")
    st.pyplot(fig3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Heatmap Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Only categorical data  
❌ Very large matrix (too crowded)  
❌ Single variable data  
❌ Time series without aggregation  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (Very Valuable)</h3>", unsafe_allow_html=True)
st.markdown("""
- **annot=True** → show values inside cells  
- **cmap** → color map  
- **linewidths** → lines between cells  
- **linecolor** → line color  
- **fmt** → number format  
- **square=True** → square cells  
- **cbar=True** → color bar  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Heatmap Example</h3>", unsafe_allow_html=True)

st.code("""sns.heatmap(corr,
           annot=True,
           cmap="viridis",
           linewidths=1,
           linecolor="white",
           square=True,
           fmt=".2f")""")

if st.button("Run", key="75"):
    corr = tips.corr(numeric_only=True)
    fig4, ax4 = plt.subplots(figsize=(6,5))
    sns.heatmap(
        corr,
        annot=True,
        cmap="viridis",
        linewidths=1,
        linecolor="white",
        square=True,
        fmt=".2f",
        ax=ax4
    )
    ax4.set_title("Stylish Heatmap", color="red")
    st.pyplot(fig4)

# ---------------- EXTRA VALUABLE CONCEPT ----------------
st.markdown("<h2 style='color:orange;'> Extra Valuable Concept</h2>", unsafe_allow_html=True)
st.markdown("""
📌 Heatmap is widely used in:
- Data Science  
- Machine Learning  
- Statistics  
- Business dashboards  

Uses:
✔ Feature correlation  
✔ Identify strong/weak relationships  
✔ Detect patterns  
✔ Compare categories  

Difference:
- **heatmap()** → matrix visualization  
- **clustermap()** → heatmap with clustering  
""")

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Heatmap shows data using colors  
✔ Best for correlation and patterns  
✔ Works with numerical matrix  
✔ Supports annotation and colormap  
✔ Used in EDA and ML  
✔ Customizable with cmap, annot, linewidths  
""")

#clusterheatmap
st.markdown("<h2 id='cluster'>🔥 Clustermap</h2>", unsafe_allow_html=True)
import numpy as np

st.set_page_config(page_title="Cluster Heatmap - Seaborn", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>CLUSTER HEATMAP (CLUSTERMAP)</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
A **Cluster Heatmap (clustermap)** is an advanced heatmap that not only shows data values using colors,
but also groups (clusters) similar rows and columns using **hierarchical clustering**.

It helps to:
- Find similarity patterns  
- Group related variables  
- Visualize correlations  
- Detect clusters in data  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
- Clustermap works on **numerical matrix data**
- It automatically rearranges rows & columns based on similarity  
- Includes **dendrograms (tree structure)**  
- Used in:
  - Data Science  
  - Machine Learning  
  - Bioinformatics  
  - Statistics  
""")

# Load dataset
tips = sns.load_dataset("tips")

# ---------------- EXAMPLE ----------------
st.markdown("<h4 style='color:yellow;'> Example (Simple Cluster Heatmap)</h4>", unsafe_allow_html=True)

st.code("""import seaborn as sns
import numpy as np

data = np.random.rand(6,6)
sns.clustermap(data, cmap="viridis")
plt.show()""")

if st.button("Run", key="76"):
    data = np.random.rand(6,6)
    g1 = sns.clustermap(data, cmap="viridis")
    st.pyplot(g1)

# ---------------- CORRELATION CLUSTER HEATMAP ----------------
st.markdown("<h4 style='color:yellow;'> Correlation Cluster Heatmap</h4>", unsafe_allow_html=True)
st.markdown("""
Used to cluster correlated numerical variables.
""")

st.code("""corr = df.corr()
sns.clustermap(corr, annot=True, cmap="coolwarm")""")

if st.button("Run", key="77"):
    corr = tips.corr(numeric_only=True)
    g2 = sns.clustermap(corr, annot=True, cmap="coolwarm")
    st.pyplot(g2)

# ---------------- PIVOT TABLE CLUSTER HEATMAP ----------------
st.markdown("<h4 style='color:yellow;'> Pivot Table Cluster Heatmap</h4>", unsafe_allow_html=True)
st.markdown("""
Create cluster heatmap from grouped data.
Example: Day vs Time with average tip.
""")

st.code("""pivot = df.pivot_table(values="tip", index="day", columns="time")
sns.clustermap(pivot, annot=True, cmap="YlGnBu")""")

if st.button("Run", key="78"):
    pivot = tips.pivot_table(values="tip", index="day", columns="time")
    g3 = sns.clustermap(pivot, annot=True, cmap="YlGnBu")
    st.pyplot(g3)

# ---------------- WHEN IT DOES NOT WORK ----------------
st.markdown("<h3 style='color:pink;'> When Cluster Heatmap Does NOT Work</h3>", unsafe_allow_html=True)
st.markdown("""
❌ Only categorical data  
❌ Very large matrix (too slow & cluttered)  
❌ Single variable data  
❌ Data with missing values (NaN) without cleaning  
""")

# ---------------- KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords (Very Valuable)</h3>", unsafe_allow_html=True)
st.markdown("""
- **cmap** → color map  
- **annot=True** → show values  
- **standard_scale** → normalize rows/columns  
- **method** → linkage method (ward, single, complete)  
- **metric** → distance metric (euclidean, cosine)  
- **linewidths** → lines between cells  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Cluster Heatmap Example</h3>", unsafe_allow_html=True)

st.code("""sns.clustermap(corr,
           cmap="viridis",
           annot=True,
           linewidths=1,
           standard_scale=1,
           method="ward",
           metric="euclidean")""")

if st.button("Run", key="79"):
    corr = tips.corr(numeric_only=True)
    g4 = sns.clustermap(
        corr,
        cmap="viridis",
        annot=True,
        linewidths=1,
        standard_scale=1,
        method="ward",
        metric="euclidean"
    )
    st.pyplot(g4)

# ---------------- EXTRA VALUABLE CONCEPT ----------------
st.markdown("<h2 style='color:orange;'> Extra Valuable Concept</h2>", unsafe_allow_html=True)
st.markdown("""
📌 Difference between Heatmap & Cluster Heatmap:

Heatmap:
✔ Shows values with colors  
✔ No grouping  

Clustermap:
✔ Shows values with colors  
✔ Groups similar rows & columns  
✔ Shows dendrogram (tree)  

Used in:
- Gene expression analysis  
- Customer segmentation  
- Feature clustering  
""")

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Cluster heatmap groups similar data  
✔ Uses hierarchical clustering  
✔ Best for correlation analysis  
✔ Shows dendrograms  
✔ Works on numerical matrix  
✔ Customizable with cmap, metric, method  
✔ Widely used in Data Science & ML  
""")


#style==============

st.set_page_config(page_title="Seaborn Styles & Themes", layout="wide")

# Title
st.markdown("<h3 style='text-align:center; color:cyan;'>SEABORN STYLES & THEMES</h3>", unsafe_allow_html=True)

# ---------------- DEFINITION ----------------
st.markdown("<h2 style='color:yellow;'> Definition</h2>", unsafe_allow_html=True)
st.markdown("""
**Seaborn Styles & Themes** control the overall **look and feel** of plots such as:
- Background color  
- Grid lines  
- Font size  
- Line thickness  
- Spacing  

They make plots more:
✔ Readable  
✔ Professional  
✔ Attractive  
""")

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:pink;'>Notes :</h2>", unsafe_allow_html=True)
st.markdown("""
Seaborn provides:
1️⃣ **Styles** → background & grid  
2️⃣ **Contexts (Themes)** → scaling for presentation size  
3️⃣ **Color Palettes** → color combinations  

Main functions:
- sns.set_style()  
- sns.set_context()  
- sns.color_palette()  
""")

# Dataset
tips = sns.load_dataset("tips")

# ---------------- ALL STYLES ----------------
st.markdown("<h2 style='color:yellow;'> All Seaborn Styles</h2>", unsafe_allow_html=True)
st.markdown("""
Available styles:
- **darkgrid**  
- **whitegrid**  
- **dark**  
- **white**  
- **ticks**  
""")

styles = ["darkgrid", "whitegrid", "dark", "white", "ticks"]

for i, style in enumerate(styles):
    st.markdown(f"<h4 style='color:lightgreen;'> Style : {style}</h4>", unsafe_allow_html=True)
    if st.button(f"Run {style}", key=f"s{i}"):
        sns.set_style(style)
        fig, ax = plt.subplots(figsize=(5,4))
        sns.histplot(tips["total_bill"], ax=ax, color="purple")
        ax.set_title(f"Style = {style}")
        st.pyplot(fig)

# ---------------- ALL CONTEXT (THEMES) ----------------
st.markdown("<h2 style='color:yellow;'> All Seaborn Contexts (Themes)</h2>", unsafe_allow_html=True)
st.markdown("""
Contexts control font size & scaling:

- **paper** → small plots (reports)  
- **notebook** → default  
- **talk** → presentations  
- **poster** → large displays  
""")

contexts = ["paper", "notebook", "talk", "poster"]

for j, context in enumerate(contexts):
    st.markdown(f"<h4 style='color:lightgreen;'> Context : {context}</h4>", unsafe_allow_html=True)
    if st.button(f"Run {context}", key=f"c{j}"):
        sns.set_context(context)
        sns.set_style("darkgrid")
        fig, ax = plt.subplots(figsize=(5,4))
        sns.scatterplot(x="total_bill", y="tip", data=tips, ax=ax)
        ax.set_title(f"Context = {context}")
        st.pyplot(fig)

# ---------------- WHEN TO USE WHICH STYLE ----------------
st.markdown("<h3 style='color:pink;'> When to use which Style</h3>", unsafe_allow_html=True)
st.markdown("""
✔ darkgrid → data comparison  
✔ whitegrid → clean reports  
✔ dark → presentations  
✔ white → minimal plots  
✔ ticks → scientific plots  

✔ paper → research paper  
✔ notebook → coding  
✔ talk → slides  
✔ poster → dashboards  
""")

# ---------------- IMPORTANT KEYWORDS ----------------
st.markdown("<h3 style='color:yellow;'> Important Keywords</h3>", unsafe_allow_html=True)
st.markdown("""
- **sns.set_style("darkgrid")**  
- **sns.set_context("talk")**  
- **sns.set_palette("coolwarm")**  
- **sns.reset_defaults()**  
- **sns.axes_style()**  
- **sns.plotting_context()**  
""")

# ---------------- STYLISH EXAMPLE ----------------
st.markdown("<h3 style='color:lightgreen;'>✨ Stylish Combined Example</h3>", unsafe_allow_html=True)

st.code("""
sns.set_style("whitegrid")
sns.set_context("talk")
sns.set_palette("coolwarm")

sns.barplot(x="day", y="total_bill", data=df)
plt.title("Stylish Seaborn Plot")
plt.show()
""")

if st.button("Run Stylish Example", key="stylex"):
    sns.set_style("whitegrid")
    sns.set_context("talk")
    sns.set_palette("coolwarm")
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.barplot(x="day", y="total_bill", data=tips, ax=ax2)
    ax2.set_title("Stylish Seaborn Plot")
    st.pyplot(fig2)

# ---------------- EXTRA VALUABLE CONCEPT ----------------
st.markdown("<h2 style='color:orange;'> Extra Valuable Concept</h2>", unsafe_allow_html=True)
st.markdown("""
Difference between:
sns.set_style() → background & grid  
sns.set_context() → font & scale  
sns.set_palette() → colors  

Order of applying:
1️⃣ set_style  
2️⃣ set_context  
3️⃣ set_palette  
""")

# ---------------- SUMMARY ----------------
st.markdown("<h2 style='color:pink;'> Summary</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Seaborn has 5 styles  
✔ Seaborn has 4 contexts (themes)  
✔ Used to control appearance  
✔ Makes plots professional  
✔ Important for dashboards  
✔ Used in reports & presentations  
""")

#dash board

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Canvas Dashboard", layout="wide")

# ---------------- TITLE ----------------
st.markdown("<h2 style='text-align:center; color:cyan;'>📊 RESTAURANT ANALYTICS DASHBOARD</h2>", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
df = sns.load_dataset("tips")

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.markdown("## 🔎 Filters")

day_filter = st.sidebar.multiselect("Select Day", df["day"].unique(), default=df["day"].unique())
sex_filter = st.sidebar.multiselect("Select Gender", df["sex"].unique(), default=df["sex"].unique())
time_filter = st.sidebar.multiselect("Select Time", df["time"].unique(), default=df["time"].unique())

filtered_df = df[
    (df["day"].isin(day_filter)) &
    (df["sex"].isin(sex_filter)) &
    (df["time"].isin(time_filter))
]

# ---------------- KPI CARDS (TOP ROW) ----------------
st.markdown("<h3 style='color:yellow;'>📌 Key Metrics</h3>", unsafe_allow_html=True)

k1, k2, k3 = st.columns(3)
k1.metric("👥 Total Customers", len(filtered_df))
k2.metric("💵 Avg Bill", round(filtered_df["total_bill"].mean(),2))
k3.metric("💰 Avg Tip", round(filtered_df["tip"].mean(),2))

st.divider()

# ---------------- CHART GRID (2x2) ----------------
c1, c2 = st.columns(2)

with c1:
    st.markdown("<h4 style='color:lightgreen;'>Average Bill by Day</h4>", unsafe_allow_html=True)
    fig1, ax1 = plt.subplots()
    sns.barplot(x="day", y="total_bill", data=filtered_df, palette="coolwarm", ax=ax1)
    st.pyplot(fig1)

with c2:
    st.markdown("<h4 style='color:lightgreen;'>Customer Count by Gender</h4>", unsafe_allow_html=True)
    fig2, ax2 = plt.subplots()
    sns.countplot(x="sex", data=filtered_df, palette="Set2", ax=ax2)
    st.pyplot(fig2)

c3, c4 = st.columns(2)

with c3:
    st.markdown("<h4 style='color:lightgreen;'>Bill vs Tip (Regression)</h4>", unsafe_allow_html=True)
    fig3, ax3 = plt.subplots()
    sns.regplot(x="total_bill", y="tip", data=filtered_df, color="purple", ax=ax3)
    st.pyplot(fig3)

with c4:
    st.markdown("<h4 style='color:lightgreen;'>Correlation Heatmap</h4>", unsafe_allow_html=True)
    fig4, ax4 = plt.subplots()
    sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax4)
    st.pyplot(fig4)

st.divider()

# ---------------- CONCLUSION ----------------
st.markdown("<h2 style='color:pink;'>📊 Final Conclusion</h2>", unsafe_allow_html=True)
st.markdown("""
✔ Weekend days generate higher revenue  
✔ Tip increases with total bill  
✔ Male and Female customer distribution is visible  
✔ Strong correlation between bill and tip  
✔ Filters allow interactive exploration  

🎯 This dashboard helps restaurant owners take better business decisions.
""")
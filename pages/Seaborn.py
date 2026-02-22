import streamlit as st
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
st.sidebar.markdown("""
## 📋 Topics Menu
- [Introduction](#intro)
- [Table of contents](#tab)
- [ Categorical Plots](#basic)
- [ Univariate Plots](#styling)
- [Bivariate Plots](#line)
- [Multivariate Plot](#bar)
- [Matrix Plots](#scatter)
- [Dashboard](#dashboard)
- [Practice](#pr)
- [About author](#a)
""", unsafe_allow_html=True)

#table of content................
st.markdown("<a id='tab'></a>",unsafe_allow_html=True)
st.markdown(
    "<h4 style='color: skyblue; text-align: center;'> Table of Contents</h4>",
    unsafe_allow_html=True
)
st.code("1. Seaborn Introduction")
st.code("2. Categorical Plots")
st.text(""" - Count Plot/Bar Plot
         - Swarm Plot
         - Point Plot
         - Categorical Box Plot
         - Categorical Violin Plot
         - Cat plot""")
st.code("3. Univariate Plots")
st.text(""" 
         - KDE Plot
         - Rug Plot
         - Dist Plot
         - Box Plot $ Violin Plot
         - Strip Plot""")

st.code("4. Bivariate Plots")
st.text(""" - Regression Plot
         - Joint Plot
         - Hexbin Plot""")

st.code("5. Multivariate Plot")
st.text(""" - Using Parameters
         - Relational Plot
         - Facet Grid
         - Pair Plot
         - Pair Grid""")

st.code("6. Matrix Plots")
st.text(""" - Heat map
         - Cluster Map""")



#intro................................................
st.markdown("<a id='intro'></a>",unsafe_allow_html=True)
st.markdown(
    "<h2 style='color: skyblue; text-align: center;'>Seaborn</h2>",
    unsafe_allow_html=True
)
st.text("Seaborn is a Python library for creating statistical visualizations. It provides clean default styles and color palettes, making plots more attractive and easier to read.")
st.text("Seaborn emphasizes visualization as an essential part of data analysis.")
st.text("Its dataset-oriented APIs allow switching between different plot types for the same variables.")
st.text("Helps in understanding patterns, trends and relationships within the data.")

import pandas as pd
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Seaborn Visualization Guide", layout="wide")

st.header("📊 Seaborn Data Visualization")
st.markdown("---")

# 1. Categorical Plots
st.subheader(":orange[1. Categorical Plots]")
st.write("Plots used to visualize categorical data (groups or labels).")
st.info("**Examples:** Bar Plot, Count Plot, Swarm Plot, Point Plot, Cat Plot, Box Plot, Violin Plot.")


# 2. Univariate Plots
st.subheader(":blue[2. Univariate Plots]")
st.write("Plots that visualize the distribution of a **single** variable.")
st.info("**Examples:** Histogram, KDE Plot, Rug Plot, Box Plot, Dist Plot, Violin Plot, Strip Plot.")


# 3. Bivariate Plots
st.subheader(":green[3. Bivariate Plots]")
st.write("Plots that visualize the relationship between **two** variables.")
st.info("**Examples:** Scatter Plot, Line Plot, Regression Plot, Joint Plot, Hexbin Plot.")


# 4. Multivariate Plots
st.subheader(":violet[4. Multivariate Plots]")
st.write("Plots that involve **more than two** variables, often using hue, size, or facets.")
st.info("**Examples:** Pair Plot, Facet Grid, Relational Plot.")


# 5. Matrix Plots
st.subheader(":red[5. Matrix Plots]")
st.write("Plots that visualize relationships within matrices of data (correlation or heat).")
st.info("**Examples:** Heatmap, Cluster Map.")


st.markdown("---")

st.header("Install seaborn")
st.code("pip install streamlit")

st.header(" Seaborn Sample Datasets")

# Dataset info
data = {
    "Dataset": [
        "tips",
        "iris",
        "titanic",
        "penguins",
        "flights",
        "diamonds",
        "mpg",
        "planets",
        "taxis",
        "geyser"
    ],
    "Definition": [
        "Restaurant bills and tip amounts; perfect for regression and categorical analysis.",
        "Measurements of three flower species; the gold standard for classification tasks.",
        "Survival data of passengers; great for binary classification and data cleaning.",
        "Body measurements of Antarctic penguins; a modern, diverse alternative to Iris.",
        "Monthly air passenger numbers (1949–1960); ideal for time-series and heatmaps.",
        "Prices and quality metrics for over 50,000 diamonds; best for large-scale regression.",
        "Fuel efficiency and engine specs for various cars; good for multivariate analysis.",
        "Discovery data for over 1,000 exoplanets; great for scatter plots and bar charts.",
        "NYC taxi trip records; useful for learning about distances, fares, and time.",
        "Eruption times of the Old Faithful geyser; excellent for showing joint distributions."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display as table in Streamlit
st.dataframe(df, use_container_width=True)
st.text("How Load Data set")
st.code("""import seaborn as sns
        tips = sns.load_dataset('tips')
        tips.head()
        """)

if st.button("Run", key="1"):
    import seaborn as sns
    # Load dataset
    tips = sns.load_dataset('tips')
    # Display first 5 rows
    st.dataframe(tips.head())



#categorical.................
st.markdown(
    "<h4 style='color: skyblue; text-align: center;'>Categorical Plots</h4>",
    unsafe_allow_html=True
)
st.text("Categorical plots in data visualization are used to visullize categorical data , which consists of discrete and distnict or groups.")
st.markdown(
    "<h4 style='color: skyblue'>Count Plot</h4>",
    unsafe_allow_html=True
)
st.text("The Count Plot displays the counts of observations in each category.Suitable for visualizing the frequency or distribution of categorical data.")
st.text("Use sns.countplot(x,data=dataframe) to create a count plot.")
st.code("""#count plot
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset('tips')
        plt.figure(figsize=(8,5))
        sns.countplot(x="day",data=tips,palette="Set3)
        plt.title("Count of tips by Dayof the Week")
        plt.show()""")
if st.button("Run", key="2"):
    # Load dataset
    tips = sns.load_dataset('tips')
    import matplotlib.pyplot as plt

    # Create figure
    fig, ax = plt.subplots(figsize=(8,5))
    sns.countplot(x="day", data=tips, palette="Set3", ax=ax)
    
    # Add title
    ax.set_title("Count of Tips by Day of the Week")
    
    # Render in Streamlit
    st.pyplot(fig)
st.markdown(
    "<h4 style='color: skyblue'>Swarm Plot</h4>",
    unsafe_allow_html=True
)
import matplotlib.pyplot as plt
# ================= HEADING & THEORY =================
st.subheader("🐝 Swarm Plot ")
st.markdown("""
A **Swarm Plot** is used to display all individual data points for each category, avoiding overlap.
It helps to visualize distribution of data points and detect patterns or outliers.
""")

# ================= SAMPLE DATA =================
# Load example dataset
df = sns.load_dataset("tips")

st.subheader("Sample Data - Tips Dataset")
st.dataframe(df.head())
st.code("""import seaborn as sns
        import matplotlib.pyplot as plt
        sns.swarmplot(x="day", y="total_bill", hue="sex", data=df, ax=ax)
        plt.title("Swarm Plot of Total Bill by Day and Gender")""")

# ================= PLOT =================
if st.button("Run:",key="4"):
    st.subheader("Swarm Plot: Total Bill vs Day")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.swarmplot(x="day", y="total_bill", hue="sex", data=df, ax=ax)
    ax.set_title("Swarm Plot of Total Bill by Day and Gender")
    st.pyplot(fig)




import seaborn as sns
import matplotlib.pyplot as plt
st.subheader("📌 Point Plot in Python")
st.markdown("""
A **Point Plot** displays the summary statistics (mean by default) of a variable across categories.
It is useful to visualize trends and compare groups clearly.
""")
st.code("""import seaborn as sns
import matplotlib.pyplot as plt
        df = sns.load_dataset("tips")
        sns.pointplot(x="day", y="total_bill", hue="sex", data=df, markers=["o", "s"], linestyles=["-", "--"], ax=ax)
        plt.title("Point Plot of Total Bill by Day and Gender")
        plt.ylabel("Average Total Bill")
        """)

if st.button("Run",key="6"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.pointplot(x="day", y="total_bill", hue="sex", data=df, markers=["o", "s"], linestyles=["-", "--"], ax=ax)
    ax.set_title("Point Plot of Total Bill by Day and Gender")
    ax.set_ylabel("Average Total Bill")
    st.pyplot(fig)


import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Categorical Box Plot")
st.markdown("""
A **Box Plot** (also called Whisker Plot) displays the distribution of a numerical variable across categories.  
It shows the **minimum, first quartile (Q1), median, third quartile (Q3), and maximum** values, along with potential outliers.  

Box plots are useful to:
- Compare distributions across different categories
- Detect outliers
- Understand the spread and symmetry of data
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x="day", y="total_bill", hue="sex", data=df, palette="Set2", ax=ax)
plt.title("Box Plot of Total Bill by Day and Gender")
plt.ylabel("Total Bill")
""")

if st.button("Run", key="boxplot"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x="day", y="total_bill", hue="sex", data=df, palette="Set2", ax=ax)
    ax.set_title("Box Plot of Total Bill by Day and Gender")
    ax.set_ylabel("Total Bill")
    st.pyplot(fig)


import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Categorical Violin Plot")
st.markdown("""
A **Violin Plot** combines aspects of a box plot and a kernel density plot.  
It shows the distribution of a numerical variable across categories, **including its probability density**, while also displaying median and quartiles.  

Violin plots are useful to:
- Compare distributions across categories
- Visualize multimodal distributions
- See both summary statistics and data density
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
sns.violinplot(x="day", y="total_bill", hue="sex", data=df, split=True, palette="Pastel1", ax=ax)
ax.set_title("Violin Plot of Total Bill by Day and Gender")
ax.set_ylabel("Total Bill")
""")

if st.button("Run", key="violinplot"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.violinplot(x="day", y="total_bill", hue="sex", data=df, split=True, palette="Pastel1", ax=ax)
    ax.set_title("Violin Plot of Total Bill by Day and Gender")
    ax.set_ylabel("Total Bill")
    st.pyplot(fig)

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Categorical Plot (Catplot) in Python")
st.markdown("""
A **Categorical Plot (`catplot`)** is a **generalized function in Seaborn** that can create several types of categorical plots such as:  
- **Strip Plot**  
- **Swarm Plot**  
- **Box Plot**  
- **Violin Plot**  
- **Bar Plot**  
- **Point Plot**  

The `catplot` is useful because it provides a **flexible way to plot categorical data** with the `kind` parameter, allowing you to switch between plot types easily.  

Key features:  
- Handles **hue, row, and column faceting**  
- Works well for **group comparisons**  
- Can combine multiple categorical variables
- kind like bar,swarm,box,violin,point,etc
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.set_style("whitegrid")
g = sns.catplot(
    x="day", y="total_bill", hue="sex", kind="bar", data=df, 
    height=5, aspect=1.5, palette="coolwarm"
)
g.set_axis_labels("Day of Week", "Total Bill")
g.fig.suptitle("Categorical Bar Plot using Catplot", y=1.05)
""")

if st.button("Run", key="catplot"):
    df = sns.load_dataset("tips")
    sns.set_style("whitegrid")
    g = sns.catplot(
        x="day", y="total_bill", hue="sex", kind="bar", data=df, 
        height=5, aspect=1.5, palette="coolwarm"
    )
    g.set_axis_labels("Day of Week", "Total Bill")
    g.fig.suptitle("Categorical Bar Plot using Catplot", y=1.05)
    st.pyplot(g.fig)


















st.markdown("""
<h2 style="color:orange;">Univariate Plot</h2>

<p>
A <strong>univariate plot</strong> is a type of data visualization that represents the distribution 
and characteristics of a single variable. It is used to analyze the patterns, trends, 
or summary statistics of one variable at a time.
</p>

<h3 style="color:deeppink;">Key Points:</h3>
<ul>
<li>Focuses on <strong>one variable</strong> only.</li>
<li>Helps in understanding the <strong>distribution</strong> of data.</li>
<li>Common types include:
    <ul>
        <li>Histogram</li>
        <li>Box plot</li>
        <li>Density plot</li>
        <li>Bar plot (for categorical data)</li>
    </ul>
</li>
<li>Useful for detecting outliers, skewness, and central tendency of the variable.</li>
</ul>

<p>
In summary, univariate plots are fundamental for exploring a dataset and understanding 
individual variable characteristics before moving to more complex analyses.
</p>
""", unsafe_allow_html=True)
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 KDE (Kernel Density Estimate) Plot in Python")
st.markdown("""
A **KDE Plot** is a way to visualize the **probability density** of a continuous numerical variable.  
It estimates the distribution of the data using a smooth curve instead of discrete bins like a histogram.  

KDE plots are useful to:
- Understand the underlying distribution of data
- Identify peaks (modes) and spread
- Compare distributions of multiple variables
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
sns.kdeplot(df['total_bill'], shade=True, color='skyblue', bw_adjust=1, ax=ax)
ax.set_title("KDE Plot of Total Bill")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Density")
""")

if st.button("Run", key="kdeplot"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.kdeplot(df['total_bill'], shade=True, color='skyblue', bw_adjust=1, ax=ax)
    ax.set_title("KDE Plot of Total Bill")
    ax.set_xlabel("Total Bill")
    ax.set_ylabel("Density")
    st.pyplot(fig)
    import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Rug Plot in Python")
st.markdown("""
A **Rug Plot** is a simple visualization that shows **individual data points** along an axis.  
Each data point is represented by a small vertical (or horizontal) line, which “rugs” the axis.  

Rug plots are useful to:
- See the distribution of individual values
- Identify clustering or gaps in data
- Combine with KDE or other plots to enhance visualization
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
sns.rugplot(df['total_bill'], height=0.05, color='red', ax=ax)
ax.set_title("Rug Plot of Total Bill")
ax.set_xlabel("Total Bill")
""")

if st.button("Run", key="rugplot"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.rugplot(df['total_bill'], height=0.05, color='red', ax=ax)
    ax.set_title("Rug Plot of Total Bill")
    ax.set_xlabel("Total Bill")
    st.pyplot(fig)
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Univariate Box Plot in Python")
st.markdown("""
A **Univariate Box Plot** displays the distribution of a **single numerical variable**.  
It shows:
- Minimum value  
- First quartile (Q1)  
- Median (Q2)  
- Third quartile (Q3)  
- Maximum value  
- Outliers (points outside 1.5 * IQR)  

Univariate box plots are useful to:
- Understand the spread of a single variable
- Detect outliers
- See the symmetry or skewness of the data
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(y=df['total_bill'], color='lightgreen', ax=ax)
ax.set_title("Univariate Box Plot of Total Bill")
ax.set_ylabel("Total Bill")
""")

if st.button("Run", key="uniboxplot"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(y=df['total_bill'], color='lightgreen', ax=ax)
    ax.set_title("Univariate Box Plot of Total Bill")
    ax.set_ylabel("Total Bill")
    st.pyplot(fig)

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Univariate Violin Plot in Python")
st.markdown("""
A **Univariate Violin Plot** displays the distribution of a **single numerical variable**.  
It combines a **kernel density estimate (KDE)** with a box plot, showing:
- The probability density of the data
- Median and quartiles (via the internal box plot)
- Symmetry or skewness of the distribution

Univariate violin plots are useful to:
- Visualize the shape of a distribution
- Identify multimodal distributions
- See spread, central tendency, and outliers in one plot
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
sns.violinplot(y=df['total_bill'], color='lightblue', ax=ax)
ax.set_title("Univariate Violin Plot of Total Bill")
ax.set_ylabel("Total Bill")
""")

if st.button("Run", key="univivinplot"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.violinplot(y=df['total_bill'], color='lightblue', ax=ax)
    ax.set_title("Univariate Violin Plot of Total Bill")
    ax.set_ylabel("Total Bill")
    st.pyplot(fig)
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Univariate Strip Plot in Python")
st.markdown("""
A **Strip Plot** is used to display **individual data points** of a single numerical variable along an axis.  

For a univariate strip plot:
- All points are plotted along one axis (usually y-axis)  
- Helps visualize the **distribution and clustering** of data  
- Can highlight **outliers and density** in combination with jitter  

Univariate strip plots are useful to:
- Understand how individual values are distributed  
- Identify clustering and gaps  
- Detect outliers visually
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
sns.stripplot(y=df['total_bill'], color='purple', size=6, ax=ax)
ax.set_title("Univariate Strip Plot of Total Bill")
ax.set_ylabel("Total Bill")
""")

if st.button("Run", key="unistripplot"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.stripplot(y=df['total_bill'], color='purple', size=6, ax=ax)
    ax.set_title("Univariate Strip Plot of Total Bill")
    ax.set_ylabel("Total Bill")
    st.pyplot(fig)
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Univariate Distribution (Dist) Plot in Python")
st.markdown("""
A **Distribution Plot (Dist Plot)** visualizes the distribution of a **single numerical variable**.  
It combines a **histogram** with a **kernel density estimate (KDE)** curve by default.  

Dist plots are useful to:
- Understand the frequency distribution of data
- Identify patterns, skewness, or outliers
- Compare shape of distributions visually
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
sns.histplot(df['total_bill'], kde=True, bins=20, color='skyblue', ax=ax)
ax.set_title("Distribution Plot of Total Bill")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Frequency / Density")
""")

if st.button("Run", key="distplot_uni"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df['total_bill'], kde=True, bins=20, color='skyblue', ax=ax)
    ax.set_title("Distribution Plot of Total Bill")
    ax.set_xlabel("Total Bill")
    ax.set_ylabel("Frequency / Density")
    st.pyplot(fig)







    #.....................................................................................................................
    import streamlit as st

st.markdown("""
<h2 style="color:orange;">Bivariate Plot</h2>

<p>
A <strong>bivariate plot</strong> is a type of data visualization that shows the relationship 
between <strong>two variables</strong>. It helps in understanding how one variable 
changes with respect to another.
</p>

<h3 style="color:deeppink;">Key Points:</h3>
<ul>
<li>Focuses on <strong>two variables</strong> at the same time.</li>
<li>Helps identify <strong>correlations, trends, and patterns</strong> between variables.</li>
<li>Common types of bivariate plots include:
    <ul>
        <li>Scatter plot – shows the relationship between two numeric variables.</li>
        <li>Line plot – often used for time series data comparing two variables.</li>
        <li>Bar plot – compares a numeric variable against a categorical variable.</li>
        <li>Heatmap – visualizes relationships in a matrix or correlation table.</li>
    </ul>
</li>
<li>Useful for detecting positive/negative correlations, clusters, or anomalies.</li>
</ul>

<p>
In summary, bivariate plots are essential for exploring interactions between two variables 
and forming hypotheses about their relationship before deeper analysis.
</p>
""", unsafe_allow_html=True)
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Bivariate Regression Plot in Python")
st.markdown("""
A **Regression Plot** shows the relationship between **two numerical variables**.  
It plots the data points (scatter) and fits a **linear regression line** to highlight the trend.  

Regression plots are useful to:
- Identify correlation between variables
- Visualize trends or patterns
- Detect outliers or deviations from the trend
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
sns.regplot(x='total_bill', y='tip', data=df, scatter_kws={'color':'blue'}, line_kws={'color':'red'}, ax=ax)
ax.set_title("Regression Plot of Tip vs Total Bill")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")
""")

if st.button("Run", key="regplot_bivar"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.regplot(x='total_bill', y='tip', data=df, scatter_kws={'color':'blue'}, line_kws={'color':'red'}, ax=ax)
    ax.set_title("Regression Plot of Tip vs Total Bill")
    ax.set_xlabel("Total Bill")
    ax.set_ylabel("Tip")
    st.pyplot(fig)
    import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Joint Plot in Python")
st.markdown("""
A **Joint Plot** visualizes the relationship between **two numerical variables** along with their **individual distributions**.  
It combines a scatter plot (or regression plot) in the center with histograms or KDE plots on the top and right axes.  

Joint plots are useful to:
- See correlation between two variables
- Observe distribution of each variable individually
- Detect trends, clusters, and outliers
""")

st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
g = sns.jointplot(x='total_bill', y='tip', data=df, kind='scatter', color='purple', height=6)
g.fig.suptitle("Joint Plot of Total Bill vs Tip", y=1.02)
""")

if st.button("Run", key="jointplot_bivar"):
    df = sns.load_dataset("tips")
    g = sns.jointplot(x='total_bill', y='tip', data=df, kind='scatter', color='purple', height=6)
    g.fig.suptitle("Joint Plot of Total Bill vs Tip", y=1.02)
    st.pyplot(g.fig)
    import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📌 Hexbin Plot in Python")
st.markdown("""
A **Hexbin Plot** visualizes the relationship between **two numerical variables** using **hexagonal bins** instead of individual points.  
It is especially useful for large datasets where scatter plots may become crowded.  
The color intensity of each hexagon represents the number of points in that bin.  

Hexbin plots are useful to:
- Detect density patterns in large datasets
- Identify clusters or high-concentration regions
- Reduce overplotting compared to scatter plots
""")

st.code("""
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8,5))
hb = ax.hexbin(df['total_bill'], df['tip'], gridsize=25, cmap='Blues', edgecolors='grey')
ax.set_title("Hexbin Plot of Total Bill vs Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")
cb = fig.colorbar(hb, ax=ax)
cb.set_label("Counts")
""")

if st.button("Run", key="hexbin_bivar"):
    df = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(8,5))
    hb = ax.hexbin(df['total_bill'], df['tip'], gridsize=25, cmap='Blues', edgecolors='grey')
    ax.set_title("Hexbin Plot of Total Bill vs Tip")
    ax.set_xlabel("Total Bill")
    ax.set_ylabel("Tip")
    cb = fig.colorbar(hb, ax=ax)
    cb.set_label("Counts")
    st.pyplot(fig)
    import streamlit as st

st.markdown("""
<h2 style="color:orange;">Multivariate Plot</h2>

<p>
A <strong>multivariate plot</strong> is a type of data visualization that represents the relationships 
among <strong>three or more variables</strong> simultaneously. It helps to explore complex interactions 
and patterns in the dataset that cannot be seen in univariate or bivariate plots.
</p>

<h3 style="color:deeppink;">Key Points:</h3>
<ul>
<li>Focuses on <strong>three or more variables</strong> at the same time.</li>
<li>Helps identify <strong>correlations, trends, clusters, and interactions</strong> among variables.</li>
<li>Common types of multivariate plots include:
    <ul>
        <li>3D scatter plots – show relationships among three numeric variables.</li>
        <li>Pair plots – visualize pairwise relationships across multiple variables.</li>
        <li>Heatmaps – represent correlations or patterns among multiple variables.</li>
        <li>Bubble plots – a scatter plot with a third variable represented by bubble size or color.</li>
    </ul>
</li>
<li>Useful for detecting complex patterns, groupings, and high-dimensional data insights.</li>
</ul>

<p>
In summary, multivariate plots are crucial for understanding the interplay among multiple variables 
and for making informed decisions in advanced data analysis.
</p>
""", unsafe_allow_html=True)

st.subheader("Using Parameters")
st.text("using Hue Parameter :")
st.text("using Hue parameter will add color to the plot based on the provided categorical variable,specifying a unique color for each of the categories . this parameter can be used almostall of the plots like .scatterplot(),.boxplot(),.violinplot(),.lineplot() e.t.c")
st.code("""#violin plot with hue
        plt.figure(figsize=(10,6))
        sns.violinplot(
        x="day",
        y="total_bill",
        data=tips,
        hue="sex",  #color by gender
        palette="Set1", #color palette
        split=True)
        plt.title("Violin Polt with Hue for Total Bill by Day and Gender")
        plt.xlabel("Day of the Week")
        plt.ylabel("Total Bill($)")
        plt.legend(title="Gender")
        plt.show()""")
if st.button('Run',key="7"):
    tips = sns.load_dataset("tips")

    fig, ax = plt.subplots(figsize=(10,6))
    sns.violinplot(
    x="day",
    y="total_bill",
    data=tips,
    hue="sex",       # Color by gender
    palette="Set1",  # Color palette
     split=True,
    ax=ax
    )

    ax.set_title("Violin Plot with Hue for Total Bill by Day and Gender")
    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Total Bill ($)")
    ax.legend(title="Gender")
    st.pyplot(fig)

st.code("""import seaborn as sns
import matplotlib.pyplot as plt
        tips=sns.load_dataset("tips")
        plt.figure(figsize=(10,6))
        sns.scatterplot(
        x="total_bill",
        y="tips"
        data=tips,
        hue="day",  #color by gender
        palette="Set1", #color palette
        size="size"
        sizes=(20,200))
        plt.title("Scatter Polt with Hue and Size for Tips Dataset")
        plt.xlabel("Day of the Week")
        plt.ylabel("Total Bill($)")
        plt.legend(title="Gender")
        plt.show()""")
if st.button('Run',key="7"):
    tips = sns.load_dataset("tips")

    fig, ax = plt.subplots(figsize=(10,6))
    sns.violinplot(
    x="day",
    y="total_bill",
    data=tips,
    hue="sex",       # Color by gender
    palette="Set1",  # Color palette
     split=True,
    ax=ax
    )

    ax.set_title("Violin Plot with Hue for Total Bill by Day and Gender")
    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Total Bill ($)")
    ax.legend(title="Gender")
    st.pyplot(fig)












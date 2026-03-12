import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
st.set_page_config(page_title="StudyNest", layout="wide")

# ---------------- THEME INITIALIZE ----------------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# ---------------- THEME BUTTON ----------------
col1, col2 = st.columns([9,1])

with col2:
    if st.button("light / dark"):
        if st.session_state.theme == "dark":
            st.session_state.theme = "light"
        else:
            st.session_state.theme = "dark"
        st.rerun()

# ---------------- BACK BUTTON ----------------
if st.button("⬅ Back to Home"):
    st.switch_page("main.py")


# ---------------- DARK MODE CSS ----------------
if st.session_state.theme == "dark":

    st.markdown("""
    <style>

    .stApp {
        background-color: #0f172a;
    }

    .fade-text {
        text-align: center;
        font-size: 48px;
        color: #FFD700;
        animation: fadeIn 2s ease-in;
        margin-top: 40px;
    }

    .subtitle {
        text-align: center;
        font-size: 22px;
        color: #e5e7eb;
        margin-bottom: 40px;
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }

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


# ---------------- LIGHT MODE CSS ----------------
else:

    st.markdown("""
    <style>

    .stApp {
        background-color: white;
        color: black;
    }

    .fade-text {
        text-align: center;
        font-size: 48px;
        color: black;
        animation: fadeIn 2s ease-in;
        margin-top: 40px;
    }

    .subtitle {
        text-align: center;
        font-size: 22px;
        color: black;
        margin-bottom: 40px;
    }

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
                p, h1, h2, h3, h4, h5, h6, span {
    color: black !important;
}
   /* BUTTON STYLE */

div.stButton > button {
    background-color: #2563eb !important;
    color: white !important;
    border-radius: 8px;
    border: none;
    padding: 8px 18px;
    font-weight: 600;
}

/* Hover */

div.stButton > button:hover {
    background-color: #1d4ed8 !important;
    color: white !important;
}
                
    /* SIDEBAR LIGHT MODE */

    section[data-testid="stSidebar"]{
        background-color:#ffffff;
        color:#0f172a;
        border-right:1px solid #e5e7eb;
    }

/* Click (Active) */

div.stButton > button:active {
    background-color: #2563eb !important;
    color: white !important;
}

/* Focus */

div.stButton > button:focus {
    background-color: #2563eb !important;
    color: white !important;
    box-shadow: none !important;
}             
                /* CODE BLOCK - st.code */

pre {
    background-color: #f1f5f9 !important;   /* light background */
    color: #0f172a !important;              /* dark text */
    border-radius: 8px;
    padding: 14px;
    border: 1px solid #e2e8f0;
    font-size: 15px;
}

/* code inside block */

code {
    color: #0f172a !important;
}

/* optional line highlight */

.stCodeBlock {
    background-color: #f8fafc !important;
}
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


# ---------------- CONTENT ----------------

if st.session_state.theme == "dark":

    st.markdown("""
    <h2 style="color:white;">Welcome : Learn Data Visualization Step by Step</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h5 style="color:green;">
    Transform raw data into meaningful insights through visualization.
    </h5>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <h2 style="color:#1e293b;">Welcome : Learn Data Visualization Step by Step</h2>
    """, unsafe_allow_html=True)

    st.markdown('<h5 style="color:green;">Transform raw data into meaningful insights through visualization.</h5>', unsafe_allow_html=True)
# ---------------- MAIN HEADING ----------------



st.markdown("""
<style>

/* Hide Emojis */

span.emoji {
    display:none;
}

</style>
""", unsafe_allow_html=True)






st.title("Matplotlib")
st.text("Matplotlib is Python's most popular plotting library for creating static, animated, and interactive visualizations.")
#installation...........


st.markdown("<h2 style='color:yellow;align:center'>Installation</h2>",unsafe_allow_html=True)
st.text("Matplotlib installs via pip or conda and requires NumPy")
st.text("Run")
st.success("pip install matplotlib")
st.markdown("<h4 style='color:pink;'>Description :</h4>",unsafe_allow_html=True)
st.text("Always import as import matplotlib.pyplot as plt and import numpy as np. Version 3.10.3 is current as of 2026.")

#simple line plot
st.markdown("<h4 style='color:pink;'>Import Basics:</h4>",unsafe_allow_html=True)



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="Matplotlib  📊", layout="wide")

# Sidebar - PERFECT Navigation
st.sidebar.markdown("""
## 📋 Topics Menu
- [Introduction](#intro)
- [Installation](#installation)
- [Error bar graph](#basic)
- [Line Styling](#styling)
- [Line Plot](#line)
- [Bar Chart](#bar)
- [Scatter](#scatter)
- [Histogram](#histogram)
- [Pie](#pie)
- [3D Charts with Matplotlib](#3)
- [Dashboard](#dashboard)
- [Practice](#pr)
- [About author](#a)
""", unsafe_allow_html=True)
#intro................
st.markdown("<a id='intro'></a>", unsafe_allow_html=True)
st.text("""Matplotlib is a widely used Python library for creating static, interactive and animated visualizations from data. It provides flexible and customizable plotting functions that help in understanding data patterns, trends and relationships effectively.""")
st.image("https://media.geeksforgeeks.org/wp-content/uploads/20250310152352123910/Matplotlib.webp")
st.text("Example :")
st.text("Let's create a simple line plot using Matplotlib, showcasing the ease with which you can visualize data.")
st.code("""import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.show()""")
if st.button("▶️ Run ", key="basic"):
    st.balloons()
    with st.spinner("Loading..."):
        time.sleep(2)
        fig,ax=plt.subplots()
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 4, 9, 16]
        ax.plot(x,y)
        st.pyplot(fig)
#components.............
st.title("Components or Parts of Matplotlib Figure")
st.text("Anatomy of a Matplotlib plot :")
st.text("This section dives into the key components of a Matplotlib plot, including figures, axes, titles and legends, essential for effective data visualization.")
st.image("https://media.geeksforgeeks.org/wp-content/uploads/20260113175352118443/matplotlib.webp")
st.text("The parts of a Matplotlib figure include (as shown in the figure above):")
with st.expander("The parts of a Matplotlib figure include (as shown in the figure above):"):
        with st.expander("Figure"):
            st.text("The overarching container that holds all plot elements, acting as the canvas for visualizations.")
        with st.expander("Axes"):
            st.text("The areas within the figure where data is plotted; each figure can contain multiple axes.")
        with st.expander("Axis"):
            st.text("Represents the x-axis and y-axis, defining limits, tick locations and labels for data interpretation.")
        with st.expander("Lines and Markers"):
            st.text("Lines connect data points to show trends, while markers denote individual data points in plots like scatter plots.")
        with st.expander("Title and Labels"):
            st.text("The title provides context for the plot, while axis labels describe what data is being represented on each axis.")

st.markdown("<h2 style='color:yellow;'>Matplotlib Pyplot</h2>", unsafe_allow_html=True)
st.text(" py.plot is a module within Matplotlib that provides a MATLAB-like interface for making plots. It simplifies the process of adding plot elements such as lines, images and text to the axes of the current figure.")
st.markdown("<h4 style='color:pink;'>Steps to Use Pyplot</h4>", unsafe_allow_html=True)
st.markdown("""<span style ="color:red;">Import matplotlib :</span> Start by importing matplotlib.pyplot as plt.<br>
               <span style= "color:red;">Create Data :</span>Prepare your data in the form of lists or arrays<br>
               <span style="color:red;">Plot Data :</span> Use plt.plot() to create the plot.<br>
               <span style="color:red;">Customize plot :</span>Add title,lebels and other elements using methods like plt.tutle(),plt.xlable() and plt.ylabel().<br>
               <span style="color:red;">Display Plot :<span>Use plt.show() to display the plot.<br> """,unsafe_allow_html=True)

st.text("Let's visualize a basic plot and understand basic components of matplotlib figure:")
st.code("""import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 8]
y = [0, 4, 16, 36, 64]

fig, ax = plt.subplots()  
ax.plot(x, y, marker='o', label="Data Points") 

ax.set_title("Basic Components of Matplotlib Figure")
ax.set_xlabel("X-Axis") 
ax.set_ylabel("Y-Axis")  
ax.legend()
plt.show()""")

if st.button("▶️ Run ", key="basic1"):
    st.balloons()
    with st.spinner("Loading..."):
        time.sleep(2)
        x = [0, 2, 4, 6, 8]
        y = [0, 4, 16, 36, 64]
        fig,ax=plt.subplots()
        ax.plot(x,y,marker='o',label="Data Points")
        ax.set_title("Basic  component of matplotlib figure")
        ax.set_xlabel("X-Axis") 
        ax.legend()
        ax.set_ylabel("Y-Axis")  
        st.pyplot(fig)
st.markdown("""
<h4 style="color:yellow; text-align:center;"> Matplotlib Keywords Explanation</h4>
<p><b style="color:deeppink;">x , y :</b> values (data points)<br></p>
<p><b style="color:deeppink;">fig :</b> full graph window (figure)</p>
<p><b style="color:deeppink;">ax :</b> plotting area (axes)</p>
<p><b style="color:deeppink;">plot :</b> draw line graph</p>
<p><b style="color:deeppink;">marker :</b> point shape<br>
Values: o (circle), s (square), ^ (triangle), * (star), + (plus), x (cross)</p>
<p><b style="color:deeppink;">label :</b> legend text<br></p>

<p><b style="color:deeppink;">set_title :</b> graph heading<br></p>

<p><b style="color:deeppink;">set_xlabel :</b> x-axis name<br></p>

<p><b style="color:deeppink;">set_ylabel :</b> y-axis name<br></p>

<p><b style="color:deeppink;">legend :</b> show legend box<br>
Positions: upper right, upper left, lower right, best</p>

<p><b style="color:deeppink;">color :</b> line color<br>
Values: red, blue, green, #FF5733</p>

<p><b style="color:deeppink;">linestyle :</b> line type<br>
Values: - (solid), -- (dashed), : (dotted), -. (dash-dot)</p>

<p><b style="color:deeppink;">linewidth :</b> line thickness<br>
Values: 1, 2, 3, 5</p>

<p><b style="color:deeppink;">markersize :</b> size of point<br>
Values: 5, 8, 10</p>

<p><b style="color:deeppink;">show :</b> display graph on screen</p>
""", unsafe_allow_html=True)


st.markdown("""
<h4 style="color:yellow;">Different Types of Plots in Matplotlib</h4>

Matplotlib offers a wide range of plot types to suit various data visualization needs.  
Here are some of the most commonly used types of plots in Matplotlib:

<br>

• Line Graph  
<br>
• Bar Chart  
<br>
• Histogram  
<br>
• Scatter Plot  
<br>
• Pie Chart  
<br>
• 3D Plot  

""", unsafe_allow_html=True)
st.image("https://media.geeksforgeeks.org/wp-content/uploads/20241205132215349786/Screenshot-2024-12-05-131953.png")

with st.expander(" Key Features of Matplotlib"):
    st.markdown("""
**Versatile Plotting:**  
Create a wide variety of visualizations, including line plots, scatter plots, bar charts and histograms.

**Extensive Customization:**  
Control every aspect of your plots, from colors and markers to labels and annotations.

**Seamless Integration with NumPy:**  
Effortlessly plot data arrays directly, enhancing data manipulation capabilities.

**High-Quality Graphics:**  
Generate publication-ready plots with precise control over aesthetics.

**Cross-Platform Compatibility:**  
Use Matplotlib on Windows, macOS and Linux without issues.

**Interactive Visualizations:**  
Engage with your data dynamically through interactive plotting features.
""")
    


with st.expander(" What is Matplotlib Used For?"):
    st.markdown("""
Matplotlib is a Python library for data visualization, primarily used to create static, animated and interactive plots.  
It provides a wide range of plotting functions to visualize data effectively.

<b><span style="color:deeppink;">Key Uses of Matplotlib:</span></b><br><br>

<b><span style="color:deeppink;">Basic Plots:</span></b><br>
Line plots, bar charts, histograms, scatter plots, etc.<br><br>

<b><span style="color:deeppink;">Statistical Visualization:</span></b><br>
Box plots, error bars and density plots.<br><br>

<b><span style="color:deeppink;">Customization:</span></b><br>
Control over colors, labels, gridlines and styles.<br><br>

<b><span style="color:deeppink;">Subplots & Layouts:</span></b><br>
Create multiple plots in a single figure.<br><br>

<b><span style="color:deeppink;">3D Plotting:</span></b><br>
Surface plots and 3D scatter plots using mpl_toolkits.mplot3d.<br><br>

<b><span style="color:deeppink;">Animations & Interactive Plots:</span></b><br>
Dynamic visualizations with FuncAnimation.<br><br>

<b><span style="color:deeppink;">Integration:</span></b><br>
Works well with Pandas, NumPy and Jupyter Notebooks.
""", unsafe_allow_html=True)








st.markdown("<a id='basic'></a>",unsafe_allow_html=True)
# ========== 1. Error bar graph in python ==========
st.markdown("""<h4 style="color:yellow;">Errorbar graph in Python using Matplotlib</h4>""",unsafe_allow_html=True)
st.text("Error bars are graphical lines on a chart that show the variability or uncertainty of data points, indicating how accurate or precise the measurements are.")
st.markdown("""
<b><span style="color:green;">Short Error Bars:</span></b>  
Indicate that the values are tightly clustered around the data point, suggesting high reliability and precision.<br><br>

<b><span style="color:red;">Long Error Bars:</span></b>  
Indicate more spread-out values, signaling lower precision and greater uncertainty.
""", unsafe_allow_html=True)
st.text("Error bars usually extend equally on both sides of a data point, but when the data distribution is skewed, their lengths can be different, showing unequal variability on each side of the measurement.")
st.image("https://media.geeksforgeeks.org/wp-content/uploads/20200407204405/e_bar.png")
st.markdown("""
<h4 style="color:orange;">Types of Error Bars</h4>

Error bars can be applied in two main orientations:<br><br>

<b><span style="color:green;">Vertical Error Bars:</span></b><br>
Applied when the uncertainty is along the y-axis (dependent variable).<br><br>

<b><span style="color:blue;">Horizontal Error Bars:</span></b><br>
Used when the uncertainty lies along the x-axis (independent variable).
""", unsafe_allow_html=True)
st.markdown("""<h4 style="color:yellow;">Visualizing Error Bars: Examples</h4>""",unsafe_allow_html=True)

st.markdown("""<h4 style="color:pint;">Creating a Simple Graph</h4>""",unsafe_allow_html=True)
st.code("""import matplotlib.pyplot as plt

x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]

plt.plot(x, y)""")

if st.button("▶️ Run ", key="basic2"):
    st.balloons()
    with st.spinner("Loading..."):
        time.sleep(2)
    fig,ax=plt.subplots()
    x =[1, 2, 3, 4, 5, 6, 7]
    y =[1, 2, 1, 2, 1, 2, 1]

    ax.plot(x, y)
    st.pyplot(fig)

st.markdown("<h4 style='color:blue';>Example 1</h4>",unsafe_allow_html=True)
st.text(" Adding Error to the y-values")
st.code("""import matplotlib.pyplot as plt 

x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]

# creating error
y_error = 0.2

# plotting graph
plt.plot(x, y)

plt.errorbar(x, y,
             yerr = y_error,
             fmt ='o')""")

if st.button("▶️ Run ", key="basic3"):
    st.balloons()
    with st.spinner("Loading..."):
        time.sleep(2)
    fig,ax=plt.subplots()
    x =[1, 2, 3, 4, 5, 6, 7]
    y =[1, 2, 1, 2, 1, 2, 1]
    y_error=0.2
    ax.plot(x, y)
    ax.errorbar(x,y,yerr=y_error,fmt='o')
    st.pyplot(fig)

st.markdown("<h4 style='color:blue';>Example 2</h4>",unsafe_allow_html=True)
st.text(" Adding Error to the x-values")
st.code("""import matplotlib.pyplot as plt 

x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]

# creating error
x_error = 0.5

# plotting graph
plt.plot(x, y)
plt.errorbar(x, y,
             xerr = x_error,
             fmt ='o')""")
if st.button("▶️ Run ", key="basic4"):
    st.balloons()
    with st.spinner("Loading..."):
        time.sleep(2)
    fig,ax=plt.subplots()
    x =[1, 2, 3, 4, 5, 6, 7]
    y =[1, 2, 1, 2, 1, 2, 1]
    x_error=0.5
    ax.plot(x, y)
    ax.errorbar(x,y,yerr=x_error,fmt='o')
    st.pyplot(fig)
st.markdown("<h4 style='color:blue';>Example 3</h4>",unsafe_allow_html=True)
st.text(" Adding Error to Both x and y")
st.code("""import matplotlib.pyplot as plt 

x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]

# creating error
x_error = 0.5
y_error = 0.3

# plotting graph
plt.plot(x, y)
plt.errorbar(x, y, 
             yerr = y_error, 
             xerr = x_error, 
             fmt ='o')""")

if st.button("▶️ Run ", key="basic5"):
    st.balloons()
    with st.spinner("Loading..."):
        time.sleep(2)
    fig,ax=plt.subplots()
    x =[1, 2, 3, 4, 5, 6, 7]
    y =[1, 2, 1, 2, 1, 2, 1]
    x_error=0.5
    y_error=0.3
    ax.plot(x, y)
    ax.errorbar(x,y,yerr=x_error,fmt='o')
    st.pyplot(fig)

st.markdown("<h4 style='color:blue';>Example 4</h4>",unsafe_allow_html=True)
st.text("Variable Error in x and y")
st.text("This demonstrates how error bars can vary in length depending on the data, reflecting different levels of uncertainty for each data point.")
st.code("""import matplotlib.pyplot as plt

x =[1, 2, 3, 4, 5]
y =[1, 2, 1, 2, 1]

# creating error
y_errormin =[0.1, 0.5, 0.9,
             0.1, 0.9]
y_errormax =[0.2, 0.4, 0.6, 
             0.4, 0.2]

x_error = 0.5
y_error =[y_errormin, y_errormax]

# plotting graph
# plt.plot(x, y)
plt.errorbar(x, y,
             yerr = y_error,
             xerr = x_error, 
             fmt ='o')""")



if st.button("▶️ Run ", key="basic6"):
    st.balloons()
    with st.spinner("Loading..."):
        time.sleep(2)
    fig,ax=plt.subplots()
    x =[1, 2, 3, 4, 5]
    y =[1, 2, 1, 2, 1]
    y_errormin =[0.1, 0.5, 0.9,
             0.1, 0.9]
    y_errormax =[0.2, 0.4, 0.6, 
             0.4, 0.2]
    x_error = 0.5
    y_error =[y_errormin, y_errormax]
    #plt.plot(x, y)
    ax.errorbar(x, y,
             yerr = y_error,
             xerr = x_error, 
             fmt ='o')
    st.pyplot(fig)


st.markdown("<h4 style='color:blue';>Example 5</h4>",unsafe_allow_html=True)
st.text("A more complex example, illustrating how error bars can be used in different contexts to represent data with varying degrees of precision.")
st.code("""import numpy as np
import matplotlib.pyplot as plt

# defining our function 
x = np.arange(10)/10 
y = (x + 0.1)**2

# defining our error 
y_error = np.linspace(0.05, 0.2, 10)

# error bar
plt.plot(x, y)

plt.errorbar(x, y, yerr = y_error, fmt ='o')""")
if st.button("▶️ Run ", key="basic7"):
    st.balloons()
    with st.spinner("Loading..."):
        time.sleep(2)
        import numpy as np
        import matplotlib.pyplot as plt
        fig,ax=plt.subplots()
        # defining our function 
        x = np.arange(10)/10 
        y = (x + 0.1)**2

        # defining our error 
        y_error = np.linspace(0.05, 0.2, 10)

        # error bar
        ax.plot(x, y)

        ax.errorbar(x, y, yerr = y_error, fmt ='o')
        st.pyplot(fig)




st.markdown("<a id='styling'></a>",unsafe_allow_html=True)


import matplotlib.pyplot as plt
import random

# ================= HEADING & THEORY =================
st.markdown("""
<h3 style="color:orange;">Line Plot Styles in Matplotlib</h3>

Line plots are important data visualization elements used to identify relationships in data.  
Using the plot function, we can customize line styles, markers and colors for better visualization.

<hr>

<h4 style="color:deeppink;">Line Styles in Matplotlib</h4>

| Character | Definition |
|----------|------------|
| - | Solid line |
| -- | Dashed line |
| -. | Dash-dot line |
| : | Dotted line |
| . | Point marker |

<hr>

<h4 style="color:deeppink;">Marker Styles in Matplotlib</h4>

| Character | Definition |
|----------|------------|
| o | Circle marker |
| , | Pixel marker |
| v | Triangle down marker |
| ^ | Triangle up marker |
| < | Triangle left marker |
| > | Triangle right marker |
| s | Square marker |
| p | Pentagon marker |
| * | Star marker |
| + | Plus marker |
| x | X marker |
| D | Diamond marker |
| _ | Horizontal line marker |

<hr>

<h4 style="color:deeppink;">Color Code Abbreviations</h4>

| Code | Description |
|------|-------------|
| b | Blue |
| g | Green |
| r | Red |
| c | Cyan |
| m | Magenta |
| y | Yellow |
| k | Black |
| w | White |

<hr>

<h4 style="color:green;">Click the Run button </h4>
""", unsafe_allow_html=True)


# ================= DATA =================
students = ["Jane","Joe","Beck","Tom","Sam","Eva","Samuel","Jack",
            "Dana","Ester","Carla","Steve","Fallon","Liam","Culhane",
            "Candance","Ana","Mari","Steffi","Adam"]

marks = [random.randint(0, 101) for _ in students]


# ================= RUN BUTTON =================

    # -------- Example 1 --------
st.subheader("Example 1: Simple Line Plot (Magenta Dashed Line)")
st.code("""import matplotlib.pyplot as plt
import random as random
students = ["Jane","Joe","Beck","Tom",
            "Sam","Eva","Samuel","Jack",
            "Dana","Ester","Carla","Steve",
            "Fallon","Liam","Culhane","Candance",
            "Ana","Mari","Steffi","Adam"]
marks=[]
for i in range(0,len(students)):
     marks.append(random.randint(0, 101))

plt.figure(figsize=(12, 6))
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("CLASS RECORDS")
plt.plot(students,marks,'m--'))
""")
if st.button("Run",key="1"):
    fig1, ax1 = plt.subplots(figsize=(12,6))
    ax1.plot(students, marks, 'm--')
    ax1.set_xlabel("Students")
    ax1.set_ylabel("Marks")
    ax1.set_title("CLASS RECORDS - Example 1")
    st.pyplot(fig1)

    # -------- Example 2 --------
st.subheader("Example 2: Line Plot with Markers")
st.code("""import matplotlib.pyplot as plt
import random as random

students = ["Jane","Joe","Beck","Tom","Sam",
            "Eva","Samuel","Jack","Dana","Ester",
            "Carla","Steve","Fallon","Liam","Culhane",
            "Candance","Ana","Mari","Steffi","Adam"]
marks=[]
for i in range(0,len(students)):
     marks.append(random.randint(0, 101))

plt.figure(figsize=(12, 6))
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("CLASS RECORDS")
plt.plot(students, marks, color = 'green',
         linestyle = 'solid', marker = 'o',
         markerfacecolor = 'red', markersize = 12)""")

if st.button("Run",key="2"):
    fig2, ax2 = plt.subplots(figsize=(12,6))
    ax2.plot(students, marks, color='green', linestyle='solid',
             marker='o', markerfacecolor='red', markersize=12)
    ax2.set_xlabel("Students")
    ax2.set_ylabel("Marks")
    ax2.set_title("CLASS RECORDS - Example 2")
    st.pyplot(fig2)

    # -------- Example 3 --------
st.subheader("Example 3: Line Plot with Grid Lines")
st.code("""
import matplotlib.pyplot as plt
import random as random

students = ["Jane", "Joe", "Beck", "Tom",
            "Sam", "Eva", "Samuel", "Jack",
            "Dana", "Ester", "Carla", "Steve",
            "Fallon", "Liam", "Culhane", "Candance",
            "Ana", "Mari", "Steffi", "Adam"]
marks = []
for i in range(0, len(students)):
    marks.append(random.randint(0, 101))
plt.figure(figsize=(14, 6))
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("CLASS RECORDS")
plt.plot(students, marks, 'm--')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
""")
if st.button("Run",key="3"):
    fig3, ax3 = plt.subplots(figsize=(12,6))
    ax3.plot(students, marks, 'm--')
    ax3.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax3.set_xlabel("Students")
    ax3.set_ylabel("Marks")
    ax3.set_title("CLASS RECORDS - Example 3")
    st.pyplot(fig3)


# ================= CONCLUSION =================
st.markdown("""
<hr>
<h4 style="color:green;">Conclusion</h4>

By combining:
- Line styles  
- Marker styles  
- Color codes  
- Grid lines  

we can create clear, attractive and informative line plots that help in identifying trends and patterns in data.
""", unsafe_allow_html=True)



#line plot
st.markdown("<a id='line'></a>", unsafe_allow_html=True)
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# ================= HEADING & THEORY =================
st.markdown("""
<h2 style="color:orange; text-align:center;"> Line Chart in Matplotlib - Python</h2>

A line chart (line plot) is used to show the relationship between two continuous variables by connecting data points with straight lines.  
It helps visualize trends, patterns and changes over time.

In Matplotlib, line charts are created using the <b>pyplot</b> sublibrary.

<hr>

<h4 style="color:deeppink;">Syntax</h4>
<code>plt.plot(x, y, color, linestyle, linewidth, marker)</code>

<ul>
<li>x → X-axis values</li>
<li>y → Y-axis values</li>
<li>color → Line color</li>
<li>linestyle → Line style</li>
<li>linewidth → Thickness</li>
<li>marker → Data point marker</li>
</ul>

<hr>
<h4 style="color:green;">Click the Run buttons to see output</h4>
""", unsafe_allow_html=True)
st.text("Consider a simple example where we visualise the weekly temperature using a line chart in Matplotlib")
st.code("""import matplotlib.pyplot as plt
import numpy as np

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperature = [22, 24, 23, 26, 25]

plt.plot(days, temperature, marker='o')
plt.title('Weekly Temperature')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.show()""")
if st.button("Run Example 1"):

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    temperature = [22, 24, 23, 26, 25]
    fig, ax = plt.subplots()
    ax.plot(days, temperature, marker='o')
    ax.set_title('Weekly Temperature')
    ax.set_xlabel('Days')
    ax.set_ylabel('Temperature (°C)')
    
    st.pyplot(fig)
# ================= EXAMPLE 1 =================
st.subheader("Example 1: Simple Line Plot")

st.code("""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = x * 2

plt.plot(x, y)
plt.show()
""")

if st.button("Run Example "):
    x = np.array([1,2,3,4])
    y = x * 2
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Simple Line Plot")
    st.pyplot(fig)


# ================= EXAMPLE 2 =================
st.subheader("Example 2: Line Plot with Labels and Title")

st.code("""
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot with Labels")
plt.show()
""")

if st.button("Run Example 2"):
    x = np.array([1,2,3,4])
    y = x * 2
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Line Plot with Labels")
    st.pyplot(fig)


# ================= EXAMPLE 3 =================
st.subheader("Example 3: Line Plot with Markers")

st.code("""
plt.plot(x, y, marker='o', linestyle='-', label='Data Points')
plt.legend()
plt.title("Line Plot with Markers")
plt.show()
""")

if st.button("Run Example 3"):
    x = np.array([1,2,3,4,5])
    y = [3,6,9,12,15]
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', label='Data Points')
    ax.legend()
    ax.set_title("Line Plot with Markers")
    st.pyplot(fig)


# ================= EXAMPLE 4 =================
st.subheader("Example 4: Line Plot with Grid")

st.code("""
plt.plot(x, y)
plt.grid(True)
plt.title("Line Plot with Grid")
plt.show()
""")

if st.button("Run Example 4"):
    x = [1,2,3,4]
    y = [1,4,9,16]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid(True)
    ax.set_title("Line Plot with Grid")
    st.pyplot(fig)


# ================= EXAMPLE 5 =================
st.subheader("Example 5: Line Chart with Annotations")

st.code("""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-')

for xi, yi in zip(x, y):
    plt.annotate(f'({xi}, {yi})',
                 (xi, yi),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')

plt.title('Line Chart with Annotations')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
""")

if st.button("Run Example 5"):
    x = [1,2,3,4,5]
    y = [2,4,6,8,10]
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    for xi, yi in zip(x, y):
        ax.annotate(f'({xi},{yi})',(xi,yi), textcoords="offset points", xytext=(0,10), ha='center')
    ax.set_title("Line Chart with Annotations")
    st.pyplot(fig)


# ================= EXAMPLE 6 =================
st.subheader("Example 6: Multiple Plots on Same Axis")

st.code("""
plt.plot(x, y, label='y=2x')
plt.plot(x1, y1, label='Second Line')
plt.legend()
plt.show()
""")

if st.button("Run Example 6"):
    x = np.array([1,2,3,4])
    y = x*2
    x1 = [2,4,6,8]
    y1 = [3,5,7,9]
    fig, ax = plt.subplots()
    ax.plot(x, y, label="y=2x")
    ax.plot(x1, y1, '-.', label="Second Line")
    ax.legend()
    ax.set_title("Multiple Lines on Same Axis")
    st.pyplot(fig)


# ================= EXAMPLE 7 =================
st.subheader("Example 7: Fill Area Between Two Lines")

st.code("""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = x * 2
y1 = [3, 5, 7, 9]

plt.plot(x, y, label='y = 2x')
plt.plot(x, y1, '-.', label='y1')

plt.fill_between(x, y, y1, color='green', alpha=0.4)

plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title("Filled Area Between Two Lines")
plt.legend()
plt.show()
""")

if st.button("Run Example 7"):
    x = np.array([1,2,3,4])
    y = x*2
    y1 = [3,5,7,9]
    fig, ax = plt.subplots()
    ax.plot(x, y, label="y=2x")
    ax.plot(x, y1, '-.', label="y1")
    ax.fill_between(x, y, y1, alpha=0.4)
    ax.legend()
    ax.set_title("Filled Area Between Two Lines")
    st.pyplot(fig)


# ================= EXAMPLE 8 =================
st.subheader("Example 8: Trigonometric Functions")

st.code("""
x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.legend()
plt.show()
""")

if st.button("Run Example 8"):
    x = np.linspace(0, 2*np.pi, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    fig, ax = plt.subplots()
    ax.plot(x, y_sin, label="sin(x)")
    ax.plot(x, y_cos, label="cos(x)")
    ax.legend()
    ax.set_title("Trigonometric Functions")
    st.pyplot(fig)


# ================= CONCLUSION =================
st.markdown("""
<hr>
<h4 style="color:green;">Conclusion</h4>
By using:
<ul>
<li>plot()</li>
<li>markers</li>
<li>grid()</li>
<li>legend()</li>
<li>fill_between()</li>
</ul>
we can create clear, attractive and informative line charts to analyze trends and patterns.
""", unsafe_allow_html=True)





#bar..........
st.markdown("<a id='bar'></a>", unsafe_allow_html=True)


# ================= HEADING & THEORY =================
st.markdown("""
<h2 style="color:orange; text-align:center;"> Bar Plot in Matplotlib</h2>


A bar plot uses rectangular bars to represent data categories, with bar length or height proportional to their values.  
It is used to compare discrete categories, where one axis represents categories and the other represents values.

<hr>

<h4 style="color:deeppink;">Syntax</h4>
<code>plt.bar(x, height, width, bottom, align)</code>

<ul>
<li><b>x</b> → Categories (fruits, students, etc.)</li>
<li><b>height</b> → Values</li>
<li><b>width</b> → Bar width (default = 0.8)</li>
<li><b>bottom</b> → Starting position</li>
<li><b>align</b> → center or edge</li>
</ul>

<hr>

<h4 style="color:green;">Click the Run buttons to see output</h4>
""", unsafe_allow_html=True)

#

# 🌙 Page config
st.set_page_config(page_title="Bar Plot", layout="centered")

# 🎨 Custom CSS for dark theme readable colors
st.markdown("""
<style>
.main-title {
    color: #00E5FF;
    text-align: center;
    font-size: 36px;
    font-weight: bold;
}
.sub-title {
    color: #FFD54F;
    font-size: 24px;
    margin-top: 20px;
}
.text {
    color: #E0E0E0;
    font-size: 18px;
}
.syntax {
    background-color: #1E1E1E;
    color: #00FFAB;
    padding: 12px;
    border-radius: 10px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# 🟢 Title
st.markdown('<div class="main-title"> Bar Plot (Bar Chart)</div>', unsafe_allow_html=True)

# 🟡 What is Bar Plot
st.markdown('<div class="sub-title">What is a Bar Plot?</div>', unsafe_allow_html=True)
st.markdown('<div class="text">A bar plot (or bar chart) is a graphical representation that uses rectangular bars to compare different categories. The height or length of each bar corresponds to the value it represents. The x-axis typically shows the categories, while the y-axis shows their values.</div>', unsafe_allow_html=True)

# 🟡 Parameters
st.markdown('<div class="sub-title">Parameters</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
• <b>x</b> : Categories (e.g., fruits)<br>
• <b>height</b> : Corresponding values (e.g., sales)<br>
• <b>width</b> : Width of bars (default = 0.8)<br>
• <b>bottom</b> : Baseline of bars (default = 0)<br>
• <b>align</b> : Alignment ('center' or 'edge')
</div>
""", unsafe_allow_html=True)

# 🟡 Why Use Bar Plot
st.markdown('<div class="sub-title">Why Use Bar Plots?</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Bar plots provide a clear and intuitive way to visualize categorical data. They help compare quantities across different groups such as survey results, sales data, or any discrete variables.</div>', unsafe_allow_html=True)

# 🟡 Syntax
st.markdown('<div class="sub-title">Syntax</div>', unsafe_allow_html=True)
st.markdown('<div class="syntax">plt.bar(x, height, width, bottom, align)</div>', unsafe_allow_html=True)

st.markdown("---")

# 📊 Example Bar Plot
st.markdown('<div class="sub-title">Example Bar Plot</div>', unsafe_allow_html=True)

fruits = ["Apple", "Banana", "Mango", "Orange"]
sales = [40, 25, 35, 30]

fig, ax = plt.subplots()
ax.bar(fruits, sales, color="#00E5FF", edgecolor="white")

ax.set_xlabel("Fruits", color="white")
ax.set_ylabel("Sales", color="white")
ax.set_title("Fruit Sales", color="#FFD54F")

ax.tick_params(colors="white")
fig.patch.set_facecolor("#0E1117")
ax.set_facecolor("#0E1117")

st.pyplot(fig)

# ================= EXAMPLE 1 =================
st.subheader("Example 1: Simple Bar Plot (Fruit Sales)")

st.code("""
import matplotlib.pyplot as plt

fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [400, 350, 300, 450]

plt.bar(fruits, sales)
plt.title('Fruit Sales')
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.show()
""")

if st.button("Run ",key="8"):
    fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sales = [400, 350, 300, 450]
    fig, ax = plt.subplots()
    ax.bar(fruits, sales)
    ax.set_title("Fruit Sales")
    ax.set_xlabel("Fruits")
    ax.set_ylabel("Sales")
    st.pyplot(fig)


# ================= EXAMPLE 2 =================
st.subheader("Example 2: Bar Plot with Color")

st.code("""
plt.bar(fruits, sales, color='violet')
plt.title('Fruit Sales')
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.show()
""")

if st.button("Run ",key="12"):
    fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sales = [400, 350, 300, 450]
    fig, ax = plt.subplots()
    ax.bar(fruits, sales, color='violet')
    ax.set_title("Fruit Sales (Violet)")
    ax.set_xlabel("Fruits")
    ax.set_ylabel("Sales")
    st.pyplot(fig)


# ================= EXAMPLE 3 =================
st.subheader("Example 3: Horizontal Bar Plot")

st.code("""
plt.barh(fruits, sales)
plt.title('Fruit Sales')
plt.xlabel('Sales')
plt.ylabel('Fruits')
plt.show()
""")

if st.button("Run ",key=13):
    fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sales = [400, 350, 300, 450]
    fig, ax = plt.subplots()
    ax.barh(fruits, sales)
    ax.set_title("Horizontal Bar Plot")
    ax.set_xlabel("Sales")
    ax.set_ylabel("Fruits")
    st.pyplot(fig)


# ================= EXAMPLE 4 =================
st.subheader("Example 4: Adjusting Bar Width")

st.code("""
plt.bar(fruits, sales, width=0.3)
plt.title('Fruit Sales')
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.show()
""")

if st.button("Run",key=14):
    fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sales = [400, 350, 300, 450]
    fig, ax = plt.subplots()
    ax.bar(fruits, sales, width=0.3)
    ax.set_title("Bar Width = 0.3")
    ax.set_xlabel("Fruits")
    ax.set_ylabel("Sales")
    st.pyplot(fig)


# ================= EXAMPLE 5 =================
st.subheader("Example 5: Multiple Bar Plot (Grouped Bar Chart)")

st.code("""
import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25

IT = [12, 30, 1, 8, 22]
ECE = [28, 6, 16, 5, 10]
CSE = [29, 3, 24, 25, 17]

br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, IT, width=barWidth, label='IT')
plt.bar(br2, ECE, width=barWidth, label='ECE')
plt.bar(br3, CSE, width=barWidth, label='CSE')

plt.xlabel('Year')
plt.ylabel('Students Passed')
plt.xticks([r + barWidth for r in range(len(IT))],
           ['2015','2016','2017','2018','2019'])

plt.legend()
plt.show()
""")

if st.button("Run ",key="15"):
    barWidth = 0.25
    IT = [12, 30, 1, 8, 22]
    ECE = [28, 6, 16, 5, 10]
    CSE = [29, 3, 24, 25, 17]

    br1 = np.arange(len(IT))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]

    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(br1, IT, width=barWidth, label='IT')
    ax.bar(br2, ECE, width=barWidth, label='ECE')
    ax.bar(br3, CSE, width=barWidth, label='CSE')

    ax.set_xlabel("Year")
    ax.set_ylabel("Students Passed")
    ax.set_xticks([r + barWidth for r in range(len(IT))])
    ax.set_xticklabels(['2015','2016','2017','2018','2019'])
    ax.legend()
    ax.set_title("Multiple Bar Plot")
    st.pyplot(fig)


# ================= EXAMPLE 6 =================
st.subheader("Example 6: Stacked Bar Plot")
st.text("""Stacked bar plots represent different groups on top of one another. The height of the bar depends on the resulting height of the combination of the results of the groups. It goes from the bottom to the value instead of going from zero to value. The following bar plot represents the contribution of boys and girls in the team.""")

st.code("""
import numpy as np
import matplotlib.pyplot as plt

boys = (20, 35, 30, 35, 27)
girls = (25, 32, 34, 20, 25)

ind = np.arange(5)
width = 0.35

p1 = plt.bar(ind, boys, width)
p2 = plt.bar(ind, girls, width, bottom=boys)

plt.ylabel('Contribution')
plt.title('Contribution by Teams')
plt.xticks(ind, ('T1','T2','T3','T4','T5'))
plt.legend((p1[0], p2[0]), ('boys','girls'))

plt.show()
""")

if st.button("Run ",key="16"):
    boys = (20, 35, 30, 35, 27)
    girls = (25, 32, 34, 20, 25)
    ind = np.arange(5)
    width = 0.35

    fig, ax = plt.subplots(figsize=(8,6))
    p1 = ax.bar(ind, boys, width)
    p2 = ax.bar(ind, girls, width, bottom=boys)

    ax.set_ylabel("Contribution")
    ax.set_title("Stacked Bar Plot")
    ax.set_xticks(ind)
    ax.set_xticklabels(('T1','T2','T3','T4','T5'))
    ax.legend((p1[0], p2[0]), ('boys','girls'))
    st.pyplot(fig)


# ================= CONCLUSION =================
st.markdown("""
<hr>
<h4 style="color:green;">Conclusion</h4>

Bar plots are useful for:
<ul>
<li>Comparing categories</li>
<li>Visualizing sales and survey data</li>
<li>Grouped comparisons</li>
<li>Stacked contributions</li>
</ul>

Using colors, width, stacked bars and legends makes bar charts more informative and attractive.
""", unsafe_allow_html=True)











#scatter
st.markdown("<a id='scatter'></a>",unsafe_allow_html=True)


st.set_page_config(page_title="Matplotlib Scatter", layout="wide")

st.markdown("""
<style>
.title {color:#00E5FF; font-size:36px; font-weight:bold; text-align:center;}
.sub {color:#FFD54F; font-size:22px; font-weight:bold;}
.text {color:#E0E0E0; font-size:18px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Matplotlib Scatter</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Scatter plots are one of the most fundamental tools for visualizing relationships between two numerical variables.</div>', unsafe_allow_html=True)

# ================= BASIC EXAMPLE =================
st.markdown('<div class="sub">Basic Scatter Plot</div>', unsafe_allow_html=True)
st.markdown('<div class="text">This example shows how to create a simple scatter plot using X and Y values.</div>', unsafe_allow_html=True)

st.code("""
x = np.array([12, 45, 7, 32, 89, 54, 23, 67, 14, 91])
y = np.array([99, 31, 72, 56, 19, 88, 43, 61, 35, 77])

plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
""")

if st.button("Show Output - Basic Scatter"):
    x = np.array([12,45,7,32,89,54,23,67,14,91])
    y = np.array([99,31,72,56,19,88,43,61,35,77])
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("Basic Scatter Plot")
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")
    st.pyplot(fig)

st.divider()


st.markdown("##  Scatter Plot Parameters")

data = {
    "Parameter": ["x, y", "s", "c", "marker", "cmap", "alpha", "edgecolors", "label"],
    "Description": [
        "Sequences of data points to plot",
        "Marker size (scalar or array-like)",
        "Marker color",
        "Shape of the marker",
        "Colormap for mapping numeric values to colors",
        "Transparency (0 = transparent, 1 = opaque)",
        "Color of marker edges",
        "Legend label for the dataset"
    ]
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

# ================= EXAMPLE 1 =================
st.markdown('<div class="sub">Example 1: Two Groups</div>', unsafe_allow_html=True)
st.markdown('<div class="text">We compare height and weight of two different groups using different colors.</div>', unsafe_allow_html=True)

st.code("""
 x1 = np.array([160,165,170,175,180,185,190,195,200,205])
    y1 = np.array([55,58,60,62,64,66,68,70,72,74])
    x2 = np.array([150,155,160,165,170,175,180,195,200,205])
    y2 = np.array([50,52,54,56,58,64,66,68,70,72])
plt.scatter(x1, y1, color='blue', label='Group 1')
plt.scatter(x2, y2, color='red', label='Group 2')
        plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    plt.title("Comparison of Height vs Weight")
    plt.legend()
""")

if st.button("Show Output - Example 1"):
    x1 = np.array([160,165,170,175,180,185,190,195,200,205])
    y1 = np.array([55,58,60,62,64,66,68,70,72,74])
    x2 = np.array([150,155,160,165,170,175,180,195,200,205])
    y2 = np.array([50,52,54,56,58,64,66,68,70,72])

    fig, ax = plt.subplots()
    ax.scatter(x1, y1, color='blue', label='Group 1')
    ax.scatter(x2, y2, color='red', label='Group 2')
    ax.set_xlabel("Height (cm)")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Comparison of Height vs Weight")
    ax.legend()
    st.pyplot(fig)

st.divider()

# ================= EXAMPLE 2 =================
st.markdown('<div class="sub">Example 2: Different Sizes and Colors</div>', unsafe_allow_html=True)
st.markdown('<div class="text">This example uses different marker sizes and colors.</div>', unsafe_allow_html=True)

st.code("""
         x = np.array([3,12,9,20,5,18,22,11,27,16])
    y = np.array([95,55,63,77,89,50,41,70,58,83])
    a = [20,50,100,200,500,1000,60,90,150,300]
    b = ['red','green','blue','purple','orange','black','pink','brown','yellow','cyan']
    plt.title("Scatter Plot with Varying Colors and Sizes")
plt.scatter(x, y, s=a, c=b, alpha=0.6, edgecolors='w')
""")

if st.button("Show Output - Example 2"):
    x = np.array([3,12,9,20,5,18,22,11,27,16])
    y = np.array([95,55,63,77,89,50,41,70,58,83])
    a = [20,50,100,200,500,1000,60,90,150,300]
    b = ['red','green','blue','purple','orange','black','pink','brown','yellow','cyan']

    fig, ax = plt.subplots()
    ax.scatter(x, y, s=a, c=b, alpha=0.6, edgecolors='w')
    ax.set_title("Scatter Plot with Varying Colors and Sizes")
    st.pyplot(fig)

st.divider()

# ================= EXAMPLE 3 =================
st.markdown('<div class="sub">Example 3: Bubble Plot</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Bubble plot where size of points represents magnitude.</div>', unsafe_allow_html=True)

st.code("""
        x = [1,2,3,4,5]
    y = [2,3,5,7,11]
    sizes = [30,80,150,200,300]
    plt.title("Bubble Plot Example")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
plt.scatter(x, y, s=sizes, alpha=0.5)
""")

if st.button("Show Output - Example 3"):
    x = [1,2,3,4,5]
    y = [2,3,5,7,11]
    sizes = [30,80,150,200,300]

    fig, ax = plt.subplots()
    ax.scatter(x, y, s=sizes, alpha=0.5, edgecolors='blue', linewidths=2)
    ax.set_title("Bubble Plot Example")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    st.pyplot(fig)

st.divider()

# ================= EXAMPLE 4 =================
st.markdown('<div class="sub">Example 4: Colormap</div>', unsafe_allow_html=True)
st.markdown('<div class="text">This example maps values to colors using a colormap.</div>', unsafe_allow_html=True)

st.code("""
         x = np.random.randint(50,150,100)
    y = np.random.randint(50,150,100)
    colors = np.random.rand(100)
    sizes = 20 * np.random.randint(10,100,100)
    plt.title("Scatter Plot with Colormap and Colorbar")
plt.scatter(x, y, c=colors, s=sizes, cmap='viridis')
plt.colorbar()
""")

if st.button("Show Output - Example 4"):
    x = np.random.randint(50,150,100)
    y = np.random.randint(50,150,100)
    colors = np.random.rand(100)
    sizes = 20 * np.random.randint(10,100,100)

    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, c=colors, s=sizes, cmap='viridis', alpha=0.7)
    plt.colorbar(sc, ax=ax, label="Color scale")
    ax.set_title("Scatter Plot with Colormap and Colorbar")
    st.pyplot(fig)

st.divider()

# ================= EXAMPLE 5 =================
st.markdown('<div class="sub">Example 5: Triangle Markers</div>', unsafe_allow_html=True)
st.markdown('<div class="text">This example uses triangle shaped markers.</div>', unsafe_allow_html=True)

st.code("""
        x = np.array([3,12,9,20,5,18,22,11,27,16])
    y = np.array([95,55,63,77,89,50,41,70,58,83])
   plt.title("Scatter Plot with Triangle Markers")
plt.scatter(x, y, marker='^', color='magenta', s=100)
""")

if st.button("Show Output - Example 5"):
    x = np.array([3,12,9,20,5,18,22,11,27,16])
    y = np.array([95,55,63,77,89,50,41,70,58,83])

    fig, ax = plt.subplots()
    ax.scatter(x, y, marker='^', color='magenta', s=100, alpha=0.7)
    ax.set_title("Scatter Plot with Triangle Markers")
    st.pyplot(fig)










#histogram

from matplotlib import colors
st.markdown("<a id='histogram'></a>",unsafe_allow_html=True)



st.set_page_config(page_title="Histogram in Matplotlib", layout="wide")

st.markdown("""
<style>
.title {color:#00E5FF; font-size:36px; font-weight:bold; text-align:center;}
.sub {color:#FFD54F; font-size:24px; font-weight:bold;}
.text {color:#E0E0E0; font-size:18px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Plotting Histogram in Python using Matplotlib</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Histograms are one of the most fundamental tools in data visualization. They provide a graphical representation of data distribution, showing how frequently each value or range of values occurs.</div>', unsafe_allow_html=True)

st.markdown('<div class="text">A histogram is a type of bar plot where:</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
• The X-axis represents intervals (called bins) of the data.<br>
• The Y-axis represents the frequency of values within each bin.<br>
• Unlike regular bar plots, histograms group data into bins.
</div>
""", unsafe_allow_html=True)

# ================= PARAMETERS TABLE =================
st.markdown('<div class="sub">Parameters of matplotlib.pyplot.hist()</div>', unsafe_allow_html=True)

import pandas as pd

data = {
    "Parameter": ["x","bins","density","range","histtype","align","weights","bottom","rwidth","color","label","log"],
    "Description": [
        "An array or sequence of numerical data.",
        "Number of bins or specific intervals.",
        "If True, normalises histogram to probability.",
        "Lower and upper limits of bins.",
        "Type of histogram: bar, barstacked, step, stepfilled.",
        "Bin alignment: left, right, mid.",
        "Weights for each data point.",
        "Baseline for bins.",
        "Relative width of bars (0–1).",
        "Color of bars.",
        "Label for legend.",
        "Uses logarithmic scale on Y-axis."
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.divider()

# ================= EXAMPLE 1 =================
st.markdown('<div class="sub">1. Basic Histogram</div>', unsafe_allow_html=True)

st.code("""
data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.show()
""")

if st.button("Show Output - Basic Histogram"):
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='skyblue', edgecolor='black')
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title('Basic Histogram')
    st.pyplot(fig)

st.divider()

# ================= EXAMPLE 2 =================
st.markdown('<div class="sub">2. Customized Histogram with Density Plot</div>', unsafe_allow_html=True)
import seaborn as sns
st.code("""
sns.histplot(data, bins=30, kde=True, color='lightgreen', edgecolor='red')
""")

if st.button("Show Output - Density Histogram"):
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    sns.histplot(data, bins=30, kde=True, color='lightgreen', edgecolor='red', ax=ax)
    ax.set_title("Customized Histogram with Density Plot")
    st.pyplot(fig)

st.divider()

# ================= EXAMPLE 3 =================
st.markdown('<div class="sub">3. Customized Histogram with Watermark</div>', unsafe_allow_html=True)

st.code("""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Creating dataset
np.random.seed(23685752)
N_points = 10000
n_bins = 20

# Creating distribution
x = np.random.randn(N_points)
y = 0.8 ** x + np.random.randn(N_points) + 25
legend = ['distribution']

# Creating figure and axes
fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)

# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    axs.spines[s].set_visible(False)

# Remove x, y ticks
axs.xaxis.set_ticks_position('none')
axs.yaxis.set_ticks_position('none')

# Add padding between axes and labels
axs.xaxis.set_tick_params(pad=5)
axs.yaxis.set_tick_params(pad=10)

# Add x, y gridlines (updated syntax)
axs.grid(visible=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

# Add text watermark
fig.text(0.9, 0.15, 'Jeeteshgavande30',
         fontsize=12,
         color='red',
         ha='right',
         va='bottom',
         alpha=0.7)

# Creating histogram
N, bins, patches = axs.hist(x, bins=n_bins)

# Setting color gradient
fracs = ((N ** (1 / 5)) / N.max())
norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# Adding extra features
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(legend)
plt.title('Customized Histogram with Watermark')

# Show plot
plt.show()
""")

if st.button("Show Output - Watermark Histogram"):
    np.random.seed(1)
    x = np.random.randn(10000)
    fig, ax = plt.subplots(figsize=(8,5))
    N, bins, patches = ax.hist(x, bins=20)
    fracs = ((N**(1/5))/N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    fig.text(0.9,0.15,'Watermark',color='red',alpha=0.7)
    ax.set_title("Customized Histogram with Watermark")
    st.pyplot(fig)

st.divider()

# ================= EXAMPLE 4 =================
st.markdown('<div class="sub">4. Multiple Histograms with Subplots</div>', unsafe_allow_html=True)

st.code("""
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for multiple histograms
data1 = np.random.randn(1000)
data2 = np.random.normal(loc=3, scale=1, size=1000)

# Creating subplots with multiple histograms
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

axes[0].hist(data1, bins=30, color='Yellow', edgecolor='black')
axes[0].set_title('Histogram 1')

axes[1].hist(data2, bins=30, color='Pink', edgecolor='black')
axes[1].set_title('Histogram 2')

# Adding labels and title
for ax in axes:
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')

# Adjusting layout for better spacing
plt.tight_layout()

# Display the figure
plt.show()
""")

if st.button("Show Output - Subplots"):
    data1 = np.random.randn(1000)
    data2 = np.random.normal(loc=3, size=1000)

    fig, axes = plt.subplots(1,2, figsize=(10,4))
    axes[0].hist(data1, bins=30, color='yellow', edgecolor='black')
    axes[0].set_title("Histogram 1")

    axes[1].hist(data2, bins=30, color='pink', edgecolor='black')
    axes[1].set_title("Histogram 2")

    st.pyplot(fig)

st.divider()

# ================= EXAMPLE 5 =================
st.markdown('<div class="sub">5. Stacked Histogram</div>', unsafe_allow_html=True)

st.code("""
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for stacked histograms
data1 = np.random.randn(1000)
data2 = np.random.normal(loc=3, scale=1, size=1000)

# Creating a stacked histogram
plt.hist([data1, data2], bins=30, stacked=True, color=['cyan', 'Purple'], edgecolor='black')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Stacked Histogram')

# Adding legend
plt.legend(['Dataset 1', 'Dataset 2'])

# Display the plot
plt.show()
""")

if st.button("Show Output - Stacked Histogram"):
    data1 = np.random.randn(1000)
    data2 = np.random.normal(loc=3, size=1000)

    fig, ax = plt.subplots()
    ax.hist([data1, data2], bins=30, stacked=True, color=['cyan','purple'], edgecolor='black')
    ax.set_title("Stacked Histogram")
    ax.legend(["Dataset 1","Dataset 2"])
    st.pyplot(fig)

st.divider()

# ================= EXAMPLE 6 =================
st.markdown('<div class="sub">6. 2D Histogram (Hexbin Plot)</div>', unsafe_allow_html=True)

st.code("""
import matplotlib.pyplot as plt
import numpy as np

# Generate random 2D data for hexbin plot
x = np.random.randn(1000)
y = 2 * x + np.random.normal(size=1000)

# Creating a 2D histogram (hexbin plot)
plt.hexbin(x, y, gridsize=30, cmap='Blues')

# Adding labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('2D Histogram (Hexbin Plot)')

# Adding colorbar
plt.colorbar(label='Counts')

plt.show()
""")

if st.button("Show Output - 2D Histogram"):
    x = np.random.randn(1000)
    y = 2*x + np.random.randn(1000)

    fig, ax = plt.subplots()
    hb = ax.hexbin(x, y, gridsize=30, cmap='Blues')
    fig.colorbar(hb, ax=ax, label="Counts")
    ax.set_title("2D Histogram (Hexbin Plot)")
    st.pyplot(fig)



#pie................
st.markdown("<a id='pie'></a>",unsafe_allow_html=True)
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pie Chart in Matplotlib", layout="wide")

# ---------------- TITLE ----------------
st.markdown("<h1 style='color:#00BFFF;text-align:center;'> Pie Chart in Matplotlib</h1>", unsafe_allow_html=True)

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:#FFD700;'>Why Use Pie Charts?</h2>", unsafe_allow_html=True)

st.write("""
Pie charts provide a visual representation of data that makes it easy to compare parts of a whole.  
They are useful for:
- Displaying relative proportions or percentages  
- Summarizing categorical data  
- Highlighting significant differences between categories  

However, pie charts can become cluttered if there are too many categories.
A well-designed pie chart improves data understanding.
""")

st.markdown("<h2 style='color:#FFD700;'>Basic Structure of Pie Chart</h2>", unsafe_allow_html=True)

st.write("""
A pie chart consists of slices that represent different categories.
Each slice size is proportional to the data value.

Components:
- Data
- Labels
- Colors (optional)
""")

st.markdown("<h2 style='color:#FFD700;'>Syntax</h2>", unsafe_allow_html=True)

st.code("matplotlib.pyplot.pie(data, explode=None, labels=None, colors=None, autopct=None, shadow=False)")

# ---------------- PARAMETERS TABLE ----------------
st.markdown("<h2 style='color:#FFD700;'>Parameters</h2>", unsafe_allow_html=True)

st.table({
    "Parameter": ["data", "labels", "colors", "autopct", "shadow"],
    "Description": [
        "Array of data values",
        "Category names",
        "Colors for slices",
        "Display percentage values",
        "Add shadow to pie chart"
    ]
})

# ---------------- SIMPLE PIE CHART ----------------
st.markdown("<h2 style='color:#00FF7F;'>Simple Pie Chart</h2>", unsafe_allow_html=True)

st.code("""
cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]

plt.pie(data, labels=cars)
plt.show()
""")

if st.button("Show Simple Pie Chart"):
    cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
    data = [23, 17, 35, 29, 12, 41]

    fig, ax = plt.subplots()
    ax.pie(data, labels=cars, autopct="%1.1f%%")
    ax.set_title("Simple Pie Chart")
    st.pyplot(fig)

# ---------------- CUSTOM PIE CHART ----------------
st.markdown("<h2 style='color:#00FF7F;'>Customized Pie Chart</h2>", unsafe_allow_html=True)

st.code("""
# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']

data = [23, 17, 35, 29, 12, 41]


# Creating explode data
explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0)

# Creating color parameters
colors = ("orange", "cyan", "brown",
          "grey", "indigo", "beige")

# Wedge properties
wp = {'linewidth': 1, 'edgecolor': "green"}

# Creating autocpt arguments


def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


# Creating plot
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct=lambda pct: func(pct, data),
                                  explode=explode,
                                  labels=cars,
                                  shadow=True,
                                  colors=colors,
                                  startangle=90,
                                  wedgeprops=wp,
                                  textprops=dict(color="magenta"))

# Adding legend
ax.legend(wedges, cars,
          title="Cars",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Customizing pie chart")

# show plot
plt.show()
""")

if st.button("Show Customized Pie Chart"):
    cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
    data = [23, 17, 35, 29, 12, 41]

    explode = (0.1,0,0.2,0.3,0,0)
    colors = ("orange","cyan","brown","grey","indigo","beige")

    fig, ax = plt.subplots()
    ax.pie(data, labels=cars, explode=explode, colors=colors,
           autopct="%1.1f%%", shadow=True, startangle=90)
    ax.legend(title="Cars")
    ax.set_title("Customized Pie Chart")
    st.pyplot(fig)

# ---------------- NESTED PIE CHART ----------------
st.markdown("<h2 style='color:#00FF7F;'>Nested Pie Chart (Donut Chart)</h2>", unsafe_allow_html=True)

st.code("""
# Import libraries
from matplotlib import pyplot as plt
import numpy as np


# Creating dataset
size = 6
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']

data = np.array([[23, 16], [17, 23],
                 [35, 11], [29, 33],
                 [12, 27], [41, 42]])

# normalizing data to 2 pi
norm = data / np.sum(data)*2 * np.pi

# obtaining ordinates of bar edges
left = np.cumsum(np.append(0,
                           norm.flatten()[:-1])).reshape(data.shape)

# Creating color scale
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(6)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9,
                              10, 12, 13, 15,
                              17, 18, 20]))

# Creating plot
fig, ax = plt.subplots(figsize=(10, 7),
                       subplot_kw=dict(polar=True))

ax.bar(x=left[:, 0],
       width=norm.sum(axis=1),
       bottom=1-size,
       height=size,
       color=outer_colors,
       edgecolor='w',
       linewidth=1,
       align="edge")

ax.bar(x=left.flatten(),
       width=norm.flatten(),
       bottom=1-2 * size,
       height=size,
       color=inner_colors,
       edgecolor='w',
       linewidth=1,
       align="edge")

ax.set(title="Nested pie chart")
ax.set_axis_off()

# show plot
plt.show()
""")

if st.button("Show Nested Pie Chart"):
    cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
    data = np.array([[23,16],[17,23],[35,11],[29,33],[12,27],[41,42]])

    fig, ax = plt.subplots()
    size = 0.3

    ax.pie(data.sum(axis=1), radius=1, labels=cars, autopct="%1.1f%%")
    ax.pie(data.flatten(), radius=1-size)

    centre_circle = plt.Circle((0,0),0.5,fc='black')
    fig.gca().add_artist(centre_circle)

    ax.set_title("Nested Pie Chart")
    st.pyplot(fig)

# ---------------- CONCLUSION ----------------
st.markdown("<h2 style='color:#FFD700;'>Conclusion</h2>", unsafe_allow_html=True)

st.write("""
Using Matplotlib's plt.pie() function, we can create:
- Simple pie charts
- Customized pie charts
- Nested pie charts

Pie charts help visualize proportions clearly and effectively.
They are useful for presentations, reports, and dashboards.
""")








st.markdown("<a id='3'></a>",unsafe_allow_html=True)
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

st.set_page_config(page_title="3D Plotting in Matplotlib", layout="wide")

st.markdown("<h1 style='color:#00BFFF;text-align:center;'>📊 3D Plotting in Matplotlib</h1>", unsafe_allow_html=True)

# ---------------- THEORY ----------------
st.markdown("<h2 style='color:#FFD700;'>Introduction</h2>", unsafe_allow_html=True)
st.write("""
Visualizing data involving three variables often requires three-dimensional plotting.  
Matplotlib provides 3D plotting through the mpl_toolkits.mplot3d toolkit.
""")

st.markdown("<h2 style='color:#FFD700;'>Basic 3D Axes Setup</h2>", unsafe_allow_html=True)
st.code("""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)

ax.plot3D(x, y, z, 'green')
ax.set_title('3D Line Plot')
plt.show()
""")

# ---------------- 1. 3D LINE PLOT ----------------
st.markdown("<h2 style='color:#00FF7F;'>1. 3D Line Plot</h2>", unsafe_allow_html=True)
st.write("A 3D line plot connects points in 3D space and shows continuous paths.")

st.code("""
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)

ax.plot3D(x, y, z, 'green')
""")

if st.button("Show 3D Line Plot"):
    z = np.linspace(0, 1, 100)
    x = z * np.sin(25 * z)
    y = z * np.cos(25 * z)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z, 'green')
    ax.set_title("3D Line Plot")
    st.pyplot(fig)

# ---------------- 2. 3D SCATTER PLOT ----------------
st.markdown("<h2 style='color:#00FF7F;'>2. 3D Scatter Plot</h2>", unsafe_allow_html=True)
st.write("A 3D scatter plot displays individual points in 3D space.")
st.code("""fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
c = x + y  # Color array based on x and y

ax.scatter(x, y, z, c=c)
ax.set_title('3D Scatter Plot')
plt.show()""")
if st.button("Show 3D Scatter Plot"):
    z = np.linspace(0, 1, 100)
    x = z * np.sin(25 * z)
    y = z * np.cos(25 * z)
    c = x + y

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(x, y, z, c=c)
    ax.set_title("3D Scatter Plot")
    st.pyplot(fig)

# ---------------- 3. SURFACE PLOT ----------------
st.markdown("<h2 style='color:#00FF7F;'>3. Surface Plot</h2>", unsafe_allow_html=True)
st.write("Surface plots visualize smooth surfaces for functions of two variables.")
st.code("""x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x**2 + y**3)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='green')
ax.set_title('Surface Plot')
plt.show()""")
if st.button("Show Surface Plot"):
    x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
    y = x.copy().T
    z = np.cos(x**2 + y**3)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='green')
    ax.set_title("Surface Plot")
    st.pyplot(fig)

# ---------------- 4. WIREFRAME PLOT ----------------
st.markdown("<h2 style='color:#00FF7F;'>4. Wireframe Plot</h2>", unsafe_allow_html=True)
st.write("Wireframe plots show the skeleton of a surface.")
st.code("""def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-1, 5, 10)
y = np.linspace(-1, 5, 10)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='green')
ax.set_title('Wireframe Plot')
plt.show()""")
if st.button("Show Wireframe Plot"):
    def f(x, y):
        return np.sin(np.sqrt(x**2 + y**2))

    x = np.linspace(-1, 5, 10)
    y = np.linspace(-1, 5, 10)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z, color='green')
    ax.set_title("Wireframe Plot")
    st.pyplot(fig)

# ---------------- 5. 3D CONTOUR PLOT ----------------
st.markdown("<h2 style='color:#00FF7F;'>5. 3D Contour Plot</h2>", unsafe_allow_html=True)
st.write("3D contour plots highlight elevation changes.")
st.code("""def fun(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)
X, Y = np.meshgrid(x, y)
Z = fun(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.8)

ax.set_title('3D Contour Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()""")
if st.button("Show 3D Contour Plot"):
    def fun(x, y):
        return np.sin(np.sqrt(x**2 + y**2))

    x = np.linspace(-10, 10, 40)
    y = np.linspace(-10, 10, 40)
    X, Y = np.meshgrid(x, y)
    Z = fun(X, Y)

    fig = plt.figure(figsize=(8,6))
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.8)
    ax.set_title("3D Contour Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    st.pyplot(fig)

# ---------------- 6. TRIANGULATION SURFACE ----------------
st.markdown("<h2 style='color:#00FF7F;'>6. Surface Triangulation Plot</h2>", unsafe_allow_html=True)
st.write("Triangulation plots build surfaces from triangular meshes.")
st.code("""from matplotlib.tri import Triangulation

def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

tri = Triangulation(X.ravel(), Y.ravel())

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(tri, Z.ravel(), cmap='cool', edgecolor='none', alpha=0.8)

ax.set_title('Surface Triangulation Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()""")
if st.button("Show Surface Triangulation Plot"):
    def f(x, y):
        return np.sin(np.sqrt(x**2 + y**2))

    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    tri = Triangulation(X.ravel(), Y.ravel())

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(tri, Z.ravel(), cmap='cool', edgecolor='none', alpha=0.8)
    ax.set_title("Surface Triangulation Plot")
    st.pyplot(fig)

# ---------------- 7. MOBIUS STRIP ----------------
st.markdown("<h2 style='color:#00FF7F;'>7. Möbius Strip Plot</h2>", unsafe_allow_html=True)
st.write("A Möbius strip is a one-sided surface with a twist.")
st.code("""R = 2
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(-1, 1, 100)
u, v = np.meshgrid(u, v)

x = (R + v * np.cos(u / 2)) * np.cos(u)
y = (R + v * np.cos(u / 2)) * np.sin(u)
z = v * np.sin(u / 2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Möbius Strip')

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

plt.show()""")
if st.button("Show Möbius Strip Plot"):
    R = 2
    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(-1, 1, 100)
    u, v = np.meshgrid(u, v)

    x = (R + v * np.cos(u / 2)) * np.cos(u)
    y = (R + v * np.cos(u / 2)) * np.sin(u)
    z = v * np.sin(u / 2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, alpha=0.5)
    ax.set_title("Möbius Strip")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    st.pyplot(fig)

# ---------------- CONCLUSION ----------------
st.markdown("<h2 style='color:#FFD700;'>Conclusion</h2>", unsafe_allow_html=True)
st.write("""
Using Matplotlib's 3D plotting tools, we can visualize:
- Line plots
- Scatter plots
- Surface plots
- Wireframes
- Contours
- Triangulated surfaces
- Möbius strips

These plots help understand complex relationships between three variables.
""")















#Dashboard
st.markdown("<a id='dashboard'></a>",unsafe_allow_html=True)
st.code("""np.random.seed(0)
sales = pd.DataFrame({
    'month': pd.date_range('2025-01', periods=12, freq='M'),
    'revenue': np.random.randint(1000, 5000, 12).cumsum(),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 12)
})

fig = plt.figure(figsize=(12, 10), layout='constrained')
gs = fig.add_gridspec(2, 2, height_ratios=[3,1])

# Line plot
ax1 = fig.add_subplot(gs[0, :])
for region in sales['region'].unique():
    data = sales[sales['region'] == region]
    ax1.plot(data['month'], data['revenue'], marker='o', label=region)
ax1.set_title('Monthly Revenue by Region')
ax1.set_ylabel('Revenue ($)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Histogram
ax2 = fig.add_subplot(gs[1, 0])
ax2.hist(sales['revenue'], bins=5, color='skyblue', edgecolor='black')
ax2.set_title('Revenue Distribution')
ax2.set_xlabel('Revenue ($)')
ax2.set_ylabel('Frequency')

# Pie chart
ax3 = fig.add_subplot(gs[1, 1])
region_sum = sales.groupby('region')['revenue'].sum()
ax3.pie(region_sum.values, labels=region_sum.index, autopct='%1.1f%%')
ax3.set_title('Revenue Share by Region')

plt.suptitle('Sales Dashboard - 2025', fontsize=16)
plt.tight_layout()
plt.show()
""")

# Set page config
st.set_page_config(page_title="Seaborn Sales Dashboard", layout="wide")

# --- Step 1: Data Preparation ---
np.random.seed(0)
sales = pd.DataFrame({
    'month': pd.date_range('2025-01', periods=12, freq='ME'), # Updated freq to 'ME' for newer pandas
    'revenue': np.random.randint(1000, 5000, 12).cumsum(),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 12)
})

st.title("🚀 Interactive Sales Dashboard (Seaborn Version)")
st.write("This dashboard converts your Matplotlib code into a modern Seaborn visualization.")

# --- Step 2: Dashboard Layout ---
# Using columns to create a balanced look
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Monthly Revenue Trends")
    # Set the style to Seaborn's darkgrid for a modern look
    sns.set_theme(style="whitegrid")
    
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    
    # Seaborn lineplot handles the 'hue' (region) automatically!
    sns.lineplot(data=sales, x='month', y='revenue', hue='region', marker='o', palette='viridis', ax=ax1)
    
    ax1.set_title('Cumulative Revenue Growth by Region', fontsize=14)
    ax1.tick_params(axis='x', rotation=45)
    st.pyplot(fig1)

with col2:
    st.subheader("Regional Performance")
    # Pie Chart (Seaborn doesn't have a direct pie chart, so we use Matplotlib with Seaborn colors)
    region_sum = sales.groupby('region')['revenue'].sum()
    colors = sns.color_palette('pastel')[0:len(region_sum)]
    
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    ax2.pie(region_sum.values, labels=region_sum.index, autopct='%1.1f%%', colors=colors, startangle=140)
    ax2.set_title('Revenue Share %')
    st.pyplot(fig2)

st.divider()

# Lower row for distribution
st.subheader("Global Revenue Distribution")
fig3, ax3 = plt.subplots(figsize=(12, 4))

# Using sns.histplot for a much cleaner histogram with a KDE curve
sns.histplot(sales['revenue'], bins=5, kde=True, color='skyblue', edgecolor='black', ax=ax3)
ax3.set_title('Distribution of Monthly Revenue Across All Regions')

st.pyplot(fig3)

# --- Step 3: Show Data ---
with st.expander("🔍 View Raw Sales Data"):
    st.dataframe(sales, use_container_width=True)



st.markdown("<a id='pr'></a>",unsafe_allow_html=True)
st.markdown("[Click here for Practice  Basic Questions ](https://www.w3resource.com/graphics/matplotlib/basic/index.php#google_vignette)")
st.markdown("[Click here for Practice  Bar Questions 📘](https://www.w3resource.com/graphics/matplotlib/barchart/index.php)")
st.markdown("[Click here for Practice  Pie Questions 📘](https://www.w3resource.com/graphics/matplotlib/piechart/index.php)")
st.markdown("[Click here for Practice  Scatter Questions 📘](https://www.w3resource.com/graphics/matplotlib/scatter/index.php))")

st.markdown("<a id='a'></a>",unsafe_allow_html=True)
st.markdown("<a id='about'></a>",unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<div style="
background-color:#0e1117;
padding:25px;
border-radius:15px;
color:white;
text-align:center;
">

<img src="https://www.python.org/static/community_logos/python-logo.png" width="120">

<h2>👩‍💻 Author: Sanya Katiyar</h2>

<p>Python & Data Science Learner 🚀 <br>
This application is built using <b>Streamlit</b>.</p>

<h4>🎓 Guided by: Dr Aditya Khamparia Sir</h4>
<p>(Project idea given by my respected teacher)</p>

<hr style="border:1px solid gray;">

<h3>📞 Contact Me</h3>

<p>
<a href="https://www.linkedin.com/feed/">🔗 LinkedIn</a> | 
<a href="https://github.com/Sanya-Katiyar-Eng" target="_blank">💻 GitHub</a> | 
<a href="https://www.youtube.com/" target="_blank">▶️ YouTube</a>
</p>

<p>📱 Phone: +91-7905639342</p>
<p>📧 Email:sanyakatiyar01@gmail.com</p>

<hr style="border:1px solid gray;">

<p style="color:lightgray;">© 2026 Sanya Katiyar | All Rights Reserved</p>

</div>
""", unsafe_allow_html=True)




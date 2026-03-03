import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="StudyNest", layout="wide")

# ---------------- BACK BUTTON ----------------
if st.button("⬅ Back to Home"):
    st.switch_page("main.py")

# ---------------- CSS STYLE ----------------
st.markdown("""
<style>
/* 🌟 Black & Gold Animated Background */
.stApp {
    background: linear-gradient(-45deg, #000000, #1a1a1a, #b8860b, #ffd700);
    background-size: 300% 300%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ✨ Title */
.fade-text {
    text-align: center;
    font-size: 48px;
    color: gold;
    animation: fadeIn 2.5s ease-in;
    margin-top: 40px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #f5f5f5;
    margin-bottom: 40px;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Banner */
.top-banner {
    background: linear-gradient(to right, #b8860b, #ffd700);
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

st.markdown('<h1 style="  text-align: center;">Pandas</h1>', unsafe_allow_html=True)
st.text("pandas is a fast ,powerful,flexible and easy to use ope source data analysis and manlpulation tool,built on top of the python programming language.")

st.markdown('<h3 style=" color:yellow; text-align: center;">Pandas Installation</h3>', unsafe_allow_html=True)
st.code("pip install pandas")
st.markdown('<h3 style=" color:yellow; text-align: center;">Importing Pandas</h3>', unsafe_allow_html=True)
st.code("import pandas as pd")
st.markdown('<h3 style=" color:yellow; text-align: center;">Pandas Series</h3>', unsafe_allow_html=True)
st.text("A Pandas Series is like a column in a table. It is a 1-D array holding data of any type.")
st.markdown('<h3 style=" color:pink; ">Series using String</h3>', unsafe_allow_html=True)
st.code("""import numpy as np
        import pandas as pd
        country=['India','Pakistan','USA','Nepal']
        pd.Series(country)""")
if st.button("Run",key="1"):

    country=['India','Pakistan','USA','Nepal']
    s=pd.Series(country)
    st.code(s)

st.markdown('<h4 style=" color:pink; ">Series using Integer</h4>', unsafe_allow_html=True)

st.code("""import numpy as np
import pandas as pd
num = [10, 20, 30, 40]
pd.Series(num)
""")

if st.button("Run", key="2"):
    num = [10, 20, 30, 40]
    s = pd.Series(num)
    st.code(s.to_string() + f"\ndtype: {s.dtype}")
st.markdown('<h4 style=" color:pink; ">Series with Custom Index</h4>', unsafe_allow_html=True)

st.code("""import numpy as np
import pandas as pd
country = ['India','Pakistan','USA','Nepal']
index = ['a','b','c','d']
pd.Series(country, index=index)
""")

if st.button("Run", key="3"):
    country = ['India','Pakistan','USA','Nepal']
    index = ['a','b','c','d']
    s = pd.Series(country, index=index)
    st.code(s.to_string() + f"\ndtype: {s.dtype}")

st.markdown('<h4 style=" color:pink; ">Series with Name</h4>', unsafe_allow_html=True)

st.code("""import numpy as np
import pandas as pd
marks = [85, 90, 88, 92]
pd.Series(marks, name="Student Marks")
""")

if st.button("Run", key="4"):
    marks = [85, 90, 88, 92]
    s = pd.Series(marks, name="Student Marks")

    output = s.to_string() + f"\nName: {s.name}, dtype: {s.dtype}"
    st.code(output)


st.markdown('<h3 style=" color:pink; ">Series from Dictionary</h3>', unsafe_allow_html=True)
st.text("when a Pandas Series is converted to a dictionary using the to_dict() method,the resulting dictionary has the same keys and values as the series.    The index value of the Series become the key in the dicctionary,and the corresponding values become the values in the dictionary.")
st.code("""import numpy as np
import pandas as pd
data = {'a':10, 'b':20, 'c':30, 'd':40}
pd.Series(data)
""")

if st.button("Run", key="5"):
    data = {'a':10, 'b':20, 'c':30, 'd':40}
    s = pd.Series(data)
    st.code(s.to_string() + f"\ndtype: {s.dtype}")

st.markdown('<h3 style=" color:yellow;text-align: center; ">Series Attributes</h3>', unsafe_allow_html=True)
st.text("size = Return the number of elements in the Series")
st.code("""import pandas as pd
import numpy as np

marks = [85, 90, 88, 92]
s = pd.Series(marks)
s.size
""")

# Run button
if st.button("Run", key="size"):
    marks = [85, 90, 88, 92]
    s = pd.Series(marks)

    result = s.size
    st.code(result)

st.text("name = Return the name of the Series")

st.code("""import pandas as pd
marks = [85, 90, 88, 92]
s = pd.Series(marks, name="Student Marks")
s.name
""")

if st.button("Run", key="name"):
    s = pd.Series([85,90,88,92], name="Student Marks")
    st.code(s.name)



st.text("shape = Return a tuple representing the dimensions of the Series")

st.code("""import pandas as pd
marks = [85, 90, 88, 92]
s = pd.Series(marks)
s.shape
""")

if st.button("Run", key="shape"):
    s = pd.Series([85,90,88,92])
    st.code(s.shape)

st.text("index = Return the index of the Series")

st.code("""import pandas as pd
marks = [85, 90, 88, 92]
s = pd.Series(marks)
s.index
""")

if st.button("Run", key="index"):
    s = pd.Series([85,90,88,92])
    st.code(s.index)

st.text("dtype = Return the data type of the Series")

st.code("""import pandas as pd
marks = [85, 90, 88, 92]
s = pd.Series(marks)
s.dtype
""")

if st.button("Run", key="dtype"):
    s = pd.Series([85, 90, 88, 92])
    st.code(s.dtype)


st.text("is_unique = Return True if all values in Series are unique, else False")

st.code("""import pandas as pd
marks = [85, 90, 88, 92, 90]
s = pd.Series(marks)
s.is_unique
""")

if st.button("Run", key="is_unique"):
    s = pd.Series([85, 90, 88, 92, 90])
    st.code(s.is_unique)
    
st.text("index = Return the index labels of the Series")

st.code("""import pandas as pd
marks = [85, 90, 88, 92]
s = pd.Series(marks)
s.index
""")

if st.button("Run", key="index"):
    s = pd.Series([85, 90, 88, 92])
    st.code(s.index)




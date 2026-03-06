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






    #.......................................................

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
    
st.text("Value : Returns the data contained in the Series as a Numpy array")

st.code("""import pandas as pd
marks = [85, 90, 88, 92, 90,dtype='int64']
s = pd.Series(marks)
s.values
""")

#..............................................
st.markdown('<h3 style=" color:yellow;text-align: center; ">Series Using read_csv</h3>', unsafe_allow_html=True)
st.code("""sub=pd.read_csv("paste link of data")""")
st.markdown('<b style=" color:yellow;">Pandas.read_csv</b>', unsafe_allow_html=True)
st.text("Automatically converts everything into data frames not in series.")
st.code("type(sub)")
st.text("Output :")
st.code("pandas.core.frame.DataFrame")
st.code("sub.head(5)")
st.text("Output :")
d={0:34,1:44,2:32,3:55,4:67}
st.table(d)
st.markdown('<b style=" color:yellow;">To convert data into series</b>', unsafe_allow_html=True)
st.text("""we have to apply a parameter called as "Squeeze" is equals to True.""")
st.code("""sub=pd.read_csv("subs.csv",sequeeze=True)
        type(sub)""")
st.text("Output :")
st.code("pandas.core.series.Series")
st.code("""#with two column
        movies=pd.read_csv("bollywood.csv",index_col="movie",sequeeze=True)
        movies""")
st.text("Output")
m={'movies':"values ",
   "Uri:The Surgical Strike":"Vicky Kaushal",
   "Battalion 609":"Vicky Ahuja",
   "The Accidental Prime Ministre (film)":"Anupam",
   "Why cheat India":"Emraan Hashmi"}
st.table(m)

#................................
st.markdown('<h3 style=" color:yellow;text-align: center; ">Series Methods</h3>', unsafe_allow_html=True)
st.text("head(n):Return the first n element of the Series.")
st.code("sub.head()")
st.text("tail(n):Return the last n element of the Series.")
st.code("sub.tail()")
st.text("sample(): Gives random data")
st.code("sub.sample()")
st.text("value_counts: Return a Series containing the counts of unique values in the Series.")
st.code("sub.value_counts()")
st.text("sort_values(): return a sorted Series by values")
st.code("sub.sort_values()")

st.code("sub.sort_values(ascending=False).head(1).values[0]")
st.code("""#For permanenet Changes use Inplace
        sub.sort_values(inplace=True)""")

st.code("""#sort by index
        sub.sort_index()
        # for ascending
        sub.sort_index(ascending=False) """)

st.markdown('<h3 style=" color:yellow;text-align: center; ">Series Math Methods</h3>', unsafe_allow_html=True)












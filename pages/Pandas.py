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

st.markdown('<h3 style="color:yellow;text-align:center;">Series Methods</h3>', unsafe_allow_html=True)

# -------- Dataset --------
st.code("""#Dataset
        data = [45, 60, 75, 60, 90, 30, 75, 60, 85, 40]
sub = pd.Series(data, name="Marks")
""")
data = [45, 60, 75, 60, 90, 30, 75, 60, 85, 40]
sub = pd.Series(data, name="Marks")
st.subheader("Original Series")
st.write(sub)


# =================================================
# HEAD
# =================================================
st.markdown('<h4 style="color:pink;">head(n)</h4>', unsafe_allow_html=True)
st.text("Return the first n elements of the Series.")

st.code("""
sub.head(3)
""")

if st.button("Run head()", key="head"):
    
    st.subheader("head(3) Output")
    st.write(sub.head(3))


# =================================================
# TAIL
# =================================================
st.markdown('<h4 style="color:pink;">tail(n)</h4>', unsafe_allow_html=True)
st.text("Return the last n elements of the Series.")

st.code("""
sub.tail(3)
""")

if st.button("Run tail()", key="tail"):
    
    st.subheader("tail(3) Output")
    st.write(sub.tail(3))


# =================================================
# SAMPLE
# =================================================
st.markdown('<h4 style="color:pink;">sample()</h4>', unsafe_allow_html=True)
st.text("Return random elements from the Series.")

st.code("""
sub.sample(3)
""")

if st.button("Run sample()", key="sample"):
    
    st.subheader("sample(3) Output")
    st.write(sub.sample(3))


# =================================================
# VALUE COUNTS
# =================================================
st.markdown('<h4 style="color:pink;">value_counts()</h4>', unsafe_allow_html=True)
st.text("Return counts of unique values in the Series.")

st.code("""
sub.value_counts()
""")

if st.button("Run value_counts()", key="value"):
    
    st.subheader("value_counts() Output")
    st.write(sub.value_counts())


# =================================================
# SORT VALUES
# =================================================
st.markdown('<h4 style="color:pink;">sort_values()</h4>', unsafe_allow_html=True)
st.text("Return a sorted Series by values.")

st.code("""
sub.sort_values()
""")

if st.button("Run sort_values()", key="sort"):
    
    st.subheader("Sorted Values")
    st.write(sub.sort_values())


# =================================================
# HIGHEST VALUE
# =================================================
st.markdown('<h4 style="color:pink;">Highest Value</h4>', unsafe_allow_html=True)
st.text("Return the highest value from the Series.")

st.code("""
sub.sort_values(ascending=False).head(1).values[0]
""")

if st.button("Run Highest Value", key="max"):
    

    st.subheader("Highest Value")
    st.write(sub.sort_values(ascending=False).head(1).values[0])


# =================================================
# SORT INDEX
# =================================================
st.markdown('<h4 style="color:pink;">sort_index()</h4>', unsafe_allow_html=True)
st.text("Sort the Series by index.")

st.code("""
sub.sort_index()
sub.sort_index(ascending=False)
""")

if st.button("Run sort_index()", key="index10"):
    

    st.subheader("Sorted by Index")
    st.write(sub.sort_index())

    st.subheader("Descending Index")
    st.write(sub.sort_index(ascending=False))
st.markdown('<h3 style="color:yellow;text-align:center;">Series Math Methods</h3>', unsafe_allow_html=True)
st.markdown('<p style=" color:yellow;">Diffence between Count And Size</p>',unsafe_allow_html=True) 
st.text("count gives the total number of items present in the series . But only NON missing values but, if we have missing values , it dosent count them . But , size gives the total item including missing value .")
# ---------------- COUNT ----------------
st.markdown('<h4 style="color:pink;">count()</h4>', unsafe_allow_html=True)

st.text("count() returns the total number of non-null values present in the Series.")

st.code("""
sub.count()
""")
st.code("""# Dataset
        data = [10, 20, 30, 40, 50]
sub = pd.Series(data)""")
data = [10, 20, 30, 40, 50]
sub = pd.Series(data)

st.subheader("Original Series")
st.write(sub)


if st.button("Run count()", key="count"):
    import pandas as pd

    st.subheader("count() Output")
    st.write(sub.count())


# ---------------- SIZE ----------------
st.markdown('<h4 style="color:pink;">size</h4>', unsafe_allow_html=True)

st.text("size returns the total number of elements in the Series including missing values.")

st.code("""
sub.size
""")

if st.button("Run size", key="size1"):
    import pandas as pd
    st.subheader("size Output")
    st.write(sub.size)


# ---------------- SUM ----------------
st.markdown('<h4 style="color:pink;">sum()</h4>', unsafe_allow_html=True)

st.text("sum() returns the total sum of all values present in the Series.")

st.code("""
sub.sum()
""")

if st.button("Run sum()", key="sum"):
    import pandas as pd
    
    st.subheader("sum() Output")
    st.write(sub.sum())


# ---------------- PRODUCT ----------------
st.markdown('<h4 style="color:pink;">product()</h4>', unsafe_allow_html=True)

st.text("product() returns the multiplication of all values present in the Series.")

st.code("""
sub.product()
""")

if st.button("Run product()", key="product"):
    import pandas as pd


    st.subheader("product() Output")
    st.write(sub.product())




st.markdown('<h3 style=" color:yellow;text-align: center; ">Statical Methods</h3>', unsafe_allow_html=True)
st.code("""#data
        data = [12, 15, 18, 20, 22, 25, 25, 30, 35, 40]
sub = pd.Series(data, name="Marks")""")
data = [12, 15, 18, 20, 22, 25, 25, 30, 35, 40]
sub = pd.Series(data, name="Marks")

st.markdown("<h4 style='color:pink;'>Mean()</h4>", unsafe_allow_html=True)

st.write("Mean returns the **average value** of all elements present in the Series.")

code_mean = """
sub.mean()
"""

st.code(code_mean, language="python")

if st.button("Run Mean"):
    st.write("Output:", sub.mean())



st.markdown("<h4 style='color:pink;'>Median()</h4>", unsafe_allow_html=True)

st.write("Median returns the **middle value** of the Series after sorting the data.")

code_median = """
sub.median()
"""

st.code(code_median, language="python")

if st.button("Run Median"):
    st.write("Output:", sub.median())


# =====================================================
# MODE
# =====================================================
st.markdown("<h4 style='color:pink;'>Mode()</h4>", unsafe_allow_html=True)

st.write("Mode returns the **most frequently occurring value** in the Series.")

code_mode = """
sub.mode()
"""

st.code(code_mode, language="python")

if st.button("Run Mode"):
    st.write("Output:")
    st.write(sub.mode())


# =====================================================
# STANDARD DEVIATION
# =====================================================
st.markdown("<h4 style='color:pink;'>Standard Deviation (std)</h4>", unsafe_allow_html=True)

st.write("Standard deviation measures the **spread of data around the mean**.")

code_std = """
sub.std()
"""

st.code(code_std, language="python")

if st.button("Run STD"):
    st.write("Output:", sub.std())


# =====================================================
# VARIANCE
# =====================================================
st.markdown("<h4 style='color:pink;'>Variance (var)</h4>", unsafe_allow_html=True)

st.write("Variance measures **how far each number in the dataset is from the mean**.")

code_var = """
sub.var()
"""

st.code(code_var, language="python")

if st.button("Run Variance"):
    st.write("Output:", sub.var())


# =====================================================
# MIN
# =====================================================
st.markdown("<h4 style='color:pink;'>Minimum Value (min)</h4>", unsafe_allow_html=True)

st.write("Min returns the **smallest value** present in the Series.")

code_min = """
sub.min()
"""

st.code(code_min, language="python")

if st.button("Run Min"):
    st.write("Output:", sub.min())


# =====================================================
# MAX
# =====================================================
st.markdown("<h4 style='color:pink;'>Maximum Value (max)</h4>", unsafe_allow_html=True)

st.write("Max returns the **largest value** present in the Series.")

code_max = """
sub.max()
"""

st.code(code_max, language="python")

if st.button("Run Max"):
    st.write("Output:", sub.max())


# =====================================================
# DESCRIBE
# =====================================================
st.markdown("<h4 style='color:pink;'>Describe()</h4>", unsafe_allow_html=True)

st.write("Describe returns the **complete statistical summary** of the Series.")

code_describe = """
sub.describe()
"""

st.code(code_describe, language="python")

if st.button("Run Describe"):
    st.write("Output:")
    st.write(sub.describe())




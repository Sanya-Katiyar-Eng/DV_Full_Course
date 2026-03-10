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


#link.................._....................................
st.markdown("""
## 📚 Pandas Table of Contents

1. [Introduction](#introduction)
2. [Pandas Series](#pandas-series)
3. [Series Attributes](#series-attributes)
4. [Series Methods](#series-methods)
5. [Series Math Methods](#series-math-methods)
6. [Statistical Methods](#statistical-methods)
7. [Series Indexing](#series-indexing)
8. [Editing Series](#editing-series)
9. [Python Functionalities on Series](#python-functionalities-on-series)
10. [Looping in Series](#looping-in-series)
11. [Operators on Series](#operators-on-series)
12. [Series Plotting Graphs](#series-plotting-graphs)
13. [Important Series Methods](#important-series-methods)
14. [Creating DataFrame](#creating-dataframe)
15. [DataFrame Attributes & Methods](#dataframe-attributes--methods)
16. [DataFrame Mathematical Methods](#dataframe-mathematical-methods)
17. [Selecting Columns from DataFrame](#selecting-columns-from-dataframe)
18. [Selecting Rows from DataFrame](#selecting-rows-from-dataframe)
19. [Filtering DataFrame](#filtering-dataframe)
20. [Adding New Column](#adding-new-column)
21. [Deleting Rows & Columns](#deleting-rows--columns)
22. [Sorting DataFrame](#sorting-dataframe)
23. [GroupBy in DataFrame](#groupby-in-dataframe)
24. [Time Series](#time-series)
25. [Merge / Join DataFrames](#merge--join-dataframes)
26. [Combining DataFrames](#combining-dataframes)
27. [Practice Question](#p)

""")
st.markdown('<a id="introduction"></a>', unsafe_allow_html=True)

st.markdown('<h1 style="  text-align: center;">Pandas</h1>', unsafe_allow_html=True)
st.text("pandas is a fast ,powerful,flexible and easy to use ope source data analysis and manlpulation tool,built on top of the python programming language.")

st.markdown('<h3 style=" color:yellow; text-align: center;">Pandas Installation</h3>', unsafe_allow_html=True)
st.code("pip install pandas")
st.markdown('<h3 style=" color:yellow; text-align: center;">Importing Pandas</h3>', unsafe_allow_html=True)
st.code("import pandas as pd")
#.....................................................
st.markdown('<a id="pandas-series"></a>', unsafe_allow_html=True)

st.markdown("""
Series Creation

- Series using String  
- Series using Integer  
- Series with Custom Index  
- Series with Name  
- Series from Dictionary  
- Series using read_csv
""")
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
    st.markdown('<h2 a="series-attributes"></a>', unsafe_allow_html=True)

st.markdown('<h3 style=" color:yellow;text-align: center; ">Series Attributes</h3>', unsafe_allow_html=True)
st.markdown("""
            Attributes
- size
- name
- shape
- index
- dtype
- is_unique
- values
""")
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
st.markdown('<a id="series-methods"></a>', unsafe_allow_html=True)

st.markdown('<h3 style="color:yellow;text-align:center;">Series Methods</h3>', unsafe_allow_html=True)
st.markdown("""
- head()
- tail()
- sample()
- value_counts()
- sort_values()
- sort_index()
""")
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

st.markdown('<a id="series-math-methods"></a>', unsafe_allow_html=True)

st.markdown('<h3 style="color:yellow;text-align:center;">Series Math Methods</h3>', unsafe_allow_html=True)
st.markdown("""
- count()
- size
- sum()
- product()
""")
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



st.markdown('<a id="statistical-methods"></a>', unsafe_allow_html=True)

st.markdown('<h3 style=" color:yellow;text-align: center; ">Statical Methods</h3>', unsafe_allow_html=True)
st.markdown("""
- mean()
- median()
- mode()
- std()
- var()
- min()
- max()
- describe()
""")
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

#.......................................................................
st.markdown('<a id="series-indexing"></a>', unsafe_allow_html=True)

st.markdown('<h3 style=" color:yellow;text-align: center; ">Series Indexing</h3>', unsafe_allow_html=True)
st.markdown("""
- Basic Indexing
- Slicing
- Fancy Indexing
""")
st.code("""
import pandas as pd
x = pd.Series([12,13,14,35,46,57,58,79,9])
""")

x = pd.Series([12,13,14,35,46,57,58,79,9])

st.subheader("Example Series")
st.write(x)

# ---------------- Basic Indexing ----------------

st.subheader("Basic Indexing")

st.code("x[1]")
st.text("Output")
st.write(x[1])

st.code("x[0]")
st.text("Output")
st.write(x[0])

# correct way for last value
st.code("x.iloc[-1]")
st.text("Output")
st.write(x.iloc[-1])

# ---------------- Slicing ----------------

st.subheader("Series Slicing")

st.code("x[4:10]")
st.text("Output")
st.write(x[4:10])

st.code("x[-5:]")
st.text("Output")
st.write(x[-5:])

st.code("x[::2]")
st.text("Output")
st.write(x[::2])

# ---------------- Fancy Indexing ----------------

st.subheader("Fancy Indexing")

st.code("x[[0,3,5]]")
st.text("Output")
st.write(x[[0,3,5]])

# ---------------- Fancy Indexing Table ----------------

st.subheader("Fancy Indexing with Table")

st.code("""
index_list=[1,4,7]
x[index_list]
""")

index_list=[1,4,7]
result = x[index_list]

st.text("Output")
st.write(result)
#...........................................................
st.markdown('<a id="editing-series"></a>', unsafe_allow_html=True)

st.markdown('<h3 style=" color:yellow;text-align: center; ">Editing the Series</h3>', unsafe_allow_html=True)
st.markdown("""
- Update value by index
- Add new element
""")

m=pd.Series({'math':67,'english':57,'scince':89,'hindi':100})

st.write(m)
st.code("""import pandas as pd
        m=pd.Series({'math':67,'english':57,'scince':89,'hindi':100})
        m""")
st.text("Series : ")
st.write(m)
st.code("""import pandas as pd
        m[1]=88
        m""")
m[1]=88
st.write(m)

st.code("""import pandas as pd
        m['social']=90
        m""")
m['social']=90
st.write(m)
#..................................................................
st.markdown('<a id="python-functionalities-on-series"></a>', unsafe_allow_html=True)
st.markdown('<h3 style=" color:yellow;text-align: center; ">Series with python Functionalities</h3>', unsafe_allow_html=True)
st.markdown("""
- len()
- type()
- sorted()
- min()
- max()
- list()
- Membership (in)
""")
st.code("""print("len :",len(m))
        print("type :",type(m))
        print("sorted:",sorted(m))
        print("min :",min(m))
        print("max :",max(m))
        print("list :",list(m))
        'english' in m
        """)

st.subheader("Output")

st.write("len :", len(m))
#st.write("type :", type(m))
st.write("sorted :", sorted(m))
st.write("min :", min(m))
st.write("max :", max(m))
st.write("list :", list(m))
st.write("'english' in m :", 'english' in m)
st.markdown('<a id="looping-in-series"></a>', unsafe_allow_html=True)
#lopping.........................
st.markdown('<h3 style=" color:yellow;text-align: center; ">Looping in Series</h3>', unsafe_allow_html=True)

st.text("Looping allows us to iterate through each value of the Series one by one.")

st.code("""
import pandas as pd

m = pd.Series({'math':67,'english':57,'science':89,'hindi':100})

for i in m:
    print(i)
""")

if st.button("Run Loop", key="loop1"):

    import pandas as pd

    m = pd.Series({'math':67,'english':57,'science':89,'hindi':100})

    st.subheader("Output")

    for i in m:
        st.write(i)
st.markdown('<a id="operators-on-series"></a>', unsafe_allow_html=True)

st.markdown('<h3 style=" color:yellow;text-align: center; ">Operators on Series</h3>', unsafe_allow_html=True)

st.text("Operators can be applied directly on Pandas Series. The operation will be applied to each element of the Series.")

st.code("""
import pandas as pd

s = pd.Series([10,20,30,40])

print(s + 5)
print(s * 2)
print(s > 20)
""")

if st.button("Run Operators", key="op1"):

    import pandas as pd

    s = pd.Series([10,20,30,40])

    st.subheader("Addition (+5)")
    st.write(s + 5)

    st.subheader("Multiplication (*2)")
    st.write(s * 2)

    st.subheader("Comparison (>20)")
    st.write(s > 20)
    st.markdown('<h4 style="color:pink;">Arithmetic Operators</h4>', unsafe_allow_html=True)

st.code("""
s1 = pd.Series([10,20,30])
s2 = pd.Series([1,2,3])

print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
""")

if st.button("Run Arithmetic", key="op2"):

    s1 = pd.Series([10,20,30])
    s2 = pd.Series([1,2,3])

    st.write("Addition")
    st.write(s1 + s2)

    st.write("Subtraction")
    st.write(s1 - s2)

    st.write("Multiplication")
    st.write(s1 * s2)
st.markdown('<h4 style="color:pink;">Boolean Operators</h4>', unsafe_allow_html=True)

st.code("""
s = pd.Series([10,25,30,15,40])

s > 20
""")

if st.button("Run Boolean", key="op3"):

    s = pd.Series([10,25,30,15,40])

    st.write("Values greater than 20")
    st.write(s > 20)
    st.markdown('<h3 style=" color:yellow;text-align: center; ">Relational Operators in Series</h3>', unsafe_allow_html=True)

st.code("""
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
s
""")

s = pd.Series([10,20,30,40,50])

st.subheader("Original Series")
st.write(s)

# Greater than
st.markdown('<h4 style="color:pink;">Greater Than (>)</h4>', unsafe_allow_html=True)

st.code("s > 25")

if st.button("Run >", key="gt"):
    st.write(s > 25)

# Less than
st.markdown('<h4 style="color:pink;">Less Than (<)</h4>', unsafe_allow_html=True)

st.code("s < 30")

if st.button("Run <", key="lt"):
    st.write(s < 30)

# Greater equal
st.markdown('<h4 style="color:pink;">Greater Than Equal (>=)</h4>', unsafe_allow_html=True)

st.code("s >= 30")

if st.button("Run >=", key="gte"):
    st.write(s >= 30)

# Less equal
st.markdown('<h4 style="color:pink;">Less Than Equal (<=)</h4>', unsafe_allow_html=True)

st.code("s <= 20")

if st.button("Run <=", key="lte"):
    st.write(s <= 20)

# Equal
st.markdown('<h4 style="color:pink;">Equal To (==)</h4>', unsafe_allow_html=True)

st.code("s == 30")

if st.button("Run ==", key="eq"):
    st.write(s == 30)

# Not equal
st.markdown('<h4 style="color:pink;">Not Equal To (!=)</h4>', unsafe_allow_html=True)

st.code("s != 30")

if st.button("Run !=", key="neq"):
    st.write(s != 30)
st.markdown('<a id="series-plotting-graphs"></a>', unsafe_allow_html=True)
st.markdown('<h3 style=" color:yellow;text-align: center; ">Series Plotting Graphs</h3>', unsafe_allow_html=True)

st.text("Pandas Series provides built-in plotting methods using Matplotlib.")

st.code("""
import pandas as pd
import matplotlib.pyplot as plt

data = [10,20,15,30,25]
s = pd.Series(data)

s.plot()
plt.show()
""")

import pandas as pd
import matplotlib.pyplot as plt

data = [10,20,15,30,25]
s = pd.Series(data)

st.subheader("Series Data")
st.write(s)
st.markdown('<h4 style="color:pink;">Line Plot</h4>', unsafe_allow_html=True)

st.code("""
s.plot(kind="line")
plt.show()
""")

if st.button("Run Line Plot"):
    
    fig, ax = plt.subplots()
    s.plot(kind="line", ax=ax)
    
    st.pyplot(fig)
st.markdown('<h4 style="color:pink;">Bar Plot</h4>', unsafe_allow_html=True)

st.code("""
s.plot(kind="bar")
plt.show()
""")

if st.button("Run Bar Plot"):
    
    fig, ax = plt.subplots()
    s.plot(kind="bar", ax=ax)
    
    st.pyplot(fig)
st.markdown('<h4 style="color:pink;">Horizontal Bar Plot</h4>', unsafe_allow_html=True)

st.code("""
s.plot(kind="barh")
plt.show()
""")

if st.button("Run Barh Plot"):
    
    fig, ax = plt.subplots()
    s.plot(kind="barh", ax=ax)
    
    st.pyplot(fig)

st.markdown('<h4 style="color:pink;">Pie Chart</h4>', unsafe_allow_html=True)

st.code("""
s.plot(kind="pie")
plt.show()
""")

if st.button("Run Pie Chart"):
    
    fig, ax = plt.subplots()
    s.plot(kind="pie", autopct='%1.1f%%', ax=ax)
    
    st.pyplot(fig)
st.markdown('<h4 style="color:pink;">Histogram</h4>', unsafe_allow_html=True)

st.code("""
s.plot(kind="hist")
plt.show()
""")

if st.button("Run Histogram"):
    
    fig, ax = plt.subplots()
    s.plot(kind="hist", ax=ax)
    
    st.pyplot(fig)
st.markdown('<h4 style="color:pink;">KDE Plot</h4>', unsafe_allow_html=True)

st.code("""
s.plot(kind="kde")
plt.show()
""")

if st.button("Run KDE Plot"):
    
    fig, ax = plt.subplots()
    s.plot(kind="kde", ax=ax)
    
    st.pyplot(fig)
st.markdown('<h4 style="color:pink;">Box Plot</h4>', unsafe_allow_html=True)

st.code("""
s.plot(kind="box")
plt.show()
""")

if st.button("Run Box Plot"):
    
    fig, ax = plt.subplots()
    s.plot(kind="box", ax=ax)
    
    st.pyplot(fig)




st.markdown('<a id="important-series-methods"></a>', unsafe_allow_html=True)
st.markdown('<h3 style=" color:yellow;text-align: center; ">Important Series Methods</h3>', unsafe_allow_html=True)

data = [10,20,np.nan,40,50,20]
s = pd.Series(data)

st.subheader("Original Series")
st.write(s)
st.markdown('<h4 style="color:pink;">astype()</h4>', unsafe_allow_html=True)

st.text("astype() is used to change the datatype of a Series.")

st.code("""
s.astype('float')
""")

if st.button("Run astype()",key="astype"):
    
    st.write(s.astype('float'))
st.markdown('<h4 style="color:pink;">between()</h4>', unsafe_allow_html=True)

st.text("between() checks whether values fall within a given range.")

st.code("""
s.between(15,45)
""")

if st.button("Run between()",key="between"):
    
    st.write(s.between(15,45))
st.markdown('<h4 style="color:pink;">clip()</h4>', unsafe_allow_html=True)

st.text("clip() limits the values within a minimum and maximum range.")

st.code("""
s.clip(20,40)
""")

if st.button("Run clip()",key="clip"):
    
    st.write(s.clip(20,40))
st.markdown('<h4 style="color:pink;">drop_duplicates()</h4>', unsafe_allow_html=True)

st.text("drop_duplicates() removes duplicate values from the Series.")

st.code("""
s.drop_duplicates()
""")

if st.button("Run drop_duplicates()",key="dropdup"):
    
    st.write(s.drop_duplicates())
st.markdown('<h4 style="color:pink;">isnull()</h4>', unsafe_allow_html=True)

st.text("isnull() checks missing values in the Series.")

st.code("""
s.isnull()
""")

if st.button("Run isnull()",key="null"):
    
    st.write(s.isnull())
st.markdown('<h4 style="color:pink;">fillna()</h4>', unsafe_allow_html=True)

st.text("fillna() replaces missing values with a specified value.")

st.code("""
s.fillna(0)
""")

if st.button("Run fillna()",key="fill"):
    
    st.write(s.fillna(0))
st.markdown('<h4 style="color:pink;">dropna()</h4>', unsafe_allow_html=True)

st.text("dropna() removes missing values from the Series.")

st.code("""
s.dropna()
""")

if st.button("Run dropna()",key="dropna"):
    
    st.write(s.dropna())
st.markdown('<h4 style="color:pink;">isin()</h4>', unsafe_allow_html=True)

st.text("isin() checks whether values exist in a given list.")

st.code("""
s.isin([20,50])
""")

if st.button("Run isin()",key="isin"):
    
    st.write(s.isin([20,50]))
st.markdown('<h4 style="color:pink;">apply()</h4>', unsafe_allow_html=True)

st.text("apply() applies a function to each element of the Series.")

st.code("""
s.apply(lambda x: x*2)
""")

if st.button("Run apply()",key="apply"):
    
    st.write(s.apply(lambda x: x*2))
st.markdown('<h4 style="color:pink;">copy()</h4>', unsafe_allow_html=True)

st.text("copy() creates a separate copy of the Series.")

st.code("""
new_series = s.copy()
new_series
""")

if st.button("Run copy()",key="copy"):
    
    new_series = s.copy()
    st.write(new_series)
#...........................................................
st.markdown('<a id="creating-dataframe"></a>', unsafe_allow_html=True)
st.markdown('<h3 style=" color:yellow;text-align: center; ">Creating DataFrame</h3>', unsafe_allow_html=True)
st.markdown('<h4 style="color:pink;">DataFrame from Dictionary</h4>', unsafe_allow_html=True)

st.text("A DataFrame can be created from a dictionary where keys become column names.")

st.code("""
import pandas as pd

data = {
"Name":["Ram","Shyam","Mohan"],
"Marks":[85,90,88]
}

df = pd.DataFrame(data)
""")

if st.button("Run Dictionary",key="dict"):
    
    data = {
    "Name":["Ram","Shyam","Mohan"],
    "Marks":[85,90,88]
    }

    df = pd.DataFrame(data)

    st.write(df)
st.markdown('<h4 style="color:pink;">DataFrame from List</h4>', unsafe_allow_html=True)

st.text("A DataFrame can be created from a list.")

st.code("""
data=[10,20,30,40]
df=pd.DataFrame(data)
""")

if st.button("Run List",key="listdf"):
    
    data=[10,20,30,40]

    df=pd.DataFrame(data)

    st.write(df)
st.markdown('<h4 style="color:pink;">DataFrame from List of Lists</h4>', unsafe_allow_html=True)

st.code("""
data=[
["Ram",85],
["Shyam",90],
["Mohan",88]
]

df=pd.DataFrame(data,columns=["Name","Marks"])
""")

if st.button("Run List of Lists",key="listlist"):
    
    data=[
    ["Ram",85],
    ["Shyam",90],
    ["Mohan",88]
    ]

    df=pd.DataFrame(data,columns=["Name","Marks"])

    st.write(df)
st.markdown('<h4 style="color:pink;">DataFrame from Numpy Array</h4>', unsafe_allow_html=True)

st.code("""
import numpy as np

data=np.array([[1,2,3],[4,5,6]])

df=pd.DataFrame(data)
""")

if st.button("Run Numpy",key="numpy"):
    
    import numpy as np

    data=np.array([[1,2,3],[4,5,6]])

    df=pd.DataFrame(data)

    st.write(df)
st.markdown('<h4 style="color:pink;">Dictionary of Lists</h4>', unsafe_allow_html=True)

st.code("""
data={
"Name":["A","B","C"],
"Age":[20,21,22]
}

df=pd.DataFrame(data)
""")

if st.button("Run Dict List",key="dictlist"):
    
    data={
    "Name":["A","B","C"],
    "Age":[20,21,22]
    }

    df=pd.DataFrame(data)

    st.write(df)
st.markdown('<h4 style="color:pink;">DataFrame from Series</h4>', unsafe_allow_html=True)

st.code("""
s=pd.Series([10,20,30])
df=pd.DataFrame(s)
""")

if st.button("Run Series",key="series"):
    
    s=pd.Series([10,20,30])

    df=pd.DataFrame(s)

    st.write(df)
st.markdown('<h4 style="color:pink;">DataFrame from CSV</h4>', unsafe_allow_html=True)

st.text("DataFrame can be created by reading CSV files.")

st.code("""
df=pd.read_csv("data.csv")
""")
st.markdown('<h4 style="color:pink;">DataFrame from Excel</h4>', unsafe_allow_html=True)

st.code("""
df=pd.read_excel("data.xlsx")
""")
st.markdown('<a id="dataframe-attributes--methods"></a>', unsafe_allow_html=True)
#.........................................................
st.markdown('<h3 style="color:yellow;text-align:center;">DataFrame Attributes & Methods</h3>', unsafe_allow_html=True)

# Sample DataFrame
st.code("""df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi","Ram"],
    "Age":[20,21,22,np.nan,20],
    "Marks":[85,90,88,76,85]
})
    print(df)""")
df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi","Ram"],
    "Age":[20,21,22,np.nan,20],
    "Marks":[85,90,88,76,85]
})

st.subheader("Original DataFrame")
st.write(df)

# ---------------- shape ----------------
st.markdown("### shape")
st.code("df.shape")

if st.button("Run shape"):
    st.write(df.shape)

# ---------------- dtypes ----------------
st.markdown("### dtypes")
st.code("df.dtypes")

if st.button("Run dtypes"):
    st.write(df.dtypes)

# ---------------- index ----------------
st.markdown("### index")
st.code("df.index")

if st.button("Run index"):
    st.write(df.index)

# ---------------- columns ----------------
st.markdown("### columns")
st.code("df.columns")

if st.button("Run columns"):
    st.write(df.columns)

# ---------------- values ----------------
st.markdown("### values")
st.code("df.values")

if st.button("Run values"):
    st.write(df.values)

# ---------------- sample ----------------
st.markdown("### sample()")
st.code("df.sample(2)")

if st.button("Run sample"):
    st.write(df.sample(2))

# ---------------- info ----------------
st.markdown("### info()")
st.code("df.info()")

if st.button("Run info"):
    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

# ---------------- describe ----------------
st.markdown("### describe()")
st.code("df.describe()")

if st.button("Run describe"):
    st.write(df.describe())

# ---------------- isnull ----------------
st.markdown("### isnull()")
st.code("df.isnull()")

if st.button("Run isnull"):
    st.write(df.isnull())

# ---------------- isnull sum ----------------
st.markdown("### isnull().sum()")
st.code("df.isnull().sum()")

if st.button("Run isnull sum"):
    st.write(df.isnull().sum())

# ---------------- duplicates ----------------
st.markdown("### duplicated().sum()")
st.code("df.duplicated().sum()")

if st.button("Run duplicated"):
    st.write(df.duplicated().sum())

# ---------------- rename ----------------
st.markdown("### rename()")
st.code("df.rename(columns={'Marks':'Score'})")

if st.button("Run rename"):
    st.write(df.rename(columns={'Marks':'Score'}))


#...................................................
st.markdown('<h3 style="color:yellow;text-align:center;">DataFrame Mathematical Methods</h3>', unsafe_allow_html=True)
st.code("""df = pd.DataFrame({
    "Math":[80,90,70],
    "English":[85,88,92],
    "Science":[78,95,89]
})
        print(df)""")
df = pd.DataFrame({
    "Math":[80,90,70],
    "English":[85,88,92],
    "Science":[78,95,89]
})

st.subheader("Original DataFrame")
st.write(df)
st.markdown("### sum()")

st.code("""
df.sum(axis=0)   # Column wise sum
df.sum(axis=1)   # Row wise sum
""")

if st.button("Run sum()"):
    
    st.write("Column wise sum (axis=0)")
    st.write(df.sum(axis=0))
    
    st.write("Row wise sum (axis=1)")
    st.write(df.sum(axis=1))

st.markdown("### mean()")

st.code("""
df.mean()
""")

if st.button("Run mean()"):
    
    st.write(df.mean())
st.markdown("### min()")

st.code("""
df.min()
""")

if st.button("Run min()"):
    
    st.write(df.min())
st.markdown("### var()")

st.code("""
df.var()
""")

if st.button("Run var()"):
    
    st.write(df.var())
#..............................................................
st.markdown('<a id="selecting-columns-form-dataframe"></a>', unsafe_allow_html=True)
st.markdown('<h3 style="color:yellow;text-align:center;">Selecting Columns from DataFrame</h3>', unsafe_allow_html=True)
st.code("""df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi"],
    "Age":[20,21,22,23],
    "Marks":[85,90,88,76],
    "City":["Kanpur","Delhi","Lucknow","Agra"]
})
print(df)""")
df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi"],
    "Age":[20,21,22,23],
    "Marks":[85,90,88,76],
    "City":["Kanpur","Delhi","Lucknow","Agra"]
})

st.subheader("Original DataFrame")
st.write(df)
st.markdown("### Selecting Single Column")

st.code("""
df["Name"]
""")

if st.button("Run Single Column"):
    
    st.write(df["Name"])
st.markdown("### Selecting Multiple Columns")

st.code("""
df[["Name","Marks"]]
""")

if st.button("Run Multiple Columns"):
    
    st.write(df[["Name","Marks"]])
st.markdown("### Selecting Column using Dot Notation")

st.code("""
df.Name
""")

if st.button("Run Dot Notation"):
    
    st.write(df.Name)
st.markdown("### Selecting Columns using loc")

st.code("""
df.loc[:, "Marks"]
""")

if st.button("Run loc"):
    
    st.write(df.loc[:, "Marks"])
st.markdown("### Selecting Columns using iloc")

st.code("""
df.iloc[:,2]
""")

if st.button("Run iloc"):
    
    st.write(df.iloc[:,2])

#......................................................
st.markdown('<h3 style="color:yellow;text-align:center;">Selecting Rows from DataFrame</h3>', unsafe_allow_html=True)
st.code("""df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi","Aman"],
    "Age":[20,21,22,23,24],
    "Marks":[85,90,88,76,91]
})
print(df)""")
df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi","Aman"],
    "Age":[20,21,22,23,24],
    "Marks":[85,90,88,76,91]
})

st.subheader("Original DataFrame")
st.write(df)
st.markdown("### iloc : Searching using Index Positions")

st.code("""
df.iloc[2]
""")

if st.button("Run iloc row"):
    
    st.write(df.iloc[2])
st.code("""
df.iloc[1:4]
""")

if st.button("Run iloc slice"):
    
    st.write(df.iloc[1:4])

st.markdown("### loc : Searching using Index Labels")

st.code("""
df.loc[2]
""")

if st.button("Run loc row"):
    
    st.write(df.loc[2])
st.code("""
df.loc[1:3]
""")

if st.button("Run loc slice"):
    
    st.write(df.loc[1:3])
st.markdown("### Row and Column Selection")

st.code("""
df.loc[1:3,["Name","Marks"]]
""")

if st.button("Run loc row+col"):
    
    st.write(df.loc[1:3,["Name","Marks"]])
#................................................................
st.markdown('<a id="filtering-dataframe"></a>', unsafe_allow_html=True)
st.markdown('<h3 style="color:yellow;text-align:center;">Filtering DataFrame</h3>', unsafe_allow_html=True)

# Sample DataFrame
st.code("""df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi","Aman"],
    "Age":[20,21,22,23,24],
    "Marks":[85,90,88,76,91],
    "City":["Kanpur","Delhi","Lucknow","Agra","Kanpur"]
}) 
        print(df)""")
df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi","Aman"],
    "Age":[20,21,22,23,24],
    "Marks":[85,90,88,76,91],
    "City":["Kanpur","Delhi","Lucknow","Agra","Kanpur"]
})

st.subheader("Original DataFrame")
st.write(df)
st.markdown("### Filter Rows where Marks > 85")

st.code("""
df[df["Marks"]>85]
""")

if st.button("Run filter 1"):
    
    st.write(df[df["Marks"]>85])

st.markdown("### Filter Marks > 80 AND Age > 21")

st.code("""
df[(df["Marks"]>80) & (df["Age"]>21)]
""")

if st.button("Run filter AND"):
    
    st.write(df[(df["Marks"]>80) & (df["Age"]>21)])
st.markdown("### Filter Marks > 90 OR Age < 21")

st.code("""
df[(df["Marks"]>90) | (df["Age"]<21)]
""")

if st.button("Run filter OR"):
    
    st.write(df[(df["Marks"]>90) | (df["Age"]<21)])
st.markdown("### Filter City in ['Kanpur','Delhi']")

st.code("""
df[df["City"].isin(["Kanpur","Delhi"])]
""")

if st.button("Run isin filter"):
    
    st.write(df[df["City"].isin(["Kanpur","Delhi"])])

st.markdown("### Filtering with loc")

st.code("""
df.loc[df["Marks"]>85]
""")

if st.button("Run loc filter"):
    
    st.write(df.loc[df["Marks"]>85])
#............................................................
st.markdown('<a id="adding-new-column"></a>', unsafe_allow_html=True)
st.markdown('<h3 style="color:yellow;text-align:center;">Adding New Column in DataFrame</h3>', unsafe_allow_html=True)
st.code("""df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi"],
    "Math":[78,85,90,76],
    "English":[88,76,95,80]
})
print("df")""")
# Sample DataFrame
df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi"],
    "Math":[78,85,90,76],
    "English":[88,76,95,80]
})

st.subheader("Original DataFrame")
st.write(df)

st.markdown("### Adding Column using Assignment")

st.code("""
df["Total"] = df["Math"] + df["English"]
""")

if st.button("Run Assignment"):
    
    df["Total"] = df["Math"] + df["English"]
    st.write(df)
st.markdown("### Adding Column using insert()")

st.code("""
df.insert(1,"City",["Kanpur","Delhi","Lucknow","Agra"])
""")

if st.button("Run insert"):
    
    df2 = df.copy()
    df2.insert(1,"City",["Kanpur","Delhi","Lucknow","Agra"])
    st.write(df2)

st.markdown("### Adding Column using assign()")

st.code("""
df.assign(Average=(df["Math"]+df["English"])/2)
""")

if st.button("Run assign"):
    
    st.write(df.assign(Average=(df["Math"]+df["English"])/2))
st.markdown("### Adding Column with Constant Value")

st.code("""
df["School"]="ABC School"
""")

if st.button("Run constant column"):
    
    df3 = df.copy()
    df3["School"]="ABC School"
    st.write(df3)


#......................................
st.markdown('<a id="deleting-rows--columns"></a>', unsafe_allow_html=True)
st.markdown('<h3 style="color:yellow;text-align:center;">Deleting Rows & Columns</h3>', unsafe_allow_html=True)
st.code("""df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi"],
    "Age":[20,21,22,23],
    "Marks":[85,90,88,76],
    "City":["Kanpur","Delhi","Lucknow","Agra"]
})
        print(df)""")
# Sample DataFrame
df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi"],
    "Age":[20,21,22,23],
    "Marks":[85,90,88,76],
    "City":["Kanpur","Delhi","Lucknow","Agra"]
})

st.subheader("Original DataFrame")
st.write(df)
st.markdown("### Delete Column using drop()")

st.code("""
df.drop("City",axis=1)
""")

if st.button("Run drop column"):
    
    st.write(df.drop("City",axis=1))
st.markdown("### Delete Row using drop()")

st.code("""
df.drop(1,axis=0)
""")

if st.button("Run drop row"):
    
    st.write(df.drop(1,axis=0))

st.markdown("### Delete Column using del")

st.code("""
del df["Age"]
""")

if st.button("Run del column"):
    
    df2=df.copy()
    del df2["Age"]
    st.write(df2)
st.markdown("### Delete Column using pop()")

st.code("""
df.pop("Marks")
""")

if st.button("Run pop column"):
    
    df3=df.copy()
    removed=df3.pop("Marks")
    
    st.write("Updated DataFrame")
    st.write(df3)
    
    st.write("Removed Column")
    st.write(removed)
st.markdown('<a id="sorting-dataframe"></a>', unsafe_allow_html=True)
st.markdown('<h3 style="color:yellow;text-align:center;">Sorting DataFrame</h3>', unsafe_allow_html=True)
st.code("""df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi"],
    "Age":[22,21,24,20],
    "Marks":[85,90,88,76],
    "City":["Kanpur","Delhi","Lucknow","Agra"]
})
        print(df)""")
# Sample DataFrame
df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi"],
    "Age":[22,21,24,20],
    "Marks":[85,90,88,76],
    "City":["Kanpur","Delhi","Lucknow","Agra"]
})

st.subheader("Original DataFrame")
st.write(df)

st.markdown("### sort_values() by Marks")

st.code("""
df.sort_values("Marks")
""")

if st.button("Run sort by Marks"):
    
    st.write(df.sort_values("Marks"))

st.markdown("### sort_values() Descending")

st.code("""
df.sort_values("Marks",ascending=False)
""")

if st.button("Run descending sort"):
    
    st.write(df.sort_values("Marks",ascending=False))

st.markdown("### Sorting by Multiple Columns")

st.code("""
df.sort_values(["Age","Marks"])
""")

if st.button("Run multi sort"):
    
    st.write(df.sort_values(["Age","Marks"]))
st.markdown("### sort_index()")

st.code("""
df.sort_index()
""")

if st.button("Run sort index"):
    
    st.write(df.sort_index())

#..................................................
st.markdown('<a id="groupby-in-dataframe"></a>', unsafe_allow_html=True)
st.markdown('<h3 style="color:yellow;text-align:center;">GroupBy in DataFrame</h3>', unsafe_allow_html=True)
st.text("groupby() method का उपयोग DataFrame को किसी column के आधार पर groups में divide करने के लिए किया जाता है। फिर हम उन groups पर sum(), mean(), count() जैसे operations apply कर सकते हैं।")
st.code("""df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi","Aman"],
    "Department":["IT","HR","IT","HR","IT"],
    "Salary":[50000,45000,60000,48000,55000],
    "Experience":[2,3,4,2,5]
})
print(df)""")
# Sample DataFrame
df = pd.DataFrame({
    "Name":["Ram","Shyam","Mohan","Ravi","Aman"],
    "Department":["IT","HR","IT","HR","IT"],
    "Salary":[50000,45000,60000,48000,55000],
    "Experience":[2,3,4,2,5]
})

st.subheader("Original DataFrame")
st.write(df)
st.markdown("### GroupBy Department with sum()")

st.code("""
df.groupby("Department")["Salary"].sum()
""")

if st.button("Run groupby sum"):
    
    st.write(df.groupby("Department")["Salary"].sum())
st.markdown("### GroupBy Department with mean()")

st.code("""
df.groupby("Department")["Salary"].mean()
""")

if st.button("Run groupby mean"):
    
    st.write(df.groupby("Department")["Salary"].mean())
st.markdown("### GroupBy Department with count()")

st.code("""
df.groupby("Department")["Name"].count()
""")

if st.button("Run groupby count"):
    
    st.write(df.groupby("Department")["Name"].count())
st.markdown("### GroupBy Department with multiple columns")

st.code("""
df.groupby("Department")[["Salary","Experience"]].mean()
""")

if st.button("Run groupby multi"):
    
    st.write(df.groupby("Department")[["Salary","Experience"]].mean())
st.markdown("### GroupBy with agg()")

st.code("""
df.groupby("Department").agg({
"Salary":["sum","mean","max"],
"Experience":"mean"
})
""")

if st.button("Run groupby agg"):
    
    st.write(df.groupby("Department").agg({
    "Salary":["sum","mean","max"],
    "Experience":"mean"
    }))
    #..............................................................
st.markdown('<a id="time-series"></a>', unsafe_allow_html=True)
st.markdown('<h3 style="color:yellow;text-align:center;">Creating Time Series</h3>', unsafe_allow_html=True)

st.text("A Time Series is a sequence of data points indexed by time (dates).")

st.code("""
import pandas as pd

dates = pd.date_range("2024-01-01", periods=5)

data = [100,120,130,90,150]

ts = pd.Series(data,index=dates)

print(ts)
""")

if st.button("Run Time Series",key="ts1"):

    import pandas as pd
    
    dates = pd.date_range("2024-01-01", periods=5)

    data = [100,120,130,90,150]

    ts = pd.Series(data,index=dates)

    st.write(ts)

st.markdown('<h3 style="color:yellow;text-align:center;">date_range()</h3>', unsafe_allow_html=True)

st.text("date_range() creates a sequence of dates.")

st.code("""
import pandas as pd

dates=pd.date_range(start="2024-01-01",periods=10)

print(dates)
""")

if st.button("Run date_range()",key="ts2"):

    import pandas as pd

    dates=pd.date_range(start="2024-01-01",periods=10)

    st.write(dates)
st.markdown('<h3 style="color:yellow;text-align:center;">Accessing Time Series</h3>', unsafe_allow_html=True)

st.code("""
ts["2024-01-03"]
""")

if st.button("Run Access",key="ts3"):

    import pandas as pd

    dates=pd.date_range("2024-01-01",periods=5)

    data=[100,120,130,90,150]

    ts=pd.Series(data,index=dates)

    st.write(ts["2024-01-03"])
st.markdown('<h3 style="color:yellow;text-align:center;">Resampling</h3>', unsafe_allow_html=True)

st.text("Resampling converts time series to different frequency.")

st.code("""
ts.resample("M").mean()
""")

if st.button("Run Resample",key="ts4"):

    import pandas as pd

    dates=pd.date_range("2024-01-01",periods=30)

    data=range(30)

    ts=pd.Series(data,index=dates)

    st.write(ts.resample("M").mean())
st.markdown('<h3 style="color:yellow;text-align:center;">Shift()</h3>', unsafe_allow_html=True)

st.code("""
ts.shift(1)
""")

if st.button("Run Shift",key="ts5"):

    import pandas as pd

    dates=pd.date_range("2024-01-01",periods=5)

    data=[10,20,30,40,50]

    ts=pd.Series(data,index=dates)

    st.write(ts.shift(1))
st.markdown('<h3 style="color:yellow;text-align:center;">Rolling Mean</h3>', unsafe_allow_html=True)

st.code("""
ts.rolling(3).mean()
""")

if st.button("Run Rolling",key="ts6"):

    import pandas as pd

    dates=pd.date_range("2024-01-01",periods=10)

    data=[10,20,30,40,50,60,70,80,90,100]

    ts=pd.Series(data,index=dates)

    st.write(ts.rolling(3).mean())
st.markdown('<h3 style="color:yellow;text-align:center;">Time Series Plot</h3>', unsafe_allow_html=True)

st.code("""
ts.plot()
""")

if st.button("Run Plot",key="ts7"):

    import pandas as pd
    import matplotlib.pyplot as plt

    dates=pd.date_range("2024-01-01",periods=10)

    data=[10,20,30,40,50,60,70,80,90,100]

    ts=pd.Series(data,index=dates)

    ts.plot()

    st.pyplot(plt)
#........................................................
st.markdown('<a id="merge--join-dataframes"></a>', unsafe_allow_html=True)
st.markdown('<h3 style="color:yellow;text-align:center;">Creating DataFrames</h3>', unsafe_allow_html=True)

st.code("""
import pandas as pd

df1=pd.DataFrame({
'id':[1,2,3,4],
'name':['Aman','Riya','Karan','Simran']
})

df2=pd.DataFrame({
'id':[1,2,3,5],
'salary':[50000,60000,55000,70000]
})
""")

if st.button("Show DataFrames",key="m1"):

    import pandas as pd

    df1=pd.DataFrame({
    'id':[1,2,3,4],
    'name':['Aman','Riya','Karan','Simran']
    })

    df2=pd.DataFrame({
    'id':[1,2,3,5],
    'salary':[50000,60000,55000,70000]
    })

    st.subheader("DataFrame 1")
    st.write(df1)

    st.subheader("DataFrame 2")
    st.write(df2)

st.markdown('<h3 style="color:pink;">Inner Merge</h3>', unsafe_allow_html=True)

st.text("Inner merge keeps only matching rows.")

st.code("""
pd.merge(df1,df2,on="id",how="inner")
""")

if st.button("Run Inner Merge",key="m2"):

    import pandas as pd

    df1=pd.DataFrame({'id':[1,2,3,4],
                      'name':['Aman','Riya','Karan','Simran']})

    df2=pd.DataFrame({'id':[1,2,3,5],
                      'salary':[50000,60000,55000,70000]})

    result=pd.merge(df1,df2,on="id",how="inner")

    st.write(result)
st.markdown('<h3 style="color:pink;">Left Join</h3>', unsafe_allow_html=True)
st.text("Left join में left dataframe की सभी rows रहती हैं।")
st.code("""
pd.merge(df1,df2,on="id",how="left")
""")

if st.button("Run Left Join",key="m3"):

    import pandas as pd

    df1=pd.DataFrame({'id':[1,2,3,4],
                      'name':['Aman','Riya','Karan','Simran']})

    df2=pd.DataFrame({'id':[1,2,3,5],
                      'salary':[50000,60000,55000,70000]})

    result=pd.merge(df1,df2,on="id",how="left")

    st.write(result)
st.markdown('<h3 style="color:pink;">Right Join</h3>', unsafe_allow_html=True)
st.text("Right join में right dataframe की सभी rows रहती हैं।")
st.code("""
pd.merge(df1,df2,on="id",how="right")
""")

if st.button("Run Right Join",key="m4"):

    import pandas as pd

    df1=pd.DataFrame({'id':[1,2,3,4],
                      'name':['Aman','Riya','Karan','Simran']})

    df2=pd.DataFrame({'id':[1,2,3,5],
                      'salary':[50000,60000,55000,70000]})

    result=pd.merge(df1,df2,on="id",how="right")

    st.write(result)
st.markdown('<h3 style="color:pink;">Outer Join</h3>', unsafe_allow_html=True)
st.text("Outer join में दोनों DataFrames की सभी rows रहती हैं।")
st.code("""
pd.merge(df1,df2,on="id",how="outer")
""")

if st.button("Run Outer Join",key="m5"):

    import pandas as pd

    df1=pd.DataFrame({'id':[1,2,3,4],
                      'name':['Aman','Riya','Karan','Simran']})

    df2=pd.DataFrame({'id':[1,2,3,5],
                      'salary':[50000,60000,55000,70000]})

    result=pd.merge(df1,df2,on="id",how="outer")

    st.write(result)
st.markdown('<h3 style="color:pink;">Join using Index</h3>', unsafe_allow_html=True)
st.text("join() method index के आधार पर join करता है।")
st.code("""
df1.join(df2)
""")

if st.button("Run Join",key="m6"):

    import pandas as pd

    df1=pd.DataFrame({'name':['Aman','Riya','Karan']},
                     index=[1,2,3])

    df2=pd.DataFrame({'salary':[50000,60000,55000]},
                     index=[1,2,3])

    result=df1.join(df2)

    st.write(result)

#.............................................
st.markdown('<a id="combining-dataframes"></a>', unsafe_allow_html=True)
st.markdown('<h3 style="color:yellow;text-align:center;">Concat DataFrames</h3>', unsafe_allow_html=True)

st.code("""
import pandas as pd

df1=pd.DataFrame({
'name':['Aman','Riya'],
'age':[21,22]
})

df2=pd.DataFrame({
'name':['Karan','Simran'],
'age':[23,24]
})

pd.concat([df1,df2])
""")

if st.button("Run Concat"):

    df1=pd.DataFrame({
    'name':['Aman','Riya'],
    'age':[21,22]
    })

    df2=pd.DataFrame({
    'name':['Karan','Simran'],
    'age':[23,24]
    })

    result=pd.concat([df1,df2])

    st.write(result)

st.markdown('<h3 style="color:yellow;text-align:center;">Pivot Table</h3>', unsafe_allow_html=True)

st.code("""
df.pivot_table(values="salary",index="dept",aggfunc="mean")
""")

if st.button("Run Pivot Table"):

    df=pd.DataFrame({
    'name':['Aman','Riya','Karan','Simran'],
    'dept':['IT','HR','IT','HR'],
    'salary':[50000,60000,55000,65000]
    })

    result=df.pivot_table(values="salary",index="dept",aggfunc="mean")

    st.write(result)

st.markdown('<h3 style="color:yellow;text-align:center;">Crosstab</h3>', unsafe_allow_html=True)

st.code("""
pd.crosstab(df['dept'],df['gender'])
""")

if st.button("Run Crosstab"):

    df=pd.DataFrame({
    'dept':['IT','HR','IT','HR','IT'],
    'gender':['Male','Female','Male','Female','Female']
    })

    result=pd.crosstab(df['dept'],df['gender'])

    st.write(result)

st.markdown('<h2 style="color:cyan;text-align:center;">📌 Conclusion</h2>', unsafe_allow_html=True)

st.markdown("""  

### Summary

Pandas is one of the most powerful Python libraries for handling structured data.  
It provides flexible and efficient tools to clean, transform, analyze, and summarize data.

By understanding these concepts, we can perform effective data analysis and build strong data processing workflows using Python.
""")
st.markdown('<a id="p"></a>', unsafe_allow_html=True)
st.markdown('<h2 style="color:cyan;">Practice Ouestion</h2>', unsafe_allow_html=True)
st.markdown("[Pandas Data Series](https://www.w3resource.com/python-exercises/pandas/index-data-series.php)")
st.markdown("[Pandas DataFrame](https://www.w3resource.com/python-exercises/pandas/index-dataframe.php)")
st.markdown("[Pandas Index](https://www.w3resource.com/python-exercises/pandas/index/index.php)")
st.markdown("[Pandas advance Indexing and Slicing](https://www.w3resource.com/python-exercises/pandas/pandas-advanced-indexing-and-slicing.php)")
st.markdown("[Pandas Filter](https://www.w3resource.com/python-exercises/pandas/filter/index.php)")
st.markdown("[Pandas Joining and Merging DataFrames](https://www.w3resource.com/python-exercises/pandas/joining-and-merging/index.php)")
st.markdown("[Pandas Advancec Merging and Joining](https://www.w3resource.com/python-exercises/pandas/pandas-advanced-merging-and-joining.php)")
st.markdown("[Pandas Grouping and Aggregation](https://www.w3resource.com/python-exercises/pandas/groupby/index.php)")
st.markdown("[Pandas Advancced Grouping and Aggregation](https://www.w3resource.com/python-exercises/pandas/advanced-grouping-and-aggregation/index.php)")
st.markdown("[Pandas String and Regular Expression](https://www.w3resource.com/python-exercises/pandas/string/index.php)")
st.markdown("[Pandas Time Series](https://www.w3resource.com/python-exercises/pandas/time-series/index.php)")
st.markdown("[Pandas Datetime](https://www.w3resource.com/python-exercises/pandas/datetime/index.php)")
st.markdown("[Pandas Resampling and Frequency Conversion](https://www.w3resource.com/python-exercises/pandas/resampling-frequency-conversion/index.php)")
st.markdown("[Pandas Handling Missing Value](https://www.w3resource.com/python-exercises/pandas/missing-values/index.php)")
st.markdown("[Pandas Data Cleaning and Preprocessing](https://www.w3resource.com/python-exercises/pandas/pandas-data-cleaning-and-preprocessing.php)")
st.markdown("[Pandas Pivot Table](https://www.w3resource.com/python-exercises/pandas/excel/index-pivot.php)")
st.markdown("[Pandas Custom Function](https://www.w3resource.com/python-exercises/pandas/pandas-custom-functions-and-apply-exercises.php)")
#st.markdown("[Pandas Pivot ](https://www.google.com)")
#st.markdown("[Pandas Custom Function](https://www.google.com)")
st.markdown("[Pandas Data Validation](https://www.w3resource.com/python-exercises/pandas/pandas-data-validation.php)")
st.markdown("[Pandas Performance Optimization](https://www.w3resource.com/python-exercises/pandas/pandas-visualization-integration.php)")
st.markdown("[Pandas Plotting](https://www.w3resource.com/python-exercises/pandas/plotting/index.php)")
st.markdown("[Pandas Visualization Integration](https://www.w3resource.com/python-exercises/pandas/pandas-visualization-integration.php)")
st.markdown("[Pandas Style](https://www.w3resource.com/python-exercises/pandas/style/index.php)")
st.markdown("[Pandas Excel Data Analysis](https://www.w3resource.com/python-exercises/pandas/excel/index.php)")
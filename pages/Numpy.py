import streamlit as st
import pandas as pd
import time
import numpy as np
import seaborn as sns

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
@import url('https://fonts.googleapis.com/css2?family=Playfair+Script&display=swap');

.title {
    font-family: 'Playfair Script', cursive;
    font-size: 60px;
    text-align: center;
    color: #2C3E50;
}
</style>

<h1 class="title">Numpy</h1>
""", unsafe_allow_html=True)


toc = """
##  NumPy Table of Contents

1. [Introduction](#intro)
2. [Getting Started](#g)
3. [Creating Arrays](#c)
4. [Array Indexing](#a)
5. [Array Slicing](#as)
6. [Data Types](#d)
7. [Copy vs View](#cv)
8. [Array Shape](#ash)
9. [Array Reshape](#ar)
10. [Array Iterating](#ai)
11. [Array Join](#aj)
12. [Array Split](#asp)
13. [Array Search](#ase)
14. [Array Sort](#aso)
15. [Array Filter](#af)
16. [All function of creating array](#f)
17. [Practice Question](#p)
"""

st.sidebar.markdown(toc)
st.markdown(toc)



#Intro...........
st.markdown("<a id='intro'></a>",unsafe_allow_html=True)
st.markdown('<h1 style="  text-align: center;">Numpy</h1>', unsafe_allow_html=True)
st.text("""NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

NumPy stands for Numerical Python.""")
st.markdown('<h3 style=" color :pink;">Why Use NumPy?</h3>', unsafe_allow_html=True)
st.text("""In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.

""")
st.success("Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.")
st.markdown('<h3 style=" color :pink;">Why is NumPy Faster Than Lists?</h3>', unsafe_allow_html=True)
st.text("""NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.""")
st.markdown('<h3 style=" color :pink;">Which Language is NumPy written in?</h3>', unsafe_allow_html=True)
st.text("NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.")

st.markdown("<a id='g'></a>", unsafe_allow_html=True)





st.title("Installation of NumPy")
st.text("""If you have Python and PIP already installed on a system, then installation of NumPy is very easy.

Install it using this command:

""")
st.code("pip install numpy")
st.text("If this command fails, then use a python distribution that already has NumPy installed like, Anaconda, Spyder etc.")
st.markdown('<h3 style=" color :pink;">Import NumPy</h3>', unsafe_allow_html=True)
st.text("Once NumPy is installed, import it in your applications by adding the import keyword:")
st.code("import numpy")
st.text("Now NumPy is imported and ready to use.")
st.success("Example")
st.code("""import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)""")

st.markdown('<h3 style=" color :pink;">NumPy as np</h3>', unsafe_allow_html=True)
st.text("NumPy is usually imported under the np alias.")
st.success("alias: In Python alias are an alternate name for referring to the same thing.")
st.text("Create an alias with the as keyword while importing:")
st.code("import numpy as np")
st.text("Now the NumPy package can be referred to as np instead of numpy.")
st.success("Example")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)""")
st.markdown('<h3 style=" color :pink;">Checking NumPy Version</h3>', unsafe_allow_html=True)
st.text("The version string is stored under __version__ attribute.")
st.success("Example")
st.code("""import numpy as np

print(np.__version__)""")





       
st.markdown("<a id='c'></a>", unsafe_allow_html=True)       # Creating Arrays
st.title("Create a NumPy ndarray Object")

st.text("""NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.
""")

st.success("Example")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))""")

st.text("type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.")

st.text("""To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:""")

st.success("Example")
st.text("Use a tuple to create a NumPy array:")
st.code("""import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)""")

st.markdown('<h3 style=" color :pink;">Dimensions in Arrays</h3>', unsafe_allow_html=True)

st.text("""A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements.
""")

st.markdown('<h3 style=" color :pink;">0-D Arrays</h3>', unsafe_allow_html=True)

st.text("""0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.""")

st.success("Example")
st.text("Create a 0-D array with value 42")
st.code("""import numpy as np

arr = np.array(42)

print(arr)""")

st.markdown('<h3 style=" color :pink;">1-D Arrays</h3>', unsafe_allow_html=True)

st.text("""An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.
""")

st.success("Example")
st.text("Create a 1-D array containing the values 1,2,3,4,5:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)""")

st.markdown('<h3 style=" color :pink;">2-D Arrays</h3>', unsafe_allow_html=True)

st.text("""An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.

NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
""")

st.success("Example")
st.text("Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:")
st.code("""import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)""")

st.markdown('<h3 style=" color :pink;">3-D arrays</h3>', unsafe_allow_html=True)

st.text("""An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.
""")

st.success("Example")
st.text("Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:")
st.code("""import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)""")

st.markdown('<h3 style=" color :pink;">Check Number of Dimensions?</h3>', unsafe_allow_html=True)

st.text("""NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.""")

st.success("Example")
st.text("Check how many dimensions the arrays have:")
st.code("""import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)""")

st.markdown('<h3 style=" color :pink;">Higher Dimensional Arrays</h3>', unsafe_allow_html=True)

st.text("""An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.
""")

st.success("Example")
st.text("Create an array with 5 dimensions and verify that it has 5 dimensions:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)""")

st.text("""In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
""")

st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.text("Consider the following array:")
st.code("""arr = np.array([[1, 2, 3], [4, 5, 6]])""")

st.text("How many dimensions does it have?")

st.text("""
1  
2  
3
""")





st.markdown("<a id='a'></a>", unsafe_allow_html=True)       # Array Indexing
st.title("NumPy Array Indexing")

st.markdown('<h3 style=" color :pink;">Access Array Elements</h3>', unsafe_allow_html=True)

st.text("""Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
""")

st.success("Example")
st.text("Get the first element from the following array:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])""")

st.success("Example")
st.text("Get the second element from the following array.")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])""")

st.success("Example")
st.text("Get third and fourth elements from the following array and add them.")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])""")

st.markdown('<h3 style=" color :pink;">Access 2-D Arrays</h3>', unsafe_allow_html=True)

st.text("""To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.
""")

st.success("Example")
st.text("Access the element on the first row, second column:")
st.code("""import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])""")

st.success("Example")
st.text("Access the element on the 2nd row, 5th column:")
st.code("""import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])""")

st.markdown('<h3 style=" color :pink;">Access 3-D Arrays</h3>', unsafe_allow_html=True)

st.text("""To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
""")

st.success("Example")
st.text("Access the third element of the second array of the first array:")
st.code("""import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])""")

st.markdown('<h3 style=" color :pink;">Example Explained</h3>', unsafe_allow_html=True)

st.text("""arr[0, 1, 2] prints the value 6.

The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]

Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]

Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6

Since we selected 2, we end up with the third value:
6
""")

st.markdown('<h3 style=" color :pink;">Negative Indexing</h3>', unsafe_allow_html=True)

st.text("""Use negative indexing to access an array from the end.
""")

st.success("Example")
st.text("Print the last element from the 2nd dim:")
st.code("""import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])""")

st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.text("Consider the following code:")
st.code("""import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[1, 1, 0])""")

st.text("What will be the printed result?")

st.text("""
1  
3  
7  
8
""")





st.markdown("<a id='as'></a>", unsafe_allow_html=True)      # Array Slicing

st.title("NumPy Array Slicing")

st.markdown('<h3 style=" color :pink;">Slicing Arrays</h3>', unsafe_allow_html=True)

st.text("""Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1
""")

st.success("Example")
st.text("Slice elements from index 1 to index 5 from the following array:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])""")

st.text("Note: The result includes the start index, but excludes the end index.")

st.success("Example")
st.text("Slice elements from index 4 to the end of the array:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])""")

st.success("Example")
st.text("Slice elements from the beginning to index 4 (not included):")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])""")

st.markdown('<h3 style=" color :pink;">Negative Slicing</h3>', unsafe_allow_html=True)

st.text("Use the minus operator to refer to an index from the end:")

st.success("Example")
st.text("Slice from the index 3 from the end to index 1 from the end:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])""")

st.markdown('<h3 style=" color :pink;">STEP</h3>', unsafe_allow_html=True)

st.text("Use the step value to determine the step of the slicing:")

st.success("Example")
st.text("Return every other element from index 1 to index 5:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])""")

st.success("Example")
st.text("Return every other element from the entire array:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])""")

st.markdown('<h3 style=" color :pink;">Slicing 2-D Arrays</h3>', unsafe_allow_html=True)

st.success("Example")
st.text("From the second element, slice elements from index 1 to index 4 (not included):")
st.code("""import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])""")

st.text("Note: Remember that second element has index 1.")

st.success("Example")
st.text("From both elements, return index 2:")
st.code("""import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])""")

st.success("Example")
st.text("From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:")
st.code("""import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])""")













st.markdown("<a id='d'></a>", unsafe_allow_html=True)       # Data Types

st.title("NumPy Data Types")

st.markdown('<h3 style=" color :pink;">Data Types in Python</h3>', unsafe_allow_html=True)

st.text("""By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"

integer - used to represent integer numbers. e.g. -1, -2, -3

float - used to represent real numbers. e.g. 1.2, 42.42

boolean - used to represent True or False.

complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
""")

st.markdown('<h3 style=" color :pink;">Data Types in NumPy</h3>', unsafe_allow_html=True)

st.text("""NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.
""")

st.text("""
i - integer  
b - boolean  
u - unsigned integer  
f - float  
c - complex float  
m - timedelta  
M - datetime  
O - object  
S - string  
U - unicode string  
V - fixed chunk of memory for other type (void)
""")

st.markdown('<h3 style=" color :pink;">Checking the Data Type of an Array</h3>', unsafe_allow_html=True)

st.text("""The NumPy array object has a property called dtype that returns the data type of the array:""")

st.success("Example")
st.text("Get the data type of an array object:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)""")

st.success("Example")
st.text("Get the data type of an array containing strings:")
st.code("""import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)""")

st.markdown('<h3 style=" color :pink;">Creating Arrays With a Defined Data Type</h3>', unsafe_allow_html=True)

st.text("""We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:""")

st.success("Example")
st.text("Create an array with data type string:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)""")

st.text("For i, u, f, S and U we can define size as well.")

st.success("Example")
st.text("Create an array with data type 4 bytes integer:")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)""")

st.markdown('<h3 style=" color :pink;">What if a Value Can Not Be Converted?</h3>', unsafe_allow_html=True)

st.text("""If a type is given in which elements can't be casted then NumPy will raise a ValueError.

ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected or incorrect.
""")

st.success("Example")
st.text("A non integer string like 'a' can not be converted to integer (will raise an error):")
st.code("""import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')""")

st.markdown('<h3 style=" color :pink;">Converting Data Type on Existing Arrays</h3>', unsafe_allow_html=True)

st.text("""The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
""")

st.success("Example")
st.text("Change data type from float to integer by using 'i' as parameter value:")
st.code("""import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)""")

st.success("Example")
st.text("Change data type from float to integer by using int as parameter value:")
st.code("""import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)""")

st.success("Example")
st.text("Change data type from integer to boolean:")
st.code("""import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)""")

st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.text("Consider the following code:")
st.code("""import numpy as np
arr = np.array([-1, 0, 1])
newarr = arr.astype(bool)
print(newarr)""")

st.text("What will be the printed result?")

st.text("""
[ True True True]  
[ True False True]  
[ False False True]  
[ False True True]
""")










st.markdown("<a id='cv'></a>", unsafe_allow_html=True)      # Copy vs View
st.title("NumPy Array Copy vs View")

st.markdown('<h3 style=" color :pink;">The Difference Between Copy and View</h3>', unsafe_allow_html=True)

st.text("""The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
""")

# ---------------- COPY ----------------
st.markdown('<h3 style=" color :pink;">COPY</h3>', unsafe_allow_html=True)

st.success("Example")
st.text("Make a copy, change the original array, and display both arrays:")

st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)""")

if st.button("Run Copy Example"):
    import numpy as np
    arr = np.array([1,2,3,4,5])
    x = arr.copy()
    arr[0] = 42

    st.write("Original Array :", arr)
    st.write("Copied Array :", x)

st.info("The copy SHOULD NOT be affected by the changes made to the original array.")

# ---------------- VIEW ----------------
st.markdown('<h3 style=" color :pink;">VIEW</h3>', unsafe_allow_html=True)

st.success("Example")
st.text("Make a view, change the original array, and display both arrays:")

st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)""")

if st.button("Run View Example"):
    import numpy as np
    arr = np.array([1,2,3,4,5])
    x = arr.view()
    arr[0] = 42

    st.write("Original Array :", arr)
    st.write("View Array :", x)

st.info("The view SHOULD be affected by the changes made to the original array.")

# ---------------- CHANGE VIEW ----------------
st.markdown('<h3 style=" color :pink;">Make Changes in the VIEW</h3>', unsafe_allow_html=True)

st.success("Example")
st.text("Make a view, change the view, and display both arrays:")

st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)""")

if st.button("Run View Change Example"):
    import numpy as np
    arr = np.array([1,2,3,4,5])
    x = arr.view()
    x[0] = 31

    st.write("Original Array :", arr)
    st.write("View Array :", x)

st.info("The original array SHOULD be affected by the changes made to the view.")

# ---------------- CHECK BASE ----------------
st.markdown('<h3 style=" color :pink;">Check if Array Owns its Data</h3>', unsafe_allow_html=True)

st.text("""Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base attribute refers to the original object.
""")

st.success("Example")
st.code("""import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)""")

if st.button("Check Base Attribute"):
    import numpy as np
    arr = np.array([1,2,3,4,5])
    x = arr.copy()
    y = arr.view()

    st.write("Copy Base :", x.base)
    st.write("View Base :", y.base)

st.info("The copy returns None. The view returns the original array.")

# ---------------- EXERCISE ----------------
st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.text("Consider the following code:")

st.code("""import numpy as np
original_array = np.array([1, 2, 3])
x = original_array.copy()
x[0] = 5
print(original_array)""")

st.text("What will be the printed result?")

option = st.radio(
    "Choose the correct answer:",
    ("[1 2 3]", "[5 2 3]")
)

if st.button("Check Answer"):
    if option == "[1 2 3]":
        st.success("Correct  Because copy does not affect the original array.")
    else:
        st.error("Incorrect Copy creates a separate array.")


st.markdown("<a id='ash'></a>", unsafe_allow_html=True)      # Array


st.title("NumPy Array Shape")

st.markdown('<h3 style=" color :pink;">Shape of an Array</h3>', unsafe_allow_html=True)

st.text("""The shape of an array is the number of elements in each dimension.
""")

st.markdown('<h3 style=" color :pink;">Get the Shape of an Array</h3>', unsafe_allow_html=True)

st.text("""NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
""")

st.success("Example")
st.text("Print the shape of a 2-D array:")

st.code("""import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)""")

if st.button("Run Shape Example"):
    import numpy as np
    arr = np.array([[1,2,3,4],[5,6,7,8]])
    st.write("Array :")
    st.write(arr)
    st.write("Shape :", arr.shape)

st.info("The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.")

st.success("Example")
st.text("Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:")

st.code("""import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)""")

if st.button("Run 5D Shape Example"):
    import numpy as np
    arr = np.array([1,2,3,4], ndmin=5)
    st.write("Array :")
    st.write(arr)
    st.write("Shape of array :", arr.shape)

st.markdown('<h3 style=" color :pink;">What does the shape tuple represent?</h3>', unsafe_allow_html=True)

st.text("""Integers at every index tells about the number of elements the corresponding dimension has.

In the example above at index-4 we have value 4, so we can say that 5th (4 + 1 th) dimension has 4 elements.
""")

st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.text("Consider the following code:")

st.code("""import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)""")

option = st.radio(
    "What will be the printed result?",
    ("(3, 2)", "(2, 3)", "(2, 2)", "(3, 3)")
)

if st.button("Check Answer",key=1):
    if option == "(2, 3)":
        st.success("Correct  The array has 2 rows and 3 columns.")
    else:
        st.error("Incorrect  Try again.")






st.markdown("<a id='ar'></a>", unsafe_allow_html=True)      # Array Reshape
st.title("NumPy Array Reshaping")

st.markdown('<h3 style=" color :pink;">Reshaping Arrays</h3>', unsafe_allow_html=True)

st.text("""Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.
""")

# ---------------- 1D to 2D ----------------
st.markdown('<h3 style=" color :pink;">Reshape From 1-D to 2-D</h3>', unsafe_allow_html=True)

st.success("Example")
st.text("""Convert the following 1-D array with 12 elements into a 2-D array.

The outermost dimension will have 4 arrays, each with 3 elements:
""")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(4,3)

print(newarr)""")

if st.button("Run 1D → 2D Example"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    newarr = arr.reshape(4,3)
    st.write("Original Array:", arr)
    st.write("Reshaped Array:")
    st.write(newarr)

# ---------------- 1D to 3D ----------------
st.markdown('<h3 style=" color :pink;">Reshape From 1-D to 3-D</h3>', unsafe_allow_html=True)

st.success("Example")
st.text("""Convert the following 1-D array with 12 elements into a 3-D array.

The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
""")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(2,3,2)

print(newarr)""")

if st.button("Run 1D → 3D Example"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    newarr = arr.reshape(2,3,2)
    st.write("Reshaped 3D Array:")
    st.write(newarr)

# ---------------- Can reshape any shape ----------------
st.markdown('<h3 style=" color :pink;">Can We Reshape Into Any Shape?</h3>', unsafe_allow_html=True)

st.text("""Yes, as long as the elements required for reshaping are equal in both shapes.

We can reshape an 8 element array into 2x4 or 4x2 but not into 3x3 because that would require 9 elements.
""")

st.success("Example (Error Case)")
st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

newarr = arr.reshape(3,3)

print(newarr)""")

if st.button("Try Invalid Reshape"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6,7,8])
    try:
        newarr = arr.reshape(3,3)
        st.write(newarr)
    except Exception as e:
        st.error(e)

# ---------------- Copy or View ----------------
st.markdown('<h3 style=" color :pink;">Returns Copy or View?</h3>', unsafe_allow_html=True)

st.success("Example")
st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

print(arr.reshape(2,4).base)""")

if st.button("Check View"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6,7,8])
    st.write(arr.reshape(2,4).base)

st.info("If it prints the original array then reshape returns a view.")

# ---------------- Unknown Dimension ----------------
st.markdown('<h3 style=" color :pink;">Unknown Dimension</h3>', unsafe_allow_html=True)

st.text("""You are allowed to have one unknown dimension.

Pass -1 as the value and NumPy will automatically calculate the correct dimension.
""")

st.success("Example")
st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

newarr = arr.reshape(2,2,-1)

print(newarr)""")

if st.button("Run -1 Dimension Example"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6,7,8])
    newarr = arr.reshape(2,2,-1)
    st.write(newarr)

# ---------------- Flatten ----------------
st.markdown('<h3 style=" color :pink;">Flattening the Arrays</h3>', unsafe_allow_html=True)

st.text("Flattening means converting a multidimensional array into a 1-D array.")

st.success("Example")
st.code("""import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

newarr = arr.reshape(-1)

print(newarr)""")

if st.button("Flatten Array"):
    import numpy as np
    arr = np.array([[1,2,3],[4,5,6]])
    newarr = arr.reshape(-1)
    st.write("Flattened Array:", newarr)
st.markdown("<a id='ai'></a>", unsafe_allow_html=True)      # Array Iterating
st.title("NumPy Array Iterating")

st.markdown('<h3 style=" color :pink;">Iterating Arrays</h3>', unsafe_allow_html=True)

st.text("""Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through each element one by one.
""")

# ---------------- 1D ARRAY ----------------
st.success("Example")
st.text("Iterate on the elements of the following 1-D array:")

st.code("""import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)""")

if st.button("Run 1D Iteration"):
    import numpy as np
    arr = np.array([1,2,3])
    for x in arr:
        st.write(x)

# ---------------- 2D ARRAY ----------------
st.markdown('<h3 style=" color :pink;">Iterating 2-D Arrays</h3>', unsafe_allow_html=True)

st.success("Example")
st.text("Iterate on the elements of the following 2-D array:")

st.code("""import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)""")

if st.button("Run 2D Row Iteration"):
    import numpy as np
    arr = np.array([[1,2,3],[4,5,6]])
    for x in arr:
        st.write(x)

st.text("To return the actual scalar values we need nested loops.")

st.success("Example")
st.code("""import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y)""")

if st.button("Run 2D Scalar Iteration"):
    import numpy as np
    arr = np.array([[1,2,3],[4,5,6]])
    for x in arr:
        for y in x:
            st.write(y)

# ---------------- 3D ARRAY ----------------
st.markdown('<h3 style=" color :pink;">Iterating 3-D Arrays</h3>', unsafe_allow_html=True)

st.success("Example")
st.text("Iterate on the elements of the following 3-D array:")

st.code("""import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in arr:
    print(x)""")

if st.button("Run 3D Iteration"):
    import numpy as np
    arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
    for x in arr:
        st.write(x)

st.success("Iterate down to the scalars:")

st.code("""import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)""")

if st.button("Run 3D Scalar Iteration"):
    import numpy as np
    arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
    for x in arr:
        for y in x:
            for z in y:
                st.write(z)

# ---------------- NDITER ----------------
st.markdown('<h3 style=" color :pink;">Iterating Arrays Using nditer()</h3>', unsafe_allow_html=True)

st.text("nditer() helps iterate through each scalar element easily.")

st.success("Example")
st.code("""import numpy as np

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for x in np.nditer(arr):
    print(x)""")

if st.button("Run nditer Example"):
    import numpy as np
    arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
    for x in np.nditer(arr):
        st.write(x)

# ---------------- DATA TYPE ITERATION ----------------
st.markdown('<h3 style=" color :pink;">Iterating Array With Different Data Types</h3>', unsafe_allow_html=True)

st.success("Example")
st.code("""import numpy as np

arr = np.array([1,2,3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)""")

if st.button("Run DataType Iteration"):
    import numpy as np
    arr = np.array([1,2,3])
    for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
        st.write(x)

# ---------------- STEP ITERATION ----------------
st.markdown('<h3 style=" color :pink;">Iterating With Different Step Size</h3>', unsafe_allow_html=True)

st.success("Example")
st.code("""import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

for x in np.nditer(arr[:, ::2]):
    print(x)""")

if st.button("Run Step Iteration"):
    import numpy as np
    arr = np.array([[1,2,3,4],[5,6,7,8]])
    for x in np.nditer(arr[:, ::2]):
        st.write(x)

# ---------------- NDENUMERATE ----------------
st.markdown('<h3 style=" color :pink;">Enumerated Iteration Using ndenumerate()</h3>', unsafe_allow_html=True)

st.success("Example")
st.code("""import numpy as np

arr = np.array([1,2,3])

for idx, x in np.ndenumerate(arr):
    print(idx, x)""")

if st.button("Run 1D Enumeration"):
    import numpy as np
    arr = np.array([1,2,3])
    for idx, x in np.ndenumerate(arr):
        st.write(idx, x)

st.success("Example")
st.code("""import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)""")

if st.button("Run 2D Enumeration"):
    import numpy as np
    arr = np.array([[1,2,3,4],[5,6,7,8]])
    for idx, x in np.ndenumerate(arr):
        st.write(idx, x)

# ---------------- EXERCISE ----------------
st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.code("""import numpy as np
arr = np.array(['a', 'b', 'c'])
for x in arr:
    print('Hello ' + x)""")

answer = st.radio(
    "What will be the printed result?",
    (
        "Hello a b c",
        "Hello ['a', 'b', 'c']",
        "Hello a\nHello b\nHello c"
    )
)

if st.button("Check Answer",key=2):
    if answer == "Hello a\nHello b\nHello c":
        st.success("Correct ")
    else:
        st.error("Incorrect ")
st.markdown("<a id='aj'></a>", unsafe_allow_html=True)      # Array Join
st.title("NumPy Joining Arrays")

st.markdown('<h3 style=" color :pink;">Joining NumPy Arrays</h3>', unsafe_allow_html=True)

st.text("""Joining means putting contents of two or more arrays into a single array.

In SQL we join tables based on keys, but in NumPy we join arrays using axes.

The concatenate() function is used to join arrays.
If axis is not specified, NumPy joins arrays along axis = 0 by default.
""")

# ---------------- CONCATENATE ----------------

st.success("Example : Join Two 1-D Arrays")

st.code("""import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1, arr2))

print(arr)""")

if st.button("Run Concatenate Example"):
    import numpy as np
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])
    arr = np.concatenate((arr1,arr2))
    st.write(arr)


# ---------------- CONCATENATE 2D ----------------

st.markdown('<h3 style=" color :pink;">Join 2-D Arrays</h3>', unsafe_allow_html=True)

st.success("Example : Join 2D arrays along columns (axis=1)")

st.code("""import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)""")

if st.button("Run 2D Join"):
    import numpy as np
    arr1 = np.array([[1,2],[3,4]])
    arr2 = np.array([[5,6],[7,8]])
    arr = np.concatenate((arr1,arr2),axis=1)
    st.write(arr)


# ---------------- STACK ----------------

st.markdown('<h3 style=" color :pink;">Joining Arrays Using stack()</h3>', unsafe_allow_html=True)

st.text("""Stacking is similar to concatenation but stacking creates a new axis.""")

st.success("Example")

st.code("""import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.stack((arr1,arr2), axis=1)

print(arr)""")

if st.button("Run Stack Example"):
    import numpy as np
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])
    arr = np.stack((arr1,arr2),axis=1)
    st.write(arr)


# ---------------- HSTACK ----------------

st.markdown('<h3 style=" color :pink;">Stacking Along Rows (hstack)</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.hstack((arr1,arr2))

print(arr)""")

if st.button("Run hstack"):
    import numpy as np
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])
    arr = np.hstack((arr1,arr2))
    st.write(arr)


# ---------------- VSTACK ----------------

st.markdown('<h3 style=" color :pink;">Stacking Along Columns (vstack)</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.vstack((arr1,arr2))

print(arr)""")

if st.button("Run vstack"):
    import numpy as np
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])
    arr = np.vstack((arr1,arr2))
    st.write(arr)


# ---------------- DSTACK ----------------

st.markdown('<h3 style=" color :pink;">Stacking Along Depth (dstack)</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.dstack((arr1,arr2))

print(arr)""")

if st.button("Run dstack"):
    import numpy as np
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])
    arr = np.dstack((arr1,arr2))
    st.write(arr)


# ---------------- EXERCISE ----------------

st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.code("""Which NumPy function is used to join two or more arrays?

A. join_array()
B. concatenate()
C. join()
""")

ans = st.radio(
    "Choose the correct answer",
    ("join_array()", "concatenate()", "join()")
)

if st.button("Check Answer",key=3):
    if ans == "concatenate()":
        st.success("Correct Answer ")
    else:
        st.error("Incorrect  Try Again")
st.markdown("<a id='asp'></a>", unsafe_allow_html=True)     # Array Split
st.title("NumPy Splitting Arrays")

st.markdown('<h3 style=" color :pink;">Splitting NumPy Arrays</h3>', unsafe_allow_html=True)

st.text("""Splitting is the reverse operation of Joining.

Joining merges multiple arrays into one array,
while Splitting breaks one array into multiple arrays.

In NumPy we use array_split() function to split arrays.
We pass the array and the number of splits required.
""")

# ---------------- BASIC SPLIT ----------------

st.success("Example : Split Array into 3 Parts")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,3)

print(newarr)""")

if st.button("Run Split Example"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6])
    newarr = np.array_split(arr,3)
    st.write(newarr)


# ---------------- SPLIT INTO 4 ----------------

st.markdown('<h3 style=" color :pink;">Split Array into 4 Parts</h3>', unsafe_allow_html=True)

st.text("If elements are not equal, NumPy adjusts automatically.")

st.success("Example")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,4)

print(newarr)""")

if st.button("Run Split into 4"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6])
    newarr = np.array_split(arr,4)
    st.write(newarr)


# ---------------- ACCESS SPLIT ARRAYS ----------------

st.markdown('<h3 style=" color :pink;">Access Split Arrays</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,3)

print(newarr[0])
print(newarr[1])
print(newarr[2])""")

if st.button("Access Split Parts"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6])
    newarr = np.array_split(arr,3)
    st.write("First Part:", newarr[0])
    st.write("Second Part:", newarr[1])
    st.write("Third Part:", newarr[2])


# ---------------- SPLIT 2D ARRAY ----------------

st.markdown('<h3 style=" color :pink;">Splitting 2-D Arrays</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])

newarr = np.array_split(arr,3)

print(newarr)""")

if st.button("Run 2D Split"):
    import numpy as np
    arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
    newarr = np.array_split(arr,3)
    st.write(newarr)


# ---------------- SPLIT ALONG AXIS ----------------

st.markdown('<h3 style=" color :pink;">Split Along Columns (axis=1)</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12],
                [13,14,15],
                [16,17,18]])

newarr = np.array_split(arr,3,axis=1)

print(newarr)""")

if st.button("Run Axis Split"):
    import numpy as np
    arr = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15],
                    [16,17,18]])
    newarr = np.array_split(arr,3,axis=1)
    st.write(newarr)


# ---------------- HSPLIT ----------------

st.markdown('<h3 style=" color :pink;">Split Using hsplit()</h3>', unsafe_allow_html=True)

st.text("hsplit() is the opposite of hstack() and splits arrays column-wise.")

st.success("Example")

st.code("""import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

newarr = np.hsplit(arr,3)

print(newarr)""")

if st.button("Run hsplit"):
    import numpy as np
    arr = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
    newarr = np.hsplit(arr,3)
    st.write(newarr)


# ---------------- EXERCISE ----------------

st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.code("""Which NumPy function is used to split an array into multiple arrays?

A. array_split()
B. decatenate()
C. decat()
""")

ans = st.radio(
    "Choose the correct answer",
    ("array_split()", "decatenate()", "decat()")
)

if st.button("Check Answer",key=5):
    if ans == "array_split()":
        st.success("Correct Answer ")
    else:
        st.error("Incorrect  Try Again")
st.markdown("<a id='ase'></a>", unsafe_allow_html=True)     # Array Search
st.title("NumPy Searching Arrays")

st.markdown('<h3 style=" color :pink;">Searching Arrays</h3>', unsafe_allow_html=True)

st.text("""You can search an array for a certain value and return the indexes that match.

To search an array we use the where() method.
It returns the indexes where the condition is true.
""")

# ---------------- SEARCH VALUE ----------------

st.success("Example : Find Indexes Where Value = 4")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,4,4])

x = np.where(arr == 4)

print(x)""")

if st.button("Run Search Value Example"):
    import numpy as np
    arr = np.array([1,2,3,4,5,4,4])
    x = np.where(arr == 4)
    st.write(x)


# ---------------- EVEN NUMBERS ----------------

st.markdown('<h3 style=" color :pink;">Find Even Numbers</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

x = np.where(arr % 2 == 0)

print(x)""")

if st.button("Run Even Search"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6,7,8])
    x = np.where(arr % 2 == 0)
    st.write(x)


# ---------------- ODD NUMBERS ----------------

st.markdown('<h3 style=" color :pink;">Find Odd Numbers</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

x = np.where(arr % 2 == 1)

print(x)""")

if st.button("Run Odd Search"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6,7,8])
    x = np.where(arr % 2 == 1)
    st.write(x)


# ---------------- SEARCHSORTED ----------------

st.markdown('<h3 style=" color :pink;">Search Sorted Array</h3>', unsafe_allow_html=True)

st.text("""searchsorted() performs a binary search and returns the index 
where a value should be inserted to maintain sorted order.""")

st.success("Example")

st.code("""import numpy as np

arr = np.array([6,7,8,9])

x = np.searchsorted(arr,7)

print(x)""")

if st.button("Run searchsorted"):
    import numpy as np
    arr = np.array([6,7,8,9])
    x = np.searchsorted(arr,7)
    st.write(x)


# ---------------- RIGHT SIDE SEARCH ----------------

st.markdown('<h3 style=" color :pink;">Search From Right Side</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([6,7,8,9])

x = np.searchsorted(arr,7, side='right')

print(x)""")

if st.button("Run Right Search"):
    import numpy as np
    arr = np.array([6,7,8,9])
    x = np.searchsorted(arr,7, side='right')
    st.write(x)


# ---------------- MULTIPLE VALUES ----------------

st.markdown('<h3 style=" color :pink;">Search Multiple Values</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([1,3,5,7])

x = np.searchsorted(arr,[2,4,6])

print(x)""")

if st.button("Run Multiple Search"):
    import numpy as np
    arr = np.array([1,3,5,7])
    x = np.searchsorted(arr,[2,4,6])
    st.write(x)


# ---------------- EXERCISE ----------------

st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.code("""import numpy as np
arr = np.array([15, 38, 41, 46])
x = np.where(arr % 2 == 1)
print(x)
""")

ans = st.radio(
    "What will be the output?",
    (
        "(array([1, 3]),)",
        "(array([15, 41]),)",
        "(array([0, 2]),)",
        "(array([38, 46]),)"
    )
)

if st.button("Check Answer",key=6):
    if ans == "(array([0, 2]),)":
        st.success("Correct Answer ")
    else:
        st.error("Incorrect  Try Again")
st.markdown("<a id='aso'></a>", unsafe_allow_html=True)     # Array Sort
st.title("NumPy Sorting Arrays")

st.markdown('<h3 style=" color :pink;">Sorting Arrays</h3>', unsafe_allow_html=True)

st.text("""Sorting means putting elements in an ordered sequence.

An ordered sequence can be numeric or alphabetical,
and can be arranged in ascending or descending order.

NumPy provides a function called sort() which sorts the array.
It returns a sorted copy and does not change the original array.
""")

# ---------------- SORT NUMBERS ----------------

st.success("Example : Sort Numeric Array")

st.code("""import numpy as np

arr = np.array([3,2,0,1])

print(np.sort(arr))""")

if st.button("Run Numeric Sort"):
    import numpy as np
    arr = np.array([3,2,0,1])
    st.write(np.sort(arr))


# ---------------- SORT STRINGS ----------------

st.markdown('<h3 style=" color :pink;">Sorting String Arrays</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array(['banana','cherry','apple'])

print(np.sort(arr))""")

if st.button("Run String Sort"):
    import numpy as np
    arr = np.array(['banana','cherry','apple'])
    st.write(np.sort(arr))


# ---------------- SORT BOOLEAN ----------------

st.markdown('<h3 style=" color :pink;">Sorting Boolean Arrays</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))""")

if st.button("Run Boolean Sort"):
    import numpy as np
    arr = np.array([True, False, True])
    st.write(np.sort(arr))


# ---------------- SORT 2D ARRAY ----------------

st.markdown('<h3 style=" color :pink;">Sorting 2-D Arrays</h3>', unsafe_allow_html=True)

st.text("When sorting a 2-D array, each row is sorted individually.")

st.success("Example")

st.code("""import numpy as np

arr = np.array([[3,2,4],[5,0,1]])

print(np.sort(arr))""")

if st.button("Run 2D Sort"):
    import numpy as np
    arr = np.array([[3,2,4],[5,0,1]])
    st.write(np.sort(arr))


# ---------------- EXERCISE ----------------

st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.code("""import numpy as np
arr = np.array([True, False, True])
print(np.sort(arr))
""")

ans = st.radio(
    "What will be the output?",
    (
        "[False True True]",
        "[True True False]",
        "[True False True]"
    )
)

if st.button("Check Answer",key=8):
    if ans == "[False True True]":
        st.success("Correct Answer ")
    else:
        st.error("Incorrect  Try Again")
st.markdown("<a id='af'></a>", unsafe_allow_html=True)      # Array Filter

st.title("NumPy Filter Arrays")

st.markdown('<h3 style=" color :pink;">Filtering Arrays</h3>', unsafe_allow_html=True)

st.text("""Filtering means selecting some elements from an existing array
and creating a new array from them.

In NumPy, filtering is done using a boolean index list.

If the value at an index is True, that element is included in the new array.
If the value is False, that element is excluded.
""")

# ---------------- BASIC FILTER ----------------

st.success("Example : Filter Using Boolean List")

st.code("""import numpy as np

arr = np.array([41,42,43,44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)""")

if st.button("Run Boolean Filter"):
    import numpy as np
    arr = np.array([41,42,43,44])
    x = [True, False, True, False]
    newarr = arr[x]
    st.write(newarr)


# ---------------- FILTER USING LOOP ----------------

st.markdown('<h3 style=" color :pink;">Create Filter Array Using Condition</h3>', unsafe_allow_html=True)

st.success("Example : Values Greater Than 42")

st.code("""import numpy as np

arr = np.array([41,42,43,44])

filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)""")

if st.button("Run Condition Filter"):
    import numpy as np
    arr = np.array([41,42,43,44])
    
    filter_arr = []
    for element in arr:
        if element > 42:
            filter_arr.append(True)
        else:
            filter_arr.append(False)

    newarr = arr[filter_arr]

    st.write("Filter Array:", filter_arr)
    st.write("Filtered Values:", newarr)


# ---------------- EVEN FILTER ----------------

st.markdown('<h3 style=" color :pink;">Filter Even Numbers</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6,7])

filter_arr = []

for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)""")

if st.button("Run Even Filter"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6,7])

    filter_arr = []
    for element in arr:
        if element % 2 == 0:
            filter_arr.append(True)
        else:
            filter_arr.append(False)

    newarr = arr[filter_arr]

    st.write("Filter Array:", filter_arr)
    st.write("Filtered Values:", newarr)


# ---------------- DIRECT FILTER ----------------

st.markdown('<h3 style=" color :pink;">Create Filter Directly From Array</h3>', unsafe_allow_html=True)

st.success("Example : Values Greater Than 42")

st.code("""import numpy as np

arr = np.array([41,42,43,44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)""")

if st.button("Run Direct Filter"):
    import numpy as np
    arr = np.array([41,42,43,44])

    filter_arr = arr > 42
    newarr = arr[filter_arr]

    st.write("Filter Array:", filter_arr)
    st.write("Filtered Values:", newarr)


# ---------------- DIRECT EVEN FILTER ----------------

st.markdown('<h3 style=" color :pink;">Direct Even Number Filter</h3>', unsafe_allow_html=True)

st.success("Example")

st.code("""import numpy as np

arr = np.array([1,2,3,4,5,6,7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)""")

if st.button("Run Direct Even Filter"):
    import numpy as np
    arr = np.array([1,2,3,4,5,6,7])

    filter_arr = arr % 2 == 0
    newarr = arr[filter_arr]

    st.write("Filter Array:", filter_arr)
    st.write("Filtered Values:", newarr)


# ---------------- EXERCISE ----------------

st.markdown('<h3 style=" color :pink;">Exercise</h3>', unsafe_allow_html=True)

st.code("""import numpy as np
arr = np.array(['a','b','c'])

x = arr[[True, False, True]]

print(x)
""")

ans = st.radio(
    "What will be the output?",
    (
        "['b']",
        "['a' 'c']",
        "['a' 'b' 'c']"
    )
)

if st.button("Check Answer",key=9):
    if ans == "['a' 'c']":
        st.success("Correct Answer ")
    else:
        st.error("Incorrect Try Again")

st.markdown("<a id='f'></a>",unsafe_allow_html=True)
st.title("Function")
st.markdown("[All Function For creating Array](https://www.geeksforgeeks.org/numpy/numpy-array-functions/)")
st.title("Practice Question")
st.markdown("<a id='p'></a>",unsafe_allow_html=True)
st.markdown("[Python Numpy basic](https://www.w3resource.com/python-exercises/numpy/basic/index.php)")
st.markdown("[Python Numpy arrays](https://www.w3resource.com/python-exercises/numpy/index-array.php)")
st.markdown("[python numpy Mathematics](https://www.w3resource.com/python-exercises/numpy/python-numpy-math.php)")
st.markdown("[Python Numpy Linear Algebra](https://www.w3resource.com/python-exercises/numpy/linear-algebra/index.php)")
st.markdown("[Python Numpy Statistics](https://www.w3resource.com/python-exercises/numpy/python-numpy-stat.php)")
st.markdown("[Python Numpy Random](https://www.w3resource.com/python-exercises/numpy/python-numpy-random.php)")
st.markdown("[Python Numpy sorting searching](https://www.w3resource.com/python-exercises/numpy/python-numpy-sorting-and-searching.php)")
st.markdown("[Python Numpy indexing](https://www.w3resource.com/python-exercises/numpy/python-numpy-advanced-indexing.php)")
st.markdown("[Python Numpy datetime](https://www.w3resource.com/python-exercises/numpy/python-numpy-datetime.php)")





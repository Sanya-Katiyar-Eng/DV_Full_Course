import streamlit as st
import pandas as pd
if st.button("Back to Home"):
    st.switch_page("main.py")

import time
#Animation
import streamlit as st

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


#sidebarr.............
st.sidebar.markdown("""
                    - [Introduction](#intro),
                    - [creating Array](#create),
                    - [Initial Placeholders (Array genration function)](#place),
                    - [Properties](#pro)""",unsafe_allow_html=True)



#Intro...........
st.markdown("<a id='intro'></a>",unsafe_allow_html=True)
st.text("""In 2005 ,Travis Oliphant ,a scientist and software developer,merged Numeric and Numarray and Named it Numpy.
        
        Founder: Travis Oliphant (2005)

Purpose: High-performance array computing in Python

Core Feature: ndarray object for fast, vectorized operations

Implementation: Written in Python with performance-critical parts in C/C++ for speed

Impact: Integral to libraries like Pandas, SciPy, scikit-learn, and TensorFlow """)

with st.expander("Key Features of Numpy"):
    st.text("""NumPy has various features that make it popular over lists.""")
    with st.expander("N-Dimensional Arrays :"):
        st.text("""NumPy's core feature is ndarray, a N-dimensional array object that supports homogeneous data types.""")
    with st.expander("Arrays with High Performance"):
        st.text("Arrays are stored in contiguous memory locations, enabling faster computations than Python lists (Please see Numpy Array vs Python List for details).")
    with st.expander("Broadcasting: "):
        st.text("This allows element-wise computations between arrays of different shapes. It simplifies operations on arrays of various shapes by automatically aligning their dimensions without creating new data.")
    with st.expander("Vectorization"):
        st.text("Eliminates the need for explicit Python loops by applying operations directly on entire arrays.")
    with st.expander("Linear algebra"):
    
         st.text(""" NumPy contains routines for linear algebra operations, such as matrix multiplication, decompositions, and determinants.""")



# installation.................
st.markdown("<h2 style='color:yellow;'>Installing Numpy in Python</h2>",unsafe_allow_html=True)
st.text("To begin using NumPy, you need to install it first. This can be done using the following pip command:")
st.success("pip install numpy")
st.text("Once installed, import the library with the alias np")
st.success("import numpy as np")


#Creation..............
st.markdown("<a id='create'></a>",unsafe_allow_html=True)
st.markdown("<h2 style='color:yellow;'>Creating Numpy Arrays</h2>",unsafe_allow_html=True)
st.markdown("<h2 style='color:pink;'>1. Using np.array() : </h2>",unsafe_allow_html=True)
st.code("""import numpy as np

a1 = np.array([1, 2, 3])    # 1D array
a2 = np.array([[1, 2], [3, 4]]) # 2D array
a3 = np.array([[[1, 2], [3, 4]],    # 3D array
               [[5, 6], [7, 8]]])

print(a1)
print(a2)
print(a3)""")
if st.button("Run",key=1):
    st.balloons()
    with st.spinner("Loading..."):
        time.sleep(2)
    st.code("""[1 2 3]
[[1 2]
 [3 4]]
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]""")
    
#one dimensional........
st.markdown("<h4 style='color:yellow;'>Creating One Dimensional Array</h4>",unsafe_allow_html=True)
st.text("NumPy one-dimensional arrays are a type of linear array. We can create a NumPy array from Python List, Tuple, and using fromiter() function.")

t=pd.DataFrame({'Creating One Dimensional Array':['From Python List','From Python Tuple','formiter() function'],
                'Example':['np.array([1,2,3,4,5])','np.array((1,2,3,4,5))','np.fromiter((a for a in range(8)),float)']})
st.table(t)
st.code("""# create a NumPy array from a list
li = [1, 2, 3, 4] 
print(np.array(li))

# create a NumPy array from a tuple
tup = (5, 6, 7, 8)
print(np.array(tup))

# create a NumPy array using fromiter()
iterable = (a for a in range(8))
print(np.fromiter(iterable, float))""")

if st.button("Run",key="2"):
    st.balloons()
    with st.spinner("Loading......"):
        time.sleep(2)
    st.success("Output :")
    st.text("""[1 2 3 4]
[5 6 7 8]
[0. 1. 2. 3. 4. 5. 6. 7.]""")
    
#Multi-dimensional........
st.markdown("<h4 style='color:yellow;'>Multi- Dimensional Array</h4>",unsafe_allow_html=True)
st.text("Numpy multi-dimensional arrays are stored in a tabular form, i.e., in the form of rows and columns.")

d=pd.DataFrame({'Create Two Dimensional Array ':['Using python Lists','Using empty()'],
                'Example':['np.array([[1,2,3,4][5,6,7,8][9,10,12]])','np.empty([4,3],dtype=int)']})

st.table(d)
st.code("""# create a NumPy array from a list
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
print(np.array([list_1, list_2, list_3]))

# create a NumPy array using numpy.empty()
print(np.empty([4, 3], dtype=int))""")

if st.button("Run",key="3"):
    st.snow()
    with st.spinner("Loading .."):
        time.sleep(2)
    st.success("Output :")
    st.code("""[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]""")
    

# Initial Placeholders
st.markdown("<a id='place'></a>",unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'>For 1-Dimensional Numpy Arrays</h4>",unsafe_allow_html=True)
st.text("Initial placeholders for a Numpy 1-dimension array can be created by using various Numpy functions.")
d=pd.DataFrame({"Initial Placeholders for 1D Array":["arange()","linespace()","zeros()","ones()","random.rand()","random.randint()"],
                "Example":["np.arange(1,10)","np.linspace(1,10,3)","np.zeros(5,dtype=int)","np.ones(5,dtype=int)","np.random.rand(5)","np.random.randint(5,size=10)"]})
st.table(d)
st.code("""# create a NumPy array using numpy.arange()
print(np.arange(1, 10))

# create a NumPy array using numpy.linspace()
print(np.linspace(1, 10, 3))

# create a NumPy array using numpy.zeros()
print(np.zeros(5, dtype=int))

# create a NumPy array using numpy.ones()
print(np.ones(5, dtype=int))

# create a NumPy array using numpy.random.rand()
print(np.random.rand(5))

# create a NumPy array using numpy.random.randint()
print(np.random.randint(5, size=10))""")

if st.button("Run ",key="5"):
    with st.snipper("Loading."):
        time.sleep(2)
    st.success("Output :")
    st.code("""[1 2 3 4 5 6 7 8 9]
[ 1.   5.5 10. ]
[0 0 0 0 0]
[1 1 1 1 1]
[0.31447226 0.89090771 0.45908938 0.92006507 0.37757036]
[4 3 2 3 1 2 4 1 4 2]""")
    
st.markdown("<h4 style='color:yellow;'>For N-Dimensional Numpy Arrays</h4>",unsafe_allow_html=True)
st.text("Initial placeholders for Numpy two dimension arrays can be created by using various NumPy functions.")
dt=pd.DataFrame({"Initial Placeholders for 2D Array ":["Zeros()","ones()","full()","eye()"],
                "Example":["np.zeros([4,3],dtype=np.int32)","np.ones([4,3],dtype=np.int32)","np.full([2,2],67,dtype=int)","np.eye(4)"]})
st.table(d)

st.code("""# create a NumPy array using numpy.zeros()
print(np.zeros([4, 3], dtype = np.int32))

# create a NumPy array using numpy.ones()
print(np.ones([4, 3], dtype = np.int32))

# create a NumPy array using numpy.full()
print(np.full([2, 2], 67, dtype = int))

# create a NumPy array using numpy.eye()
print(np.eye(4))""")

if st.button("Run ",key="6"):
    with st.spinner("Loading."):
        time.sleep(2)
        st.success("Output :")
        st.code("""[[0 0 0]
 [0 0 0]
 [0 0 0]
 [0 0 0]]
[[1 1 1]
 [1 1 1]
 [1 1 1]
 [1 1 1]]
[[67 67]
 [67 67]]
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]""")
    

#Inspecting Properties
st.markdown("<a id='place'></a>",unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'>Inspecting Properties</h4>",unsafe_allow_html=True)
d=pd.DataFrame({
    "Property": ["Size", "Length", "Shape", "Datatype", "Change Datatype", "Convert to List"],
    "Code": ["arr.size", "len(arr)", "arr.shape", "arr.dtype", "arr.astype('float64')", "arr.tolist()"]})
st.table(d)
st.text("Example 1: One Dimensional Numpy Array")
st.code("""arr = np.asarray([1, 2, 3, 4])
# check size of the array
print("Size:", arr.size)

# check len of the array
print("len:", len(arr))

# check shape of the array
print("Shape:", arr.shape)

# check dtype of the array elements
print("Datatype:", arr.dtype)

# change the dtype to 'float64'
arr = arr.astype('float64')
print(arr)
print("Datatype:", arr.dtype)

# convert array to list
lis = arr.tolist()
print("\nList:", lis)
print(type(lis))""")

if st.button("Run ",key="a"):
    with st.spinner("Loading."):
        time.sleep(2)
    st.success("Output :")
    st.code("""Size: 4
len: 4
Shape: (4,)
Datatype: int64
[1. 2. 3. 4.]
Datatype: float64
List: [1.0, 2.0, 3.0, 4.0]
<class 'list'>""")

st.text("Example 2 : N-Dimensional Numpy Array")
st.code("""# Two dimensional numpy array
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
arr = np.array([list_1, list_2, list_3]) 

# check size of the array
print("Size:", arr.size)

# check length of the array
print("Length:", len(arr))

# check shape of the array
print("Shape:", arr.shape)

# check dtype of the array elements
print("Datatype:", arr.dtype)

# change the dtype to 'float64'
arr = arr.astype('float64')
print(arr)
print(arr.dtype)

# convert array to list
lis = arr.tolist()
print("\nList:", lis)
print(type(lis))""")

if st.button("Run ",key="7"):
    with st.spinner("Loading."):
        time.sleep(2)
    st.success("Output :")
    st.code("""Size: 12
Length: 3
Shape: (3, 4)
Datatype: int64
[[ 1.  2.  3.  4.]
 [ 5.  6.  7.  8.]
 [ 9. 10. 11. 12.]]
float64
List: [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]]
<class 'list'>
""")
    

#Geting information on numpy Function
st.markdown("<h4 style='color:yellow;'>Getting Information on a Numpy Function</h4>",unsafe_allow_html=True)
st.text("The np.info() function is used to get information about any Numpy function, class, or module along with its parameters, return values, and any other information.")
st.code("""import sys
print(np.info(np.add, output=sys.stdout))""")
if st.button("Run ",key="b"):
    with st.spinner("Loading."):
        time.sleep(2)
    st.success("Output :")
    st.code("""add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', 
dtype=None, subok=True[, signature, extobj])
Add arguments element-wise.
Parameters
----------
x1, x2 : array_like
    The arrays to be added.
.....""")


#Saving and Loading File

st.markdown("<a id='load'></a>",unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'>Saving and Loading File</h4>",unsafe_allow_html=True)
st.text("""Numpy arrays can be stored or loaded from a disk file with the '.npy' extension. There are various ways by which we can import a text file in a NumPy array.""")

data = pd.DataFrame({
    "Operation": [
        "Saving array on disk",
        "Loading a file",
        "Importing a Text File",
        "Importing CSV File",
        "Write Text File"
    ],
    "Example": [
        "np.save('file', np.arange(5))",
        "np.load('file.npy')",
        "np.loadtxt('file.txt')",
        "np.genfromtxt('file.csv', delimiter=',')",
        "np.savetxt('file.txt', arr, delimiter=' ')"
    ]
})

st.table(data)

if st.button("Run ",key="8"):
    with st.spinner("Loading."):
        time.sleep(2)
    st.success("Output :")




st.markdown("<a id='place'></a>",unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'>Inspecting Properties</h4>",unsafe_allow_html=True)
if st.button("Run ",key="9"):
    with st.spinner("Loading."):
        time.sleep(2)
    st.success("Output :")






st.markdown("<a id='place'></a>",unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'>Inspecting Properties</h4>",unsafe_allow_html=True)
if st.button("Run ",key="10"):
    with st.spinner("Loading."):
        time.sleep(2)
    st.success("Output :")







st.markdown("<a id='place'></a>",unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'>Inspecting Properties</h4>",unsafe_allow_html=True)
if st.button("Run ",key="11"):
    with st.spinner("Loading."):
        time.sleep(2)
    st.success("Output :")








st.markdown("<a id='place'></a>",unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'>Inspecting Properties</h4>",unsafe_allow_html=True)
if st.button("Run ",key="15"):
    with st.snipper("Loading."):
        time.sleep(2)
    st.success("Output :")






st.markdown("<a id='place'></a>",unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'>Inspecting Properties</h4>",unsafe_allow_html=True)
if st.button("Run ",key="14"):
    with st.snipper("Loading."):
        time.sleep(2)
    st.success("Output :")






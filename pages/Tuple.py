import streamlit as st
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
st.markdown("""
1. [Practice](#p)""")
st.markdown('<h2 style="color:yellow;text-align:center;">Python Tuples</h2>', unsafe_allow_html=True)
st.code("""mytuple = ("apple", "banana", "cherry")""")
st.text("""Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.""")
st.success("Example :")
st.code("""#Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)""")
st.markdown('<h3 style="color:pink;"> Tuple Items</h3>', unsafe_allow_html=True)
st.text("""Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.""")

st.markdown('<h3 style="color:pink;">Ordered</h3>', unsafe_allow_html=True)
st.text("When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.")
st.markdown('<h3 style="color:pink;">Unchangeable</h3>', unsafe_allow_html=True)
st.text("Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.")
st.markdown('<h3 style="color:pink;">Allow Duplicates</h3>', unsafe_allow_html=True)
st.text("Since tuples are indexed, they can have items with the same value:")
st.success("Example")
st.code("""#Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)""")
st.markdown('<h3 style="color:pink;">Tuple Length</h3>', unsafe_allow_html=True)
st.text("To determine how many items a tuple has, use the len() function")
st.success("Example")
st.code("""#Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))""")
st.markdown('<h3 style="color:pink;">Create Tuple With One Item</h3>', unsafe_allow_html=True)
st.text("To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.")
st.success("Example")
st.code("""#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))""")
st.markdown('<h3 style="color:pink;">Tuple Items - Data Types</h3>', unsafe_allow_html=True)
st.text("Tuple items can be of any data type:")
st.success("Example")
st.code("""#String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)""")
st.text("A tuple can contain different data types:")
st.success("Example")
st.code("""#A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")""")
st.markdown('<h3 style="color:pink;">type()</h3>', unsafe_allow_html=True)
st.text("From Python's perspective, tuples are defined as objects with the data type 'tuple':")
st.code("<class 'tuple'>")
st.success("Example")
st.code("""#What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))""")
st.markdown('<h3 style="color:pink;">The tuple() Constructor</h3>', unsafe_allow_html=True)
st.text("It is also possible to use the tuple() constructor to make a tuple.")
st.success("Example")
st.code("""#Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)""")
st.markdown('<h3 style="color:pink;">Python Collections (Arrays)</h3>', unsafe_allow_html=True)
st.write("""There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.""")

st.success("""*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.""")
st.markdown('<a id="p"></a>', unsafe_allow_html=True)
st.markdown('<h2 style="color:cyan;">Practice Ouestion</h2>', unsafe_allow_html=True)
st.markdown("[ practice Question](https://www.w3resource.com/python-exercises/tuple/)")











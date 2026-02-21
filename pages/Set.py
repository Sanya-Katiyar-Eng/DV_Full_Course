import streamlit as st
if st.button("Back to Home"):
    st.switch_page("main.py")


#animation
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












#banner
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



st.set_page_config(page_title="Python Sets Tutorial", layout="wide")

# Sidebar navigation using markdown with anchors
st.sidebar.markdown("""
## 📚 Python Sets
- [Introduction](#introduction)
- [Type Casting](#type-casting)
- [Unique & Immutable](#unique--immutable)
- [Heterogeneous Elements](#heterogeneous-elements)
- [Frozen Sets](#frozen-sets)
- [Methods for Sets](#methods-for-sets)
- [Operators](#operators)
- [Method ](#method)
- [Practice Link](#practice)
""")

# -------------------------
# Introduction
# -------------------------
st.markdown("## Introduction")
st.markdown("""
A **Set** in Python is a collection of **unique items** with the following properties:

- No duplicate elements.
- Unordered collection (cannot access by index).
- Efficient search, insert, delete (uses hashing internally).
- Mutable (add/remove elements), but elements themselves are immutable.
""")
st.code("""
s = {10, 50, 20}
print(s)
print(type(s))
""", language="python")
if st.button("Show Output - Introduction"):
    st.text("""
{10, 50, 20}
<class 'set'>
""")

# -------------------------
# Type Casting
# -------------------------
st.markdown("## Type Casting")
st.markdown("""
You can convert other data types (lists, tuples) into sets using `set()`.
""")
st.code("""
# Convert list to set
s = set(["a", "b", "c"])
print(s)

# Add element
s.add("d")
print(s)
""", language="python")
if st.button("Show Output - Type Casting"):
    st.text("""
{'c', 'b', 'a'}
{'c', 'b', 'a', 'd'}
""")

# -------------------------
# Unique & Immutable
# -------------------------
st.markdown("## Unique & Immutable")
st.markdown("""
- Sets **cannot have duplicates**.  
- Individual elements **cannot be modified** directly. Use `add()` or `remove()`.
""")
st.code("""
s = {"Alpha", "Beta", "Alpha"}
print(s)

# Cannot modify directly
# s[1] = "Gamma"  # This will raise an error
""", language="python")
if st.button("Show Output - Unique & Immutable"):
    st.text("""
{'Alpha', 'Beta'}
TypeError: 'set' object does not support item assignment
""")

# -------------------------
# Heterogeneous Elements
# -------------------------
st.markdown("## Heterogeneous Elements")
st.markdown("""
A set can store **different types**: integers, strings, booleans, floats, etc.
""")
st.code("""
s = {"Alpha", "Beta", 10, 3.14, True}
print(s)
""", language="python")
if st.button("Show Output - Heterogeneous"):
    st.text("""
{True, 3.14, 'Alpha', 10, 'Beta'}
""")

# -------------------------
# Frozen Sets
# -------------------------
st.markdown("## Frozen Sets")
st.markdown("""
A **frozenset** is an **immutable set**. Cannot use `add()` or `remove()`.  
Useful for dictionary keys.
""")
st.code("""
# Mutable set
s = set(["a", "b", "c"])
print("Normal Set:", s)

# Immutable frozenset
fs = frozenset(["x", "y", "z"])
print("Frozen Set:", fs)
""", language="python")
if st.button("Show Output - Frozen Sets"):
    st.text("""
Normal Set: {'c', 'b', 'a'}
Frozen Set: frozenset({'x', 'y', 'z'})
""")

# -------------------------
# Methods for Sets
# -------------------------
st.markdown("## Methods for Sets")
st.markdown("""
Common methods:

1. **add()** → add elements  
2. **union()** → combine sets  
3. **intersection()** → common elements  
4. **difference()** → elements in first set but not in second  
5. **clear()** → remove all elements
""")
st.code("""
# Add elements
s = {"a", "b", "c"}
s.add("d")
print(s)

# Union
a = {"x", "y"}
b = {"y", "z"}
print(a.union(b))

# Intersection
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))

# Difference
print(a.difference(b))

# Clear set
s = {1, 2, 3}
s.clear()
print(s)
""", language="python")
if st.button("Show Output - Methods"):
    st.text("""
{'d', 'c', 'a', 'b'}
{'x', 'y', 'z'}
{2, 3}
{1}
set()
""")

# -------------------------
# Operators
# -------------------------
st.markdown("## Operators")
st.markdown("""
Sets and frozensets support these operators:

| Operator | Meaning |
|----------|---------|
| `key in s` | Check if key exists |
| `key not in s` | Check if key does not exist |
| `s1 == s2` | Sets are equal |
| `s1 != s2` | Sets are not equal |
| `s1 <= s2` | s1 is subset of s2 |
| `s1 < s2` | s1 is proper subset |
| `s1 >= s2` | s1 is superset of s2 |
| `s1 > s2` | s1 is proper superset |
| `s1 | s2` | Union |
| `s1 & s2` | Intersection |
| `s1 - s2` | Difference |
| `s1 ^ s2` | Symmetric difference |
""")
st.code("""
a = {1, 2, 3}
b = {2, 3, 4}

print(2 in a)
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)
""", language="python")
if st.button("Show Output - Operators"):
    st.text("""
True
{1, 2, 3, 4}
{2, 3}
{1}
{1, 4}
""")
    

st.markdown("<a id='method'></a>",unsafe_allow_html=True)
st.subheader("Read alll method")
st.markdown("[click here for Read All Method ](https://www.w3schools.com/python/python_ref_set.asp)")

st.markdown("<a id='practice'></a>",unsafe_allow_html=True)
st.subheader("problem with solution")
st.markdown("[click here for Prctice question ](https://www.w3resource.com/python-exercises/sets/)")

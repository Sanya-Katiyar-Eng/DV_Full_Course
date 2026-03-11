import streamlit as st
import pandas as pd
import time

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





st.title("String Basics to advance : ")
import time

st.set_page_config(page_title="Python Strings ", page_icon="📝", layout="wide")

# -------------------------
# Heading styles
# -------------------------
def colored_header(text, color="yellow", size=35):
    st.markdown(f"<h1 style='color:{color}; font-size:{size}px'>{text}</h1>", unsafe_allow_html=True)

def colored_subheader(text, color="pink", size=22):
    st.markdown(f"<h3 id='{text.replace(' ','')}' style='color:{color}; font-size:{size}px'>{text}</h3>", unsafe_allow_html=True)

# Main heading
colored_header("Python Strings Interactive Tutorial")

st.markdown("""
Welcome! Explore Python **strings** interactively.  
Use the sidebar to jump to a section, or scroll down to see everything.
""")

# -------------------------
# Sidebar Table of Contents
# -------------------------
st.sidebar.markdown("""
###  Topics
- [What is a String](#WhatisaString)
- [String Indexing & Slicing](#StringIndexing&Slicing)
- [String Methods](#StringMethods)
- [String Formatting](#StringFormatting)
- [Concatenation & Repetition](#Concatenation&Repetition)
- [Escape Sequences](#EscapeSequences)
- [Iterating Over a String](#IteratingOveraString)
- [Checking String Properties](#CheckingStringProperties)
- [Raw Strings & Immutability](#RawStrings&Immutability)
- [Tutorial link](#link)
- [ALL Method List](#method)
- [Practice Question](#practice)
""")

# -------------------------
# Tutorial data
# -------------------------
tutorial = {
    "What is a String": {
        "theory": "A string is a sequence of characters enclosed in quotes ('', \"\", or triple quotes). Triple quotes allow multi-line strings.",
        "code": '''str1 = 'Hello'
str2 = "World"
str3 = """This is
a multi-line string"""
print(str1)
print(str2)
print(str3)''',
        "output": """Hello
World
This is
a multi-line string"""
    },
    "String Indexing & Slicing": {
        "theory": "Strings are ordered sequences. Access characters using indexing [0], [-1], or slicing [start:end].",
        "code": '''text = "Python"
print(text[0])
print(text[-1])
print(text[0:4])
print(text[2:])
print(text[:3])''',
        "output": """P
n
Pyth
thon
Pyt"""
    },
    "String Methods": {
        "theory": "Python strings have many methods: upper(), lower(), strip(), replace(), split(), join(), title(), count().",
        "code": '''s = "  hello world  "
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace("world", "Python"))
print(s.split())
print("Python" in s)
print(s.title())
print(s.count("l"))
print(" ".join(["Python","is","fun"]))''',
        "output": """HELLO WORLD
hello world
hello world
  hello Python  
['hello', 'world']
True
Hello World
3
Python is fun"""
    },
    "String Formatting": {
        "theory": "String formatting allows inserting values into strings: f-strings or format().",
        "code": '''name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))''',
        "output": """My name is Alice and I am 25 years old.
My name is Alice and I am 25 years old."""
    },
    "Concatenation & Repetition": {
        "theory": "Concatenation (+) combines strings. Repetition (*) repeats them.",
        "code": '''s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)
print(s1 * 3)''',
        "output": """Hello World
HelloHelloHello"""
    },
    "Escape Sequences": {
        "theory": "Escape sequences: \\n newline, \\t tab, \\\" or \\' quotes.",
        "code": '''print("Line1\\nLine2")
print("Tab\\tSpace")
print("Quote: \\"Hello\\"")''',
        "output": """Line1
Line2
Tab	Space
Quote: "Hello\""""
    },
    "Iterating Over a String": {
        "theory": "Strings are iterable. Loop over each character with a for loop.",
        "code": '''word = "Hi"
for char in word:
    print(char)''',
        "output": """H
i"""
    },
    "Checking String Properties": {
        "theory": "Check string properties: isalpha(), isdigit(), isalnum(). Useful for validation.",
        "code": '''txt = "Python123"
print(txt.isalpha())
print(txt.isdigit())
print(txt.isalnum())''',
        "output": """False
False
True"""
    },
    "Raw Strings & Immutability": {
        "theory": "Raw strings (r'') treat backslashes literally. Strings are immutable.",
        "code": '''path = r"C:\\Users\\Name\\Documents"
print(path)
s = "Hello"
s = "h" + s[1:]
print(s)''',
        "output": """C:\\Users\\Name\\Documents
hello"""
    }
}

# -------------------------
# Display all topics
# -------------------------
for topic, content in tutorial.items():
    colored_subheader(topic, color="pink")
    st.write(content["theory"])
    st.code(content["code"], language="python")
    
    if st.button(f"▶ Run Code: {topic}"):
        st.text(content["output"])
st.markdown("<a id='link'></a>",unsafe_allow_html=True)
st.subheader("you tube tutorial")
st.markdown("[click here for Tutorial](https://www.youtube.com/watch?v=0peYiWVY_Ak&t=29s)")

st.markdown("<a id='method'></a>",unsafe_allow_html=True)
st.subheader("Read alll method")
st.markdown("[click here for Read All Method ](https://www.w3schools.com/python/python_ref_string.asp)")

st.markdown("<a id='practice'></a>",unsafe_allow_html=True)
st.subheader("300 + problem with solution")
st.markdown("[click here for Prctice question ](https://www.w3resource.com/python-exercises/string/)")
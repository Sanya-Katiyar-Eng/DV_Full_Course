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


st.markdown('<h2 style="color:yellow;text-align:center;">Python Functions</h2>', unsafe_allow_html=True)

st.write("""
A **function** is a block of code which runs only when it is called.
Functions help avoid repeating the same code again and again.
They can also return data as a result.
""")
st.markdown('<h3 style="color:pink;">Creating  Functions</h3>', unsafe_allow_html=True)
st.text("In Python, a function is defined using the def keyword, followed by a function name and parentheses:")
st.success("Example :")
st.code("""def my_function():
  print("Hello from a function")""")
st.text("""This creates a function named my_function that prints "Hello from a function" when called.""")
st.success("The code inside the function must be indented. Python uses indentation to define code blocks.")
st.markdown('<h3 style="color:pink;">Calling a Function</h3>', unsafe_allow_html=True)
st.text("To call a function, write its name followed by parentheses:")
st.success("Example")
st.code("""def my_function():
  print("Hello from a function")

my_function()""")
st.text("You can call the same function multiple times:")
st.success("Example")
st.code("""def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()""")

st.markdown('<h3 style="color:pink;">Function Names</h3>', unsafe_allow_html=True)
st.text("""Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)""")
st.success("Example")
st.code("""#Valid function names:

calculate_sum()
_private_function()
myFunction2()""")
st.success("It's good practice to use descriptive names that explain what the function does.")
st.markdown('<h3 style="color:pink;">Why Use Functions ?</h3>', unsafe_allow_html=True)
st.code("Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:")
st.success("Example")
st.code("""#Without functions - repetitive code:

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)""")

st.success("Example")
st.code("""#With functions - reusable code:

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))""")

st.markdown('<h3 style="color:pink;">Return Values</h3>', unsafe_allow_html=True)
st.text("""Functions can send data back to the code that called them using the return statement.

When a function reaches a return statement, it stops executing and sends the result back:""")
st.success("Example")
st.code("""# A function that returns a value:

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)""")
st.text("You can use the returned value directly:")
st.success("Example")
st.code("""# Using the return value directly:

def get_greeting():
  return "Hello from a function"

print(get_greeting())""")
st.success("If a function doesn't have a return statement, it returns None by default.")
st.markdown('<h3 style="color:pink;">The pass Statement</h3>', unsafe_allow_html=True)
st.text("Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:")
st.success("Example")
st.code("""def my_function():
  pass""")
st.text("The pass statement is often used when developing, allowing you to define the structure first and implement details later.")
st.markdown('<a id="p"></a>', unsafe_allow_html=True)
st.markdown('<h2 style="color:cyan;">Practice Ouestion</h2>', unsafe_allow_html=True)
st.markdown("[functions practice](https://www.w3resource.com/python-exercises/python-functions-exercises.php)")








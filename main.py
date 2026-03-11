import streamlit as st
import pandas as pd
import time
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
    <h2 style="color:white;">Welcome : Learn Data Visualization Step by Step</h2>
""", unsafe_allow_html=True)
st.markdown("<h5 style='color:red;'>Transform raw data into meaningful insights through visualization.</h5>",unsafe_allow_html=True)

#Use of side bar ...........................................................................
st.sidebar.title("Go to Topics")

st.sidebar.markdown("""
- [Introduction](#introduction)
- [Keyword](#keyword)
- [Operators](#operators)
- [Input and Output](#inputoutput)
- [control and loop statement](#controlLoop)
- [Type casting](#type)
- [Practice Question](#practice)
- [Intro of Data Visualization](#intro)
- [Loading new page](#load)
- [About Author](#about)
""", unsafe_allow_html=True)


st.markdown("<h3 id='introduction' style='text-align:left; color:yellow;'>Introduction</h3>", unsafe_allow_html=True)

st.text(
        "Python is a high-level, easy-to-learn programming language.\n"
        "It was created by Guido van Rossum in 1991.\n"
        "Python is used to write programs for computers to perform tasks like calculations, data processing, web development, and automation.\n\n"
        "Python is popular because:\n"
        "- It is simple and readable\n"
        "- It uses English-like words\n"
        "- It has fewer lines of code\n"
        "- It works on all operating systems (Windows, Linux, Mac)"
    )

with st.expander("Features of Python"):
        with st.expander("1.Simple and Easy to Learn"):
                     st.text("Python syntax is very easy compared to other languages.")

        with st.expander("2.Interpreted Language"):
                     st.text("Python runs line by line, so errors are easy to find.")
        with st.expander("3.High-Level Language"):
                     st.text("You do not need to manage memory or hardware details.")
        with st.expander("4.Portable"):
                     st.text("A Python program written on one system can run on another system")
        with st.expander("5.Open Source"):
                     st.text("Python is free to use and download.")
        with st.expander("6.Object-Oriented Language"):
                     st.text("Python supports classes and objects.")
with st.expander("Applications of Python"):
        st.write("""Web Development (Django, Flask)

Data Science and Machine Learning

Artificial Intelligence

Game Development

Desktop Applications

Automation and Scripting

Scientific Computing""")
        
        
st.subheader("Create and Run First Python Program")
st.markdown(
    "<h6 style='color:yellow; margin-bottom:0;'>Installation Button</h6>",
    unsafe_allow_html=True
)
st.markdown("""<style>div.stButton>button{background-color:white;color:blue}</style>""",unsafe_allow_html=True)
st.markdown("""<style>div.stLinkButton>a{backgroun-color:white;color:blue}</style>""",unsafe_allow_html=True)
st.link_button("Link for Installed Python","https://www.python.org/downloads/")
st.text("""Once you have Python installed, you can run the program by following these steps:
1.Open a text editor (e.g., Notepad on Windows, TextEdit on macOS, or any code editor like VS Code, PyCharm, etc.).
2.Copy the code: print('Hello World') above and paste it into the text editor.
3.Save the file with .py extension (e.g., Hello.py).
3.Open the terminal.
4.Run the program by pressing Enter.""")
st.markdown("<h8 style='text-align : left;color : yellow;'>program</h8>",unsafe_allow_html=True)
st.code("""
    print("Hello")
    """, language="python")
if st.button("Run program"):
    with st.spinner("Loading"):
                    time.sleep(2)
    st.success("Output:")
    st.write("Hello")
st.markdown("<h3 style='text-align:left; color:yellow;'>Variables</h3>", unsafe_allow_html=True)
with st.expander("About Variables"):
    st.text("""In Python, variables are containers, which is used to store data values. Python supports various datatypes, including integers, floats, strings, and booleans. It represents the kind of value that tells what operations can be performed on a particular data. 

Variables are created when we assign a value to them, using the assignment operator (=).""")
st.markdown("<h8 style='text-align : left;color : yellow;'>program</h8>",unsafe_allow_html=True)
st.code("""Var = "Geeksforgeeks"
print(Var)""",language="python")

if st.button("Run Program"):
    with st.spinner("Loading"):
                    time.sleep(2)
    st.success("Output :")
    st.write("Geeksforgeeks")
st.subheader("Python Data Types")
with st.expander("about Data Types "):
    st.expander("""Python Data types are the classification or categorization of data items.  It represents the kind of value that tells what operations can be performed on a particular data.

The following are the standard or built-in data types in Python:\n

Numeric – int, float, complex\n
Sequence Type – string, list, tuple\n
Mapping Type – dict\n
Boolean – bool\n
Set Type – set, frozenset\n
Binary Types – bytes, bytearray, memoryview
Example""")
    st.code("""a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))""")
    
if st.button("Run program",key="1"):
       with st.spinner("Loading ....."):
               time.sleep(2)
       st.success("Output :")
       st.code("<class 'int'> \n<class 'float'>\n<class 'complex'>")
st.markdown("<h4 style ='color:pink;'>Numeric Data Types in Python</h4>",unsafe_allow_html=True)
st.text("Integers – This value is represented by int class.\nFloat – This value is represented by the float class.\nComplex Numbers – A complex number is represented by a complex class. For example – 2+3j")
st.code("""a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))""")
if st.button("Run program",key="2"):
         st.text("""<class 'int'>
<class 'float'>
<class 'complex'>""")
st.markdown("<h4 style ='color:pink;'>Sequence Data Types in Python</h4>",unsafe_allow_html=True)
st.text("""There are several sequence data types of Python:

Python String
Python List
Python Tuple""")
st.code("""# Python String
s = "Hello, Python!"
print(s[0])  

# Python List
a = [10, 20, 30, 40]
print(a[1])  

# Python Tuple
tup = (100, 200, 300, 400)
print(tup[2])""")
if st.button("Run program",key="3"):
        with st.spinner('Loading...'):
                 time.sleep(2)
        st.success("Output :")
        st.code("""H
20
300""")
         


#keyword...............
st.markdown("<h4 id='keyword' style='color:yellow;'>Keyword</h4>", unsafe_allow_html=True)
#st.markdown("<h4 id='keyword' style ='color:yellow;'>Python Keywords</h4>",unsafe_allow_html=True)
st.text("Keywords in Python are reserved words that have special meanings and serve specific purposes in the language syntax. Python keywords cannot be used as the names of variables, functions and classes or any other identifier.")
a=pd.Series(["True","False","None","and","or"])
b=pd.Series(["not","is","if","else","elif"])
c=pd.Series(["for","while","break","continue","pass"])
d=pd.Series(["try","except","finally","raise","assert"])
e=pd.Series(["def","return","lambda","yield","class"])
f=pd.Series(["import","from","in","as","del"])
g=pd.Series(["global","with","nonlocal","Async","Await"])
df = pd.DataFrame({
    "Logical Keywords": a,
    "Conditional Keywords": b,
    "Loop Keywords": c,
    "Exception Keywords": d,
    "Function/Class": e,
    "Import Keywords": f,
    "Other Keywords": g
})
st.table(df)


#Operators...............................
st.markdown("<h4 id='operators' style ='color:yellow;'>Operators</h4>",unsafe_allow_html=True)
st.text("In Python programming, Operators in general are used to perform operations on values and variables. These are standard symbols used for logical and arithmetic operations.")
st.markdown("<h4 style ='color:pink;'>Types of Operators in Python</h4>",unsafe_allow_html=True)
st.text("""Arithmetic Operators
Comparison Operators
Logical Operators
Bitwise Operators
Assignment Operators
Identity Operators and Membership Operators""")    
dt = pd.DataFrame({
    "Operators": [
        "+, -, *, /, %",
        "<, <=, >, >=, ==, !=",
        "AND, OR, NOT",
        "^, -, >>, <<, +=, -=, &",
        "=, +=, -=, *=, %="
    ],
    "Type": [
        "Arithmetic operator",
        "Relational operator",
        "Logical operator",
        "Bitwise operator",
        "Assignment operator"
    ]
})
st.table(dt)



# input output ............................
#st.markdown("<h4 id='inputoutput' style ='color:yellow;'>Input</h4>",unsafe_allow_html=True)
st.markdown("<a id='inputoutput'></a>", unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'>Input and Output</h4>", unsafe_allow_html=True)
st.text("Understanding input and output operations is fundamental to Python programming. With the print() function, you can display output in various formats, while the input() function enables interaction with users by gathering input during program execution.")
st.markdown("<h4 style ='color:pink;'>input()</h4>",unsafe_allow_html=True)
st.text("This function first takes the input from the user and converts it into a string. The type of the returned object always will be <class ‘str’>. ")
st.markdown("<h4 style ='color:green;'>Syntax</h4>",unsafe_allow_html=True)
st.code("inp = input('STATEMENT')")
st.text("Example")
st.code("""# Python program showing 
# a use of input()

val = input("Enter your value: ")
print(val)""")
if st.button("Run",key="5"):
       with st.spinner("Loading .."):
               time.sleep(2)
       st.success("Output")
       st.code("""Enter your value : 123
            123""")
st.text("""integer= int(input('statement'))
               float=float(input('statement'))""")
st.markdown("<h4 style ='color:pink;'>How to Print Output in Python</h4>",unsafe_allow_html=True)
st.text("Python print() function prints the message to the screen or any other standard output device.")
st.code("""# print() function example
print("GeeksforGeeks")

a = [1, 2, 'gfg']
print(a)""")
if st.button("Run",key="4"):
            with st.spinner("Loading"):
                    time.sleep(2)
            st.success("Output")
            st.code("""GeeksforGeeks
[1, 2, 'gfg']""")
st.markdown("<h4 style ='color:pink;'>Print Single and Multiple variable in Python</h4>",unsafe_allow_html=True)
st.text("The code assigns values to variables name and age, then prints them with labels")
st.code("""name = "Alice"
age = 30
print("Name:", name, "Age:", age)""")
if st.button("Run"):
                 with st.spinner("Loading"):
                    time.sleep(2)
                 st.success("Output :")
                 st.code("""Name: Alice Age: 30""")

st.markdown("<h4 style='color:pink;'>Comments in Python</h4>",unsafe_allow_html=True)
st.code("""(#singe comment)
        (""multiple comment"") """)

#control statement
st.markdown("<a id='controlLoop'></a>",unsafe_allow_html=True)
st.markdown("<h4 style='color:yellow;'> control-and-loop-statement</h4>",unsafe_allow_html=True)
st.text("In Python, loops and control statements are essential for controlling the flow of execution.")
st.markdown("<h4 style= 'color:pink;'>  While Loop</h4>",unsafe_allow_html=True)
st.text("A while loop in Python allows you to execute a block of code repeatedly as long as a given condition is true")
st.text("Key Points:")
st.text("""The loop runs as long as the condition evaluates to True.
Use break to exit the loop early.
Use continue to skip the current iteration and proceed with the next one.""")
st.text("Example :")
st.code("""count = 1
while count <= 10:
    print("Count is:", count)
    count += 1""")
if st.button("Run",key="6"):
        with st.spinner("Loading"):
                    time.sleep(2)
        st.success("Output :")
        st.text("""Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
Count is: 6
Count is: 7
Count is: 8
Count is: 9
                
Count is: 10""")
        st.text("This loop increments count until the condition count <= 10 becomes False.")

st.markdown("<h4 style= 'color:pink;'>  For Loop</h4>",unsafe_allow_html=True)
st.text("There is a “for in” loop which is similar to for each loop in other languages.  It’s ideal for cases where the number of iterations is known or defined by the sequence.")
st.text("Key Points:")
st.text("""Iterates over items in a sequence one by one.
Use break to exit the loop early.
Use continue to skip the current iteration.""")
st.code("""a = ["apple", "banana", "cherry"]
for i in a:
    print(i)""")
if st.button("Run",key="9"):
        with st.spinner("Loading"):
                    time.sleep(2)
        st.success("Output")
        st.text("""apple
banana
cherry""")
        st.text("This loop iterates through each item in the fruits list and prints it.")
st.markdown("<h4 style= 'color:pink;'>  Nested Loop</h4>",unsafe_allow_html=True)
st.text("Python programming language allows using one loop inside another loop. The following section shows a few examples to illustrate the concept. ")
st.text("Key Points:")
st.text("""The outer loop controls the number of times the inner loop executes.
You can use any combination of loops (e.g., for inside while).
Be mindful of performance, as nested loops can increase computational complexity.
""")
st.text("Example: Nested Loops for Multiplication Table")
st.code("""for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} x {j} = {i * j}")
    print("---")  # Separator for better readability""")
if st.button("Run",key="7"):
        
        with st.spinner("Loading"):
                    time.sleep(2)

        st.success("Output :")
        st.text("""1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
---
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
---
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
---""")
        st.text("""This example demonstrates a multiplication table for numbers 1 through 3, with the outer loop iterating over rows and the inner loop iterating over columns.""")
st.markdown("<h4 style= 'color:pink;'>Control statement</h4>",unsafe_allow_html=True)
st.subheader("if-else")
st.code("""if age >= 18:
    print("Adult")
else:
    print("Minor")
""")
st.subheader("elif")
st.code("""if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
""")
st.subheader("Python Continue")
st.text("It returns the control to the beginning of the loop. ")
st.code("""# Prints all letters except 'e' and 's'
for i in 'geeksforgeeks':
	if i == 'e' or i == 's':
		continue
	print(i)""")
if st.button("Run",key="10"):
        with st.spinner("Loading"):
                    time.sleep(2)
        st.success("Output :")
        st.text("""g
k
f
o
r
g
k""")
st.subheader("Python Break")
st.text("It brings control out of the loop.")
st.code("""for i in 'geeksforgeeks':

	# break the loop as soon it sees 'e'
	# or 's'
	if i == 'e' or i == 's':
		break
print(i)""")
if st.button("Run",key="11"):
        with st.spinner("Loading"):
                    time.sleep(2)

        st.success("Output :")
        st.text("e")
#python Type casting 
st.markdown("<a id ='type'></a>",unsafe_allow_html=True)
st.markdown("<h2 style='color:yellow;'>Type casting</h2>",unsafe_allow_html=True)
st.text("Type casting in Python refers to the process of converting a value from one data type to another")
st.text("""Python has several built-in functions for type casting: int(): Converts a value to an integer. float(): Converts a value to a floating-point number. str(): Converts a value to a string. list(), tuple(), set(), dict() and bool()""")
st.text("Example ")
st.code("""# Converting String to Integer:
         str_num = "26"
         int_num = int(str_num) 
        print(int_num)
         print(type(int_num))""")
if st.button("Run",key="12"):
        with st.spinner("Loading..."):
            time.sleep(3)
        st.text("Output :")
        st.text(""" 26
                <class 'int'>""")
st.markdown("<h4 style='color:pink;'>Types of Type casting</h4>",unsafe_allow_html=True)
st.subheader("1. Implicit Type Casting (Type Conversion)")
st.text("""Done automatically by Python.
Happens when converting a smaller data type to a larger data type to avoid data loss.""")
st.text("Example :")
st.code("""# Implicit type casting
num_int = 10       # int
num_float = 5.5    # float

result = num_int + num_float  # int is converted to float automatically
print(result)        
print(type(result)) """)
if st.button("Run",key="13"):
        with st.spinner("Loding.."):
                time.sleep(2)
        st.success("Output :")
        st.text(""" 15.5
                    <class 'float'>""")
st.subheader("2. Explicit Type Casting (Type Conversion)")
st.text("""Done manually using constructor functions:
int() → converts to integer
float() → converts to float
str() → converts to string
bool() → converts to boolean
list(), tuple(), set() → converts between collections""")
st.text("Example :")
st.code("""# Explicit type casting
num_str = "100"
num_int = int(num_str)   # Convert string to integer
num_float = float(num_str)  # Convert string to float

print(num_int, type(num_int))    
print(num_float, type(num_float)) """)
if st.button("Run",key="14"):
        with st.spinner("Loding.."):
                time.sleep(2)
        st.success("Output :")
        st.text(""" 100 <class 'int'>
                    100.0 <class 'float'>""")
st.subheader("3. Common Examples")
st.code("""# String to int
print(int("42"))  # 42

# Float to int (truncates decimal part)
print(int(9.99))  # 9

# Int to string
print(str(123) + " is a number")  # "123 is a number"

# List to tuple
print(tuple([1, 2, 3]))  # (1, 2, 3)""")

st.text("""✅ Key Points:

Implicit casting is safe and automatic.
Explicit casting must be done carefully to avoid ValueError (e.g., int("abc") will fail).
Casting between incompatible types will raise an error.
""")
st.markdown("<a id='practice'></a>",unsafe_allow_html=True)
st.title("1000+ practice Question ")
st.markdown("[Click here for Practice  Basic Questions (part 1) 📘](https://www.w3resource.com/python-exercises/python-basic-exercises.php)")
st.markdown("[Click here for Practice  Basic Questions (part 2) 📘](https://www.w3resource.com/python-exercises/basic/)")
st.markdown("[Click here for Practice  Puzzles Questions 📘](https://www.w3resource.com/python-exercises/puzzles/index.php#google_vignette)")
st.markdown("[Click here for Practice  Mastering Questions  📘](https://www.w3resource.com/python-exercises/python_100_exercises_with_solutions.php)")
st.markdown("[Click here for Practice  Advances Questions  📘](https://www.w3resource.com/python-exercises/advanced/index.php)")
st.markdown("[Click here for Practice  Conditional Statements and Loops  📘](https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php#google_vignette)")

        
        
        
        
        
        
       
    
# going on new page .....................................................................
st.markdown("<a id='load'></a>",unsafe_allow_html=True)

st.markdown("<a id='load'></a>", unsafe_allow_html=True)
st.markdown("## 📚 Learning Dashboard")
st.markdown("Click on any button to visit that topic page 👇")
st.markdown("---")

# -------------------
# Python Basics
# -------------------
st.markdown("### 🐍 Python Basics")
st.markdown("Explore the core Python data types and methods:")

col1, col2 = st.columns(2)

with col1:
    if st.button("🐍 Strings", use_container_width=True):
        st.balloons()
        st.switch_page("pages/String.py")
    if st.button("🧵 Method", use_container_width=True):
        st.switch_page("pages/Methods.py")
    if st.button("📦 Tuple", use_container_width=True):
        st.switch_page("pages/Tuple.py")
    if st.button("🧺 Set", use_container_width=True):
        st.switch_page("pages/Set.py")
    if st.button("📖 Dictionary", use_container_width=True):
        st.switch_page("pages/Dict.py")

# -------------------
# Data Visualization
# -------------------
st.markdown("<a id='intro'></a>",unsafe_allow_html=True)
st.markdown("---")
st.markdown("### 📊 Data Visualization")
st.markdown(
    """
**Data Visualization?**  
Data Visualization is the graphical representation of information and data.  
It helps in understanding trends, patterns, and insights from data easily.  
In this section, you can explore libraries like Pandas, Numpy, Matplotlib, and Seaborn to learn how to visualize and manipulate data.
"""
)
with st.expander("Key concept :"):
        st.markdown("<h5 style='color:pink;'>Visual Representation</h5>",unsafe_allow_html=True)
        st.text("""Data is transformed into visual elements to enhance understanding.
                Example:
                A bar char representing monthly sales data""")
        st.markdown("<h5 style='color:pink;'>Communication</h5>",unsafe_allow_html=True)
        st.text("""Effective communication of inshghts to a diverse audience.
                Example:
                A pie chart illustrating the distribution of market share among different products.""")
        st.markdown("<h5 style='color:pink;'>Decision Support</h5>",unsafe_allow_html=True)
        st.text("""Empowering decision making through clear and intutive data representation..
                Example:
                A line chart showing trends in website traffic ,aiding decisions on marketing strategies.""")
with st.expander("Importance :") :
        st.markdown("<h5 style='color:pink;'>Enhanced Understanding</h5>",unsafe_allow_html=True)
        st.text("""Visualization simplify complex data for better comprehension
                Exampple:
                A heat map highlighting areas with the highest customer engagement on a website""")
        st.markdown("<h5 style='color:pink;'>Pattern Recognition :</h5>",unsafe_allow_html=True)
        st.text("""Visual patterns in data can be Quickly indentified
                Example:
                A scatter plot revealing a correlation between advertising spending and sales revenue.""")
        st.markdown("<h5 style='color:pink;'>Storytelling</h5>",unsafe_allow_html=True)
        st.text("""Data visualization can tell a story. making insights more memorable.
                Example :
                A flowchart showing the customer journey.narrating the user experience on a website """)
with st.expander("Tools and Technologies :"):
        st.markdown("<h5 style='color:pink;'>Graphical Tools :</h5>",unsafe_allow_html=True)
        st.text("""Software : like wekka , Tableau ,Microsoft Power BI , and Google Dta Studio
                Example:
                Creating an interactive dashboard in Tableau to analyze sales data across regions.""")
        
        st.markdown("<h5 style='color:pink;'>Programming Libraries  :</h5>",unsafe_allow_html=True)
        st.text("""python libraries : like Matplotlib and seaborn ,javaScript etc.""")

# -----------------------------
# Challenges Section
# -----------------------------
with st.expander("📌 Challenges of Data Visualization"):
    st.subheader("1. Misinterpretation")
    st.write("Incorrect visualizations may lead to misinterpretation of data.")
    st.write("**Example:** Choosing a misleading scale on a bar chart, making differences appear larger than they are.")
    
    st.subheader("2. Complexity")
    st.write("Some datasets are inherently complex, requiring careful design of visualizations.")
    st.write("**Example:** Visualizing a network of interconnected data points in a complex organizational structure.")

# -----------------------------
# Examples of Data Visualization
# -----------------------------
with st.expander("📈 Examples of Data Visualization"):

    # Bar Chart Example
    st.subheader("Bar Chart")
    st.write("Purpose: Comparing quantities across categories.")
    st.write("Example: Monthly sales figures for different products.")
    sales_data = pd.DataFrame({
        "Products": ["Product A", "Product B", "Product C", "Product D"],
        "Sales": [150, 200, 300, 100]
    })
    st.bar_chart(sales_data.set_index("Products"))

    # Line Chart Example
    st.subheader("Line Chart")
    st.write("Purpose: Displaying trends or changes over a continuous interval.")
    st.write("Example: Stock prices over six months.")
    stock_prices = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Price": [100, 105, 102, 108, 110, 115]
    })
    st.line_chart(stock_prices.set_index("Month"))

    # Pie Chart Example
    st.subheader("Pie Chart")
    st.write("Purpose: Showing proportion of parts to a whole.")
    st.write("Example: Distribution of expenses in a budget.")
    expense_data = pd.DataFrame({
        "Category": ["Rent", "Food", "Transport", "Entertainment"],
        "Amount": [1200, 500, 200, 100]
    })
    st.write(expense_data)
    st.write("Pie charts can be visualized using matplotlib or plotly.")

    # Scatter Plot Example
    st.subheader("Scatter Plot")
    st.write("Purpose: Revealing relationships between two variables.")
    st.write("Example: Advertising spending vs Sales.")
    scatter_data = pd.DataFrame({
    "Advertising": [50, 60, 70, 80, 90, 100],
    "Sales": [200, 220, 240, 260, 280, 300]
})


# -----------------------------
# Applications Section
# -----------------------------
with st.expander("💼 Applications of Data Visualization"):

    st.subheader("Business and Finance")
    st.write("""
    - **Visualizing financial data:** Represent trends and patterns.
    - **Forecasting:** Predictive analysis for future trends.
    - **Decision-making:** Stakeholders can make informed decisions.
    """)

    st.subheader("Healthcare")
    st.write("""
    - **Diagnostics:** Visualize medical test results.
    - **Patient monitoring:** Track patient health over time.
    - **Research:** Analyze medical research data for patterns.
    """)

    st.subheader("Education")
    st.write("""
    - **Enhancing understanding:** Make complex concepts easier.
    - **Interactive learning:** Engage students visually.
    - **Performance tracking:** Identify areas of improvement.
    """)

# -----------------------------
# Process of Data Visualization
# -----------------------------
with st.expander("🛠 Process of Data Visualization"):
    st.subheader("1. Data Collection")
    st.write("Gather relevant data from various sources (databases, surveys, APIs) and ensure accuracy and completeness.")
    
    st.subheader("2. Data Cleaning and Preparation")
    st.write("Handle missing values, outliers, and transform data into a format suitable for visualization tools.")
    
    st.subheader("3. Choosing Visualization Types")
    st.write("Select charts, graphs, or maps appropriate to the data's nature.")
    
    st.subheader("4. Designing and Creating Visualizations")
    st.write("Choose tools like Tableau, Power BI, or Python libraries (Matplotlib, Plotly, Seaborn). Design color schemes, labels, and other visual elements for clarity.")
    
    st.subheader("5. Interpretation and Analysis")
    st.write("Analyze visualizations to identify trends, outliers, patterns, and validate findings with statistics.")
    
    st.subheader("6. Communication")
    st.write("Effectively communicate insights and findings to stakeholders using visualized data.")





        

st.markdown("Click on any library to explore its functionalities:")

col3, col4 = st.columns(2)

with col3:
    if st.button("🐼 Pandas", use_container_width=True):
        st.switch_page("pages/Pandas.py")
    if st.button("🧺 Numpy", use_container_width=True):
        st.switch_page("pages/Numpy.py")

with col4:
    if st.button("📊 Matplotlib", use_container_width=True):
        st.switch_page("pages/Matplotlib.py")
    if st.button("📊 Seaborn", use_container_width=True):
        st.switch_page("pages/Seaborn.py")
    


    
    


#About me....
st.markdown("<a id='about'></a>",unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<div style="
background-color:#0e1117;
padding:25px;
border-radius:15px;
color:white;
text-align:center;
">

<img src="https://www.python.org/static/community_logos/python-logo.png" width="120">

<h2>👩‍💻 Author: Sanya Katiyar</h2>

<p>Python & Data Science Learner 🚀 <br>
This application is built using <b>Streamlit</b>.</p>

<h4>🎓 Guided by: Dr Aditya Khamparia Sir</h4>
<p>(Project idea given by my respected teacher)</p>

<hr style="border:1px solid gray;">

<h3>📞 Contact Me</h3>

<p>
<a href="https://www.linkedin.com/feed/">🔗 LinkedIn</a> | 
<a href="https://github.com/Sanya-Katiyar-Eng" target="_blank">💻 GitHub</a> | 
<a href="https://www.youtube.com/" target="_blank">▶️ YouTube</a>
</p>

<p>📱 Phone: +91-7905639342</p>
<p>📧 Email:sanyakatiyar01@gmail.com</p>

<hr style="border:1px solid gray;">

<p style="color:lightgray;">© 2026 Sanya Katiyar | All Rights Reserved</p>

</div>
""", unsafe_allow_html=True)



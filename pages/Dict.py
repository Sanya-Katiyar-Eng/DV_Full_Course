import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="StudyNest", layout="wide")

# ---------------- BACK BUTTON ----------------
if st.button("⬅ Back to Home"):
    st.switch_page("main.py")

# ---------------- CSS STYLE ----------------
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
    from {opacity:0; transform:translateY(20px);}
    to {opacity:1; transform:translateY(0);}
}

.top-banner {
    background:#FFD700;
    padding:12px;
    text-align:center;
    color:black;
    font-size:22px;
    font-weight:bold;
    border-radius:8px;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<h1 class="fade-text">Welcome to StudyNest</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Learn • Practice • Grow with Interactive Notes</p>', unsafe_allow_html=True)

st.markdown("""
<div class="top-banner">
✨ 📘 Welcome to StudyNest – Your Smart Learning Hub ✨
</div>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.markdown("""
## 📚 Python Dictionary Topics

<a href="#intro">1. Introduction</a><br>
<a href="#create">2. Creating Dictionary</a><br>
<a href="#access">3. Accessing Items</a><br>
<a href="#addupdate">4. Adding & Updating</a><br>
<a href="#remove">5. Removing Items</a><br>
<a href="#iterate">6. Iterating Dictionary</a><br>
<a href="#nested">7. Nested Dictionary</a><br>
<a href="#methods">8. All Methods</a><br>
<a href="#practice">9. Practice</a><br>
<a href="#youtube">10. Youtube Tutorial</a>
""", unsafe_allow_html=True)


# ---------------- 1 INTRODUCTION ----------------
st.markdown('<a id="intro"></a>', unsafe_allow_html=True)
st.markdown('<h2 id="intro">Python Dictionary</h2>', unsafe_allow_html=True)

st.markdown("""
A Python dictionary stores data in **key-value pairs**.

Each key must be **unique** and is used to access its value.
""")

st.code("""
data = {"name":"Liam","age":25}
print(data)
""")

if st.button("Show Output - Introduction"):
    st.text("{'name': 'Liam', 'age': 25}")

st.markdown('<a id="create"></a>', unsafe_allow_html=True)
# ---------------- 2 CREATE ----------------
st.markdown('<h2 id="create">Creating a Dictionary</h2>', unsafe_allow_html=True)

st.markdown("A dictionary can be created using `{}` or `dict()`.")

st.code("""
d1 = {1:'Alpha',2:'Beta',3:'Gamma'}
print(d1)

d2 = dict(a="Delta",b="Epsilon",c="Zeta")
print(d2)
""")

if st.button("Show Output - Creating"):
    st.text("""
{1: 'Alpha', 2: 'Beta', 3: 'Gamma'}
{'a': 'Delta', 'b': 'Epsilon', 'c': 'Zeta'}
""")

st.markdown('<a id="access"></a>', unsafe_allow_html=True)
# ---------------- 3 ACCESS ----------------
st.markdown('<h2 id="access">Accessing Dictionary Items</h2>', unsafe_allow_html=True)

st.code("""
d = {"name":"Maya",1:"Python",(1,2):[10,20,30]}

print(d["name"])
print(d.get("name"))
""")

if st.button("Show Output - Accessing"):
    st.text("""
Maya
Maya
""")

st.markdown('<a id="addupdate"></a>', unsafe_allow_html=True)
# ---------------- 4 ADD UPDATE ----------------
st.markdown('<h2 id="addupdate">Adding and Updating Dictionary Items</h2>', unsafe_allow_html=True)

st.code("""
d = {1:'Alpha',2:'Beta',3:'Gamma'}

d["age"]=30
d[1]="Omega"

print(d)
""")

if st.button("Show Output - Add/Update"):
    st.text("{1:'Omega',2:'Beta',3:'Gamma','age':30}")

st.markdown('<a id="remove"></a>', unsafe_allow_html=True)
# ---------------- 5 REMOVE ----------------
st.markdown('<h2 id="remove">Removing Dictionary Items</h2>', unsafe_allow_html=True)

st.code("""
d={1:'Alpha',2:'Beta',3:'Gamma','age':30}

del d["age"]
val=d.pop(1)
key,val=d.popitem()
d.clear()
""")

if st.button("Show Output - Removing"):
    st.text("""
{1:'Alpha',2:'Beta',3:'Gamma'}
Alpha
Key:3 Value:Gamma
{}
""")

st.markdown('<a id="iterate"></a>', unsafe_allow_html=True)
# ---------------- 6 ITERATE ----------------
st.markdown('<h2 id="iterate">Iterating Through Dictionary</h2>', unsafe_allow_html=True)

st.code("""
d={1:'Alpha',2:'Beta','age':30}

for key in d:
    print(key)

for val in d.values():
    print(val)

for key,val in d.items():
    print(key,val)
""")

if st.button("Show Output - Iterating"):
    st.text("""
1
2
age
Alpha
Beta
30
1 Alpha
2 Beta
age 30
""")

st.markdown('<a id="nested"></a>', unsafe_allow_html=True)
# ---------------- 7 NESTED ----------------
st.markdown('<h2 id="nested">Nested Dictionary</h2>', unsafe_allow_html=True)

st.code("""
d={1:'Alpha',2:'Beta',3:{'X':'Hello','Y':'World','Z':'Python'}}

print(d)
""")

if st.button("Show Output - Nested"):
    st.text("{1:'Alpha',2:'Beta',3:{'X':'Hello','Y':'World','Z':'Python'}}")


# ---------------- METHODS ----------------
st.markdown('<a id="methods"></a>', unsafe_allow_html=True)
st.markdown('<h2 id="methods">All Dictionary Methods</h2>', unsafe_allow_html=True)

st.markdown("[Click for Methods](https://www.w3schools.com/python/python_ref_dictionary.asp)")


# ---------------- PRACTICE ----------------
st.markdown('<a id="practice"></a>', unsafe_allow_html=True)
st.title("Practice Questions")
st.markdown("[Click for Practice](https://www.w3resource.com/python-exercises/dictionary/)")


# ---------------- YOUTUBE ----------------
st.markdown('<a id="youtube"></a>', unsafe_allow_html=True)
st.title("Youtube Tutorial")

st.markdown("[Watch Tutorial](https://www.youtube.com/watch?v=brnsFCa7npc)")
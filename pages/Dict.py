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



st.set_page_config(page_title="Python Dictionary ", layout="wide")

# Sidebar for navigation
st.sidebar.markdown("## 📚 Topics")
topics = {
    "Introduction": "intro",
    "Creating a Dictionary": "create",
    "Accessing Items": "access",
    "Adding & Updating Items": "add_update",
    "Removing Items": "remove",
    "Iterating Through a Dictionary": "iterate",
    "Nested Dictionaries": "nested",
    "Practice link":"pr"
}

# Sidebar checkboxes
selected_topics = {}
for topic_name, topic_id in topics.items():
    selected_topics[topic_id] = st.sidebar.checkbox(topic_name, value=False)

# -------------------------
# 1. Introduction
# -------------------------
if selected_topics["intro"] or True:
    st.markdown("## Python Dictionary")
    st.markdown("""
A Python dictionary is a data structure that stores data in **key-value pairs**, where each key is **unique**.  
It is mainly used when you want to access data by a **name (key)** instead of position like in a list.
""")
    st.code("""
data = { "name": "Liam", "age": 25 }
print(data)
""", language="python")
    if st.button("Show Output - Introduction"):
        st.text("{'name': 'Liam', 'age': 25}")

# -------------------------
# 2. Creating a Dictionary
# -------------------------
if selected_topics["create"] or True:
    st.markdown("## Creating a Dictionary")
    st.markdown("""
A dictionary can be created using `{}` with key-value pairs or using the `dict()` constructor.
""")
    st.code("""
# Using curly braces
d1 = {1: 'Alpha', 2: 'Beta', 3: 'Gamma'}
print(d1)

# Using dict() constructor
d2 = dict(a="Delta", b="Epsilon", c="Zeta")
print(d2)
""", language="python")
    if st.button("Show Output - Creating"):
        st.text("""
{1: 'Alpha', 2: 'Beta', 3: 'Gamma'}
{'a': 'Delta', 'b': 'Epsilon', 'c': 'Zeta'}
""")

# -------------------------
# 3. Accessing Items
# -------------------------
if selected_topics["access"] or True:
    st.markdown("## Accessing Dictionary Items")
    st.markdown("""
A value is accessed by its key using `[]` or the `get()` method.
""")
    st.code("""
d = { "name": "Maya", 1: "Python", (1, 2): [10, 20, 30] }

# Using key
print(d["name"])

# Using get()
print(d.get("name"))
""", language="python")
    if st.button("Show Output - Accessing"):
        st.text("""
Maya
Maya
""")

# -------------------------
# 4. Adding & Updating Items
# -------------------------
if selected_topics["add_update"] or True:
    st.markdown("## Adding and Updating Dictionary Items")
    st.markdown("""
Add new items or update existing ones using `=` operator.
""")
    st.code("""
d = {1: 'Alpha', 2: 'Beta', 3: 'Gamma'}

# Add
d["age"] = 30

# Update
d[1] = "Omega"
print(d)
""", language="python")
    if st.button("Show Output - Add/Update"):
        st.text("{1: 'Omega', 2: 'Beta', 3: 'Gamma', 'age': 30}")

# -------------------------
# 5. Removing Items
# -------------------------
if selected_topics["remove"] or True:
    st.markdown("## Removing Dictionary Items")
    st.markdown("""
Use `del`, `pop()`, `popitem()`, or `clear()` to remove items.
""")
    st.code("""
d = {1: 'Alpha', 2: 'Beta', 3: 'Gamma', 'age': 30}

del d["age"]
val = d.pop(1)
key, val = d.popitem()
d.clear()
""", language="python")
    if st.button("Show Output - Removing"):
        st.text("""
{1: 'Alpha', 2: 'Beta', 3: 'Gamma'}
Alpha
Key: 3, Value: Gamma
{}
""")

# -------------------------
# 6. Iterating Through a Dictionary
# -------------------------
if selected_topics["iterate"] or True:
    st.markdown("## Iterating Through a Dictionary")
    st.markdown("""
Use loops to iterate over keys, values, or key-value pairs.
""")
    st.code("""
d = {1: 'Alpha', 2: 'Beta', 'age': 30}

# Keys
for key in d:
    print(key)

# Values
for val in d.values():
    print(val)

# Key-Value pairs
for key, val in d.items():
    print(f"{key}: {val}")
""", language="python")
    if st.button("Show Output - Iterating"):
        st.text("""
1
2
age
Alpha
Beta
30
1: Alpha
2: Beta
age: 30
""")

# -------------------------
# 7. Nested Dictionaries
# -------------------------
if selected_topics["nested"] or True:
    st.markdown("## Nested Dictionaries")
    st.markdown("""
A dictionary can contain another dictionary as a value.
""")
    st.code("""
d = {1: 'Alpha', 2: 'Beta', 3: {'X': 'Hello', 'Y': 'World', 'Z': 'Python'}}
print(d)
""", language="python")
    if st.button("Show Output - Nested"):
        st.text("{1: 'Alpha', 2: 'Beta', 3: {'X': 'Hello', 'Y': 'World', 'Z': 'Python'}}")
st.subheader("all Method ")
st.markdown("[click for method](https://www.w3schools.com/python/python_ref_dictionary.asp)")
st.subheader("Practice link")
st.markdown("[click for practice link](https://www.w3resource.com/python-exercises/dictionary/)")
st.subheader("Youtube vidio")
st.markdown("[click for Tutorial link](https://www.youtube.com/watch?v=brnsFCa7npc)")


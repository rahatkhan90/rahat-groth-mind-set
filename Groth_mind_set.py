import streamlit as st

# 1. Introduction
st.title("Growth Mindset Challenge")
st.write("""
A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes.
""")


# 2. Quiz Section
st.header("Quiz: Growth vs. Fixed Mindset")
question = st.radio(
    "Which statement reflects a growth mindset?",
    (
        "I'm just not good at math.",
        "With practice, I can get better at math."
    )
)
if st.button("Check Answer"):
    if question == "With practice, I can get better at math.":
        st.success("Correct! That's a growth mindset.")
    else:
        st.error("That's a fixed mindset. Try again!")

# 3. Reflection Journal
st.header("Reflection Journal")
reflection = st.text_area("Describe a recent challenge and how you responded.")
if st.button("Submit Reflection"):
    st.write("Great job reflecting! Next time, try to reframe your response with a growth mindset.")

# 4. Tips & Resources
st.header("Tips for a Growth Mindset")
st.markdown("""
- Embrace challenges
- Learn from mistakes
- Persist through difficulties
- Celebrate effort
- Keep an open mind
""")
st.write("Learn more: [Growth Mindset by rahat khan")

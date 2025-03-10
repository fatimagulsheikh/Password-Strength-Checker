# import streamlit as st
# import re

# # Page Configuration
# st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

# # Custom CSS for Styling
# st.markdown(
#     """
#     <style>
#         .title {
#             text-align: center;
#             color: #4A90E2;
#             font-size: 36px;
#             font-weight: bold;
#         }
#         .subtext {
#             text-align: center;
#             font-size: 18px;
#             color: #666;
#         }
#         .suggestions {
#             background-color: #f8f9fa;
#             padding: 10px;
#             border-radius: 10px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Title and Description
# st.markdown("<h1 class='title'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
# st.markdown("<p class='subtext'>Use this simple tool to check your password strength and get tips on how to make it stronger.</p>", unsafe_allow_html=True)

# # Password Input
# password = st.text_input("Enter your password", type="password")

# # Variables
# feedback = []
# score = 0

# # Password Strength Checking
# if password:
#     if len(password) >= 8:
#         score += 1
#     else:
#         feedback.append("❌ Password should be at least 8 characters long.")
    
#     if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
#         score += 1
#     else:
#         feedback.append("❌ Password should contain both uppercase and lowercase letters.")
    
#     if re.search(r'\d', password):
#         score += 1
#     else:
#         feedback.append("❌ Password should contain at least one digit.")
    
#     if re.search(r'[!@#$%^&*]', password):
#         score += 1
#     else:
#         feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")
    
#     # Password Strength Result
#     if score == 4:
#         st.success("✅ Your password is strong! 🎉")
#     elif score == 3:
#         st.warning("🟡 Your password is medium strength. Consider making it stronger.")
#     else:
#         st.error("🔴 Your password is weak. Please improve it.")
    
#     # Display Suggestions
#     if feedback:
#         st.markdown("<h3 class='suggestions'>💡 Improvement Suggestions</h3>", unsafe_allow_html=True)
#         for tip in feedback:
#             st.write(tip)
# else:
#     st.info("Please enter your password to get started.")












import streamlit as st
import re

# Page Configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f0f8ff;
        }
        .title {
            text-align: center;
            color: #4A90E2;
            font-size: 36px;
            font-weight: bold;
        }
        .subtext {
            text-align: center;
            font-size: 18px;
            color: #666;
        }
        .suggestions {
            background-color: #e3f2fd;
            padding: 10px;
            border-radius: 10px;
            color: #1565c0;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            font-size: 16px;
            color: #555;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<h1 class='title'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Use this simple tool to check your password strength and get tips on how to make it stronger.</p>", unsafe_allow_html=True)

# Password Input
password = st.text_input("Enter your password", type="password")

# Variables
feedback = []
score = 0

# Password Strength Checking
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")
    
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")
    
    # Password Strength Result
    if score == 4:
        st.success("✅ Your password is strong! 🎉")
    elif score == 3:
        st.warning("🟡 Your password is medium strength. Consider making it stronger.")
    else:
        st.error("🔴 Your password is weak. Please improve it.")
    
    # Display Suggestions
    if feedback:
        st.markdown("<h3 class='suggestions'>💡 Improvement Suggestions</h3>", unsafe_allow_html=True)
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")

# Footer
st.markdown("<p class='footer'>Made by <b>Fatima Sheikh</b></p>", unsafe_allow_html=True)

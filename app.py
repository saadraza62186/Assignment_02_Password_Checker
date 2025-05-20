import streamlit as st
import re

def check_password_strength(password):
    suggestions = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append(("error", "❌ Password should be at least 8 characters long."))

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append(("error", "❌ Include both uppercase and lowercase letters."))

    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append(("error", "❌ Add at least one number (0-9)."))

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        suggestions.append(("error", "❌ Include at least one special character (!@#$%^&*)."))

    if score == 4:
        suggestions.append(("success", "✅ Strong Password!"))
    elif score == 3:
        suggestions.append(("warning", "⚠️ Moderate Password - Consider adding more security features."))
    else:
        suggestions.append(("error", "❌ Weak Password - Improve it using the suggestions above."))

    return suggestions

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:")

if st.button("Check Strength"):
    if password:
        feedback = check_password_strength(password)
        for msg_type, msg in feedback:
            if msg_type == "error":
                st.error(msg)
            elif msg_type == "warning":
                st.warning(msg)
            elif msg_type == "success":
                st.success(msg)
    else:
        st.warning("⚠️ Please enter a password before checking.")

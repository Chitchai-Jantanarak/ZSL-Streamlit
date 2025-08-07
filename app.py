# app.py

import streamlit as st
from classifier import classify

st.title("Zero-Shot Role Classifier (Thai)")

# Input fields
description = st.text_area("คำอธิบายจากผู้เข้าร่วม:", "ผมออกแบบ UX สำหรับแอปมือถือ และจัดทำ wireframe ด้วย Figma")
role = st.text_input("บทบาทที่ต้องการ:", "Designer")

# Button fields
if st.button("PREDICT"):
    results = classify(description, role)

    st.subheader("ผลลัพธ์การจัดประเภท:")
    for label_enum, score in results:
        st.write(f"**{label_enum.value}**: {score:.2f}")

import streamlit as st
from classifier import classify
import random

st.set_page_config(page_title="Zero-Shot Role Classifier")

st.title("Zero-Shot Role Classifier (TH)")

role_options = [
    "Designer",
    "Developer",
    "Manager",
    "Data Scientist",
    "UX Researcher",
]

example_descriptions = [
    "ผมรับผิดชอบการออกแบบ UX/UI สำหรับแอปพลิเคชันมือถือ รวมถึงสร้าง wireframe และ prototype ด้วย Figma เพื่อให้ทีมพัฒนาเข้าใจดีไซน์ได้ชัดเจน",
    "เขาเขียนโปรแกรมด้วยภาษา Python และพัฒนา API โดยใช้ FastAPI เพื่อเชื่อมต่อระบบภายในและให้บริการข้อมูลกับผู้ใช้งาน",
    "ฉันทำหน้าที่วิเคราะห์ข้อมูลเชิงลึก และสร้างโมเดล Machine Learning เพื่อพยากรณ์แนวโน้มทางธุรกิจและช่วยตัดสินใจอย่างมีประสิทธิภาพ",
    "เธอมีบทบาทในการวางแผนโครงการและจัดการทีมพัฒนาซอฟต์แวร์ เพื่อให้มั่นใจว่าการส่งมอบงานตรงตามเวลาที่กำหนดและคุณภาพดี",
]

role = st.selectbox("เลือกบทบาทที่ต้องการ:", role_options)

description = st.text_area("รายละเอียดงานของผู้สมัคร:", height=150)

if st.button("PREDICT"):
    if not description.strip():
        st.warning("กรุณากรอกข้อมูลก่อน")
    else:
        with st.spinner("กำลังประมวลผล..."):
            results = classify(description, role)

        st.subheader("ผลลัพธ์การจัดประเภท:")

        for label_enum, score in results:
            st.markdown(f"**{label_enum.value}:** {score:.2%}")

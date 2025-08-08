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

example_descriptions = {
    "Designer": [
        "ผมรับผิดชอบการออกแบบ UX/UI สำหรับแอปพลิเคชันมือถือ รวมถึงสร้าง wireframe และ prototype ด้วย Figma เพื่อให้ทีมพัฒนาเข้าใจดีไซน์ได้ชัดเจน",
        "ออกแบบประสบการณ์ผู้ใช้และสร้างภาพรวมของแอปมือถือเพื่อให้เหมาะกับความต้องการของผู้ใช้งาน",
    ],
    "Developer": [
        "เขียนโปรแกรมด้วยภาษา Python และพัฒนา API โดยใช้ FastAPI เพื่อเชื่อมต่อระบบภายในและให้บริการข้อมูลกับผู้ใช้งานได้",
        "พัฒนาและดูแลระบบ API ด้วยภาษา Python เพื่อรองรับการทำงานของแอปพลิเคชัน",
    ],
    "Data Scientist": [
        "ฉันทำหน้าที่วิเคราะห์ข้อมูลเชิงลึก และสร้างโมเดล Machine Learning เพื่อพยากรณ์แนวโน้มทางธุรกิจและช่วยตัดสินใจอย่างมีประสิทธิภาพ",
        "วิเคราะห์ข้อมูลและสร้างโมเดลเพื่อสนับสนุนการตัดสินใจทางธุรกิจ",
    ],
    "Manager": [
        "เธอมีบทบาทในการวางแผนโครงการและจัดการทีมพัฒนาซอฟต์แวร์ เพื่อให้มั่นใจว่าการส่งมอบงานตรงตามเวลาที่กำหนดและคุณภาพดี",
        "บริหารจัดการโครงการและทีมงานเพื่อให้การพัฒนาซอฟต์แวร์สำเร็จตามเป้าหมาย",
    ],
    "UX Researcher": [
        "ศึกษาพฤติกรรมผู้ใช้และรวบรวมข้อมูลเพื่อปรับปรุงประสบการณ์การใช้งานให้ตอบโจทย์ความต้องการ",
    ]
}

if "description" not in st.session_state:
    st.session_state.description = random.choice(example_descriptions[role_options[0]])

def on_role_change():
    st.session_state.description = random.choice(example_descriptions[st.session_state.role])

role = st.selectbox("เลือกบทบาทที่ต้องการ:", role_options, index=0, key="role", on_change=on_role_change)

description = st.text_area("รายละเอียดงานของผู้สมัคร:", value=st.session_state.description, height=150, key="description")

if st.button("PREDICT"):
    if not description.strip():
        st.warning("กรุณากรอกข้อมูลก่อน")
    else:
        with st.spinner("กำลังประมวลผล..."):
            st.markdown(f" Role : {role}")
            st.markdown(f" Description : {description}")
            results = classify(description, role)

        st.subheader("ผลลัพธ์การจัดประเภท:")

        for label_enum, score in results:
            st.markdown(f"**{label_enum.value}:** {score:.2%}")

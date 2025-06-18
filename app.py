import streamlit as st

# 设置页面标题
st.title("极简 Streamlit 应用")

# 添加一个简单的输入框
user_name = st.text_input("请输入你的名字：", "世界")

# 添加一个按钮
if st.button("点击问候"):
    st.write(f"你好，{user_name}！欢迎使用 Streamlit！")

# 添加一个滑块
age = st.slider("选择你的年龄：", 0, 100, 25)
st.write(f"你选择的年龄是：{age}")

# 添加一个选择框
favorite_color = st.selectbox(
    "选择你喜欢的颜色：",
    ["红色", "蓝色", "绿色", "黄色", "紫色"]
)
st.write(f"你喜欢的颜色是：{favorite_color}")

# 显示一些基本信息
st.markdown("---")
st.markdown("### 关于这个应用")
st.markdown("这是一个最简单的 Streamlit 应用示例，可以在 Streamlit Cloud 上部署。") 
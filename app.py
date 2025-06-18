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

# 添加文件读取功能
st.markdown("---")
st.markdown("### 📁 文件读取演示")

# 文件上传组件
uploaded_file = st.file_uploader(
    "选择一个文本文件来测试文件读取功能：", 
    type=['txt', 'md', 'py', 'json', 'csv']
)

if uploaded_file is not None:
    # 显示文件信息
    st.success(f"✅ 成功上传文件：{uploaded_file.name}")
    st.info(f"📊 文件大小：{uploaded_file.size} 字节")
    
    # 读取并显示文件内容
    try:
        # 读取文件内容
        file_content = uploaded_file.read()
        
        # 尝试解码为文本
        try:
            text_content = file_content.decode('utf-8')
        except UnicodeDecodeError:
            text_content = file_content.decode('latin-1')
        
        # 显示文件内容
        st.markdown("#### 📄 文件内容：")
        st.text_area("文件内容预览：", text_content, height=200)
        
        # 显示统计信息
        lines = text_content.split('\n')
        words = text_content.split()
        st.markdown(f"**📈 统计信息：**")
        st.markdown(f"- 行数：{len(lines)}")
        st.markdown(f"- 单词数：{len(words)}")
        st.markdown(f"- 字符数：{len(text_content)}")
        
    except Exception as e:
        st.error(f"❌ 读取文件时出错：{str(e)}")

# 显示一些基本信息
st.markdown("---")
st.markdown("### 关于这个应用")
st.markdown("这是一个最简单的 Streamlit 应用示例，可以在 Streamlit Cloud 上部署。")
st.markdown("**新功能：** 支持本地文件上传和内容读取！") 
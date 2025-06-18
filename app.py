import streamlit as st
import json
import pandas as pd
import os

# 设置页面标题
st.title("极简 Streamlit 应用")

# 初始化 session state
if 'user_name' not in st.session_state:
    st.session_state.user_name = "世界"

# 添加一个简单的输入框
user_name = st.text_input("请输入你的名字：", value=st.session_state.user_name, key="user_name_input")

# 更新 session state
st.session_state.user_name = user_name

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

# 添加静态文件读取功能
st.markdown("---")
st.markdown("### 📂 静态文件读取演示")

# 创建两列布局
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📊 JSON 数据文件")
    
    # 读取 JSON 文件
    try:
        with open('data/sample_data.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        # 显示应用信息
        st.markdown("**应用信息：**")
        app_info = json_data['app_info']
        st.write(f"- 名称：{app_info['name']}")
        st.write(f"- 版本：{app_info['version']}")
        st.write(f"- 描述：{app_info['description']}")
        
        # 显示功能列表
        st.markdown("**功能特性：**")
        for feature in app_info['features']:
            st.write(f"- {feature}")
        
        # 显示用户数据
        st.markdown("**用户数据：**")
        users = json_data['sample_data']['users']
        for user in users:
            st.write(f"- {user['name']} ({user['age']}岁, {user['city']})")
        
        # 显示统计信息
        stats = json_data['sample_data']['statistics']
        st.markdown("**统计信息：**")
        st.write(f"- 总用户数：{stats['total_users']}")
        st.write(f"- 平均年龄：{stats['average_age']}")
        st.write(f"- 城市：{', '.join(stats['cities'])}")
        
    except Exception as e:
        st.error(f"❌ 读取 JSON 文件时出错：{str(e)}")

with col2:
    st.markdown("#### 🌤️ CSV 数据文件")
    
    # 读取 CSV 文件
    try:
        df = pd.read_csv('data/weather_data.csv')
        
        # 显示数据表格
        st.markdown("**天气数据：**")
        st.dataframe(df, use_container_width=True)
        
        # 显示统计信息
        st.markdown("**数据统计：**")
        st.write(f"- 总记录数：{len(df)}")
        st.write(f"- 城市数量：{df['城市'].nunique()}")
        st.write(f"- 平均温度：{df['温度'].mean():.1f}°C")
        st.write(f"- 平均湿度：{df['湿度'].mean():.1f}%")
        
        # 显示天气状况统计
        weather_counts = df['天气状况'].value_counts()
        st.markdown("**天气状况分布：**")
        for weather, count in weather_counts.items():
            st.write(f"- {weather}：{count}次")
            
    except Exception as e:
        st.error(f"❌ 读取 CSV 文件时出错：{str(e)}")

# 添加文件读取功能
st.markdown("---")
st.markdown("### 📁 文件上传演示")

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

# 创建两列布局显示应用信息
col1, col2 = st.columns(2)

with col1:
    st.markdown("**🎯 应用特性：**")
    st.markdown("- 用户交互功能")
    st.markdown("- 文件上传读取")
    st.markdown("- 静态文件处理")
    st.markdown("- 数据展示分析")
    st.markdown("- 响应式设计")

with col2:
    st.markdown("**🛠️ 技术栈：**")
    st.markdown(f"- Streamlit {st.__version__}")
    st.markdown("- Pandas 2.2.0+")
    st.markdown("- Python 3.13+")
    st.markdown("- 云端部署就绪")

# 显示版本和链接信息
st.markdown("---")
st.markdown("**📚 相关链接：**")
st.markdown("- [GitHub 仓库](https://github.com/franksunye/StreamlitCCDemo)")
st.markdown("- [在线演示](https://sccdemo.streamlit.app/)")
st.markdown("- [Streamlit 文档](https://docs.streamlit.io/)")

# 显示当前版本信息
st.markdown("---")
st.markdown(f"**📋 版本信息：** Streamlit {st.__version__} | 支持 Python 3.13+ | 兼容 Streamlit Cloud") 
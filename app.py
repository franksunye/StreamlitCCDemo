import streamlit as st
import json
import pandas as pd
import os
from database import FeedbackDB

# 初始化数据库
@st.cache_resource
def init_db():
    return FeedbackDB()

db = init_db()

# 设置页面配置
st.set_page_config(
    page_title="Streamlit Cloud Demo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 侧边栏菜单
st.sidebar.title("🚀 导航菜单")

# 菜单选项
menu_options = {
    "🏠 首页": "home",
    "📊 数据展示": "data_display",
    "📁 文件处理": "file_processing",
    "💬 数据库": "database",
    "ℹ️ 关于": "about"
}

# 当前页面选择
current_page = st.sidebar.selectbox(
    "选择功能模块：",
    list(menu_options.keys()),
    key="menu_selection"
)

# 获取当前页面标识
current_page_id = menu_options[current_page]

# 页面内容
if current_page_id == "home":
    # 首页 - 基础交互功能
    st.title("🏠 首页 - 基础交互功能")
    st.markdown("欢迎使用 Streamlit Cloud Demo！这是一个功能完整的 Streamlit 应用示例。")
    
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
    st.markdown("### 📋 功能说明")
    st.markdown("这个应用展示了 Streamlit 的各种功能：")
    st.markdown("- 🎯 用户交互组件")
    st.markdown("- 📊 数据展示和分析")
    st.markdown("- 📁 文件上传和处理")
    st.markdown("- 💬 数据库操作")
    st.markdown("- ☁️ 云端部署")

elif current_page_id == "data_display":
    # 数据展示页面 - 静态文件读取
    st.title("📊 数据展示 - 静态文件读取")
    st.markdown("展示从项目中的静态数据文件读取和展示功能。")
    
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

elif current_page_id == "file_processing":
    # 文件处理页面 - 文件上传功能
    st.title("📁 文件处理 - 文件上传功能")
    st.markdown("支持多种格式文件的上传、读取和内容分析。")
    
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
    else:
        st.info("👆 请上传一个文件来开始测试")
        
        # 显示支持的文件格式
        st.markdown("### 📋 支持的文件格式")
        st.markdown("- **文本文件** (.txt) - 纯文本内容")
        st.markdown("- **Markdown** (.md) - 格式化文档")
        st.markdown("- **Python** (.py) - Python 代码文件")
        st.markdown("- **JSON** (.json) - 结构化数据")
        st.markdown("- **CSV** (.csv) - 表格数据")

elif current_page_id == "database":
    # 数据库页面 - SQLite 用户反馈系统
    st.title("💬 数据库 - SQLite 用户反馈系统")
    st.markdown("展示 SQLite 数据库的增删改查操作。")
    
    # 创建两列布局
    feedback_col1, feedback_col2 = st.columns([1, 2])
    
    with feedback_col1:
        st.markdown("#### 📝 提交反馈")
        
        # 反馈表单
        with st.form("feedback_form"):
            feedback_name = st.text_input("您的姓名：", key="feedback_name")
            feedback_message = st.text_area("反馈内容：", height=100, key="feedback_message")
            submit_button = st.form_submit_button("提交反馈")
            
            if submit_button:
                if feedback_name and feedback_message:
                    if db.add_feedback(feedback_name, feedback_message):
                        st.success("✅ 反馈提交成功！")
                        # 清空表单
                        st.rerun()
                    else:
                        st.error("❌ 反馈提交失败，请重试")
                else:
                    st.warning("⚠️ 请填写姓名和反馈内容")
    
    with feedback_col2:
        st.markdown("#### 📊 反馈统计")
        
        # 获取反馈统计
        feedback_count = db.get_feedback_count()
        st.metric("总反馈数", feedback_count)
        
        # 显示最新反馈
        st.markdown("**最新反馈：**")
        all_feedback = db.get_all_feedback()
        
        if all_feedback:
            # 只显示最新的3条反馈
            for i, (feedback_id, name, message, created_at) in enumerate(all_feedback[:3]):
                with st.container():
                    st.markdown(f"**{name}** ({created_at})")
                    st.markdown(f"_{message}_")
                    if st.button(f"删除", key=f"delete_{feedback_id}"):
                        if db.delete_feedback(feedback_id):
                            st.success("✅ 删除成功！")
                            st.rerun()
                        else:
                            st.error("❌ 删除失败")
                    st.markdown("---")
        else:
            st.info("暂无反馈")

elif current_page_id == "about":
    # 关于页面 - 应用信息
    st.title("ℹ️ 关于 - 应用信息")
    st.markdown("了解这个 Streamlit 应用的详细信息。")
    
    # 创建两列布局显示应用信息
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🎯 应用特性：**")
        st.markdown("- 用户交互功能")
        st.markdown("- 文件上传读取")
        st.markdown("- 静态文件处理")
        st.markdown("- 数据展示分析")
        st.markdown("- SQLite 数据库支持")
        st.markdown("- 响应式设计")
        st.markdown("- 菜单导航系统")
    
    with col2:
        st.markdown("**🛠️ 技术栈：**")
        st.markdown(f"- Streamlit {st.__version__}")
        st.markdown("- Pandas 2.2.0+")
        st.markdown("- SQLite 数据库")
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
    
    # 显示项目结构
    st.markdown("---")
    st.markdown("**📁 项目结构：**")
    st.markdown("""
    ```
    StreamlitCCDemo/
    ├── app.py                    # 主应用文件
    ├── requirements.txt          # Python 依赖
    ├── README.md                # 项目说明
    ├── LICENSE                  # MIT 许可证
    ├── database.py              # 数据库操作
    ├── init_db.py               # 数据库初始化
    ├── feedback.db              # SQLite 数据库
    ├── sample.txt               # 示例文本文件
    └── data/                    # 数据文件目录
        ├── sample_data.json     # JSON 示例数据
        └── weather_data.csv     # CSV 天气数据
    ```
    """) 
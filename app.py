import streamlit as st
import json
import pandas as pd
import os
from database import FeedbackDB
from i18n import get_text, get_language, set_language, get_available_languages, get_language_display_name

# 必须放在所有 Streamlit 相关代码之前
st.set_page_config(
    page_title="Streamlit Community Cloud Demo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 初始化数据库
@st.cache_resource
def init_db():
    return FeedbackDB()

db = init_db()

# 获取当前语言
current_language = get_language()

# 语言切换器
st.sidebar.markdown("---")
available_languages = get_available_languages()
language_options = [get_language_display_name(lang) for lang in available_languages]
current_lang_index = available_languages.index(current_language) if current_language in available_languages else 0

selected_language_display = st.sidebar.selectbox(
    get_text("language_selector", current_language),
    language_options,
    index=current_lang_index,
    key="language_selector"
)

# 更新语言设置
selected_language = available_languages[language_options.index(selected_language_display)]
if selected_language != current_language:
    set_language(selected_language)
    current_language = selected_language
    st.rerun()

# 侧边栏菜单
st.sidebar.title(get_text("sidebar_title", current_language))

# 菜单选项
menu_options = {
    "home": get_text("menu_home", current_language),
    "data_display": get_text("menu_data_display", current_language),
    "file_processing": get_text("menu_file_processing", current_language),
    "database": get_text("menu_database", current_language),
    "chat": get_text("menu_chat", current_language),
    "about": get_text("menu_about", current_language)
}

# 当前页面选择 - 使用按钮式导航
st.sidebar.markdown("### 📋 " + get_text("select_module", current_language))

# 初始化当前页面
if 'current_page_id' not in st.session_state:
    st.session_state.current_page_id = "home"

# 创建按钮式菜单
for page_id, page_name in menu_options.items():
    # 根据当前页面设置按钮样式
    if st.sidebar.button(
        page_name,
        key=f"menu_{page_id}",
        type="primary" if st.session_state.current_page_id == page_id else "secondary"
    ):
        st.session_state.current_page_id = page_id
        st.rerun()

# 获取当前页面标识
current_page_id = st.session_state.current_page_id

# 在侧边栏底部添加版本号
st.sidebar.markdown("---")
st.sidebar.markdown("**📋 Version:** v0.1.0")
st.sidebar.markdown("*Streamlit Community Cloud Demo*")

# 颜色选项 - 根据语言提供不同的颜色选项
color_options_map = {
    "en": ["Red", "Blue", "Green", "Yellow", "Purple"],
    "zh": ["红色", "蓝色", "绿色", "黄色", "紫色"],
    "es": ["Rojo", "Azul", "Verde", "Amarillo", "Púrpura"]
}
color_options = color_options_map.get(current_language, color_options_map["en"])

# 页面内容
if current_page_id == "home":
    # 首页 - 基础交互功能
    st.title(get_text("home_title", current_language))
    st.markdown(get_text("home_welcome", current_language))
    
    # 添加一个简单的输入框
    user_name = st.text_input(get_text("input_name_label", current_language), get_text("input_name_default", current_language))
    
    # 添加一个按钮
    if st.button(get_text("greet_button", current_language)):
        st.write(get_text("greet_message", current_language).format(user_name))
    
    # 添加一个滑块
    age = st.slider(get_text("age_slider_label", current_language), 0, 100, 25)
    st.write(get_text("age_selected", current_language).format(age))
    
    # 添加一个选择框
    favorite_color = st.selectbox(
        get_text("color_select_label", current_language),
        color_options
    )
    st.write(get_text("color_selected", current_language).format(favorite_color))
    
    # 显示一些基本信息
    st.markdown("---")
    st.markdown(get_text("features_title", current_language))
    st.markdown(get_text("features_intro", current_language))
    st.markdown(get_text("feature_interactive", current_language))
    st.markdown(get_text("feature_data", current_language))
    st.markdown(get_text("feature_file", current_language))
    st.markdown(get_text("feature_db", current_language))
    st.markdown(get_text("feature_cloud", current_language))

elif current_page_id == "data_display":
    # 数据展示页面 - 静态文件读取
    st.title(get_text("data_display_title", current_language))
    st.markdown(get_text("data_display_intro", current_language))
    
    # 创建两列布局
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(get_text("json_data_title", current_language))
        
        # 读取 JSON 文件
        try:
            with open('data/sample_data.json', 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            # 显示应用信息
            st.markdown(get_text("app_info_title", current_language))
            app_info = json_data['app_info']
            st.write(get_text("name_label", current_language).format(app_info['name']))
            st.write(get_text("version_label", current_language).format(app_info['version']))
            st.write(get_text("description_label", current_language).format(app_info['description']))
            
            # 显示功能列表
            st.markdown(get_text("features_list_title", current_language))
            for feature in app_info['features']:
                st.write(f"- {feature}")
            
            # 显示用户数据
            st.markdown(get_text("user_data_title", current_language))
            users = json_data['sample_data']['users']
            for user in users:
                age_text = f"{user['age']}岁" if current_language == "zh" else f"{user['age']} years old"
                st.write(get_text("user_info", current_language).format(user['name'], age_text, user['city']))
            
            # 显示统计信息
            stats = json_data['sample_data']['statistics']
            st.markdown(get_text("statistics_title", current_language))
            st.write(get_text("total_users", current_language).format(stats['total_users']))
            st.write(get_text("avg_age", current_language).format(stats['average_age']))
            st.write(get_text("cities", current_language).format(', '.join(stats['cities'])))
            
        except Exception as e:
            st.error(get_text("json_error", current_language).format(str(e)))
    
    with col2:
        st.markdown(get_text("csv_data_title", current_language))
        
        # 读取 CSV 文件
        try:
            df = pd.read_csv('data/weather_data.csv')
            
            # 显示数据表格
            st.markdown(get_text("weather_data_title", current_language))
            st.dataframe(df, use_container_width=True)
            
            # 显示统计信息
            st.markdown(get_text("data_stats_title", current_language))
            st.write(get_text("total_records", current_language).format(len(df)))
            st.write(get_text("city_count", current_language).format(df['城市'].nunique()))
            st.write(get_text("avg_temp", current_language).format(df['温度'].mean()))
            st.write(get_text("avg_humidity", current_language).format(df['湿度'].mean()))
            
            # 显示天气状况统计
            weather_counts = df['天气状况'].value_counts()
            st.markdown(get_text("weather_dist_title", current_language))
            for weather, count in weather_counts.items():
                st.write(get_text("weather_count", current_language).format(weather, count))
                
        except Exception as e:
            st.error(get_text("csv_error", current_language).format(str(e)))

elif current_page_id == "file_processing":
    # 文件处理页面 - 文件上传功能
    st.title(get_text("file_processing_title", current_language))
    st.markdown(get_text("file_processing_intro", current_language))
    
    # 文件上传组件
    uploaded_file = st.file_uploader(
        get_text("file_uploader_label", current_language), 
        type=['txt', 'md', 'py', 'json', 'csv']
    )
    
    if uploaded_file is not None:
        # 显示文件信息
        st.success(get_text("upload_success", current_language).format(uploaded_file.name))
        st.info(get_text("file_size", current_language).format(uploaded_file.size))
        
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
            st.markdown(get_text("file_content_title", current_language))
            st.text_area(get_text("file_preview_label", current_language), text_content, height=200)
            
            # 显示统计信息
            lines = text_content.split('\n')
            words = text_content.split()
            st.markdown(get_text("stats_info_title", current_language))
            st.markdown(get_text("line_count", current_language).format(len(lines)))
            st.markdown(get_text("word_count", current_language).format(len(words)))
            st.markdown(get_text("char_count", current_language).format(len(text_content)))
            
        except Exception as e:
            st.error(get_text("file_read_error", current_language).format(str(e)))
    else:
        st.info(get_text("upload_prompt", current_language))
        
        # 显示支持的文件格式
        st.markdown(get_text("supported_formats_title", current_language))
        st.markdown(get_text("txt_format", current_language))
        st.markdown(get_text("md_format", current_language))
        st.markdown(get_text("py_format", current_language))
        st.markdown(get_text("json_format", current_language))
        st.markdown(get_text("csv_format", current_language))

elif current_page_id == "database":
    # 数据库页面 - SQLite 用户反馈系统
    st.title(get_text("database_title", current_language))
    st.markdown(get_text("database_intro", current_language))
    
    # 创建两列布局
    feedback_col1, feedback_col2 = st.columns([1, 2])
    
    with feedback_col1:
        st.markdown(get_text("submit_feedback_title", current_language))
        
        # 反馈表单
        with st.form("feedback_form"):
            feedback_name = st.text_input(get_text("feedback_name_label", current_language), key="feedback_name")
            feedback_message = st.text_area(get_text("feedback_message_label", current_language), height=100, key="feedback_message")
            submit_button = st.form_submit_button(get_text("submit_button", current_language))
            
            if submit_button:
                if feedback_name and feedback_message:
                    if db.add_feedback(feedback_name, feedback_message):
                        st.success(get_text("feedback_success", current_language))
                        # 清空表单
                        st.rerun()
                    else:
                        st.error(get_text("feedback_error", current_language))
                else:
                    st.warning(get_text("feedback_warning", current_language))
    
    with feedback_col2:
        st.markdown(get_text("feedback_stats_title", current_language))
        
        # 获取反馈统计
        feedback_count = db.get_feedback_count()
        st.metric(get_text("total_feedback", current_language), feedback_count)
        
        # 显示最新反馈
        st.markdown(get_text("latest_feedback_title", current_language))
        all_feedback = db.get_all_feedback()
        
        if all_feedback:
            # 只显示最新的3条反馈
            for i, (feedback_id, name, message, created_at) in enumerate(all_feedback[:3]):
                with st.container():
                    st.markdown(f"**{name}** ({created_at})")
                    st.markdown(f"_{message}_")
                    if st.button(get_text("delete_button", current_language), key=f"delete_{feedback_id}"):
                        if db.delete_feedback(feedback_id):
                            st.success(get_text("delete_success", current_language))
                            st.rerun()
                        else:
                            st.error(get_text("delete_error", current_language))
                    st.markdown("---")
        else:
            st.info(get_text("no_feedback", current_language))

elif current_page_id == "chat":
    st.title(get_text("chat_title", current_language))
    st.markdown(get_text("chat_welcome", current_language))
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []
    # 展示历史消息
    if st.session_state.chat_messages:
        for msg in st.session_state.chat_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    else:
        st.info(get_text("chat_empty", current_language))
    # 聊天输入
    if prompt := st.chat_input(get_text("chat_input_placeholder", current_language)):
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        # AI回复（简单回显/多语言）
        with st.chat_message("assistant"):
            st.markdown(get_text("chat_ai_thinking", current_language))
        response = f"Echo: {prompt}"
        st.session_state.chat_messages.append({"role": "assistant", "content": response})
        st.rerun()

elif current_page_id == "about":
    # 关于页面 - 应用信息
    st.title(get_text("about_title", current_language))
    st.markdown(get_text("about_intro", current_language))
    
    # 创建两列布局显示应用信息
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(get_text("app_features_title", current_language))
        st.markdown(get_text("feature_interactive_about", current_language))
        st.markdown(get_text("feature_file_about", current_language))
        st.markdown(get_text("feature_static_about", current_language))
        st.markdown(get_text("feature_data_about", current_language))
        st.markdown(get_text("feature_sqlite", current_language))
        st.markdown(get_text("feature_responsive", current_language))
        st.markdown(get_text("feature_menu_nav", current_language))
        st.markdown(get_text("feature_bilingual", current_language))
    
    with col2:
        st.markdown(get_text("tech_stack_title", current_language))
        st.markdown(get_text("tech_streamlit", current_language).format(version=st.__version__))
        st.markdown(get_text("tech_pandas", current_language))
        st.markdown(get_text("tech_sqlite", current_language))
        st.markdown(get_text("tech_python", current_language))
        st.markdown(get_text("tech_cloud", current_language))
        st.markdown(get_text("tech_i18n", current_language))
    
    # 显示相关链接
    st.markdown("---")
    st.markdown(get_text("links_title", current_language))
    st.markdown(get_text("link_github", current_language), unsafe_allow_html=True)
    st.markdown(get_text("link_demo", current_language), unsafe_allow_html=True)
    st.markdown(get_text("link_docs", current_language), unsafe_allow_html=True)
    
    # 显示当前版本信息
    st.markdown("---")
    st.markdown(get_text("version_info_title", current_language))
    st.markdown(get_text("version_info", current_language).format(app_version="v0.1.0", streamlit_version=st.__version__))
    
    # 显示项目结构
    st.markdown("---")
    st.markdown(get_text("project_structure_title", current_language))
    st.markdown("""
    ```
    StreamlitCCDemo/
    ├── app.py                    # 主应用文件
    ├── translations.json         # 多语言翻译配置
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
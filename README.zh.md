# 🚀 Streamlit Community Cloud 多语言数据可视化演示

![Streamlit 徽章](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
![Python 3.13+](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Streamlit 1.45.1](https://img.shields.io/badge/Streamlit-1.45.1-red.svg)
![Pandas 2.2.0+](https://img.shields.io/badge/Pandas-2.2.0+-green.svg)
![MIT 许可证](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub 仓库](https://img.shields.io/badge/GitHub-Repository-brightgreen.svg)

## 🌐 选择语言: [English](README.md) | [Español](README.es.md)

> 🌐 **在线演示**: [https://community-cloud-demo.streamlit.app/](https://community-cloud-demo.streamlit.app/)

**开源 Streamlit 多语言数据可视化演示项目，支持交互式数据展示、文件上传、用户反馈、聊天演示，适合云端一键部署。支持英文、中文、西班牙文。**

## ✨ 功能特性

- �� **极简设计** - 简洁清晰的用户界面
- 🔄 **实时交互** - 文本输入、按钮点击、滑块调节、下拉选择
- 💬 **聊天演示** - 基于 Streamlit 官方组件的多语言聊天界面
- 📁 **文件上传** - 支持多种格式文件上传和内容读取
- 📂 **静态文件读取** - 读取项目中的 JSON 和 CSV 数据文件
- 📊 **数据展示** - 表格展示、统计分析、数据可视化
- 📱 **响应式布局** - 适配各种设备屏幕
- 🌐 **多语言切换** - 侧边栏可随时切换 English/中文/西班牙语
- ☁️ **云端部署** - 一键部署到 Streamlit Community Cloud
- 🚀 **快速启动** - 最小化依赖，快速运行

## 🛠️ 技术栈

- **Python** - 3.13+
- **Streamlit** - 1.45.1（最新）
- **Pandas** - 2.2.0+（支持 Python 3.13）
- **GitHub** - 代码托管
- **Streamlit Community Cloud** - 云端部署

## 📦 安装与运行

### 环境要求
- Python 3.13 或更高版本
- pip 包管理器

### 本地运行

1. **克隆仓库**
```bash
git clone https://github.com/franksunye/StreamlitCCDemo.git
cd StreamlitCCDemo
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **启动应用**
```bash
streamlit run app.py
```

4. **访问应用**
打开浏览器访问 `http://localhost:8501`

## ☁️ 云端部署

### Streamlit Community Cloud 部署

1. **Fork 本仓库** 到你的 GitHub 账号
2. **访问** [Streamlit Community Cloud](https://share.streamlit.io/)
3. **登录** 使用 GitHub 账号
4. **创建新应用**：
   - Repository: `你的用户名/StreamlitCCDemo`
   - Branch: `main`
   - Main file path: `app.py`
5. **点击 Deploy** 等待部署完成

### 自定义部署

你也可以修改代码后重新部署：
```bash
git add .
git commit -m "feat: 添加新功能"
git push origin main
```

## 📁 项目结构

```
StreamlitCCDemo/
├── app.py                    # 主应用文件
├── translations.json         # 多语言翻译配置
├── requirements.txt          # Python 依赖
├── README.md                # 项目说明（英文）
├── README.zh.md             # 项目说明（中文）
├── README.es.md             # 项目说明（西班牙文）
├── LICENSE                  # MIT 许可证
├── sample.txt               # 示例文本文件
└── data/                    # 数据文件目录
    ├── sample_data.json     # JSON 示例数据
    └── weather_data.csv     # CSV 天气数据
```

## 🎮 使用说明

### 语言切换
- **侧边栏语言切换器**：可随时切换 English/中文/西班牙语，所有界面和功能即时切换为对应语言。
- **默认语言**：应用首次打开为英文，可手动切换为中文或西班牙文。

### 基础交互功能
- **文本输入框** - 输入你的名字，支持 session state 持久化
- **问候按钮** - 点击获取个性化问候
- **年龄滑块** - 选择年龄范围 (0-100)
- **颜色选择器** - 选择喜欢的颜色

### 文件处理功能
- **文件上传** - 支持 txt, md, py, json, csv 格式
- **内容预览** - 实时显示文件内容
- **统计信息** - 显示行数、单词数、字符数
- **编码支持** - 自动处理 UTF-8 和 Latin-1 编码

### 静态数据展示
- **JSON 数据** - 应用信息、用户数据、统计信息
- **CSV 数据** - 天气数据表格和统计分析
- **双列布局** - 左右分栏展示不同类型数据

## 🔧 技术细节

### 国际化（i18n）实现
- 所有界面文本均通过 `translations.json` 统一管理，支持多语言扩展
- 语言切换即时生效，无需刷新页面
- 采用 Streamlit session state 保持用户选择

### Session State 管理
应用使用 Streamlit 的 session state 功能来保持用户输入状态：
```python
# 初始化 session state
if 'user_name' not in st.session_state:
    st.session_state.user_name = "世界"

# 使用 session state
user_name = st.text_input("请输入你的名字：", value=st.session_state.user_name, key="user_name_input")
```

### 文件读取处理
支持多种文件格式的安全读取：
```python
# 安全解码
try:
    text_content = file_content.decode('utf-8')
except UnicodeDecodeError:
    text_content = file_content.decode('latin-1')
```

### 数据展示优化
使用 pandas 进行数据处理和展示：
```python
# 数据统计
st.write(f"- 总记录数：{len(df)}")
st.write(f"- 平均温度：{df['温度'].mean():.1f}°C")
```

## 🚀 版本历史

### v0.1.0（当前版本）
- ✅ 新增英文、中文、西班牙文多语言切换，支持国际化（i18n）
- ✅ 所有界面和功能均可即时切换语言
- ✅ 新增 translations.json 统一管理多语言文本
- ✅ 升级到 Streamlit 1.45.1
- ✅ 升级到 Pandas 2.2.0+（支持 Python 3.13）
- ✅ 修复 session state 兼容性问题
- ✅ 添加静态文件读取功能
- ✅ 完善错误处理机制

### 主要更新
- **依赖升级** - 使用最新稳定版本
- **兼容性修复** - 解决 Python 3.13 兼容性问题
- **功能增强** - 添加数据展示和文件处理功能
- **国际化支持** - 支持多语言切换
- **代码优化** - 改进错误处理和用户体验

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支（`git checkout -b feature/AmazingFeature`）
3. 提交更改（`git commit -m 'Add some AmazingFeature'`）
4. 推送到分支（`git push origin feature/AmazingFeature`）
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🔗 相关链接

- [Streamlit 官方文档](https://docs.streamlit.io/)
- [Streamlit Community Cloud 部署指南](https://docs.streamlit.io/streamlit-community-cloud)
- [Pandas 官方文档](https://pandas.pydata.org/docs/)
- [GitHub 仓库](https://github.com/franksunye/StreamlitCCDemo)

## 📞 联系方式

- **GitHub**: [@franksunye](https://github.com/franksunye)
- **在线演示**: [https://community-cloud-demo.streamlit.app/](https://community-cloud-demo.streamlit.app/) 
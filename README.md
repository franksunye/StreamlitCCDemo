# 极简 Streamlit 应用

这是一个最简单的 Streamlit 应用示例，可以在 Streamlit Cloud 上部署。

## 功能

- 文本输入框
- 按钮交互
- 滑块控件
- 下拉选择框

## 本地运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
streamlit run app.py
```

## 部署到 Streamlit Cloud

1. 将代码推送到 GitHub 仓库
2. 访问 [Streamlit Cloud](https://share.streamlit.io/)
3. 点击 "New app"
4. 选择你的 GitHub 仓库
5. 设置主文件路径为 `app.py`
6. 点击 "Deploy"

## 文件结构

```
├── app.py              # 主应用文件
├── requirements.txt    # Python 依赖
└── README.md          # 说明文档
``` 
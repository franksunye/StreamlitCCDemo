# 🚀 Streamlit Community Cloud Demo

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sccdemo.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2.0+-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-brightgreen.svg)](https://github.com/franksunye/StreamlitCCDemo)

## 🌐 Read this in other languages: [中文](README.zh.md) | [Español](README.es.md)

> 🌐 **Online Demo**: [https://community-cloud-demo.streamlit.app/](https://community-cloud-demo.streamlit.app/)

A fully-featured Streamlit application demo, showing how to quickly deploy interactive web apps on Streamlit Community Cloud. **Supports English, Chinese, and Spanish (i18n)**, including user interaction, file processing, data display, and database features.

## ✨ Features

- 🎯 **Minimalist Design** - Clean and clear user interface
- 🔄 **Real-time Interaction** - Text input, button click, slider, selectbox
- 📁 **File Upload** - Supports multiple file formats and content preview
- 📂 **Static File Reading** - Read JSON and CSV data files in the project
- 📊 **Data Display** - Table, statistics, and data visualization
- 📱 **Responsive Layout** - Adapts to all device screens
- 🌐 **Multi-language Switch** - Sidebar language selector for English/中文/Español
- ☁️ **Cloud Deployment** - One-click deploy to Streamlit Community Cloud
- 🚀 **Quick Start** - Minimal dependencies, fast to run

## 🛠️ Tech Stack

- **Python** - 3.13+
- **Streamlit** - 1.45.1 (latest)
- **Pandas** - 2.2.0+ (supports Python 3.13)
- **GitHub** - Code hosting
- **Streamlit Community Cloud** - Cloud deployment

## 📦 Installation & Run

### Requirements
- Python 3.13 or above
- pip package manager

### Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/franksunye/StreamlitCCDemo.git
cd StreamlitCCDemo
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Start the app**
```bash
streamlit run app.py
```

4. **Visit the app**
Open your browser and go to `http://localhost:8501`

## ☁️ Cloud Deployment

### Deploy on Streamlit Community Cloud

1. **Fork this repo** to your GitHub account
2. **Go to** [Streamlit Community Cloud](https://share.streamlit.io/)
3. **Log in** with your GitHub account
4. **Create a new app**:
   - Repository: `your-username/StreamlitCCDemo`
   - Branch: `main`
   - Main file path: `app.py`
5. **Click Deploy** and wait for deployment

### Custom Deployment

You can also modify the code and redeploy:
```bash
git add .
git commit -m "feat: add new feature"
git push origin main
```

## 📁 Project Structure

```
StreamlitCCDemo/
├── app.py                    # Main app file
├── translations.json         # Multi-language translations
├── requirements.txt          # Python dependencies
├── README.md                # Project description (English)
├── README.zh.md             # Project description (Chinese)
├── README.es.md             # Project description (Spanish)
├── LICENSE                  # MIT License
├── sample.txt               # Sample text file
└── data/                    # Data files
    ├── sample_data.json     # JSON sample data
    └── weather_data.csv     # CSV weather data
```

## 🎮 Usage

### Language Switch
- **Sidebar Language Selector**: Instantly switch between English/中文/Español, all UI and features update immediately.
- **Default Language**: English on first load, can be changed anytime.

### Basic Interactive Features
- **Text Input** - Enter your name, supports session state
- **Greet Button** - Click to get a personalized greeting
- **Age Slider** - Select age (0-100)
- **Color Selector** - Choose your favorite color

### File Processing
- **File Upload** - Supports txt, md, py, json, csv
- **Content Preview** - Real-time file content display
- **Statistics** - Show line, word, and character count
- **Encoding Support** - Handles UTF-8 and Latin-1

### Static Data Display
- **JSON Data** - App info, user data, statistics
- **CSV Data** - Weather data table and analysis
- **Two-column Layout** - Display different data types side by side

## 🔧 Technical Details

### Internationalization (i18n)
- All UI texts managed via `translations.json`, easy to extend to more languages
- Language switch is instant, no page reload needed
- Uses Streamlit session state to remember user choice

### Session State
The app uses Streamlit's session state to persist user input:
```python
# Initialize session state
if 'user_name' not in st.session_state:
    st.session_state.user_name = "World"

# Use session state
user_name = st.text_input("Enter your name:", value=st.session_state.user_name, key="user_name_input")
```

### File Reading
Safe reading for multiple file formats:
```python
# Safe decode
try:
    text_content = file_content.decode('utf-8')
except UnicodeDecodeError:
    text_content = file_content.decode('latin-1')
```

### Data Display
Uses pandas for data processing and display:
```python
# Data statistics
st.write(f"- Total records: {len(df)}")
st.write(f"- Average temperature: {df['Temperature'].mean():.1f}°C")
```

## 🚀 Version History

### v0.1.0 (Current)
- ✅ Added English, Chinese, and Spanish language support (i18n)
- ✅ All UI and features can switch language instantly
- ✅ Added translations.json for unified text management
- ✅ Upgraded to Streamlit 1.45.1
- ✅ Upgraded to Pandas 2.2.0+ (Python 3.13 support)
- ✅ Improved session state compatibility
- ✅ Added static file reading
- ✅ Enhanced error handling

### Major Updates
- **Dependency Upgrades** - Latest stable versions
- **Compatibility Fixes** - Python 3.13 support
- **Feature Enhancements** - Data display and file processing
- **Internationalization** - Multi-language support
- **Code Optimization** - Better error handling and UX

## 🤝 Contributing

Contributions are welcome!

1. Fork this repo
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Community Cloud Guide](https://docs.streamlit.io/streamlit-community-cloud)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [GitHub Repository](https://github.com/franksunye/StreamlitCCDemo)

## 📞 Contact

- **GitHub**: [@franksunye](https://github.com/franksunye)
- **Online Demo**: [https://community-cloud-demo.streamlit.app/](https://community-cloud-demo.streamlit.app/)

## 🎯 Project Highlights

- **Latest Tech Stack** - Use latest versions of Streamlit and Pandas
- **Complete Feature Demo** - Covers main features of Streamlit
- **Production Ready** - Includes error handling, compatibility check, and best practices
- **Easy to Extend** - Clear code structure, easy to add new features
- **Internationalization** - Multi-language support, suitable for global users
- **Documentation** - Detailed explanation and usage guide

---

⭐ If this project helps you, please give it a star! 
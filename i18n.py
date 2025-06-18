import streamlit as st
import json
import os

class I18nManager:
    """国际化管理器"""
    
    def __init__(self):
        self.translations = {}
        self.languages = {}
        self.load_translations()
    
    def load_translations(self):
        """加载翻译文件"""
        try:
            with open('translations.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.languages = data.get('languages', {})
                self.translations = data.get('translations', {})
        except Exception as e:
            st.error(f"Error loading translations: {e}")
            # 使用默认英文
            self.languages = {"en": {"name": "English", "native_name": "English", "flag": "🇺🇸"}}
            self.translations = {}
    
    def get_text(self, key, language="en"):
        """获取指定语言的文本"""
        try:
            return self.translations.get(language, {}).get(key, key)
        except:
            return key
    
    def get_language_info(self, language_code):
        """获取语言信息"""
        return self.languages.get(language_code, {})
    
    def get_available_languages(self):
        """获取可用语言列表"""
        return list(self.languages.keys())
    
    def get_language_display_name(self, language_code):
        """获取语言显示名称"""
        lang_info = self.get_language_info(language_code)
        return f"{lang_info.get('flag', '')} {lang_info.get('native_name', language_code)}"

# 全局国际化管理器实例
@st.cache_resource
def get_i18n_manager():
    return I18nManager()

def get_text(key, language="en"):
    """获取指定语言的文本（便捷函数）"""
    i18n = get_i18n_manager()
    return i18n.get_text(key, language)

def get_language():
    """获取当前语言设置"""
    if 'language' not in st.session_state:
        st.session_state.language = "en"  # 默认英文
    return st.session_state.language

def set_language(language):
    """设置语言"""
    st.session_state.language = language

def get_available_languages():
    """获取可用语言列表"""
    i18n = get_i18n_manager()
    return i18n.get_available_languages()

def get_language_display_name(language_code):
    """获取语言显示名称"""
    i18n = get_i18n_manager()
    return i18n.get_language_display_name(language_code) 
 
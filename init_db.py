import sqlite3
import os
from datetime import datetime

def init_database():
    """初始化 SQLite 数据库"""
    db_path = 'feedback.db'
    
    # 如果数据库文件已存在，先删除
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # 创建数据库连接
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 创建反馈表
    cursor.execute('''
        CREATE TABLE feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 插入示例数据
    sample_feedback = [
        ('张三', '这个应用很棒，界面很清晰！'),
        ('李四', '文件上传功能很实用，希望能支持更多格式'),
        ('王五', '数据展示功能很直观，统计信息很有用'),
        ('系统', '欢迎使用我们的 Streamlit 应用！'),
        ('开发者', '这是一个功能完整的 Streamlit 示例应用')
    ]
    
    cursor.executemany(
        'INSERT INTO feedback (name, message) VALUES (?, ?)',
        sample_feedback
    )
    
    # 提交更改并关闭连接
    conn.commit()
    conn.close()
    
    print(f"数据库初始化完成：{db_path}")
    print(f"已创建 {len(sample_feedback)} 条示例反馈")

if __name__ == "__main__":
    init_database() 
import sqlite3
import os
from datetime import datetime

class FeedbackDB:
    def __init__(self, db_path='feedback.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """初始化数据库，如果不存在则创建"""
        if not os.path.exists(self.db_path):
            self.create_tables()
            self.insert_sample_data()
    
    def create_tables(self):
        """创建数据库表"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def insert_sample_data(self):
        """插入示例数据"""
        sample_feedback = [
            ('张三', '这个应用很棒，界面很清晰！'),
            ('李四', '文件上传功能很实用，希望能支持更多格式'),
            ('王五', '数据展示功能很直观，统计信息很有用'),
            ('系统', '欢迎使用我们的 Streamlit 应用！'),
            ('开发者', '这是一个功能完整的 Streamlit 示例应用')
        ]
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.executemany(
            'INSERT INTO feedback (name, message) VALUES (?, ?)',
            sample_feedback
        )
        
        conn.commit()
        conn.close()
    
    def add_feedback(self, name, message):
        """添加新反馈"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute(
                'INSERT INTO feedback (name, message) VALUES (?, ?)',
                (name, message)
            )
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"添加反馈时出错：{e}")
            return False
    
    def get_all_feedback(self):
        """获取所有反馈"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, name, message, created_at 
                FROM feedback 
                ORDER BY created_at DESC
            ''')
            
            feedback = cursor.fetchall()
            conn.close()
            return feedback
        except Exception as e:
            print(f"获取反馈时出错：{e}")
            return []
    
    def get_feedback_count(self):
        """获取反馈总数"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM feedback')
            count = cursor.fetchone()[0]
            
            conn.close()
            return count
        except Exception as e:
            print(f"获取反馈数量时出错：{e}")
            return 0
    
    def delete_feedback(self, feedback_id):
        """删除指定反馈"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM feedback WHERE id = ?', (feedback_id,))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"删除反馈时出错：{e}")
            return False 
"""
Supabase 数据库连接配置
"""
import os
from pathlib import Path
from supabase import create_client, Client
from dotenv import load_dotenv

# 加载环境变量（从 server 目录的 .env 文件）
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

class SupabaseConfig:
    """Supabase 配置类"""
    
    def __init__(self):
        self.url = os.getenv('SUPABASE_URL')
        self.anon_key = os.getenv('SUPABASE_ANON_KEY')
        self.service_role_key = os.getenv('SUPABASE_SERVICE_ROLE_KEY')
        
        if not self.url or not self.anon_key:
            raise ValueError("Supabase URL 和 ANON_KEY 必须配置在 .env 文件中")
    
    def get_client(self, use_service_role: bool = False) -> Client:
        """
        获取 Supabase 客户端
        
        Args:
            use_service_role: 是否使用服务角色密钥（用于需要绕过RLS的操作）
        
        Returns:
            Supabase 客户端实例
        """
        key = self.service_role_key if use_service_role else self.anon_key
        return create_client(self.url, key)
    
    @property
    def table_names(self):
        """返回表名配置"""
        return {
            'schemas': os.getenv('TABLE_SCHEMAS', 'schemas'),
            'groups': os.getenv('TABLE_GROUPS', 'groups'),
            'fields': os.getenv('TABLE_FIELDS', 'fields'),
            'data_rows': os.getenv('TABLE_DATA_ROWS', 'data_rows')
        }

# 全局配置实例
supabase_config = SupabaseConfig()


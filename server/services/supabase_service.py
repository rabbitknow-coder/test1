"""
Supabase 数据库服务
提供数据持久化功能
"""
from typing import List, Dict, Optional
from config.supabase import supabase_config

class SupabaseService:
    """Supabase 数据库服务类"""
    
    def __init__(self):
        self.client = supabase_config.get_client()
        self.tables = supabase_config.table_names
    
    # ========== Schema 相关操作 ==========
    
    def create_schema(self, schema_data: Dict) -> Dict:
        """创建 Schema"""
        response = self.client.table(self.tables['schemas']).insert(schema_data).execute()
        return response.data[0] if response.data else None
    
    def get_schema(self, schema_id: int) -> Optional[Dict]:
        """获取 Schema"""
        response = self.client.table(self.tables['schemas']).select('*').eq('id', schema_id).execute()
        return response.data[0] if response.data else None
    
    def update_schema(self, schema_id: int, schema_data: Dict) -> Dict:
        """更新 Schema"""
        response = self.client.table(self.tables['schemas']).update(schema_data).eq('id', schema_id).execute()
        return response.data[0] if response.data else None
    
    def delete_schema(self, schema_id: int) -> bool:
        """删除 Schema"""
        response = self.client.table(self.tables['schemas']).delete().eq('id', schema_id).execute()
        return True
    
    def list_schemas(self) -> List[Dict]:
        """列出所有 Schema"""
        response = self.client.table(self.tables['schemas']).select('*').order('created_at', desc=True).execute()
        return response.data or []
    
    # ========== Group 相关操作 ==========
    
    def create_group(self, group_data: Dict) -> Dict:
        """创建分组"""
        response = self.client.table(self.tables['groups']).insert(group_data).execute()
        return response.data[0] if response.data else None
    
    def get_group(self, group_id: int) -> Optional[Dict]:
        """获取分组"""
        response = self.client.table(self.tables['groups']).select('*').eq('id', group_id).execute()
        return response.data[0] if response.data else None
    
    def update_group(self, group_id: int, group_data: Dict) -> Dict:
        """更新分组"""
        response = self.client.table(self.tables['groups']).update(group_data).eq('id', group_id).execute()
        return response.data[0] if response.data else None
    
    def delete_group(self, group_id: int) -> bool:
        """删除分组"""
        response = self.client.table(self.tables['groups']).delete().eq('id', group_id).execute()
        return True
    
    def list_groups(self, schema_id: Optional[int] = None) -> List[Dict]:
        """列出分组"""
        query = self.client.table(self.tables['groups']).select('*')
        if schema_id:
            query = query.eq('schema_id', schema_id)
        response = query.order('id').execute()
        return response.data or []
    
    # ========== Field 相关操作 ==========
    
    def create_field(self, field_data: Dict) -> Dict:
        """创建字段"""
        response = self.client.table(self.tables['fields']).insert(field_data).execute()
        return response.data[0] if response.data else None
    
    def get_field(self, field_id: int) -> Optional[Dict]:
        """获取字段"""
        response = self.client.table(self.tables['fields']).select('*').eq('id', field_id).execute()
        return response.data[0] if response.data else None
    
    def update_field(self, field_id: int, field_data: Dict) -> Dict:
        """更新字段"""
        response = self.client.table(self.tables['fields']).update(field_data).eq('id', field_id).execute()
        return response.data[0] if response.data else None
    
    def delete_field(self, field_id: int) -> bool:
        """删除字段"""
        response = self.client.table(self.tables['fields']).delete().eq('id', field_id).execute()
        return True
    
    def list_fields(self, schema_id: Optional[int] = None) -> List[Dict]:
        """列出字段"""
        query = self.client.table(self.tables['fields']).select('*')
        if schema_id:
            query = query.eq('schema_id', schema_id)
        response = query.order('order_index').execute()
        return response.data or []
    
    # ========== Data Row 相关操作 ==========
    
    def create_data_row(self, row_data: Dict) -> Dict:
        """创建数据行"""
        response = self.client.table(self.tables['data_rows']).insert(row_data).execute()
        return response.data[0] if response.data else None
    
    def get_data_row(self, row_id: int) -> Optional[Dict]:
        """获取数据行"""
        response = self.client.table(self.tables['data_rows']).select('*').eq('id', row_id).execute()
        return response.data[0] if response.data else None
    
    def update_data_row(self, row_id: int, row_data: Dict) -> Dict:
        """更新数据行"""
        response = self.client.table(self.tables['data_rows']).update(row_data).eq('id', row_id).execute()
        return response.data[0] if response.data else None
    
    def delete_data_row(self, row_id: int) -> bool:
        """删除数据行"""
        response = self.client.table(self.tables['data_rows']).delete().eq('id', row_id).execute()
        return True
    
    def list_data_rows(self, schema_id: Optional[int] = None, group_id: Optional[int] = None) -> List[Dict]:
        """列出数据行"""
        query = self.client.table(self.tables['data_rows']).select('*')
        if schema_id:
            query = query.eq('schema_id', schema_id)
        if group_id:
            query = query.eq('group_id', group_id)
        response = query.order('group_id').order('index').execute()
        return response.data or []
    
    def bulk_insert_data_rows(self, rows: List[Dict]) -> List[Dict]:
        """批量插入数据行"""
        response = self.client.table(self.tables['data_rows']).insert(rows).execute()
        return response.data or []
    
    def bulk_update_data_rows(self, updates: List[Dict]) -> List[Dict]:
        """批量更新数据行（需要包含id字段）"""
        # Supabase 不支持批量更新，需要逐个更新
        results = []
        for update_data in updates:
            row_id = update_data.pop('id')
            result = self.update_data_row(row_id, update_data)
            if result:
                results.append(result)
        return results
    
    def bulk_delete_data_rows(self, row_ids: List[int]) -> bool:
        """批量删除数据行"""
        response = self.client.table(self.tables['data_rows']).delete().in_('id', row_ids).execute()
        return True


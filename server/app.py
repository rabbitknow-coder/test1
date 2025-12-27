"""
Flask 应用入口
提供 API 接口用于前端与 Supabase 数据库交互
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.supabase_service import SupabaseService
from config.supabase import SupabaseConfig

# 加载环境变量
load_dotenv()

# 初始化 Flask 应用
app = Flask(__name__)
CORS(app)

# 配置
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# 初始化 Supabase 服务
try:
    supabase_service = SupabaseService()
    print("Supabase 连接成功")
except Exception as e:
    print(f"Supabase 连接失败: {e}")
    supabase_service = None

@app.route('/')
def health_check():
    """健康检查"""
    return jsonify({
        'status': 'ok',
        'message': 'API 服务运行正常',
        'supabase_connected': supabase_service is not None
    })

# ========== Schema API ==========

@app.route('/api/schemas', methods=['GET'])
def list_schemas():
    """获取所有 Schema"""
    try:
        schemas = supabase_service.list_schemas()
        return jsonify({'success': True, 'data': schemas})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/schemas', methods=['POST'])
def create_schema():
    """创建 Schema"""
    try:
        data = request.json
        schema = supabase_service.create_schema(data)
        return jsonify({'success': True, 'data': schema}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/schemas/<int:schema_id>', methods=['GET'])
def get_schema(schema_id):
    """获取单个 Schema"""
    try:
        schema = supabase_service.get_schema(schema_id)
        if schema:
            return jsonify({'success': True, 'data': schema})
        return jsonify({'success': False, 'error': 'Schema not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/schemas/<int:schema_id>', methods=['PUT'])
def update_schema(schema_id):
    """更新 Schema"""
    try:
        data = request.json
        schema = supabase_service.update_schema(schema_id, data)
        return jsonify({'success': True, 'data': schema})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/schemas/<int:schema_id>', methods=['DELETE'])
def delete_schema(schema_id):
    """删除 Schema"""
    try:
        supabase_service.delete_schema(schema_id)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ========== Groups API ==========

@app.route('/api/groups', methods=['GET'])
def list_groups():
    """获取分组列表"""
    try:
        schema_id = request.args.get('schema_id', type=int)
        groups = supabase_service.list_groups(schema_id)
        return jsonify({'success': True, 'data': groups})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/groups', methods=['POST'])
def create_group():
    """创建分组"""
    try:
        data = request.json
        group = supabase_service.create_group(data)
        return jsonify({'success': True, 'data': group}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/groups/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    """更新分组"""
    try:
        data = request.json
        group = supabase_service.update_group(group_id, data)
        return jsonify({'success': True, 'data': group})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    """删除分组"""
    try:
        supabase_service.delete_group(group_id)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ========== Fields API ==========

@app.route('/api/fields', methods=['GET'])
def list_fields():
    """获取字段列表"""
    try:
        schema_id = request.args.get('schema_id', type=int)
        fields = supabase_service.list_fields(schema_id)
        return jsonify({'success': True, 'data': fields})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/fields', methods=['POST'])
def create_field():
    """创建字段"""
    try:
        data = request.json
        field = supabase_service.create_field(data)
        return jsonify({'success': True, 'data': field}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/fields/<int:field_id>', methods=['PUT'])
def update_field(field_id):
    """更新字段"""
    try:
        data = request.json
        field = supabase_service.update_field(field_id, data)
        return jsonify({'success': True, 'data': field})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/fields/<int:field_id>', methods=['DELETE'])
def delete_field(field_id):
    """删除字段"""
    try:
        supabase_service.delete_field(field_id)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ========== Data Rows API ==========

@app.route('/api/data-rows', methods=['GET'])
def list_data_rows():
    """获取数据行列表"""
    try:
        schema_id = request.args.get('schema_id', type=int)
        group_id = request.args.get('group_id', type=int)
        rows = supabase_service.list_data_rows(schema_id, group_id)
        return jsonify({'success': True, 'data': rows})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/data-rows', methods=['POST'])
def create_data_row():
    """创建数据行"""
    try:
        data = request.json
        row = supabase_service.create_data_row(data)
        return jsonify({'success': True, 'data': row}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/data-rows/bulk', methods=['POST'])
def bulk_create_data_rows():
    """批量创建数据行"""
    try:
        rows = request.json.get('rows', [])
        results = supabase_service.bulk_insert_data_rows(rows)
        return jsonify({'success': True, 'data': results}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/data-rows/<int:row_id>', methods=['PUT'])
def update_data_row(row_id):
    """更新数据行"""
    try:
        data = request.json
        row = supabase_service.update_data_row(row_id, data)
        return jsonify({'success': True, 'data': row})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/data-rows/bulk', methods=['PUT'])
def bulk_update_data_rows():
    """批量更新数据行"""
    try:
        updates = request.json.get('updates', [])
        results = supabase_service.bulk_update_data_rows(updates)
        return jsonify({'success': True, 'data': results})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/data-rows/<int:row_id>', methods=['DELETE'])
def delete_data_row(row_id):
    """删除数据行"""
    try:
        supabase_service.delete_data_row(row_id)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/data-rows/bulk', methods=['DELETE'])
def bulk_delete_data_rows():
    """批量删除数据行"""
    try:
        row_ids = request.json.get('row_ids', [])
        supabase_service.bulk_delete_data_rows(row_ids)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ========== 完整数据同步 API ==========

@app.route('/api/sync', methods=['POST'])
def sync_all_data():
    """同步所有数据（用于前端保存）"""
    try:
        data = request.json
        schema_id = data.get('schema_id')
        
        # 同步分组
        if 'groups' in data:
            for group in data['groups']:
                if 'id' in group and group['id']:
                    supabase_service.update_group(group['id'], group)
                else:
                    group['schema_id'] = schema_id
                    supabase_service.create_group(group)
        
        # 同步字段
        if 'fields' in data:
            for field in data['fields']:
                if 'id' in field and field['id']:
                    supabase_service.update_field(field['id'], field)
                else:
                    field['schema_id'] = schema_id
                    supabase_service.create_field(field)
        
        # 同步数据行
        if 'data_rows' in data:
            for row in data['data_rows']:
                row['schema_id'] = schema_id
                if 'id' in row and row['id']:
                    supabase_service.update_data_row(row['id'], row)
                else:
                    supabase_service.create_data_row(row)
        
        return jsonify({'success': True, 'message': '数据同步成功'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/load', methods=['GET'])
def load_all_data():
    """加载所有数据（用于前端加载）"""
    try:
        schema_id = request.args.get('schema_id', type=int)
        if not schema_id:
            return jsonify({'success': False, 'error': 'schema_id is required'}), 400
        
        groups = supabase_service.list_groups(schema_id)
        fields = supabase_service.list_fields(schema_id)
        data_rows = supabase_service.list_data_rows(schema_id)
        
        return jsonify({
            'success': True,
            'data': {
                'groups': groups,
                'fields': fields,
                'data_rows': data_rows
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)


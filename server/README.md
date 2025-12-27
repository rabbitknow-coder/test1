# 后端服务说明

## 环境配置

1. 复制 `.env.example` 为 `.env`
2. 填写 Supabase 配置信息：

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key-here
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 数据库初始化

1. 登录 Supabase Dashboard
2. 进入 SQL Editor
3. 执行 `models/schema.sql` 中的 SQL 语句创建表结构

## 运行服务

```bash
python app.py
```

服务将在 `http://localhost:5000` 启动

## API 接口

### Schema 管理
- `GET /api/schemas` - 获取所有 Schema
- `POST /api/schemas` - 创建 Schema
- `GET /api/schemas/<id>` - 获取单个 Schema
- `PUT /api/schemas/<id>` - 更新 Schema
- `DELETE /api/schemas/<id>` - 删除 Schema

### Groups 管理
- `GET /api/groups?schema_id=<id>` - 获取分组列表
- `POST /api/groups` - 创建分组
- `PUT /api/groups/<id>` - 更新分组
- `DELETE /api/groups/<id>` - 删除分组

### Fields 管理
- `GET /api/fields?schema_id=<id>` - 获取字段列表
- `POST /api/fields` - 创建字段
- `PUT /api/fields/<id>` - 更新字段
- `DELETE /api/fields/<id>` - 删除字段

### Data Rows 管理
- `GET /api/data-rows?schema_id=<id>&group_id=<id>` - 获取数据行列表
- `POST /api/data-rows` - 创建数据行
- `POST /api/data-rows/bulk` - 批量创建数据行
- `PUT /api/data-rows/<id>` - 更新数据行
- `PUT /api/data-rows/bulk` - 批量更新数据行
- `DELETE /api/data-rows/<id>` - 删除数据行
- `DELETE /api/data-rows/bulk` - 批量删除数据行

### 数据同步
- `POST /api/sync` - 同步所有数据
- `GET /api/load?schema_id=<id>` - 加载所有数据


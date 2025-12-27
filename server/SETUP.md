# Supabase 配置指南

## 1. 获取 Supabase 配置信息

1. 登录 [Supabase Dashboard](https://app.supabase.com)
2. 选择你的项目
3. 进入 **Settings** > **API**
4. 复制以下信息：
   - **Project URL** → `SUPABASE_URL`
   - **anon public** key → `SUPABASE_ANON_KEY`
   - **service_role** key → `SUPABASE_SERVICE_ROLE_KEY` (可选，用于需要绕过RLS的操作)

## 2. 配置环境变量

在 `server/` 目录下创建 `.env` 文件：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的配置：

```env
SUPABASE_URL=https://znipeprdmraqszfjbsgq.supabase.co
SUPABASE_ANON_KEY=sb_publishable_82RiEJDW98uQ_JD6NR23iQ_j1_Nu10x
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here
ZHIPU_API_KEY=your-zhipu-api-key-here
PORT=5000
FLASK_ENV=development
```

**已配置的信息**：
- ✅ `SUPABASE_URL`: https://znipeprdmraqszfjbsgq.supabase.co
- ✅ `SUPABASE_ANON_KEY`: sb_publishable_82RiEJDW98uQ_JD6NR23iQ_j1_Nu10x

**需要配置的信息**：
- ⚠️ `SUPABASE_SERVICE_ROLE_KEY`: 从 Supabase Dashboard 的 Settings > API 中获取 `service_role` key（这个 key 具有完整权限，请妥善保管）
- ⚠️ `ZHIPU_API_KEY`: 你的智谱 API Key（如果需要使用智谱 API）

## 3. 初始化数据库

1. 登录 Supabase Dashboard
2. 进入 **SQL Editor**
3. 点击 **New Query**
4. 复制 `models/schema.sql` 中的 SQL 语句
5. 执行 SQL 语句创建表结构

## 4. 安装依赖

```bash
cd server
pip install -r requirements.txt
```

## 5. 运行服务

```bash
python app.py
```

服务将在 `http://localhost:5000` 启动

## 6. 测试连接

访问 `http://localhost:5000/` 查看健康检查，应该返回：

```json
{
  "status": "ok",
  "message": "API 服务运行正常",
  "supabase_connected": true
}
```

## 注意事项

- `.env` 文件包含敏感信息，不要提交到 Git
- `SUPABASE_SERVICE_ROLE_KEY` 具有完整权限，请妥善保管
- 生产环境建议使用更严格的 RLS 策略


-- Supabase 数据库表结构定义

-- Schema 表（存储配置方案）
CREATE TABLE IF NOT EXISTS schemas (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    meta JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Groups 表（存储分组信息）
CREATE TABLE IF NOT EXISTS groups (
    id BIGSERIAL PRIMARY KEY,
    schema_id BIGINT REFERENCES schemas(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    struct_name VARCHAR(255) NOT NULL,
    parent_id BIGINT REFERENCES groups(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(schema_id, name)
);

-- Fields 表（存储字段定义）
CREATE TABLE IF NOT EXISTS fields (
    id BIGSERIAL PRIMARY KEY,
    schema_id BIGINT REFERENCES schemas(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL DEFAULT 'text',
    required BOOLEAN DEFAULT FALSE,
    visible BOOLEAN DEFAULT TRUE,
    order_index INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(schema_id, name)
);

-- Data Rows 表（存储数据行）
CREATE TABLE IF NOT EXISTS data_rows (
    id BIGSERIAL PRIMARY KEY,
    schema_id BIGINT REFERENCES schemas(id) ON DELETE CASCADE,
    group_id BIGINT REFERENCES groups(id) ON DELETE SET NULL,
    index INTEGER DEFAULT 1,
    data JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 创建索引
CREATE INDEX IF NOT EXISTS idx_groups_schema_id ON groups(schema_id);
CREATE INDEX IF NOT EXISTS idx_groups_parent_id ON groups(parent_id);
CREATE INDEX IF NOT EXISTS idx_fields_schema_id ON fields(schema_id);
CREATE INDEX IF NOT EXISTS idx_data_rows_schema_id ON data_rows(schema_id);
CREATE INDEX IF NOT EXISTS idx_data_rows_group_id ON data_rows(group_id);
CREATE INDEX IF NOT EXISTS idx_data_rows_index ON data_rows(group_id, index);

-- 创建更新时间触发器函数
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- 为每个表创建更新时间触发器
CREATE TRIGGER update_schemas_updated_at BEFORE UPDATE ON schemas
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_groups_updated_at BEFORE UPDATE ON groups
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_fields_updated_at BEFORE UPDATE ON fields
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_data_rows_updated_at BEFORE UPDATE ON data_rows
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- 启用 Row Level Security (RLS)
ALTER TABLE schemas ENABLE ROW LEVEL SECURITY;
ALTER TABLE groups ENABLE ROW LEVEL SECURITY;
ALTER TABLE fields ENABLE ROW LEVEL SECURITY;
ALTER TABLE data_rows ENABLE ROW LEVEL SECURITY;

-- 创建 RLS 策略（允许所有操作，可根据需要修改）
-- 注意：在生产环境中应该设置更严格的策略

-- Schema 策略
CREATE POLICY "Allow all operations on schemas" ON schemas
    FOR ALL USING (true) WITH CHECK (true);

-- Groups 策略
CREATE POLICY "Allow all operations on groups" ON groups
    FOR ALL USING (true) WITH CHECK (true);

-- Fields 策略
CREATE POLICY "Allow all operations on fields" ON fields
    FOR ALL USING (true) WITH CHECK (true);

-- Data Rows 策略
CREATE POLICY "Allow all operations on data_rows" ON data_rows
    FOR ALL USING (true) WITH CHECK (true);


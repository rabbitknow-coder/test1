# Windows 安装指南

## 问题：pip 命令无法识别

如果你看到 `pip：无法将"pip"项识别为 cmdlet、函数、脚本文件或可运行程序的名称`，说明 Python 可能没有安装或没有正确配置。

## 解决方案

### 方法 1：安装 Python（推荐）

1. **下载 Python**
   - 访问 [Python 官网](https://www.python.org/downloads/)
   - 下载最新版本的 Python 3.x（推荐 3.11 或更高版本）
   - 选择 "Windows installer (64-bit)"

2. **安装 Python**
   - 运行下载的安装程序
   - ✅ **重要**：勾选 "Add Python to PATH"（添加到环境变量）
   - 选择 "Install Now" 或 "Customize installation"
   - 等待安装完成

3. **验证安装**
   - 关闭当前命令行窗口
   - 打开新的 PowerShell 或 CMD 窗口
   - 运行以下命令验证：
   ```powershell
   python --version
   pip --version
   ```

4. **安装项目依赖**
   ```powershell
   cd server
   pip install -r requirements.txt
   ```

### 方法 2：使用 Python Launcher（如果已安装但未添加到 PATH）

如果你已经安装了 Python 但没有添加到 PATH，可以尝试：

```powershell
# 使用 Python Launcher
py -m pip install -r requirements.txt
```

或者：

```powershell
# 使用完整路径（需要找到 Python 安装目录）
C:\Users\你的用户名\AppData\Local\Programs\Python\Python3xx\python.exe -m pip install -r requirements.txt
```

### 方法 3：手动添加到 PATH（如果 Python 已安装）

1. **找到 Python 安装目录**
   - 通常在：`C:\Users\你的用户名\AppData\Local\Programs\Python\Python3xx\`
   - 或者在：`C:\Python3xx\`

2. **添加到 PATH**
   - 按 `Win + R`，输入 `sysdm.cpl`，回车
   - 点击 "高级" 标签
   - 点击 "环境变量"
   - 在 "系统变量" 中找到 `Path`，点击 "编辑"
   - 点击 "新建"，添加以下路径：
     - `C:\Users\你的用户名\AppData\Local\Programs\Python\Python3xx\`
     - `C:\Users\你的用户名\AppData\Local\Programs\Python\Python3xx\Scripts\`
   - 点击 "确定" 保存
   - **重启命令行窗口**

3. **验证**
   ```powershell
   python --version
   pip --version
   ```

## 安装项目依赖

安装完 Python 后，在项目目录下运行：

```powershell
# 进入 server 目录
cd server

# 安装依赖
pip install -r requirements.txt
```

如果遇到权限问题，可以尝试：

```powershell
pip install --user -r requirements.txt
```

## 常见问题

### 问题 1：提示 "pip 不是内部或外部命令"

**解决方案**：
- 确保 Python 安装时勾选了 "Add Python to PATH"
- 或者使用 `python -m pip` 代替 `pip`

### 问题 2：提示 "需要管理员权限"

**解决方案**：
```powershell
# 使用 --user 参数安装到用户目录
pip install --user -r requirements.txt
```

### 问题 3：安装速度慢

**解决方案**：
```powershell
# 使用国内镜像源（清华大学）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或使用阿里云镜像
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

### 问题 4：SSL 证书错误

**解决方案**：
```powershell
# 临时禁用 SSL 验证（不推荐，仅用于测试）
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

## 验证安装

安装完成后，运行以下命令验证：

```powershell
python --version
pip list
```

如果看到 Python 版本和已安装的包列表，说明安装成功！

## 下一步

安装完依赖后，按照 `SETUP.md` 中的说明配置 Supabase 并运行服务：

```powershell
python app.py
```


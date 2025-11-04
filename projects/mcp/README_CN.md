# SmartResume MCP 服务器

使用 fastmcp 实现的 SmartResume 简历解析服务的 MCP 服务器。

## 安装

```bash
pip install -r requirements.txt
```

## 启动服务

```bash
python -m smartresume_mcp.server
```

或指定端口：
```bash
python -m smartresume_mcp.server --port 8080
```

## 可用工具

1. **analyze_resume** - 分析简历文件并提取结构化信息
   - `file_path`: 简历文件路径
   - `resume_id`: 可选的简历ID
   - `extract_types`: 要提取的信息类型

2. **extract_text_from_file** - 从文件中提取文本内容
   - `file_path`: 文件路径

3. **extract_info_from_text** - 从文本中提取结构化信息
   - `text_content`: 文本内容
   - `extract_types`: 要提取的信息类型
   - `resume_id`: 可选的简历ID

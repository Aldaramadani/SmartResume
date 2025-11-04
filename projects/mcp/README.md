# SmartResume MCP Server

MCP server for SmartResume resume parsing service using fastmcp.

## Installation

```bash
pip install -r requirements.txt
```

## Start Server

```bash
python -m smartresume_mcp.server
```

Or specify port:
```bash
python -m smartresume_mcp.server --port 8080
```

## Available Tools

1. **analyze_resume** - Analyze resume file and extract structured information
   - `file_path`: Resume file path
   - `resume_id`: Optional resume ID
   - `extract_types`: Types of information to extract

2. **extract_text_from_file** - Extract text content from file
   - `file_path`: File path

3. **extract_info_from_text** - Extract structured information from text
   - `text_content`: Text content
   - `extract_types`: Types of information to extract
   - `resume_id`: Optional resume ID

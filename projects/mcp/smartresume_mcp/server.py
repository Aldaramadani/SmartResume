import os
import sys
import uuid
from pathlib import Path
from typing import List, Optional

import fastmcp

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

try:
    from smartresume import create_analyzer
except ImportError as e:
    print(f"Error importing smartresume: {e}")
    sys.exit(1)

analyzer = None

def get_analyzer():
    global analyzer
    if analyzer is None:
        analyzer = create_analyzer(init_ocr=True, init_llm=True)
    return analyzer

server = fastmcp.FastMCP("SmartResume MCP Server")


@server.tool()
async def analyze_resume(file_path: str, resume_id: Optional[str] = None, extract_types: Optional[List[str]] = None):
    try:
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}", "success": False}
        
        if resume_id is None:
            resume_id = str(uuid.uuid4())
        
        if extract_types is None:
            extract_types = ["basic_info"]
        
        analyzer_instance = get_analyzer()
        result = analyzer_instance.pipeline(cv_path=file_path, resume_id=resume_id, extract_types=extract_types)
        
        return {"success": True, "resume_id": resume_id, "result": result}
        
    except Exception as e:
        return {"error": str(e), "success": False}


@server.tool()
async def extract_text_from_file(file_path: str):
    try:
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}", "success": False}
        
        analyzer_instance = get_analyzer()
        result = analyzer_instance.process_file(file_path)
        
        return {"success": True, "result": result}
        
    except Exception as e:
        return {"error": str(e), "success": False}


@server.tool()
async def extract_info_from_text(text_content: str, extract_types: List[str], resume_id: Optional[str] = None):
    try:
        if resume_id is None:
            resume_id = str(uuid.uuid4())
        
        analyzer_instance = get_analyzer()
        result = analyzer_instance.extract_info_only(text_content=text_content, extract_types=extract_types, resume_id=resume_id)
        
        return {"success": True, "resume_id": resume_id, "result": result}
        
    except Exception as e:
        return {"error": str(e), "success": False}


def main():
    import argparse
    parser = argparse.ArgumentParser(description="SmartResume MCP Server")
    parser.add_argument("--host", default="localhost", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    args = parser.parse_args()
    
    print(f"Starting SmartResume MCP Server at http://{args.host}:{args.port}")
    server.run(host=args.host, port=args.port)

if __name__ == "__main__":
    main()

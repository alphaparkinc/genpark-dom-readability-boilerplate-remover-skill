import sys
import json
from client import ReadabilityBoilerplateRemover

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-dom-readability-boilerplate-remover-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "extract_substantive_content",
                        "description": "Strip boilerplate header, footer, ads and extract main article paragraphs",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "html": {"type": "string"}
                            },
                            "required": ["html"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        args = params.get("arguments", {})
        h = args.get("html", "")
        res = ReadabilityBoilerplateRemover.extract_main_content(h)
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": res}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()

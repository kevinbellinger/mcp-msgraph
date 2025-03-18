from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict
import requests

app = FastAPI()

CLIENT_ID = "insert client id here"
CLIENT_SECRET = "insert client secret here"
TENANT_ID = "insert tenant id here"
SCOPE = "https://graph.microsoft.com/.default"

class MCPRequest(BaseModel):
    action: str
    contextId: str
    data: Dict[str, Any]

def get_access_token() -> str:
    token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": SCOPE,
        "grant_type": "client_credentials"
    }
    resp = requests.post(token_url, data=data)
    resp.raise_for_status()
    token_data = resp.json()
    return token_data["access_token"]

@app.post("/mcp")
def mcp_endpoint(request: MCPRequest):
    action = request.action
    context_id = request.contextId
    data = request.data

    if action == "readUserProfile":
        user_id = data.get("userId")
        token = get_access_token()

        graph_url = f"https://graph.microsoft.com/beta/users/{user_id}/profile"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        resp = requests.get(graph_url, headers=headers)
        if resp.status_code == 200:
            return {
                "status": "success",
                "action": action,
                "contextId": context_id,
                "data": resp.json()
            }
        else:
            return {
                "status": "error",
                "action": action,
                "contextId": context_id,
                "errorCode": resp.status_code,
                "errorMessage": resp.text
            }

    return {
        "status": "error",
        "action": action,
        "contextId": context_id,
        "errorMessage": "Unsupported or unknown action"
    }

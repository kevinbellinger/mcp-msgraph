from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")
SCOPE = os.getenv("SCOPE", "https://graph.microsoft.com/.default")

class MCPRequest(BaseModel):
    action: str
    contextId: str
    data: Dict[str, Any]

def get_access_token() -> str:
    """Retrieve a bearer token using the client credentials flow."""
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

    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # ------------------------------------
    # Read the user’s profile
    # ------------------------------------
    if action == "readUserProfile":
        user_id = data.get("userId")
        graph_url = f"https://graph.microsoft.com/beta/users/{user_id}/profile"
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

    # ------------------------------------
    # Read the user's profile skills
    # ------------------------------------
    elif action == "readUserProfileSkills":
        user_id = data.get("userId")
        graph_url = f"https://graph.microsoft.com/beta/users/{user_id}/profile/skills"
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

    # ------------------------------------
    # Add a new skill to the user’s profile
    # ------------------------------------
    elif action == "addUserProfileSkill":
        user_id = data.get("userId")
        skill_body = data.get("skill", {})
        graph_url = f"https://graph.microsoft.com/beta/users/{user_id}/profile/skills"
        resp = requests.post(graph_url, headers=headers, json=skill_body)
        if 200 <= resp.status_code < 300:
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

    # ------------------------------------
    # Update an existing skill
    # ------------------------------------
    elif action == "updateUserProfileSkill":
        user_id = data.get("userId")
        skill_id = data.get("skillId")
        update_body = data.get("skill", {})
        graph_url = f"https://graph.microsoft.com/beta/users/{user_id}/profile/skills/{skill_id}"
        resp = requests.patch(graph_url, headers=headers, json=update_body)
        if 200 <= resp.status_code < 300:

            return {
                "status": "success",
                "action": action,
                "contextId": context_id,
                "data": "Skill updated successfully."
            }
        else:
            return {
                "status": "error",
                "action": action,
                "contextId": context_id,
                "errorCode": resp.status_code,
                "errorMessage": resp.text
            }

    # ------------------------------------
    # Read the user's profile interests
    # ------------------------------------
    elif action == "readUserProfileInterests":
        user_id = data.get("userId")
        graph_url = f"https://graph.microsoft.com/beta/users/{user_id}/profile/interests"
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

    # ------------------------------------
    # Add a new interest
    # ------------------------------------
    elif action == "addUserProfileInterest":
        user_id = data.get("userId")
        interest_body = data.get("interest", {})
        graph_url = f"https://graph.microsoft.com/beta/users/{user_id}/profile/interests"
        resp = requests.post(graph_url, headers=headers, json=interest_body)
        if 200 <= resp.status_code < 300:
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

    # ------------------------------------
    # Update an existing interest
    # ------------------------------------
    elif action == "updateUserProfileInterest":
        user_id = data.get("userId")
        interest_id = data.get("interestId")
        update_body = data.get("interest", {})
        graph_url = f"https://graph.microsoft.com/beta/users/{user_id}/profile/interests/{interest_id}"
        resp = requests.patch(graph_url, headers=headers, json=update_body)
        if 200 <= resp.status_code < 300:
            return {
                "status": "success",
                "action": action,
                "contextId": context_id,
                "data": "Interest updated successfully."
            }
        else:
            return {
                "status": "error",
                "action": action,
                "contextId": context_id,
                "errorCode": resp.status_code,
                "errorMessage": resp.text
            }

    # ------------------------------------
    # Default fallback if action not recognized
    # ------------------------------------
    return {
        "status": "error",
        "action": action,
        "contextId": context_id,
        "errorMessage": "Unsupported or unknown action"
    }

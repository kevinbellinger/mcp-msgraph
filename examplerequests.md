# MCP Graph Actions – Example `curl` Commands

Below are **example requests** for each supported action in your MCP server. Each request is a `POST` to the `/mcp` endpoint, with `Content-Type: application/json`. Update the JSON as needed (e.g., with your user’s actual UPN or the ID of the skill/interest you want to modify).

---

## Read Full User Profile

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "action": "readUserProfile",
        "contextId": "12345",
        "data": {
          "userId": "someUser@yourtenant.onmicrosoft.com"
        }
      }'

```

## Read Skills in a User Profile

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "action": "readUserProfileSkills",
        "contextId": "abc123",
        "data": {
          "userId": "someUser@yourtenant.onmicrosoft.com"
        }
      }'
```

## Add Skills to a User Profile

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "action": "addUserProfileSkill",
        "contextId": "abc123",
        "data": {
          "userId": "someUser@yourtenant.onmicrosoft.com",
          "skill": {
            "displayName": "Python",
            "proficiency": "expert",
          }
        }
      }'
```

## Update Skills in a User Profile

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "action": "updateUserProfileSkill",
        "contextId": "abc123",
        "data": {
          "userId": "someUser@yourtenant.onmicrosoft.com",
          "skillId": "YOUR_SKILL_ID_HERE",
          "skill": {
            "proficiency": "intermediate",
          }
        }
      }'

```

## Read Interests in a User Profile

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "action": "readUserProfileInterests",
        "contextId": "abc123",
        "data": {
          "userId": "someUser@yourtenant.onmicrosoft.com"
        }
      }'
```

## Update existing interests in a User Profile

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "action": "updateUserProfileInterest",
        "contextId": "abc123",
        "data": {
          "userId": "someUser@yourtenant.onmicrosoft.com",
          "interestId": "YOUR_INTEREST_ID_HERE",
          "interest": {
            "displayName": "Advanced ML"
          }
        }
      }'
```
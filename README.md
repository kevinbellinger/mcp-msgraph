# MCP-MSGraph

A prototype **MCP (Model Context Protocol)** server that reads a user profile from **Microsoft Graph**.  
This project demonstrates how to connect MCP to data stored in Microsoft Graph as a proof of concept.

---

## Create an Azure AD Application

1. Log into [Azure Portal](https://portal.azure.com).
2. Navigate to **Azure Active Directory** > **App registrations** > **New registration**.
3. Create a new application.
4. Note the generated **Application (client) ID** and **Client Secret**.
5. Under **API permissions**, add **User.Read.All** (as delegated or application permission as appropriate) and grant admin consent.

---

## Instructions to run the server: 

1. **Clone** the repository or setup your own folder and files structure.

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install fastapi uvicorn requests requests-oauthlib pydantic
```

4. Open 'main.py' and replace the placeholder values with your App ID, Tenant ID, and Client Secret.

5. Start the server

```bash
uvicorn main:app --reload
```
Your server will be available at http://127.0.0.1:8000.

---
## Example Request

Use curl (or any REST client) to send a request to retrieve a user’s profile:

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "action":"readUserProfile",
        "contextId":"abc123",
        "data": {"userId":"someUser@yourtenant.onmicrosoft.com"}
      }'
```

Result should look something like: 

```json
{"status":"success","action":"readUserProfile","contextId":"abc123","data":{"@odata.context":"https://graph.microsoft.com/beta/$metadata#users('adelev%40M365x17584779.onmicrosoft.com')/profile/$entity","id":"profileId","account@odata.context":"https://graph.microsoft.com/beta/$metadata#users('adelev%40M365x17584779.onmicrosoft.com')/profile/account","account":[{"ageGroup":"","countryCode":"","userPrincipalName":"AdeleV@M365x17584779.OnMicrosoft.com","allowedAudiences":"organization","createdDateTime":"2025-01-30T11:06:01.7661211Z","lastModifiedDateTime":"2025-01-30T11:06:01.9431431Z","id":"c74cb3af-2f62-43fa-9709-5d2cfc4b4042","isSearchable":false,"inference":null,"preferredLanguageTag":{"locale":null,"displayName":null},"createdBy":{"user":null,"device":null,"application":{"displayName":"AAD","id":null}},"lastModifiedBy":{"user":null,"device":null,"application":{"displayName":"MsGraph","id":null}},"source":{"type":["AAD","MsGraph"]},"sources":[{"sourceId":"4ce763dd-9214-4eff-af7c-da491cc3782d","isDefaultSource":true},{"sourceId":"0024a795-114d-4031-95c7-5fb543e00e80","properties":["isSipEnabled"]}]},{"ageGroup":"","countryCode":"","userPrincipalName":"","allowedAudiences":"federatedOrganizations","createdDateTime":"2025-01-30T11:06:01.7661213Z","lastModifiedDateTime":"2025-01-30T11:06:01.9431431Z","id":"750f8cc2-2f72-4b38-88c6-531dfc5ed47f","isSearchable":false,"inference":null,"preferredLanguageTag":{"locale":null,"displayName":null},"createdBy":{"user":null,"device":null,"application":{"displayName":"AAD","id":null}},"lastModifiedBy":{"user":null,"device":null,"application":{"displayName":"MsGraph","id":null}},"source":{"type":["AAD","MsGraph"]},"sources":[{"sourceId":"4ce763dd-9214-4eff-af7c-da491cc3782d","isDefaultSource":true},{"sourceId":"0024a795-114d-4031-95c7-5fb543e00e80","properties":["isSipEnabled"]}]}]}}%  
```
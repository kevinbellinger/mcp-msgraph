# mcp-msgraph
A prototype MCP server which reads a user profile from Microsoft Graph. 

This is a basic proof of concept to test the Model Context Protocol and enable it to connect to data stored in Microsoft Graph.

Basic Instructions to create an app:

1. Login to portal.azure.com with an admin account.
2. Create a new app registraction and note the app-id and secret.
3. Add User.Read.All and Admin consent it in the scopes. 


Basic instructions to run the server: 

1. Clone
2. Create a virtual environment:

python3 -m venv venv
source venv/bin/activate


3. Install the required packages:

pip install fastapi uvicorn requests requests-oauthlib pydantic

4. Add your app-id, tenant-id, and client secret in the applicable places in main.py

4. Run the server

uvicorn main:app --reload

5. Send a client request:

curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "action":"readUserProfile",
        "contextId":"abc123",
        "data": {"userId":"someUser@yourtenant.onmicrosoft.com"}
      }'

Result should look something like: 

{"status":"success","action":"readUserProfile","contextId":"abc123","data":{"@odata.context":"https://graph.microsoft.com/beta/$metadata#users('adelev%40M365x17584779.onmicrosoft.com')/profile/$entity","id":"profileId","account@odata.context":"https://graph.microsoft.com/beta/$metadata#users('adelev%40M365x17584779.onmicrosoft.com')/profile/account","account":[{"ageGroup":"","countryCode":"","userPrincipalName":"AdeleV@M365x17584779.OnMicrosoft.com","allowedAudiences":"organization","createdDateTime":"2025-01-30T11:06:01.7661211Z","lastModifiedDateTime":"2025-01-30T11:06:01.9431431Z","id":"c74cb3af-2f62-43fa-9709-5d2cfc4b4042","isSearchable":false,"inference":null,"preferredLanguageTag":{"locale":null,"displayName":null},"createdBy":{"user":null,"device":null,"application":{"displayName":"AAD","id":null}},"lastModifiedBy":{"user":null,"device":null,"application":{"displayName":"MsGraph","id":null}},"source":{"type":["AAD","MsGraph"]},"sources":[{"sourceId":"4ce763dd-9214-4eff-af7c-da491cc3782d","isDefaultSource":true},{"sourceId":"0024a795-114d-4031-95c7-5fb543e00e80","properties":["isSipEnabled"]}]},{"ageGroup":"","countryCode":"","userPrincipalName":"","allowedAudiences":"federatedOrganizations","createdDateTime":"2025-01-30T11:06:01.7661213Z","lastModifiedDateTime":"2025-01-30T11:06:01.9431431Z","id":"750f8cc2-2f72-4b38-88c6-531dfc5ed47f","isSearchable":false,"inference":null,"preferredLanguageTag":{"locale":null,"displayName":null},"createdBy":{"user":null,"device":null,"application":{"displayName":"AAD","id":null}},"lastModifiedBy":{"user":null,"device":null,"application":{"displayName":"MsGraph","id":null}},"source":{"type":["AAD","MsGraph"]},"sources":[{"sourceId":"4ce763dd-9214-4eff-af7c-da491cc3782d","isDefaultSource":true},{"sourceId":"0024a795-114d-4031-95c7-5fb543e00e80","properties":["isSipEnabled"]}]}]}}%  
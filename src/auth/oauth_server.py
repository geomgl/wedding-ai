# auth/oauth_server.py
from flask import Flask, request, redirect
from google_auth_oauthlib.flow import Flow
import os

app = Flask(__name__)

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/spreadsheets"
]

REDIRECT_URI = os.getenv("OAUTH_REDIRECT_URI")

@app.route("/authorize")
def authorize():
    flow = Flow.from_client_secrets_file(
        "auth/data/credentials.json",
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    auth_url, _ = flow.authorization_url(prompt="consent", access_type="offline", include_granted_scopes="true")
    return redirect(auth_url)

@app.route("/oauth2callback")
def oauth2callback():
    flow = Flow.from_client_secrets_file(
        "auth/data/credentials.json",
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    flow.fetch_token(code=request.args.get("code"))
    creds = flow.credentials

    with open("auth/data/token.json", "w") as token_file:
        token_file.write(creds.to_json())

    return "✅ Authorization complete! You may close this window."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
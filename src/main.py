# Entry point for the AI Wedding Venue Automation Agent
# Orchestrates the main workflow and module execution
import os
import logging
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

logging.basicConfig(level=logging.INFO)

def check_gmail_auth():
    creds_path = os.getenv("GOOGLE_TOKEN_PATH", "data/token.json")
    if not os.path.exists(creds_path):
        logging.error("❌ No token.json file found. Run auth flow first.")
        return

    creds = Credentials.from_authorized_user_file(creds_path)
    service = build("gmail", "v1", credentials=creds)
    profile = service.users().getProfile(userId="me").execute()
    logging.info("✅ Gmail OAuth worked. Logged in as: %s", profile.get("emailAddress"))

if __name__ == "__main__":
    check_gmail_auth()

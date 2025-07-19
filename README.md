# 💍 AI Wedding Venue Automation Agent

An autonomous agent that manages and organizes wedding venue communications. It fetches and processes Gmail threads and attachments, extracts structured venue data using LLMs, populates a Google Sheet, and automates follow-up messages via Gmail or wedding platforms like The Knot and WeddingWire.

---

## 🧠 What It Does

- Connects to your Gmail to process **new and past venue-related emails**
- Extracts venue data from:
  - Email text
  - PDFs, DOCX, and scanned documents (OCR)
- Classifies messages as:
  - Direct email
  - Platform notification (e.g., The Knot)
- Opens browser session to fetch full message threads from The Knot
- Extracts structured info (price, capacity, services, etc.)
- Updates a Google Sheet for easy venue comparison
- Sends follow-up emails or messages via platform UI
- Supports Pydantic validation and retry logic

---

## 📦 Folder Structure

```bash
ai_wedding_agent/
├── main.py
├── config.py
├── gmail/
│   ├── fetch_emails.py
│   └── send_email.py
├── llm/
│   ├── classify_email.py
│   ├── extract_venue_info.py
│   ├── identify_missing_info.py
│   └── generate_follow_up.py
├── sheets/
│   └── update_sheet.py
├── automation/
│   ├── message_bot.py
│   ├── knot_bot.py
│   └── weddingwire_bot.py
├── auth/
│   └── oauth_server.py
├── utils/
│   └── logger.py
├── data/
│   ├── credentials.json        # OAuth client secret (DO NOT COMMIT)
│   └── token.json              # Generated after login
├── .env
├── requirements.txt
└── README.md
```

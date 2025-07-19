# 🛠️ AI Wedding Venue Automation Agent – Technical Task List

This list includes all core and refined tasks to build the system using **Python**, **LangChain**, **Gmail API**, **Google Sheets**, and **Playwright**. Tasks are grouped by module.

---

## 🔑 Initial Setup & Authentication

- [ ] Configure OAuth2 for Gmail
- [ ] Set up Google Service Account for Sheets access
- [ ] Use `.env` for secure credential handling
- [ ] Playwright login automation for The Knot / WeddingWire (with support for storing session cookies if needed)

## 📁 Project Setup

- [ ] Create project structure:

  ```
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
  ├── utils/
  │   └── logger.py
  ├── data/
  │   └── credentials.json
  ├── .env
  ├── requirements.txt
  └── README.md
  ```

- [ ] Define `.env` variables:

  - `GOOGLE_CREDENTIALS_JSON`
  - `OPENAI_API_KEY`
  - `KNOT_USERNAME`, `KNOT_PASSWORD`
  - `WW_USERNAME`, `WW_PASSWORD`

- [ ] `requirements.txt` dependencies:
  ```text
  langchain
  openai
  google-api-python-client
  google-auth
  gspread
  pandas
  playwright
  pypdf
  python-docx
  dotenv
  pytesseract
  python-magic
  ```

---

## 📥 Gmail Email Ingestion

- [ ] `fetch_emails.py`:

  - Authenticate using OAuth2.
  - Fetch unread + labeled emails.
  - Fetch attachments (PDF, DOCX).
  - Return subject, sender, body, attachment paths, labels, and full raw content.

- [ ] Label processed emails as `wedding-processed`.

---

## 🧠 LangChain Email Processing

### 1. Email Classification

- [ ] `classify_email.py`:

  - Use LLM to classify email:
    - `"direct"` or `"platform_notification"`
  - If `"platform_notification"`, extract:
    - `platform` (e.g. The Knot, WeddingWire)
    - `venue_name`
    - `message_url`

- [ ] Use prompt like:
  ```
  You are an AI assistant helping to classify wedding-related emails. Given the raw email body below, determine:
  ```

1. Is the email a direct message from a venue or a notification from a wedding planning platform?
2. If it's a notification, extract:
   - The name of the platform (e.g., The Knot, WeddingWire)
   - The name of the venue (if mentioned)
   - A URL from the email body that opens the message thread on the platform. For emails for The Knot notifications, this url can be parsed from the reply button
     in the email

Respond only in the following strict JSON format:
{
"type": "direct" | "platform_notification",
"platform": "The Knot" | "WeddingWire" | null,
"venue": "string or null",
"url": "string or null"
}

````

---

### 2. 📬 Platform Thread Inspection & Attachment Parsing

#### a. Thread Reader (Playwright)

- [ ] Extend `knot_bot.py`:
  - Log into The Knot
  - Navigate to provided message thread URL
  - Scroll/load the entire conversation
  - Extract all visible message text

- [ ] Handle conversation structure:
  - Capture sender/recipient names if available
  - Flatten all message bubbles into a single block of plain text

- [ ] Detect and download attachments:
  - Locate attachment icons/buttons
  - Download any PDFs, DOCXs
  - Save to `/tmp/attachments/{venue_id}/`

#### b. File Parsing + OCR (if needed)

- [ ] For each downloaded file:
  - If PDF: use `PyPDF2` or `pdfplumber` to extract text
  - If image-scanned: run OCR with `pytesseract`
  - If DOCX: use `python-docx`
  - Aggregate all content into one string

#### c. LangChain Thread + Attachment Analyzer

### 🧠 LangChain Agent: Venue Info Extractor

- [ ] Create a LangChain agent:
  - Input:
    ```python
    {
      "conversation_text": str,
      "attachment_texts": List[str]
    }
    ```
  - Combine all inputs into a single context window
  - Prompt the LLM to extract structured venue information into the following fields:

    ```text
    Venue Name
    Location
    Venue Link (The Knot or WeddingWire)
    Contact Email
    Status
    Availability (Aug 2026 / Apr 2027)
    Capacity
    Estimate Provided
    Cost Breakdown (for 125 guests)
    In-House Services
    Vendor Policy
    Included Amenities
    Alcohol Policy
    Rental Timeframe
    Notes
    Follow-up Date
    ```

- [ ] Field-specific logic:
  - **Estimate Provided**:
    - If the message includes a total cost estimate explicitly (e.g., “$15,000 for 125 guests”), extract that into this field.
    - If no estimate is given, return `null`.

  - **Cost Breakdown**:
    - If breakdown details are present (e.g., $100/head, $2,000 rental fee, etc.), calculate and return a breakdown **for 125 guests**.
    - Otherwise, return `null`.

- [ ] Return results in a JSON object validated by a Pydantic schema (see below).

#### d. Sheet Sync

- [ ] Connect to the existing Google Sheet using the Sheets API.
  - Sheet will already contain pre-defined column headers:
    - Venue Name
    - Location
    - Venue Link
    - Contact Email
    - Status
    - Availability (Aug 2026 / Apr 2027)
    - Capacity
    - Estimate Provided
    - Cost Breakdown
    - In-House Services
    - Vendor Policy
    - Included Amenities
    - Alcohol Policy
    - Rental Timeframe
    - Notes
    - Follow-up Date

- [ ] Locate row by unique Venue Name (or Venue Link if available).
  - If row exists:
    - Update fields only if new non-null data is available.
    - Do not overwrite existing values with null.
  - If row does not exist:
    - Append new row with extracted venue info.

- [ ] Field Normalization:
  - Format dates as `YYYY-MM-DD`
  - Flatten Cost Breakdown into a readable string (e.g., "Rental: $2000, Catering: $125/head")

- [ ] Follow-up logic:
  - If any of the following fields are null or incomplete:
    - `Availability`, `Estimate Provided`, `Cost Breakdown`, `Vendor Policy`, `Alcohol Policy`
  - Then:
    - Add a row comment or mark in `Notes` indicating missing fields
    - Generate a follow-up message with those field names included

- [ ] Set `Status` column using logic:
  - `"Waiting for response"` → follow-up already sent, awaiting reply
  - `"Needs follow-up"` → follow-up not yet sent, but required
  - `"Complete"` → all required fields filled, no further action


#### e. Error Handling & Logging

- [ ] Log:
  - Which fields were inferred from messages vs attachments
  - Which files were parsed
  - Which messages triggered follow-ups
  - Screenshots of message UI + attachment list

- [ ] Add retry logic for timeouts / element not found

#### f. Testing

- [ ] Test cases:
  - Message threads with:
    - Only conversation text
    - Only attachments
    - Mixed formats
  - Attachments with scanned vs text-based PDFs

---

### 3. Missing Info Identification

- [ ] `identify_missing_info.py`:
- Compare extracted info to required field list.
- Return list of missing fields.

---

### 4. Follow-up Message Generation

- [ ] `generate_follow_up.py`:
- Prompt to generate follow-up for missing fields:
````

Write a message to {venue_name} asking for: {missing_fields}.
Tone: professional and friendly.
Platform: {platform}

```


## 📤 Sending Follow-Ups

### 1. Direct Email Follow-Ups

- [ ] `send_email.py`:
- Send Gmail messages to venue contacts with follow-up text.
- Log subject, timestamp, message body.

### 2. Platform UI Message Dispatch

- [ ] `message_bot.py`:
- Router: Based on platform, dispatch to appropriate bot.
- Accepts `platform`, `venue`, `url`, `message`.

#### a. The Knot Automation

- [ ] `knot_bot.py`:
- Login using credentials.
- Navigate to message URL.
- Detect message input.
- Paste and send follow-up.
- Screenshot confirmation.
- Handle captcha, retries, 2FA.

#### b. WeddingWire Automation

- [ ] `weddingwire_bot.py`:
- Same steps as Knot bot with DOM selectors adjusted.

---

## 📁 Attachment Parsing & OCR

- [ ] Detect if PDF is scanned image:

- If so, run OCR using `pytesseract`.

- [ ] Parse text from:
- PDFs
- DOCX
- Save extracted text for LLM input.

---

## 🔔 Notifications

- [ ] Send user alert if:

- Missing info detected
- Follow-up sent

- [ ] Notification channels:
- Email summary
- Slack webhook
- (Optional) SMS via Twilio

---

## 🧪 Testing & Simulation

- [ ] Create test inbox with:

- Direct venue emails
- Platform notifications
- Empty attachments
- Multi-threaded conversations

- [ ] Validate:
- Classification accuracy
- Field extraction
- Sheet population
- Follow-up delivery

---

## 🚀 Deployment & Ops

- [ ] Dockerize the project:

- `Dockerfile`
- `docker-compose.yml`

- [ ] Add CLI flags to:

- Run once (`--once`)
- Run continuously (`--watch`)
- Dry run (`--dry-run`)

- [ ] Schedule with:

- Cron (local)
- Or deploy to server/cloud VM

- [ ] Secrets:
- Store `.env` locally
- (Optional) Use Google Secret Manager or AWS Secrets Manager

---

## 📈 Logging & Monitoring

- [ ] Log each run:

- Emails processed
- Venue info extracted
- Follow-ups sent
- Platform automation outcomes
- Failures/retries

- [ ] Log format: JSON or structured plain text.
```

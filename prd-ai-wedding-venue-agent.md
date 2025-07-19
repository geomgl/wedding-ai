# AI Wedding Venue Automation Agent PRD

## Introduction/Overview

This document describes an AI automation agent designed to help a user manage and shortlist wedding venues by parsing and organizing venue-related email communications. The agent will extract relevant information from emails and attachments, store it in a Google Sheet, flag missing details, and automate follow-up communications when necessary. The goal is to reduce the manual effort required to track, compare, and communicate with multiple venues during the wedding planning process.

## Goals

- Automatically parse venue-related emails (including retroactive and new emails) from Gmail.
- Extract and organize venue information and attachments into a Google Sheet
- Identify missing information and flag it for follow-up.
- Automate follow-up communications via email or wedding planning platforms (The Knot, Wedding Wire) to request missing details.
- Enable the user to see all venue details in an organized table for easy comparison and shortlisting.

## User Stories

- As someone who is recently engaged and finding a wedding venue I want to be able to see venue details in an organized table for venues that have already sent me information and inquire details about venues that have not sent me all of the information that I need.

## Functional Requirements

1. The agent must connect to the user's Gmail account and process both new and existing emails.
2. The agent must identify and process only venue-related emails.
3. The agent must extract relevant venue information from email bodies and attachments (e.g., brochures, PDFs).
4. The agent must store extracted venue data in a Google sheet database (the Google Sheet does not already exist).
5. The agent must flag missing or incomplete information for each venue.
6. The agent must automate follow-up communications:
   - For missing info via email (Gmail)
   - For missing info via wedding planning platforms (The Knot, Wedding Wire) by authenticating and interacting with their web UIs
7. The agent must support browser automation for sending messages through The Knot and Wedding Wire.
8. The agent must not process non-venue-related emails.

## Non-Goals (Out of Scope)

- The agent will not process communications related to other wedding planning vendors (e.g., caterers, photographers).
- The agent will not send follow-up emails or messages without user review (unless explicitly enabled in the future).
- The agent will not delete or modify emails in the user's inbox.
- The agent will create a Google Sheet database

## Design Considerations (Optional)

- The Google Sheet should be structured to allow easy comparison of venues (e.g., columns for name, location, price, capacity, available dates, contact info, etc.).
- The agent should provide a simple notification mechanism (e.g., text) when missing info is flagged or follow-up is sent.
- UI/dashboard is optional; initial version can be fully automated with notifications.

## Technical Considerations (Optional)

- Integration with Gmail API for email access and sending.
- Integration with Google Sheets API for data storage.
- Use of an LLM (e.g., OpenAI/ChatGPT) for parsing unstructured email content and attachments.
- Browser automation (e.g., Puppeteer, Playwright) for interacting with The Knot and Wedding Wire web UIs.
- Secure handling of authentication credentials for Gmail, and wedding planning platforms.

## Success Metrics

- 100% of venue-related emails are processed and relevant information is extracted and stored in Google Sheet.
- All missing information is flagged and follow-up communications are generated for 100% of incomplete venue entries.
- User can view and compare all venue details in a single Google Sheet table.
- Reduction in manual effort and time spent tracking venue communications.

## Open Questions

- What is the full list of data fields to extract for each venue (e.g., name, location, price, capacity, available dates, contact info, amenities, etc.)?
- Should the agent support user review/approval before sending follow-up communications, or should it be fully automated?
- Are there any privacy or security requirements for handling sensitive information in emails or attachments?

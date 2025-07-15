# AI Wedding Venue Automation Agent PRD

## Introduction/Overview

This document describes an AI automation agent designed to help a user manage and shortlist wedding venues by parsing and organizing venue-related email communications. The agent will extract relevant information from emails and attachments, store it in a Notion database, flag missing details, and automate follow-up communications when necessary. The goal is to reduce the manual effort required to track, compare, and communicate with multiple venues during the wedding planning process.

## Goals

- Automatically parse venue-related emails (including retroactive and new emails) from Gmail.
- Extract and organize venue information and attachments into a Notion database.
- Identify missing information and flag it for follow-up.
- Automate follow-up communications via email or wedding planning platforms (The Knot, Wedding Wire) to request missing details, with human-in-the-loop approval.
- Enable the user to see all venue details in an organized table for easy comparison and shortlisting.
- Ensure every venue communication is tracked as a row in the Notion database, with concise, digestible details and relevant attachments.
- Distinguish between domestic and international venues, and track additional information for destination venues.
- Provide a daily summary email of all venues processed that day, with a concise, helpful summary in the tone of a wedding planner.

## User Stories

- As someone who is recently engaged and finding a wedding venue I want to be able to see venue details in an organized table for venues that have already sent me information and inquire details about venues that have not sent me all of the information that I need.
- As a user, I want to preview and approve any follow-up messages before they are sent, so I remain in control of communications.
- As a user, I want to see relevant attachments (e.g., brochures) stored alongside venue details in Notion.
- As a user considering destination weddings, I want to see room block rates and nightly rates per person for international venues.
- As a user, I want to receive a daily summary email with a concise, helpful overview of all venues processed that day.

## Functional Requirements

1. The agent must connect to the user's Gmail account and process both new and existing emails.
2. The agent must identify and process only venue-related emails.
3. The agent must extract relevant venue information from email bodies and attachments (e.g., brochures, PDFs).
4. The agent must store extracted venue data in a Notion database (using an existing database).
5. The agent must guarantee that every parsed venue-related email results in a row in the Notion database, even if some details are missing.
6. The agent must ensure all details are short and concise for readability within the Notion table.
7. The agent must extract and track the following information for each venue (all fields should be columns in the Notion table):
   - **Venue Name**
   - **Location**
   - **Venue Link** (main landing page on The Knot or Wedding Wire, as found in the Messenger UI or conversation interface)
   - **Contact Email**
   - **Status** (should use standard values/consts/enums for easy searching, e.g., `NEW`, `IN_PROGRESS`, `AWAITING_REPLY`, `SHORTLISTED`, `REJECTED`, `BOOKED`)
   - **Availability** (Aug 2026 / Apr 2027)
   - **Capacity**
   - **Price Range**
   - **In-House Services**
   - **Vendor Policy**
   - **Included Amenities**
   - **Alcohol Policy**
   - **Rental Timeframe**
   - **Nearby Accommodations** (e.g., hotels, room blocks)
   - **Venue Location** (domestic or international)
     - For international/destination venues:
       - **Room block rates** and/or **nightly rates per person**
   - **Notes**
   - **Follow-up Date**
   - **Relevant Attachments** (e.g., brochures, linked to the row)
8. The agent must store any relevant attachments (e.g., brochures) in the Notion table, linked to the corresponding venue row.
9. The agent must flag missing or incomplete information for each venue.
10. The agent must automate follow-up communications, but only after human-in-the-loop approval:

    - When missing info is detected, the agent must send a text message to the user, previewing the follow-up message and requesting approval.
    - Only after receiving user approval, the agent sends the follow-up via email (Gmail) or via wedding planning platforms (The Knot, Wedding Wire) by authenticating and interacting with their web UIs.
    - The follow-up message should use the following template, omitting any items already collected:

      ***

      Hi,

      My partner and I are beginning our search for a wedding venue and are very interested in learning more about your space. We’re planning for **100–125 guests**, and are currently looking at **August 2026 or April 2027** as our wedding timeframe.

      Could you please share the following information?

      - **Availability** in August 2026 or April 2027
      - **Capacity** for a guest count of 100–125
      - **Pricing** details and any food & beverage minimums
      - **In-house services** you provide (e.g. catering, bar, rentals, coordination, etc.)
      - **Vendor policy**: Are we required to use specific vendors (e.g. caterers, DJs), or can we bring in our own? (We’re hoping to bring our own DJ.)
      - **Included amenities** (e.g. tables, chairs, linens, lighting, A/V, etc.)
      - **Alcohol policy**: Do you offer bar services or allow BYO alcohol?
      - **Rental timeframe** and any noise curfews
      - **Nearby accommodations** (e.g., hotels, room blocks)
      - For international venues: **Room block rates** and/or **nightly rates per person**

      If your venue sounds like a good fit, we’d love to explore next steps such as a brochure or scheduling a tour.

      Thanks so much,

      ## George + Adriana

      ***

11. The agent must send a daily end-of-day (EOD) summary email with the subject line `Wedding Planning Summary [DATE]`, where `[DATE]` is the current date. The summary must:
    - Include only venues for which information was processed that day.
    - Be concise but not omit important details.
    - Use a tone similar to a helpful wedding planner, providing all the information the user should know without information overload.
12. The agent must support browser automation for sending messages through The Knot and Wedding Wire.
13. The agent must not process non-venue-related emails.

## Non-Goals (Out of Scope)

- The agent will not process communications related to other wedding planning vendors (e.g., caterers, photographers).
- The agent will not send follow-up emails or messages without user review (unless explicitly enabled in the future).
- The agent will not delete or modify emails in the user's inbox.
- The agent will not create a new Notion database (will use an existing one).

## Design Considerations (Optional)

- The Notion database should be structured to allow easy comparison of venues (e.g., columns for name, location, price, capacity, available dates, contact info, etc.).
- The agent should provide a simple notification mechanism (e.g., email or Notion comment) when missing info is flagged or follow-up is sent.
- UI/dashboard is optional; initial version can be fully automated with notifications.

## Technical Considerations (Optional)

- Integration with Gmail API for email access and sending.
- Integration with Notion API for data storage.
- Use of an LLM (e.g., OpenAI/ChatGPT) for parsing unstructured email content and attachments.
- Browser automation (e.g., Puppeteer, Playwright) for interacting with The Knot and Wedding Wire web UIs.
- Secure handling of authentication credentials for Gmail, Notion, and wedding planning platforms.
- Integration with SMS/text messaging service (e.g., Twilio) for human-in-the-loop approval.

## Success Metrics

- 100% of venue-related emails are processed and relevant information is extracted and stored in Notion.
- All missing information is flagged and follow-up communications are generated for 100% of incomplete venue entries, with user approval.
- User can view and compare all venue details in a single Notion table, including attachments and special fields for destination venues.
- User receives a daily summary email with a helpful, concise overview of all venues processed that day.
- Reduction in manual effort and time spent tracking venue communications.

## Open Questions

- Should the agent support user review/approval before sending follow-up communications, or should it be fully automated? (Default: human-in-the-loop)
- Are there any privacy or security requirements for handling sensitive information in emails or attachments?
- Should the agent support exporting the Notion table to other formats (e.g., CSV, Google Sheets)?

## Relevant Files

- `src/agents/weddingVenueAgent.ts` - Main automation agent logic for parsing emails, extracting data, and orchestrating workflows.
- `src/agents/weddingVenueAgent.test.ts` - Unit tests for the main agent logic.
- `src/integrations/gmail.ts` - Handles Gmail API integration for reading and sending emails.
- `src/integrations/gmail.test.ts` - Unit tests for Gmail integration.
- `src/integrations/notion.ts` - Handles Notion API integration for storing and updating venue data.
- `src/integrations/notion.test.ts` - Unit tests for Notion integration.
- `src/integrations/sms.ts` - Handles SMS/text messaging for human-in-the-loop approval.
- `src/integrations/sms.test.ts` - Unit tests for SMS integration.
- `src/integrations/weddingPlatforms.ts` - Integrates with The Knot and Wedding Wire for browser automation and message sending.
- `src/integrations/weddingPlatforms.test.ts` - Unit tests for wedding platform integration.
- `src/utils/emailParser.ts` - Utility for parsing and extracting structured data from emails and attachments.
- `src/utils/emailParser.test.ts` - Unit tests for email parsing utility.
- `src/utils/summaryEmail.ts` - Generates and sends daily summary emails.
- `src/utils/summaryEmail.test.ts` - Unit tests for summary email utility.
- `src/types/venue.ts` - Type definitions and enums for venue data and status fields.

### Notes

- Unit tests should be placed alongside the code files they are testing (e.g., `weddingVenueAgent.test.ts` in the same directory as `weddingVenueAgent.ts`).
- Use `npx jest [optional/path/to/test/file]` to run tests. Running without a path executes all tests found by the Jest configuration.

## Tasks

- [ ] 1.0 Set up project structure and type definitions

  - [ ] 1.1 Initialize project repository and directory structure
  - [ ] 1.2 Create `src/types/venue.ts` with all required type definitions and enums (including status values)
  - [ ] 1.3 Set up basic configuration files (e.g., tsconfig, .env.example)
  - [ ] 1.4 Add initial README with project overview and setup instructions

- [ ] 2.0 Implement Gmail integration for reading and sending emails

  - [ ] 2.1 Set up Gmail API credentials and authentication
  - [ ] 2.2 Implement logic to fetch new and historical emails
  - [ ] 2.3 Filter and identify venue-related emails
  - [ ] 2.4 Implement email sending functionality (for follow-ups and daily summaries)
  - [ ] 2.5 Write unit tests for Gmail integration

- [ ] 3.0 Implement Notion integration for storing and updating venue data

  - [ ] 3.1 Set up Notion API credentials and authentication
  - [ ] 3.2 Implement logic to create and update rows in the existing Notion database
  - [ ] 3.3 Map extracted data fields to Notion columns (including attachments)
  - [ ] 3.4 Implement logic to link attachments (e.g., brochures) to the correct row
  - [ ] 3.5 Write unit tests for Notion integration

- [ ] 4.0 Implement email and attachment parsing logic

  - [ ] 4.1 Develop utility to parse email bodies for required venue fields
  - [ ] 4.2 Implement attachment extraction and parsing (e.g., PDFs, images)
  - [ ] 4.3 Extract venue main page links from The Knot/Wedding Wire Messenger UI
  - [ ] 4.4 Normalize and validate extracted data (including enums/consts for status)
  - [ ] 4.5 Write unit tests for parsing utilities

- [ ] 5.0 Implement human-in-the-loop approval workflow via SMS

  - [ ] 5.1 Set up SMS provider (e.g., Twilio) credentials and integration
  - [ ] 5.2 Implement logic to notify user via SMS when follow-up is needed
  - [ ] 5.3 Include preview of follow-up message in SMS
  - [ ] 5.4 Implement approval/response handling to proceed with or cancel follow-up
  - [ ] 5.5 Write unit tests for SMS workflow

- [ ] 6.0 Implement browser automation for The Knot and Wedding Wire messaging

  - [ ] 6.1 Set up browser automation framework (e.g., Puppeteer or Playwright)
  - [ ] 6.2 Implement login/authentication for The Knot and Wedding Wire
  - [ ] 6.3 Automate navigation to Messenger UI and extraction of venue links
  - [ ] 6.4 Automate sending of follow-up messages via web UI
  - [ ] 6.5 Write unit tests for browser automation

- [ ] 7.0 Implement daily summary email generation and delivery

  - [ ] 7.1 Implement logic to track venues processed each day
  - [ ] 7.2 Generate concise, helpful summary in the tone of a wedding planner
  - [ ] 7.3 Format summary email with subject line `Wedding Planning Summary [DATE]`
  - [ ] 7.4 Send summary email at EOD
  - [ ] 7.5 Write unit tests for summary email logic

- [ ] 8.0 Orchestrate agent workflow and error handling
  - [ ] 8.1 Integrate all modules into main agent workflow
  - [ ] 8.2 Implement error handling and logging for all integrations
  - [ ] 8.3 Add configuration for environment variables and secrets
  - [ ] 8.4 Write integration tests for end-to-end workflow

# PBI-1: Henry Ward B2B AI Engineering Website

[View in Backlog](../backlog.md#product-backlog)

## Overview

Create a professional single-page marketing website on GitHub Pages for Henry Ward that positions AI engineering services for general B2B clients.

## Problem Statement

The repository did not yet provide a business-facing website that explains AI service offerings and business outcomes clearly. Potential clients need a clear path from understanding capabilities to booking a conversation.

## User Stories

- As a business stakeholder, I want to quickly understand AI services and outcomes so I can assess fit.
- As a potential client, I want to see practical benefits tied to each service so I can estimate business value.
- As a lead, I want to book a strategy call directly from the website.

## Technical Approach

- Use Jekyll and GitHub Pages with the Minimal Mistakes remote theme.
- Build a single-page splash layout in `index.md`.
- Define service cards and benefit cards with feature rows.
- Add custom styling in `assets/css/main.scss` for a clean corporate look.
- Embed a placeholder Calendly iframe for CTA.

## UX/UI Considerations

- Corporate and professional visual style.
- Clear sectioning: services, products, benefits, about, and booking.
- Mobile-friendly layout and readable card spacing.
- Action-oriented hero section with direct booking CTA.

## Acceptance Criteria

1. Website is a single-page design using Jekyll.
2. Five popular AI engineering services are listed with business outcomes.
3. Popular AI product patterns are shown to make offerings concrete.
4. Embedded Calendly call booking uses a placeholder URL.
5. Styling is responsive and suitable for desktop and mobile.

## Dependencies

- GitHub Pages build pipeline.
- Minimal Mistakes remote theme.
- Calendly public booking URL placeholder.

## Open Questions

- Final Calendly URL to replace placeholder.
- Final brand assets and bio details.

## Related Tasks

- [1-1 Build single-page Jekyll marketing website](./1-1.md)

# Giving

Add-on module for donations, Gift Aid, pledges and reports. Landing: 562. Getting started: 455.

## Core objects

- **Givers**: profile pages with donations, pledges, declarations. Can be linked to an Address Book contact (required for My Giving). Import givers from other systems including Gift Aid declarations and linked spouse splits (article 292). Import never auto links to contacts, so run the **Potential Contacts** report afterwards.
- **Funds**: unlimited funds (General, Building, Missions). Funds can be flagged Gift Aid-able.
- **Donations**: add singly or in batches. Payment types include cash, cheque, standing order and custom donation methods.
- **Batches**: each import creates a Batch.
- **Pledges**: manual pledges (standing orders, planned giving) and subscription pledges created by online recurring giving, visually marked "DD" or "Card".
- **Flows**: givers can be put through flows.

## Importing donations (article 51)

From Donations, Import donations, Import file. Accepts CSV or OFX bank statements, or your own CSV with a header row (acceptable headings listed on the Import Donations page). Only credit transactions are imported. ChurchSuite learns each giver's bank reference and auto matches future imports. Delete non donation lines such as interest before importing.

## Online giving: Donate (article 114)

- Embeddable or Connect based form for one off and recurring gifts, processed by **Stripe** (cards) and **GoCardless** (direct debit). Stripe set up: Integrating Stripe for online card donations. Reconcile with **Viewing Stripe transfers**.
- Confirmation emails include a Manage Giving link for recurring donors. Stripe fees apply when a giver increases a donation.
- Donate adds Gift Aid declarations per selected fund only (no "All funds" declarations) and cannot backdate declarations by 4 years.
- Tap to Donate (contactless on iPhone or Android) was in beta in late 2024.

## Gift Aid (UK only)

- Declarations (article 118): per giver, per fund or all funds. Can cover a single donation, enduring, or past donations (backdated up to 4 years, set the declaration start date to when Gift Aid can be claimed). Add in ChurchSuite or in My Giving if "Enable declaration management" is on. Active and Deleted declarations reports, plus **Declarations Missing** report (active givers without a current declaration, filter by fund or tag).
- Reclaiming Gift Aid: build the claim in ChurchSuite and submit direct to HMRC online or download for manual submission. Corrected declarations change historic donations to Unclaimed so they are claimable next claim.
- Gift Aid small donations scheme (GASDS) for eligible cash and contactless gifts.
- Overclaims and refunds have their own article.
- Elim churches: central claims via the Elim International Office (case study 649).
- ExpensePlus can also claim Gift Aid. Most churches using both claim through ChurchSuite.

## Statements and reports

Email givers a statement for a period (Producing giving statements). Reports section includes declarations reports, Potential Contacts, and donation summaries. Smart tags treat a couple giver as both contacts.

## My Giving (My ChurchSuite)

Members view history, make donations, manage pledges and (UK) Gift Aid declarations. Activate in Giving module, My ChurchSuite Options (article 61). Admin guide: 674 (member view).

## Notes

- Giving is subject to data protection: restrict access using module permissions and User Groups. Gift Aid declarations must be kept for 6 years under HMRC rules.
- Transactions from LoveGiving and similar need reconciling before they appear as claimable elsewhere. This is specific to ExpensePlus workflows, not ChurchSuite.

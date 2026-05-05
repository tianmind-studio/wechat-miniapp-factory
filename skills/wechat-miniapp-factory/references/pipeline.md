# Factory Pipeline Details

## Intake Defaults

If the user provides only an idea, infer:

- target users
- 3 to 5 core features
- minimum data model
- three pages: home, main workflow, profile/admin/status
- likely service category, with uncertainty marked
- CloudBase-ready backend unless the user says local only

Write assumptions into `docs/product-brief.md` so the next agent can adjust them.

## Generated Project Checklist

- `project.config.json` with placeholder AppID unless the user provides one.
- `app.json` with all pages declared.
- `sitemap.json`.
- at least three page folders with `.json`, `.wxml`, `.wxss`, and `.js`.
- `utils/` for seed data and reusable logic.
- `cloudfunctions/` when CloudBase is selected.
- `docs/product-brief.md`, `docs/submission-checklist.md`, `docs/review-notes.md`.
- `tests/validate-miniapp.js` and `package.json` with `npm test`.

## Validation Checklist

- Parse every JSON file.
- Ensure every `app.json` page has matching page files.
- Ensure no obvious placeholder strings remain in first-screen copy.
- Ensure `project.config.json` exists.
- Ensure CloudBase functions have `package.json` and `index.js` when generated.
- Run any project-specific tests.

## Reviewer Gate

After implementation, use `wechat-miniapp-reviewer` and include:

- verdict
- top risks
- exact fix plan
- reviewer path
- suggested submission note

If the reviewer returns `NO-GO`, fix P0 issues before calling the task done unless the user asked only for a diagnostic pass.

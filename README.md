# WeChat MiniApp Factory

Generate a native WeChat Mini Program from an idea, then run a reviewer-style pre-submission check before upload.

This repo packages two Codex / Claude-compatible skills:

- `wechat-miniapp-factory`: the orchestrator that turns an idea into a runnable Mini Program project.
- `wechat-miniapp-reviewer`: a strict pre-submission reviewer for service category, privacy, content safety, virtual payment, and common rejection risks.

It is designed for builders who want more than a one-off AI code dump: project files, CloudBase-ready structure, validation, reviewer notes, and a safer path toward submission.

## Why This Exists

AI can write Mini Program code quickly. The hard part is making the output useful:

- pages declared correctly
- realistic demo content
- CloudBase-ready backend structure
- no frontend secrets
- reviewer-friendly navigation
- submission checklist and review notes
- a preflight pass against common WeChat rejection patterns

This project turns that into a repeatable workflow.

## Quick Start

Install the skills into Codex:

```bash
./scripts/install.sh
```

Generate a starter Mini Program:

```bash
python3 skills/wechat-miniapp-factory/scripts/scaffold_native_miniapp.py \
  ./demo-miniapp \
  --name "Campus Helper" \
  --description "A small WeChat Mini Program for campus services" \
  --cloudbase
```

Validate the generated project:

```bash
cd demo-miniapp
npm test
```

Then ask Codex:

```text
Use $wechat-miniapp-factory to turn this idea into a review-ready WeChat Mini Program.
```

Or in Chinese:

```text
用小程序工厂做一个校园服务小程序，生成项目后让小程序审核员做提审前检查。
```

## What Gets Generated

The scaffold creates:

- `project.config.json`
- `app.json`
- `sitemap.json`
- three native pages: home, workflow, review readiness
- shared WXSS styling
- local seed data
- optional CloudBase `cloudfunctions/`
- `docs/product-brief.md`
- `docs/submission-checklist.md`
- `docs/review-notes.md`
- `tests/validate-miniapp.js`

The generated project is intentionally simple. The skill then guides Codex to customize the real workflow, data model, copy, CloudBase functions, and review notes.

## Review Gate

`wechat-miniapp-reviewer` checks for common risks:

- service category mismatch
- placeholder or incomplete content
- forced login before clear value
- missing privacy/permission explanation
- UGC without content safety handling
-诱导分享,诱导关注,诱导下载
- virtual payment and external payment routing risk
- reviewer path hidden behind confusing UI
- attempts to bypass or deceive platform review

The skill does not guarantee approval. It reduces avoidable rejection risk.

## Repository Layout

```text
skills/
  wechat-miniapp-factory/
    SKILL.md
    scripts/scaffold_native_miniapp.py
    references/
  wechat-miniapp-reviewer/
    SKILL.md
    references/official-links.md
scripts/
  install.sh
  validate.sh
```

## Validate This Repo

```bash
./scripts/validate.sh
```

If Codex's `quick_validate.py` is available, the script uses it. Otherwise it checks that each skill folder has a `SKILL.md`.

## Public-Safe Scope

This repo intentionally includes only the Mini Program factory/reviewer workflow. It does not include private deployment runbooks, credentials, client context, or personal business workflows.

## Links

- Author / Studio: [Tianmind Studio](https://github.com/tianmind-studio)
- Website: [tianmind.com](https://tianmind.com)
- Related public skills: [expert-review-panel](https://github.com/tianmind-studio/expert-review-panel), [english-coach](https://github.com/tianmind-studio/english-coach)

## License

MIT

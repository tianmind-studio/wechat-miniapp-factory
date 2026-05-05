---
name: wechat-miniapp-factory
description: Orchestrate one-click WeChat Mini Program creation from an idea to a runnable, review-prepared project. Use when the user asks for 一键生成小程序, 小程序工厂, 微信小程序工厂, 自动生成小程序, 从想法做小程序, 小程序脚手架, CloudBase 小程序, 小程序提审材料, or wants Codex to generate a WeChat Mini Program end-to-end and then run a pre-submission review with wechat-miniapp-reviewer.
---

# Wechat Miniapp Factory

## Overview

Build a real WeChat Mini Program project, not a chat-only plan. This skill is the orchestrator: choose an implementation path, generate the project, validate it, then call the sibling `wechat-miniapp-reviewer` skill as the submission gate.

Default to native WeChat Mini Program plus CloudBase-ready structure for custom thesis/demo/business prototypes. Use another path only when the user's constraints clearly fit better.

## One-Click Pipeline

1. Clarify only the blockers. If the user asks for one-click generation and gives a vague idea, make reasonable assumptions and write them into `docs/product-brief.md`.
2. Run a short build-vs-buy scan unless the user clearly wants practice, a private/custom prototype, thesis work, or code ownership. See `references/ecosystem.md`.
3. Choose the architecture:
   - `native-cloudbase`: default for real custom WeChat Mini Programs.
   - `native-local-demo`: fastest offline prototype with local seed data.
   - `uni-app`: when the user explicitly wants cross-platform output.
   - `weda-low-code`: when the user mainly needs an internal CRUD/admin workflow and accepts low-code lock-in.
4. Create the project. For a native baseline, run `scripts/scaffold_native_miniapp.py` first, then customize pages, data, cloud functions, copy, and docs.
5. Make it useful: implement the core workflow, at least three real pages, realistic demo data, empty/error/loading states, and a reviewer-friendly path through the app.
6. Add CloudBase where relevant: `cloudfunctions/`, seed data docs, cloud/local fallback notes, and no secrets in the Mini Program frontend.
7. Validate locally: parse JSON, check declared routes, run `npm test` or the generated validator, and inspect obvious WXML/WXSS/JS mistakes.
8. Use `wechat-miniapp-reviewer` before final delivery. If that skill is installed at `${CODEX_HOME:-$HOME/.codex}/skills/wechat-miniapp-reviewer`, read it and apply its verdict format.
9. Produce handoff artifacts: generated project path, validation results, `docs/submission-checklist.md`, `docs/review-notes.md`, and remaining risks.

## Build Standards

- Do not leave placeholder-only pages. Every first-run screen needs plausible content or a clear empty state.
- Keep login optional until a feature truly needs identity.
- Avoid hidden reviewer-only flows, fake data switching, or any attempt to bypass platform review.
- Do not include AppSecret or private keys in Mini Program code.
- Prefer concise native WXML/WXSS/JS unless the existing repo already uses a framework.
- For thesis/demo projects, include visible system layers: user profile, data model, recommendation/business logic, persistence plan, and evaluation/demo notes.

## Quick Scaffold

Use the bundled scaffold only as the first draft:

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/wechat-miniapp-factory/scripts/scaffold_native_miniapp.py \
  /path/to/output \
  --name "My Mini Program" \
  --description "Short product description" \
  --cloudbase
```

Then immediately adapt the generated pages and docs to the user's actual idea.

## Output Contract

End with:

- `Project`: absolute path to the generated Mini Program.
- `Architecture`: chosen path and why.
- `Validation`: commands run and result.
- `Review Gate`: `PASS`, `CONDITIONAL GO`, or `NO-GO` from the reviewer pass.
- `Next Manual Step`: only unavoidable platform actions such as opening WeChat DevTools, filling a real AppID, or uploading credentials.

Never claim guaranteed approval. Say the workflow reduces review risk.

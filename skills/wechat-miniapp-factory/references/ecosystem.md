# Mini Program Ecosystem Choices

Use this as the quick routing map before building.

## Existing Options

- Tencent CloudBase and WeDa: good for low-code, CRUD-heavy, internal tools, and teams that accept platform conventions.
- CloudBase Mini Program skills and AI model integration skills: useful for adding cloud functions, storage, database, and AI streaming.
- Community Mini Program development skills: useful for native syntax, DevTools diagnosis, performance, and compatibility.
- `wechat-miniapp-reviewer`: local sibling skill for pre-submission review, rejection diagnosis, service category checks, privacy, content safety, and virtual payment risks.

## When To Build Custom

Build a custom native Mini Program when the user needs:

- thesis/demo credibility with inspectable source code
- a custom workflow or algorithm
- ownership of project files
- CloudBase functions plus local fallback
- reviewer-ready materials, not only a visual low-code app

## Default Stack

- Native WeChat Mini Program: WXML, WXSS, JS, JSON.
- CloudBase-ready backend: `cloudfunctions/`, seed data docs, and frontend fallback data.
- Validation: generated JSON/route checker plus project-specific tests.
- Review gate: run `wechat-miniapp-reviewer` after implementation.

## Trigger Phrases Worth Preserving

Keep these phrases in generated docs and skill descriptions when relevant:

- 一键生成小程序
- 小程序工厂
- 小程序审核员
- 提审前检查
- 小程序过审
- CloudBase 小程序

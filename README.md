# WeChat MiniApp Factory / 微信小程序工厂

从一句想法生成原生微信小程序项目，再用“小程序审核员”做提审前预审。  
Generate a native WeChat Mini Program from an idea, then run a reviewer-style pre-submission check before upload.

这个项目打包了两个 Codex / Claude 兼容的 skills：

This repo packages two Codex / Claude-compatible skills:

- `wechat-miniapp-factory`: 小程序生成总控，负责从需求到项目骨架、CloudBase-ready 结构、校验和交付文档。  
  The orchestrator that turns an idea into a runnable Mini Program project with validation and handoff docs.
- `wechat-miniapp-reviewer`: 小程序审核员，负责服务类目、隐私、内容安全、虚拟支付和常见驳回风险的提审前检查。  
  A strict pre-submission reviewer for service category, privacy, content safety, virtual payment, and common rejection risks.

它适合想快速做微信小程序原型、课程/毕设 demo、客户方案验证，或者把 Codex / Claude skills 用在真实交付里的开发者。  
It is useful for Mini Program prototypes, student projects, client demos, and agentic coding workflows that need real project files instead of a one-off AI code dump.

## 为什么做这个 / Why This Exists

AI 写几页小程序代码不难，难的是让结果能继续推进：页面要声明正确，内容不能是空壳，CloudBase 结构要能接上，审核路径要清楚，提审材料也要有人整理。

AI can write Mini Program code quickly. The harder part is turning that output into something you can continue from: valid page declarations, realistic demo content, CloudBase-ready structure, reviewer-friendly navigation, and submission notes.

这个项目把这些步骤整理成一个可重复的 workflow：

This project turns those steps into a repeatable workflow:

- 生成原生微信小程序项目 / scaffold a native WeChat Mini Program
- 补 CloudBase-ready 后端结构 / add CloudBase-ready backend structure
- 生成真实可替换的 demo 内容 / create replaceable demo content
- 跑本地 JSON 和路由校验 / validate JSON and declared routes
- 输出产品说明、提审清单和审核备注 / write product brief, submission checklist, and review notes
- 用审核员 skill 做提审前风险检查 / run a reviewer-style preflight check

## 快速开始 / Quick Start

安装 skills 到 Codex：

Install the skills into Codex:

```bash
./scripts/install.sh
```

生成一个小程序 starter：

Generate a starter Mini Program:

```bash
python3 skills/wechat-miniapp-factory/scripts/scaffold_native_miniapp.py \
  ./demo-miniapp \
  --name "Campus Helper" \
  --description "A small WeChat Mini Program for campus services" \
  --cloudbase
```

校验生成结果：

Validate the generated project:

```bash
cd demo-miniapp
npm test
```

然后让 Codex 继续定制：

Then ask Codex to customize it:

```text
用小程序工厂做一个校园服务小程序，生成项目后让小程序审核员做提审前检查。
```

```text
Use $wechat-miniapp-factory to turn this idea into a review-ready WeChat Mini Program.
```

## 生成内容 / What Gets Generated

脚手架会生成：

The scaffold creates:

- `project.config.json`
- `app.json`
- `sitemap.json`
- 三个原生页面：home、workflow、review readiness  
  three native pages: home, workflow, review readiness
- 全局 WXSS 样式 / shared WXSS styling
- 本地 seed data / local seed data
- 可选 CloudBase `cloudfunctions/` / optional CloudBase `cloudfunctions/`
- `docs/product-brief.md`
- `docs/submission-checklist.md`
- `docs/review-notes.md`
- `tests/validate-miniapp.js`

生成项目保持简单，方便继续改成真实业务。`wechat-miniapp-factory` 会引导 Codex 补产品逻辑、数据模型、页面文案、云函数和审核材料。

The generated project stays simple on purpose, so it can be adapted to a real product. `wechat-miniapp-factory` guides Codex to add business logic, data models, page copy, cloud functions, and review notes.

## 审核员预审 / Review Gate

`wechat-miniapp-reviewer` 会检查常见提审风险：

`wechat-miniapp-reviewer` checks common submission risks:

- 服务类目和实际功能不一致 / service category mismatch
- 占位内容、空页面、功能不完整 / placeholder or incomplete content
- 登录过早或登录理由不清楚 / forced login before clear value
- 隐私政策或权限说明缺失 / missing privacy or permission explanation
- UGC 没有内容安全处理 / UGC without content safety handling
- 诱导分享、诱导关注、诱导下载 / induced sharing, following, or app download
- 虚拟支付和外部支付跳转风险 / virtual payment and external payment routing risk
- 审核路径不清楚 / reviewer path hidden behind confusing UI
- 绕开、规避或欺骗平台审核的设计 / attempts to bypass or deceive platform review

它不能保证过审，但能减少很多本来可以提前发现的驳回风险。  
It does not guarantee approval, but it reduces avoidable rejection risk.

## 目录结构 / Repository Layout

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

## 校验仓库 / Validate This Repo

```bash
./scripts/validate.sh
```

如果 Codex 自带的 `quick_validate.py` 存在，脚本会调用它；否则只检查每个 skill 是否有 `SKILL.md`。

If Codex's `quick_validate.py` is available, the script uses it. Otherwise it checks that each skill folder has a `SKILL.md`.

## 公开范围 / Public-Safe Scope

这个仓库只包含小程序工厂和审核员 workflow，不包含私人部署手册、账号线索、客户上下文、密钥或个人业务流程。

This repo only includes the Mini Program factory/reviewer workflow. It does not include private deployment runbooks, account details, client context, credentials, or personal business workflows.

## 链接 / Links

- 作者 / Studio: [Tianmind Studio](https://github.com/tianmind-studio)
- 官网 / Website: [tianmind.com](https://tianmind.com)
- 相关 skills / Related skills: [expert-review-panel](https://github.com/tianmind-studio/expert-review-panel), [english-coach](https://github.com/tianmind-studio/english-coach)

## License

MIT

# 脚手架使用指南 / Scaffold Guide

本文介绍如何使用 `scaffold_native_miniapp.py` 生成微信小程序项目骨架，以及生成后如何进一步定制。

This guide explains how to use `scaffold_native_miniapp.py` to generate a WeChat Mini Program project skeleton and how to customize it afterward.

## 前置条件 / Prerequisites

- Python 3.7+
- 微信开发者工具 (WeChat DevTools)：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

## 快速生成 / Quick Start

```bash
# 基础用法：生成一个本地 demo 小程序
python3 skills/wechat-miniapp-factory/scripts/scaffold_native_miniapp.py \
  ./my-miniapp \
  --name "我的小程序" \
  --description "一句话描述你的小程序功能"

# 带 CloudBase 云函数目录
python3 skills/wechat-miniapp-factory/scripts/scaffold_native_miniapp.py \
  ./my-miniapp \
  --name "我的小程序" \
  --description "一句话描述你的小程序功能" \
  --cloudbase

# 指定真实 AppID（需要在微信公众平台注册）
python3 skills/wechat-miniapp-factory/scripts/scaffold_native_miniapp.py \
  ./my-miniapp \
  --name "我的小程序" \
  --description "一句话描述你的小程序功能" \
  --appid "wx1234567890abcdef" \
  --cloudbase
```

## 命令行参数 / CLI Options

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `output` | 输出目录路径（必填） | — |
| `--name` | 小程序名称 | "Mini Program Starter" |
| `--description` | 小程序简介 | "A generated WeChat Mini Program starter." |
| `--appid` | 小程序 AppID | "touristappid"（游客模式） |
| `--cloudbase` | 生成 CloudBase 云函数目录 | 不生成 |
| `--force` | 允许写入非空目录 | 禁止 |

## 生成的目录结构 / Generated Structure

```
my-miniapp/
├── app.js                   # 小程序入口
├── app.json                 # 全局配置
├── app.wxss                 # 全局样式
├── project.config.json      # 项目配置
├── sitemap.json             # 索引配置
├── package.json             # npm 配置
├── pages/
│   ├── home/                # 首页
│   │   ├── index.json
│   │   ├── index.wxml
│   │   ├── index.wxss
│   │   └── index.js
│   ├── catalog/             # 工作流页
│   │   └── ...
│   └── profile/             # 审核就绪页
│       └── ...
├── utils/
│   └── seed.js              # 本地 mock 数据
├── cloudfunctions/          # （仅 --cloudbase）
│   └── ping/
│       ├── index.js
│       └── package.json
├── docs/
│   ├── product-brief.md     # 产品说明
│   ├── submission-checklist.md  # 提审清单
│   └── review-notes.md      # 审核备注
└── tests/
    └── validate-miniapp.js  # 校验脚本
```

## 校验项目 / Validate the Project

```bash
cd my-miniapp
npm test
```

校验脚本会检查：
- 所有 JSON 文件是否可解析
- `app.json` 中声明的页面是否都有对应文件
- 至少声明了 3 个页面

## 下一步定制 / Next Steps

1. **替换 demo 内容**：修改 `utils/seed.js` 中的数据，以及各页面的文案
2. **添加业务页面**：在 `pages/` 下新建目录，同时更新 `app.json` 的 pages 数组
3. **配置真实 AppID**：在 `project.config.json` 中替换 `appid` 字段
4. **接入 CloudBase**：
   - 在微信开发者工具中开通云开发
   - 修改 `cloudfunctions/` 下的云函数
   - 前端调用 `wx.cloud.callFunction()`
5. **运行审核员预审**：完成开发后，使用 `wechat-miniapp-reviewer` skill 做提审前检查

## 架构选型说明 / Architecture Choices

脚手架默认生成原生微信小程序（WXML + WXSS + JS + JSON），原因：

- **审核友好**：原生代码结构清晰，审核员易于理解
- **灵活可控**：没有框架依赖，便于按需修改
- **CloudBase-ready**：可直接对接微信云开发
- **体积最小**：无额外 runtime 开销

如果需要跨端或 TypeScript，可以考虑 uni-app 或 Taro，但需要自行配置构建流程。

## 常见问题 / FAQ

### Q: touristappid 是什么？
A: 游客模式 AppID，可以在微信开发者工具中预览和调试，但无法真机扫码、上传或发布。开发阶段足够用，正式上线前需要替换为在微信公众平台注册的真实 AppID。

### Q: 生成的项目能直接提审吗？
A: 不能。生成的是脚手架，内容是占位的 demo 数据。你需要：
1. 替换为真实业务内容
2. 确认服务类目和资质
3. 准备隐私政策
4. 运行 `wechat-miniapp-reviewer` 预审

### Q: CloudBase 云函数怎么部署？
A: 在微信开发者工具中右键点击 `cloudfunctions/ping` 目录，选择"上传并部署"。首次需要在工具中开通云开发环境。

## 相关文档 / Related Docs

- [构建与预览指南](./devtools-build-preview.md)
- [常见踩坑](./common-pitfalls.md)
- [示例：骰盅组局小程序](../examples/dice-party/README.md)

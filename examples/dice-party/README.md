# 骰盅组局 / Dice Party

一个用于聚会游戏的微信小程序示例：出题 → 摇骰 → 结果展示。

A WeChat Mini Program example for party games: pick a topic → roll dice → show result.

## 功能概述 / Features

- **题目页**：选择或随机生成一道"谁最可能..."或"真心话/大冒险"题目
- **摇骰页**：动画摇骰，决定谁来执行
- **结果页**：展示结果，支持重来或换题

这是一个纯 mock 示例，所有数据都是本地硬编码。适合学习小程序开发、理解页面跳转、感受提审前该准备什么。

## 目录结构 / Structure

```
dice-party/
├── app.js
├── app.json
├── app.wxss
├── project.config.json
├── sitemap.json
├── package.json
├── pages/
│   ├── topic/           # 题目选择页
│   ├── roll/            # 摇骰页
│   └── result/          # 结果展示页
├── utils/
│   └── mock-data.js     # mock 题库和玩家
├── docs/
│   ├── product-brief.md
│   ├── submission-checklist.md
│   └── review-notes.md
└── tests/
    └── validate-miniapp.js
```

## 如何运行 / How to Run

1. 打开微信开发者工具
2. 导入项目，选择 `examples/dice-party` 目录
3. 使用游客 AppID 或填入你自己的 AppID
4. 点击"编译"即可预览

详细步骤见 [构建与预览指南](../../docs/devtools-build-preview.md)

## 本地校验 / Validation

```bash
cd examples/dice-party
npm test
```

## 声明 / Disclaimer

- 这是**示例骨架**，不是上架产品
- 所有题目都是 mock 数据，无真实运营内容
- 不包含任何真实 AppID 或密钥
- 提审前需替换内容、确认服务类目、准备隐私政策

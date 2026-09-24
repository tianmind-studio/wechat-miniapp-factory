# 构建与预览指南 / Build & Preview Guide

本文介绍如何在微信开发者工具中导入、构建和预览小程序项目。

## 前置准备 / Prerequisites

### 1. 下载微信开发者工具

官方下载地址：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

支持 Windows、macOS、Linux。

### 2. 注册微信小程序账号（可选）

如果只是本地预览，可以使用"游客模式"（touristappid）。

如果需要真机预览、上传或发布，需要在微信公众平台注册小程序账号：
https://mp.weixin.qq.com/

## 导入项目 / Import Project

1. 打开微信开发者工具
2. 点击"加号"创建新项目
3. 选择项目目录（例如 `examples/dice-party`）
4. AppID 选择：
   - **游客模式**：选择"使用测试号"，可本地预览但无法真机扫码
   - **正式 AppID**：填入在微信公众平台注册的 AppID
5. 后端服务选择"不使用云服务"（除非项目需要 CloudBase）
6. 点击"确定"导入

## 本地编译与预览 / Local Build & Preview

### 编译

导入项目后，开发者工具会自动编译。如需手动重新编译：
- 点击工具栏的"编译"按钮
- 或使用快捷键 Ctrl+B (Windows) / Cmd+B (macOS)

### 模拟器预览

编译成功后，左侧模拟器会自动显示小程序界面。可以：
- 点击模拟器中的按钮进行交互
- 在顶部切换不同机型（iPhone、Android 等）
- 在顶部切换网络状态（WiFi、4G、离线）

### 调试

- **Console**：查看 `console.log` 输出和错误信息
- **Network**：查看网络请求（API 调用、图片加载等）
- **AppData**：实时查看和修改页面数据
- **Wxml**：检查页面结构，类似浏览器的 Elements 面板
- **Sources**：查看源代码，支持断点调试

## 真机预览 / Device Preview

### 前提条件

- 需要正式 AppID（不能是游客模式）
- 手机和电脑在同一网络，或手机有网络连接

### 预览步骤

1. 点击工具栏的"预览"按钮
2. 选择"扫描二维码预览"
3. 使用微信扫描生成的二维码
4. 在手机上体验小程序

### 自动预览

开发者工具支持自动推送到手机：
1. 点击"预览"旁边的下拉箭头
2. 选择"自动预览"
3. 每次编译后自动推送到已绑定的手机

## 上传代码 / Upload

### 前提条件

- 需要正式 AppID
- 需要在微信公众平台绑定开发者账号

### 上传步骤

1. 点击工具栏的"上传"按钮
2. 填写版本号（如 1.0.0）
3. 填写项目备注
4. 点击"上传"

上传后代码进入"开发版本"，需要在微信公众平台提交审核。

## 项目配置 / Project Settings

### project.config.json

```json
{
  "appid": "你的AppID或touristappid",
  "compileType": "miniprogram",
  "libVersion": "latest",
  "projectname": "项目名称",
  "setting": {
    "urlCheck": false,
    "es6": true,
    "enhance": true,
    "postcss": true,
    "minified": true
  }
}
```

关键配置说明：

| 字段 | 说明 |
|------|------|
| `appid` | 小程序 AppID，游客模式填 `touristappid` |
| `libVersion` | 基础库版本，建议 `latest` 或指定版本号 |
| `setting.urlCheck` | 是否校验域名，开发阶段建议 `false` |
| `setting.es6` | 是否将 ES6 转 ES5 |
| `setting.minified` | 是否压缩代码 |

### app.json

```json
{
  "pages": [
    "pages/topic/index",
    "pages/roll/index",
    "pages/result/index"
  ],
  "window": {
    "navigationBarTitleText": "小程序名称",
    "navigationBarBackgroundColor": "#6366F1",
    "navigationBarTextStyle": "white"
  }
}
```

**注意**：`pages` 数组中的第一个页面是小程序的启动页面。

## 常见问题 / Troubleshooting

### Q: 导入项目后一片空白？

检查 `app.json` 中 `pages` 数组声明的页面是否都有对应的文件夹和文件。

### Q: 真机预览显示"网络请求失败"？

1. 检查是否在 `project.config.json` 中设置了 `urlCheck: false`
2. 正式环境需要在微信公众平台配置服务器域名

### Q: 编译报错 "xxx is not defined"？

检查 JS 文件中是否正确引入了依赖：
```javascript
const { xxx } = require('../../utils/xxx');
```

### Q: 样式不生效？

1. 检查 WXSS 文件是否和 WXML 文件同名
2. 检查选择器是否正确
3. 使用 rpx 单位而不是 px

### Q: 游客模式有什么限制？

- 无法真机预览
- 无法上传代码
- 无法使用部分 API（如支付、订阅消息）
- 足够用于本地开发和学习

## 相关文档 / Related Docs

- [脚手架使用指南](./scaffold-guide.md)
- [常见踩坑](./common-pitfalls.md)
- [示例：骰盅组局小程序](../examples/dice-party/README.md)
- [微信官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/)

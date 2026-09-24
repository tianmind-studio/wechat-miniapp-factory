# 常见踩坑 / Common Pitfalls

微信小程序从开发到上架过程中的常见问题和避坑指南。

## 一、备案相关 / ICP Filing

### 什么是小程序备案？

2023 年 9 月起，微信小程序需要完成备案才能上架。这是独立于网站 ICP 备案的小程序专属备案流程。

官方指南：https://developers.weixin.qq.com/miniprogram/product/record/guidelines

### 备案流程

1. 在微信公众平台完成小程序注册
2. 进入"设置" → "基本设置" → "小程序备案"
3. 填写主体信息、负责人信息、小程序信息
4. 上传相关证件（身份证、营业执照等）
5. 等待管局审核（通常 1-20 个工作日）

### 常见问题

#### Q: 个人主体可以备案吗？
A: 可以。个人和企业都可以备案，但个人主体可选的服务类目较少，且部分类目要求企业资质。

#### Q: 备案需要多长时间？
A: 微信初审通常 1-2 天，管局终审 3-20 个工作日，各省份时间不同。

#### Q: 备案号和网站 ICP 备案号一样吗？
A: 不一样。小程序备案号格式类似 `京ICP备XXXXXXXX号-小程序`，网站备案号没有后缀。

#### Q: 没备案可以提交审核吗？
A: 不可以。2023 年 9 月后，未备案的小程序无法提交审核。

### 备案材料准备

| 主体类型 | 必需材料 |
|---------|---------|
| 个人 | 身份证正反面、手持身份证照片 |
| 企业 | 营业执照、法人身份证、负责人身份证 |
| 其他组织 | 组织机构代码证/登记证书、负责人身份证 |

**注意**：
- 照片要清晰，边角完整
- 证件在有效期内
- 负责人手机号需实名认证

## 二、名称规范 / Naming Rules

### 名称审核要求

小程序名称需要通过微信的名称审核，常见被驳回的原因：

#### 1. 侵权问题

- 不能使用已注册商标（除非有授权）
- 不能包含"微信"、"腾讯"、"WeChat"等官方词汇
- 不能使用名人姓名、知名品牌名（除非有授权）

**示例**：
- ❌ 微信相册助手
- ❌ 腾讯云笔记
- ❌ XX明星粉丝团（未授权）
- ✅ 我的相册整理
- ✅ 云端笔记本

#### 2. 广告性质

- 不能包含"最"、"第一"、"唯一"等绝对化用语
- 不能包含联系方式（电话、微信号、QQ）
- 不能包含价格、促销信息

**示例**：
- ❌ 最好用的计算器
- ❌ 第一购物平台
- ❌ 联系我们 138XXXX
- ✅ 便捷计算器
- ✅ 优选购物

#### 3. 泛化/混淆

- 名称不能过于宽泛，要能区分具体功能
- 不能与已有知名小程序高度相似

**示例**：
- ❌ 工具（太宽泛）
- ❌ 小程序（太宽泛）
- ✅ 单位换算工具
- ✅ 日程提醒助手

### 名称建议

1. **简短明确**：3-10 个字为佳
2. **体现功能**：让用户一眼知道这是干什么的
3. **独特性**：避免和已有小程序重名
4. **提前检索**：在微信中搜索候选名称，看是否已被使用

## 三、隐私合规 / Privacy Compliance

### 隐私政策要求

2021 年起，微信小程序需要配置用户隐私保护指引。

#### 配置位置

微信公众平台 → 设置 → 功能设置 → 用户隐私保护指引

#### 必须声明的内容

| 收集信息 | 使用场景 | 示例说明 |
|---------|---------|---------|
| 用户信息（昵称、头像） | wx.getUserProfile | "用于显示您的个人资料" |
| 地理位置 | wx.getLocation | "用于查找附近的服务" |
| 相册 | wx.chooseImage | "用于上传图片" |
| 手机号 | 手机号快速验证组件 | "用于账号登录和找回密码" |

#### 代码中的隐私处理

```javascript
// 在请求敏感权限前检查隐私协议
wx.requirePrivacyAuthorize({
  success() {
    // 用户同意后继续
    wx.getUserProfile({ ... });
  },
  fail() {
    // 用户拒绝
    wx.showToast({ title: '需要同意隐私协议', icon: 'none' });
  }
});
```

### 常见隐私问题

#### 1. 过度收集

- ❌ 首次打开就要求授权用户信息
- ✅ 需要时才请求，并说明原因

#### 2. 未声明就使用

- ❌ 使用了 `wx.getLocation` 但未在隐私指引中声明
- ✅ 所有使用的敏感 API 都要在指引中声明

#### 3. 无法撤回授权

- ❌ 用户无法取消已授权的权限
- ✅ 提供设置页面或引导用户去系统设置中取消

### 登录规范

#### 不允许

- 首页强制登录（没有任何可用功能）
- 要求输入微信密码
- 诱导用户授权不必要的信息

#### 建议

- 核心功能尽量免登录可用
- 需要登录时说明原因
- 只请求必要的信息

```javascript
// 好的做法：需要时才请求
Page({
  saveRecord() {
    if (!this.data.userInfo) {
      wx.showModal({
        title: '提示',
        content: '保存记录需要登录，是否继续？',
        success: (res) => {
          if (res.confirm) {
            this.login();
          }
        }
      });
      return;
    }
    // 继续保存逻辑
  }
});
```

## 四、服务类目 / Service Categories

### 类目选择原则

1. **如实选择**：选择与实际功能最匹配的类目
2. **不要贪多**：只选必要的，多选反而容易被质疑
3. **提前了解资质**：部分类目需要特殊资质

### 常见类目问题

#### 1. 类目与功能不符

- ❌ 选了"医疗健康"类目但只是记录喝水
- ✅ 选"工具 > 健康管理"

#### 2. 缺少必要资质

| 类目 | 常见资质要求 |
|-----|------------|
| 社交 > 陌生人交友 | ICP证、增值电信业务许可 |
| 医疗 > 在线诊疗 | 医疗机构执业许可证 |
| 金融 > 贷款 | 金融许可证 |
| 电商 > 食品销售 | 食品经营许可证 |
| 教育 > 在线教育 | 备案或办学许可证 |

#### 3. 审核员找不到对应功能

- ❌ 选了多个类目但首页看不出来
- ✅ 首页能清晰到达所有类目对应的功能

### 类目查询

官方类目资质要求：https://developers.weixin.qq.com/miniprogram/product/material/

## 五、内容安全 / Content Safety

### UGC 风险

如果小程序有用户生成内容（评论、发帖、上传图片等），必须：

1. **接入内容安全 API**：
   - 文本：`security.msgSecCheck`
   - 图片：`security.imgSecCheck`
   - 音频：`security.mediaCheckAsync`

2. **人工审核机制**：高风险内容需人工复核

3. **举报入口**：用户可以举报违规内容

4. **违规处理**：有删除、封禁等处理流程

### 代码示例

```javascript
// 发布内容前检查
async function checkContent(text) {
  try {
    const res = await wx.cloud.callFunction({
      name: 'securityCheck',
      data: { content: text }
    });
    return res.result.ok;
  } catch (err) {
    console.error('内容检查失败', err);
    return false;
  }
}

// 云函数 securityCheck
const cloud = require('wx-server-sdk');
cloud.init();

exports.main = async (event) => {
  try {
    const result = await cloud.openapi.security.msgSecCheck({
      content: event.content
    });
    return { ok: result.errCode === 0 };
  } catch (err) {
    return { ok: false, error: err.message };
  }
};
```

## 六、其他常见驳回原因

### 1. 诱导分享

- ❌ "分享到群可获得奖励"
- ❌ "转发 3 个群解锁功能"
- ✅ 自然分享，不强制不诱导

### 2. 功能不完整

- ❌ "敬请期待"、"即将上线"页面
- ❌ 空白页面或占位图片
- ✅ 所有可点击的入口都有完整功能

### 3. 虚拟支付

- ❌ 在 iOS 上用微信支付购买虚拟商品
- ✅ iOS 虚拟商品使用苹果内购，或免费+广告模式

### 4. 外部跳转

- ❌ 诱导跳转到 App 或网页
- ❌ 核心功能在小程序外完成
- ✅ 主要功能在小程序内闭环

## 提审前自查清单 / Pre-Submission Checklist

- [ ] 已完成小程序备案
- [ ] 名称不侵权、不违规
- [ ] 配置了隐私保护指引
- [ ] 服务类目与功能一致
- [ ] 有资质要求的类目已准备材料
- [ ] UGC 功能接入了内容安全 API
- [ ] 无诱导分享行为
- [ ] 无占位/空白页面
- [ ] 审核路径清晰可达
- [ ] 运行了 `wechat-miniapp-reviewer` 预审

## 相关资源 / Resources

- [微信小程序运营规范](https://developers.weixin.qq.com/miniprogram/product/)
- [常见驳回原因](https://developers.weixin.qq.com/miniprogram/product/reject.html)
- [服务类目资质](https://developers.weixin.qq.com/miniprogram/product/material/)
- [小程序备案指引](https://developers.weixin.qq.com/miniprogram/product/record/guidelines)
- [内容安全 API](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/sec-check/)

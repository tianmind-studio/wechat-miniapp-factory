#!/usr/bin/env python3
"""Create a review-friendly native WeChat Mini Program starter project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


def slugify(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_-]+", "-", value.strip()).strip("-")
    return value.lower() or "miniapp"


def write_text(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(root: Path, rel: str, data: object) -> None:
    write_text(root, rel, json.dumps(data, ensure_ascii=False, indent=2))


def ensure_output(path: Path, force: bool) -> None:
    if path.exists() and any(path.iterdir()) and not force:
        raise SystemExit(f"Output directory is not empty: {path}. Use --force to write into it.")
    path.mkdir(parents=True, exist_ok=True)


def page_json(title: str) -> dict[str, str]:
    return {"navigationBarTitleText": title}


def build_project(args: argparse.Namespace) -> None:
    root = Path(args.output).expanduser().resolve()
    ensure_output(root, args.force)

    project_name = args.name.strip() or "Mini Program Starter"
    description = args.description.strip() or "A generated WeChat Mini Program starter."
    project_slug = slugify(project_name)
    appid = args.appid.strip() or "touristappid"

    write_json(
        root,
        "project.config.json",
        {
            "appid": appid,
            "compileType": "miniprogram",
            "libVersion": "latest",
            "projectname": project_slug,
            "setting": {
                "urlCheck": False,
                "es6": True,
                "enhance": True,
                "postcss": True,
                "minified": True,
            },
        },
    )

    write_json(
        root,
        "app.json",
        {
            "pages": ["pages/home/index", "pages/catalog/index", "pages/profile/index"],
            "window": {
                "navigationBarTitleText": project_name,
                "navigationBarBackgroundColor": "#0F766E",
                "navigationBarTextStyle": "white",
                "backgroundColor": "#F6F7F2",
            },
            "style": "v2",
            "sitemapLocation": "sitemap.json",
        },
    )

    write_json(root, "sitemap.json", {"rules": [{"action": "allow", "page": "*"}]})

    write_text(
        root,
        "app.js",
        f"""App({{
  globalData: {{
    appName: {json.dumps(project_name, ensure_ascii=False)},
    description: {json.dumps(description, ensure_ascii=False)}
  }}
}});
""",
    )

    write_text(
        root,
        "app.wxss",
        """.page {
  min-height: 100vh;
  box-sizing: border-box;
  padding: 32rpx;
  background: #f6f7f2;
  color: #172026;
}

.section {
  margin-bottom: 28rpx;
}

.title {
  font-size: 44rpx;
  font-weight: 700;
  line-height: 1.2;
}

.muted {
  color: #667085;
  font-size: 26rpx;
  line-height: 1.6;
}

.card {
  border-radius: 12rpx;
  background: #ffffff;
  padding: 28rpx;
  box-shadow: 0 8rpx 24rpx rgba(15, 23, 42, 0.06);
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 8rpx;
  background: #0f766e;
  color: #ffffff;
  padding: 18rpx 24rpx;
  font-size: 28rpx;
}
""",
    )

    write_text(
        root,
        "utils/seed.js",
        f"""const appProfile = {{
  name: {json.dumps(project_name, ensure_ascii=False)},
  description: {json.dumps(description, ensure_ascii=False)},
  status: 'demo-ready'
}};

const catalogItems = [
  {{
    id: 'core-flow',
    title: 'Core workflow',
    summary: 'Replace this item with the main user journey.',
    tag: 'Feature'
  }},
  {{
    id: 'data-layer',
    title: 'Data layer',
    summary: 'Connect this page to CloudBase or a local fallback dataset.',
    tag: 'Data'
  }},
  {{
    id: 'review-path',
    title: 'Reviewer path',
    summary: 'Keep the review-critical path visible from the home page.',
    tag: 'Review'
  }}
];

module.exports = {{
  appProfile,
  catalogItems
}};
""",
    )

    write_json(root, "pages/home/index.json", page_json("Home"))
    write_text(
        root,
        "pages/home/index.wxml",
        """<view class="page">
  <view class="section">
    <view class="title">{{appName}}</view>
    <view class="muted">{{description}}</view>
  </view>

  <view class="card section">
    <view class="muted">Start from the main workflow, then keep reviewer-facing paths easy to reach.</view>
  </view>

  <button class="button" bindtap="goCatalog">Open workflow</button>
</view>
""",
    )
    write_text(
        root,
        "pages/home/index.wxss",
        """.card {
  margin-top: 24rpx;
}
""",
    )
    write_text(
        root,
        "pages/home/index.js",
        """const { appProfile } = require('../../utils/seed');

Page({
  data: {
    appName: appProfile.name,
    description: appProfile.description
  },

  goCatalog() {
    wx.navigateTo({ url: '/pages/catalog/index' });
  }
});
""",
    )

    write_json(root, "pages/catalog/index.json", page_json("Workflow"))
    write_text(
        root,
        "pages/catalog/index.wxml",
        """<view class="page">
  <view class="section">
    <view class="title">Workflow</view>
    <view class="muted">Replace these cards with real business data before submission.</view>
  </view>

  <block wx:for="{{items}}" wx:key="id">
    <view class="card item">
      <view class="item-title">{{item.title}}</view>
      <view class="muted">{{item.summary}}</view>
      <view class="tag">{{item.tag}}</view>
    </view>
  </block>

  <button class="button" bindtap="goProfile">Review readiness</button>
</view>
""",
    )
    write_text(
        root,
        "pages/catalog/index.wxss",
        """.item {
  margin-bottom: 20rpx;
}

.item-title {
  font-size: 32rpx;
  font-weight: 700;
  margin-bottom: 8rpx;
}

.tag {
  display: inline-block;
  margin-top: 16rpx;
  padding: 6rpx 12rpx;
  border-radius: 6rpx;
  background: #e0f2f1;
  color: #0f766e;
  font-size: 22rpx;
}
""",
    )
    write_text(
        root,
        "pages/catalog/index.js",
        """const { catalogItems } = require('../../utils/seed');

Page({
  data: {
    items: catalogItems
  },

  goProfile() {
    wx.navigateTo({ url: '/pages/profile/index' });
  }
});
""",
    )

    write_json(root, "pages/profile/index.json", page_json("Review"))
    write_text(
        root,
        "pages/profile/index.wxml",
        """<view class="page">
  <view class="section">
    <view class="title">Review readiness</view>
    <view class="muted">Use this page to keep submission notes, test paths, and compliance items visible.</view>
  </view>

  <view class="card section">
    <block wx:for="{{checks}}" wx:key="label">
      <view class="check-row">
        <text>{{item.done ? 'OK' : 'TODO'}}</text>
        <text>{{item.label}}</text>
      </view>
    </block>
  </view>
</view>
""",
    )
    write_text(
        root,
        "pages/profile/index.wxss",
        """.check-row {
  display: flex;
  gap: 20rpx;
  padding: 14rpx 0;
  border-bottom: 1rpx solid #eef2f7;
  font-size: 26rpx;
}

.check-row:last-child {
  border-bottom: 0;
}
""",
    )
    write_text(
        root,
        "pages/profile/index.js",
        """Page({
  data: {
    checks: [
      { label: 'Real content is filled in', done: false },
      { label: 'Service category is confirmed', done: false },
      { label: 'Privacy and permission copy is ready', done: false },
      { label: 'Reviewer path is documented', done: true }
    ]
  }
});
""",
    )

    if args.cloudbase:
        write_json(root, "cloudfunctions/ping/package.json", {"name": "ping", "version": "1.0.0", "main": "index.js"})
        write_text(
            root,
            "cloudfunctions/ping/index.js",
            """exports.main = async () => {
  return {
    ok: true,
    message: 'CloudBase function is reachable'
  };
};
""",
        )

    write_json(
        root,
        "package.json",
        {
            "name": project_slug,
            "version": "0.1.0",
            "private": True,
            "scripts": {"test": "node tests/validate-miniapp.js"},
        },
    )

    write_text(
        root,
        "tests/validate-miniapp.js",
        """const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');

function readJson(rel) {
  return JSON.parse(fs.readFileSync(path.join(root, rel), 'utf8'));
}

function assertFile(rel) {
  if (!fs.existsSync(path.join(root, rel))) {
    throw new Error(`Missing file: ${rel}`);
  }
}

const app = readJson('app.json');
readJson('project.config.json');
readJson('sitemap.json');

if (!Array.isArray(app.pages) || app.pages.length < 3) {
  throw new Error('app.json should declare at least three pages');
}

for (const page of app.pages) {
  assertFile(`${page}.json`);
  assertFile(`${page}.wxml`);
  assertFile(`${page}.wxss`);
  assertFile(`${page}.js`);
}

console.log('[miniapp] validation passed');
""",
    )

    write_text(
        root,
        "docs/product-brief.md",
        f"""# Product Brief

Name: {project_name}

Description: {description}

Architecture: Native WeChat Mini Program{" + CloudBase-ready cloudfunctions" if args.cloudbase else " with local seed data"}

Assumptions to replace:

- Target users:
- Core workflow:
- Service category:
- Required credentials:
- Reviewer test path:
""",
    )

    write_text(
        root,
        "docs/submission-checklist.md",
        """# Submission Checklist

- Confirm AppID in `project.config.json`.
- Replace demo content with real operating content.
- Confirm service category and qualifications.
- Confirm privacy policy and permission explanations.
- Prepare reviewer account if login-gated features exist.
- Document path: Home -> Workflow -> Review readiness.
- Run `npm test`.
- Run the `wechat-miniapp-reviewer` skill before upload.
""",
    )

    write_text(
        root,
        "docs/review-notes.md",
        """# Review Notes Draft

Reviewer path:

1. Open the home page.
2. Tap "Open workflow".
3. Inspect the core workflow cards.
4. Tap "Review readiness".

Submission note draft:

This version provides a complete demo path from home page to core workflow and review readiness page. Please use the visible navigation path above to inspect the main feature.
""",
    )

    print(f"Created Mini Program starter at: {root}")
    print("Next: customize product copy/data, run `npm test`, then run the reviewer gate.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a native WeChat Mini Program starter.")
    parser.add_argument("output", help="Output project directory")
    parser.add_argument("--name", default="Mini Program Starter", help="Mini Program name")
    parser.add_argument("--description", default="A generated WeChat Mini Program starter.", help="Short product description")
    parser.add_argument("--appid", default="touristappid", help="WeChat Mini Program AppID or touristappid")
    parser.add_argument("--cloudbase", action="store_true", help="Include a CloudBase-ready cloudfunctions directory")
    parser.add_argument("--force", action="store_true", help="Allow writing into a non-empty directory")
    args = parser.parse_args()
    build_project(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())

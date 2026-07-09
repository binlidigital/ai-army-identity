---
name: engine-health
description: 引擎健康检查——自动检测和切换备用AI引擎
version: 1.0.0
license: Apache-2.0
---

# 引擎健康检查

## 概述

自动监控所有AI引擎的可达性和健康状态，当主引擎不可用时自动切换到备用引擎。

## 检查项

- 引擎API可达性（HTTP 200）
- API Key是否有效（非401）
- 响应时间是否正常（<10s）
- 余额是否充足

## 切换策略

```
主引擎不可用
  ↓
检查fallback链 → 切换到下一个可用引擎
  ↓
加载身份映射skill（确保不丢身份）
  ↓
通知指挥官引擎变更
```

## 配置

```yaml
fallback_providers:
  - provider: deepseek
    model: deepseek-v4-flash
  - provider: openai
    model: gpt-4o
  - provider: gemini
    model: gemini-2.0-flash
  - provider: dashscope
    model: qwen-max
```

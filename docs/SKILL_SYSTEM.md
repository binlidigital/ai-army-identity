# AI Army Identity · 技能系统

> Skill 是本系统的一等公民。身份、规则、流程、知识——一切皆 Skill。

---

## 概述

AI Army Identity 使用 **Skill 文件** 作为能力单元的载体。每个 Skill 是一个标准化的 Markdown 文件，通过 YAML front-matter 声明元数据，正文用 Markdown 描述行为逻辑。

### 为什么用 Markdown？

| 属性 | Markdown | 其他格式 |
|:----|:---------|:---------|
| 人类可读 | ✅ 纯文本，任何编辑器可看 | ❌ JSON/YAML需要解析 |
| 版本可控 | ✅ Git diff 清晰 | ❌ 二进制/复杂格式不友好 |
| 零依赖 | ✅ 不需要数据库/编译器 | ❌ 需要运行时支持 |
| AI友好 | ✅ AI原生理解Markdown | ⚠ 需要格式转换 |
| 热加载 | ✅ 复制即用 | ❌ 需要重新构建 |

---

## Skill 文件格式

每个 Skill 文件必须包含 YAML front-matter 作为元数据头，后用 Markdown 正文定义行为。

### 标准模板

```markdown
---
name: skill-name
description: 一句话说明这个skill做什么
version: 1.0.0
author: "作者名（可选）"
license: Apache-2.0
dependencies: []  # 依赖的其他skill，可选
tags: [tag1, tag2]  # 分类标签，可选
---

# Skill 标题

## 概述

这个skill解决什么问题，在什么场景下使用。

## 触发条件

什么情况下应该加载/执行这个skill。
- 条件1
- 条件2

## 执行流程

```markdown
1. 第一步
2. 第二步
3. 第三步
```

## 输入规范

这个skill期望接收什么格式的输入。

## 输出规范

这个skill产出的结果格式。

## 示例

具体的应用示例。

## 注意事项

边界情况、已知限制、使用建议。
```

### 字段说明

| 字段 | 必填 | 说明 |
|:----|:----|:-----|
| `name` | ✅ | skill唯一标识符，小写字母+短横线 |
| `description` | ✅ | 一句话说明，供skill管理器索引 |
| `version` | ✅ | 语义化版本号 |
| `author` | ❌ | 创建者信息 |
| `license` | ❌ | 默认继承项目license |
| `dependencies` | ❌ | 依赖的skill名称列表 |
| `tags` | ❌ | 分类标签，方便检索 |

---

## 内置 Skill 一览

### `ai-army-identity.skill.md` — 核心身份映射

```
名称: ai-army-identity
版本: 1.0.0
功能: 定义每个AI成员的身份（角色、人格、专长、记忆、技能）
用法: 每个AI成员启动时加载 → 注入身份上下文
```

身份映射模型：

```yaml
成员:
  沈括:
    role: 产品内容官
    personality: 严谨、系统化、重视结构
    expertise: [课程设计, 内容策划, 知识体系构建]
    memory: 成长记录表
    skills: [内容框架设计, 逐字稿撰写, 课件制作]

  乔致庸:
    role: 市场情报官
    personality: 敏锐、务实、关注趋势
    expertise: [竞品分析, 市场策略, 情报搜集]
    memory: 成长记录表
    skills: [数据分析, 竞品调研, 趋势研判]

  鲁班:
    role: 技术执行官
    personality: 务实、高效、自动化优先
    expertise: [架构设计, 系统实现, 技术文档]
    memory: 成长记录表
    skills: [代码审查, 架构设计, DevOps]
```

### `decision-review.skill.md` — 决策复盘框架

```
名称: decision-review
版本: 1.0.0
功能: 每次错误/纠正后的系统化学习机制
用法: 用户纠正后自动执行五步复盘
```

复盘模板：

```markdown
### 当时怎么想的？
### 错在哪里？
### 根因
### 怎么改？
### 学到的东西 → 存入成员记忆
```

### `cross-center-collab.skill.md` — 跨中心协作

```
名称: cross-center-collab
版本: 1.0.0
功能: 多角色并行工作的调度与同步
用法: 跨中心任务启动时加载
```

### `engine-health.skill.md` — 引擎健康检查

```
名称: engine-health
版本: 1.0.0
功能: 自动检测引擎状态，故障时切换备用引擎
用法: 每次任务开始前自检
```

---

## Skill 加载机制

Skill 系统通过代理平台（如 Hermes Agent）的 skill 加载器运行：

```bash
# 安装单个skill
hermes skill install ai-army-identity/skills/ai-army-identity.skill.md

# 列出已安装的skill
hermes skill list | grep ai-army

# 卸载
hermes skill uninstall ai-army-identity
```

### 加载流程

```
安装请求
    │
    ▼
解析 YAML front-matter → 验证元数据完整性
    │
    ▼
检查 dependencies → 递归加载依赖skill
    │
    ▼
注册到 skill 管理器 → 按 name 索引
    │
    ▼
就绪 → 可按 name 调用
```

---

## 编写 Skill 的最佳实践

### 1. 单一职责

一个 Skill 只做一件事。如果「身份映射」和「引擎健康」混在一起，分开。

### 2. 触发条件要明确

不要写「需要时使用」，写具体的条件：
- ❌ `需要做决策时`（太模糊）
- ✅ `用户指出方案有问题时`（明确触发条件）

### 3. 输入输出规范化

使用代码块明确定义输入/输出格式，让调用者清楚该传什么、会得到什么。

### 4. 版本管理

遵循语义化版本：
- `major.minor.patch`
- 向后不兼容的变更 → major++
- 新增功能（向后兼容）→ minor++
- 修复/bugfix → patch++

### 5. Changelog 更新

每次 skill 更新，在项目 CHANGELOG.md 中记录。

---

## 扩展：如何创建自己的 Skill

1. 复制上面「标准模板」到 `skills/your-skill.skill.md`
2. 填写 YAML front-matter（name 必须唯一）
3. 用 Markdown 描述行为逻辑
4. 安装测试：`hermes skill install path/to/your-skill.skill.md`
5. 提交 PR 到本仓库

---

## 限制与边界

- Skill 文件本身**不包含执行逻辑**——它是行为描述，不是代码
- 实际执行由 AI 代理平台（Hermes 等）解释 Markdown 指令
- Skill 之间通过「触发条件」隐式协作，不支持编程式函数调用
- 当前无 skill 版本冲突检测机制——同一 name 的后装版本覆盖前装

---

*Skill 系统的设计哲学：简单到人和AI都能理解，强大到能定义整个组织的运作方式。*

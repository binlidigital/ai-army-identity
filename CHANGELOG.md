# Changelog

## [1.0.0] - 2026-07-09

### 新增
- 首个公开发布版本
- 核心身份映射框架（ai-army-identity.skill.md）
  - 身份映射模型：每个AI成员有独立人格、专业定位、成长记忆
  - 引擎切换后自动恢复身份，不丢失记忆
- 决策复盘框架（decision-review.skill.md）
  - 标准复盘模板：当时怎么想的→错在哪里→根因→怎么改→学到的东西
  - 支持自动触发和手动触发两种模式
- 跨中心协作流程（cross-center-collab.skill.md）
  - 多角色并行工作的标准调度流程
  - 独立子任务+结果汇聚模式
- 引擎健康检查机制（engine-health.skill.md）
  - 多API健康监控+自动故障切换
  - 5层fallback链：DeepSeek→OpenAI→Gemini→DashScope→硅基流动
- 完整组织架构定义（6大中心，8个AI成员）
- Apache 2.0 License
- 贡献指南（CONTRIBUTING.md）
- 行为准则（CODE_OF_CONDUCT.md）
- 安全策略（SECURITY.md）
- 路线图（ROADMAP.md）
- 完整文档体系：
  - 系统概述（docs/OVERVIEW.md）
  - 技术架构（docs/ARCHITECTURE.md）
  - 核心理念（docs/PHILOSOPHY.md）
  - 技能系统（docs/SKILL_SYSTEM.md）
  - 决策框架（docs/DECISION_FRAMEWORK.md）
  - 六大中心文档（docs/CENTERS/）
  - 团队成员档案（docs/MEMBERS/）
- 项目完整性验证脚本（scripts/validate.py）
  - 检查文件结构、skill front-matter、README链接、License、Changelog
- 设计图Prompt集（assets/README_DESIGN_PROMPTS.md）
  - 主Logo 3套方案、架构图2版、README横幅、概念图2张
- GitHub基础设施：
  - Issue模板（.github/ISSUE_TEMPLATE/bug_report.md）
  - .gitignore
  - GitHub Actions CI（.github/workflows/validate.yml）

### 核心理念
- **身份优先**：每个AI成员有独立人格和专业定位，不是万能回复机
- **记忆即生命**：集体记忆让团队持续进化，每次交互是进化不是重启
- **事件驱动**：没有固定时间表，有任务自动响应，空闲自动学习
- **学习产出标准**：不产出可调用skill的学习不算学习
- **AI管理资源**：AI管理Token预算/API调用，不管理时间

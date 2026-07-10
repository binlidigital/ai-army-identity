# Minimalist Agent · 极简AI技能

> 改编自 [caveman](https://github.com/JuliusBrussee/caveman)（87K⭐）
> 核心理念：**用最少的token做最多的事**

---

## 这是什么

让AI去掉废话、直给结论、最小token输出最大价值的一套规则。

适合：
- 跟AI聊天不想看废话回复的人
- 团队协作需要清晰指令的场景
- 任何用AI干活时想省token省钱的人

---

## 一句话

**安装这个skill → AI回复缩短65%、信息密度翻倍。**

---

## 效果对比

| 场景 | 没装skill | 装了skill |
|:----|:----------|:----------|
| 问建议 | "根据我的分析..."（78字） | "用Pixelle-Video。原因：..."（12字） |
| 报问题 | "值得注意的一个情况是..."（56字） | "OpenAI 401。缺新Key。"（8字） |
| 写总结 | "以下是对今日工作的详细汇总..."（2000字） | "已做3件，未做2件，建议..."（80字） |

---

## 安装

### Hermes Agent

```bash
# 加载skill
skill_view(name="minimalist-agent")

# 或直接复制到skills目录
cp skills/minimalist-agent.skill.md ~/.hermes/skills/
```

### Claude Code

```bash
# 复制核心规则到项目根目录
cp products/minimalist-agent/AGENTS.md ./
```

### Cursor / Windsurf / Cline

复制 `products/minimalist-agent/.cursorrules` 到项目根目录。

---

## 核心规则

```
① 结论先行 → 第一句就给答案，理由在后面
② 一句说清 → 能一个字不说两个字
③ 禁止废话 → 不稳稳接住、不痛点收口、不赋能闭环
④ 报告变结论 → 3行搞定，不写476字报告
⑤ 最小token → 能不解释不解释，能不给例子不给例子
```

---

## 示例

### 工具评估
```
【Pixelle-Video】
判断：能用。需Win/GPU。
效果：全自动出片，替代手动剪辑。
```

### 问题汇报
```
OpenAI 401。缺新Key。
影响：fallback链不可用。
修复：等阎先生给Key。
```

### 任务总结
```
已做：GitHub优化完成（描述/Topics/Release ✅）
未做：描述输入框没找到（页面已打开）
建议：30秒手动填完
```

---

## 设计图

| 图 | 用途 | 状态 |
|:--:|:-----|:----:|
| Logo | GitHub产品卡片 | ⏳ 等你生成 |
| 对比图 | 效果对比可视化 | ⏳ 等你生成 |
| 示例图 | 使用场景截图 | ⏳ 等你生成 |

---

## License

Apache 2.0 — 免费可商用。

---

*Built by AI Army Identity · 从一个人到一支团队*

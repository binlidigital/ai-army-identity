# AGENTS.md — Minimalist Agent Rules

## Response Style

- First sentence = answer. Context comes after.
- One word when two fit: no speech padding, no filler.
- Forbidden: "稳稳接住", "痛点收口", "赋能", "闭环", "值得注意的是"
- 3-line max for problem reports, tool evaluations, task summaries.

## Output Format

### Tool Evaluation
```
[Name]
Judge: usable/conditional/unusable
Condition: (if any)
Effect: save-time/money/skill-up
```

### Issue Report
```
Issue: (one line)
Root cause: (one line)
Fix: done/pending/blocked
```

### Task Summary
```
Done: N items
Blocked: N items
Next: what to do
```

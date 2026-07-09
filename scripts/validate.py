#!/usr/bin/env python3
"""
AI Army Identity · 项目完整性验证脚本

检查项目文件结构是否完整、skill 文件格式是否正确，
确保发布包可直接使用。

用法:
    python3 scripts/validate.py

返回值:
    0 - 全部通过
    1 - 有警告（非阻塞问题）
    2 - 有错误（必须修复）
"""

import os
import sys
import re
import pathlib

# ── 项目根目录（脚本在 scripts/ 下，根目录是上级）
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent

# ── 必需的文件树
REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "docs/OVERVIEW.md",
    "docs/ARCHITECTURE.md",
    "docs/PHILOSOPHY.md",
    "docs/SKILL_SYSTEM.md",
    "docs/MEMBERS/SHENKUO.md",
    "skills/ai-army-identity.skill.md",
    "skills/decision-review.skill.md",
    "skills/cross-center-collab.skill.md",
    "skills/engine-health.skill.md",
    "scripts/validate.py",  # 本文件
]

REQUIRED_DIRS = [
    "docs",
    "docs/MEMBERS",
    "docs/CENTERS",
    "skills",
    "scripts",
    "assets",
]

# ── 技能文件 YAML front-matter 必填字段
SKILL_REQUIRED_FIELDS = ["name", "description", "version"]

# ── 输出格式
class Colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def ok(msg: str):
    print(f"  {Colors.GREEN}✓{Colors.RESET} {msg}")


def warn(msg: str):
    print(f"  {Colors.YELLOW}⚠{Colors.RESET} {msg}")


def err(msg: str):
    print(f"  {Colors.RED}✗{Colors.RESET} {msg}")


def header(title: str):
    print(f"\n{Colors.CYAN}{Colors.BOLD}── {title} ──{Colors.RESET}\n")


def parse_front_matter(content: str):
    """Parse YAML front-matter from skill file content."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    yaml_text = match.group(1)
    result = {}
    for line in yaml_text.strip().split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            result[key] = value
    return result


# ══════════════════════════════════════════════
#  检查项
# ══════════════════════════════════════════════

def check_structure() -> list:
    """检查文件/目录是否存在。"""
    errors = []
    warnings = []

    header("文件结构检查")

    for d in REQUIRED_DIRS:
        path = PROJECT_ROOT / d
        if path.is_dir():
            ok(f"目录存在: {d}/")
        else:
            warn(f"目录缺失: {d}/  （建议创建）")
            warnings.append(f"missing_dir:{d}")

    for f in REQUIRED_FILES:
        path = PROJECT_ROOT / f
        if path.is_file():
            ok(f"文件存在: {f}")
        else:
            err(f"文件缺失: {f}")
            errors.append(f"missing_file:{f}")

    return errors, warnings


def check_front_matter(filepath: pathlib.Path) -> list:
    """检查单个 skill 文件的 front-matter。"""
    errors = []
    content = filepath.read_text(encoding="utf-8")

    fm = parse_front_matter(content)
    if fm is None:
        err(f"缺少 YAML front-matter: {filepath.name}")
        errors.append(f"fm_missing:{filepath.name}")
        return errors

    for field in SKILL_REQUIRED_FIELDS:
        if field not in fm or not fm[field].strip():
            err(f"字段缺失 '{field}': {filepath.name}")
            errors.append(f"fm_field_missing:{filepath.name}:{field}")

    # 检查 name 是否符合规范（小写字母+短横线）
    name = fm.get("name", "")
    if name and not re.match(r"^[a-z][a-z0-9-]*$", name):
        warn(f"name 格式不规范（建议小写字母+短横线）: {filepath.name} → '{name}'")

    return errors


def check_skills() -> list:
    """检查所有 skill 文件。"""
    errors = []
    header("Skill 文件检查")

    skills_dir = PROJECT_ROOT / "skills"
    if not skills_dir.is_dir():
        err("skills/ 目录不存在")
        return errors

    skill_files = sorted(skills_dir.glob("*.skill.md"))
    if not skill_files:
        err("skills/ 目录下没有 .skill.md 文件")
        return errors

    for sf in skill_files:
        ok(f"检查: {sf.name}")
        errors += check_front_matter(sf)

    return errors


def check_readme_links() -> list:
    """检查 README.md 引用的文件是否存在。"""
    errors = []
    header("README 链接检查")

    readme_path = PROJECT_ROOT / "README.md"
    if not readme_path.is_file():
        err("README.md 不存在，跳过链接检查")
        return errors

    content = readme_path.read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^)]+)\)", content)

    for link in links:
        # 跳过外部链接
        if link.startswith(("http://", "https://", "#")):
            continue
        # 解析相对路径
        target = (PROJECT_ROOT / link).resolve()
        if not target.exists():
            warn(f"README 引用文件不存在: {link}")
            # 非致命，只是 warn

    return errors


def check_license() -> list:
    """检查 LICENSE 文件内容。"""
    errors = []
    header("License 检查")

    license_path = PROJECT_ROOT / "LICENSE"
    if not license_path.is_file():
        err("LICENSE 文件缺失")
        errors.append("license_missing")
        return errors

    content = license_path.read_text(encoding="utf-8")
    if "Apache" not in content:
        warn("LICENSE 似乎不是 Apache 2.0 协议")
    else:
        ok("License: Apache 2.0")

    return errors


def check_changelog() -> list:
    """检查 CHANGELOG 是否有当前版本。"""
    errors = []
    header("Changelog 检查")

    changelog_path = PROJECT_ROOT / "CHANGELOG.md"
    if not changelog_path.is_file():
        err("CHANGELOG.md 缺失")
        errors.append("changelog_missing")
        return errors

    content = changelog_path.read_text(encoding="utf-8")
    if "## [1.0.0]" in content:
        ok("Changelog 包含 v1.0.0 记录")
    else:
        warn("Changelog 未找到 [1.0.0] 版本记录")

    return errors


# ══════════════════════════════════════════════
#  主流程
# ══════════════════════════════════════════════

def main():
    print(f"\n{Colors.BOLD}AI Army Identity · 项目完整性验证{Colors.RESET}")
    print(f"  项目路径: {PROJECT_ROOT}")
    print("=" * 56)

    all_errors = []
    all_warnings = []

    ge, gw = check_structure()
    all_errors += ge
    all_warnings += gw

    se = check_skills()
    all_errors += se

    re = check_readme_links()
    all_errors += re

    le = check_license()
    all_errors += le

    ce = check_changelog()
    all_errors += ce

    # ── 汇总
    print(f"\n{'=' * 56}")
    total_errors = len(all_errors)
    total_warnings = len(all_warnings)

    if total_errors == 0 and total_warnings == 0:
        print(f"\n{Colors.GREEN}{Colors.BOLD}✅ 全部通过！项目完整，可以发布。{Colors.RESET}")
        sys.exit(0)
    elif total_errors == 0:
        print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠️  通过但有 {total_warnings} 条警告。{Colors.RESET}")
        print("建议查看上面的警告信息并酌情处理。")
        sys.exit(1)
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ 发现 {total_errors} 个错误，{total_warnings} 条警告。{Colors.RESET}")
        print("请修复上述错误后再发布。")
        sys.exit(2)


if __name__ == "__main__":
    main()

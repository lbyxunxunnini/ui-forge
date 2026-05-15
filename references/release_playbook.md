# Release Playbook

## 版本规则

| 格式 | 用途 |
|------|------|
| `vX.Y.Z` | 正式发布版本 |
| `vX.Y.Z-rc.N` | 候选版本 |
| `vX.Y.Z-dev.N` | 开发版本 |

版本号递增规则：

- **Z (patch)**: bug fix、文档修正、脚本改进
- **Y (minor)**: 新功能、新模式、新脚本
- **X (major)**: 架构变更、breaking change

## 发布前检查清单

### 1. 运行 doctor

```bash
bash scripts/doctor.sh
```

确认：0 errors，warnings 已 review。

### 2. 运行路由测试

```bash
python3 scripts/route_golden_tests.py
```

确认：全部通过。如有失败，先修复路由规则。

### 3. 运行发布 gate

```bash
bash scripts/validate_release.sh
```

确认：全部通过。

### 4. 手动检查

- [ ] SKILL.md 入口表与实际触发词一致
- [ ] CHEATSHEET.md 示例与实际行为一致
- [ ] QUICKSTART.md 安装步骤可执行
- [ ] CHANGELOG.md 包含当前版本条目
- [ ] 所有新增文件已在 README.md 中列出

## 发布步骤

### Step 1: 更新版本号

三个文件必须同步更新：

```bash
# VERSION
echo "vX.Y.Z" > VERSION

# .skillhub.json
python3 -c "
import json
with open('.skillhub.json', 'r') as f: d = json.load(f)
d['version'] = 'vX.Y.Z'
with open('.skillhub.json', 'w') as f: json.dump(d, f, indent=2, ensure_ascii=False)
"

# README.md — 更新 Version 行和 Current 段落
```

### Step 2: 更新 CHANGELOG

在 `# Changelog` 下方添加：

```markdown
## [vX.Y.Z] - YYYY-MM-DD

简短描述。

### Added
- ...

### Changed
- ...

### Fixed
- ...
```

### Step 3: 运行发布 gate

```bash
bash scripts/validate_release.sh
```

### Step 4: 提交

```bash
git add -A
git commit -m "Release vX.Y.Z: 简短描述"
```

### Step 5: 打 tag

```bash
git tag "vX.Y.Z"
```

### Step 6: 推送

```bash
git push origin main --tags
```

## 发布后验证

```bash
# 验证 tag
git tag -l "v*"

# 验证版本一致性
cat VERSION
python3 -c "import json; print(json.load(open('.skillhub.json'))['version'])"

# 验证 doctor
bash scripts/doctor.sh
```

## Hotfix 流程

当发布后发现紧急 bug：

1. 从 tag 创建 hotfix 分支：`git checkout -b hotfix/vX.Y.Z-1 vX.Y.Z`
2. 修复 bug
3. 更新版本号为 `vX.Y.Z-1`（patch + 1）
4. 运行 `bash scripts/validate_release.sh`
5. 提交、打 tag、推送
6. 合并回 main

## 文档同步检查

每次发布前确认以下链接/内容一致：

| 检查项 | 来源 | 目标 |
|--------|------|------|
| 版本号 | VERSION | .skillhub.json, README.md |
| 入口表 | SKILL.md | README.md, CHEATSHEET.md |
| 脚本列表 | scripts/ | README.md |
| 引用列表 | SKILL.md references 段 | references/ 目录实际文件 |
| CHANGELOG 条目 | CHANGELOG.md | 版本号 |

可用脚本自动检查：

```bash
bash scripts/doctor.sh  # 检查版本一致性
```

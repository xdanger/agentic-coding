# 文档标准检查器

本文档详细介绍了文档标准检查工具的使用方法和实现细节。该工具用于确保项目中的所有文档都遵循一致的文档标准。

## 1. 概述

文档标准检查工具是一个 Python 脚本，用于检查 Markdown 文档是否符合项目的文档标准规范（详见 `/docs/specs/documentation-standards.md`）。该工具可以检查文件命名、目录命名、文件引用格式、代码块格式和 Markdown 结构等多个方面的规范性。

## 2. 功能特点

该工具可以检查以下内容：

1. **文件命名规范**
   - 文件名应使用小写字母
   - 单词之间使用连字符(`-`)分隔，而非下划线或空格

2. **目录命名规范**
   - 目录名应使用小写字母
   - 单词之间使用连字符(`-`)分隔，而非下划线或空格
   - 集合类目录使用复数形式(如 `decisions`、`guides`、`debts`)

3. **文件引用格式**
   - 在文档中引用文件名或目录名时，使用反引号(`` ` ``)将其包围起来
   - 引用文件路径时，也应使用反引号

4. **代码块格式**
   - 代码块应指定语言
   - 纯文本代码区块必须使用 ```plaintext 而非仅使用```

5. **Markdown 结构**
   - 文档应以单个一级标题开始
   - 标题应遵循层次结构，不跳级使用
   - 使用 `-` 作为无序列表标记

## 3. 使用方法

### 3.1 基本使用

可以使用以下命令运行文档标准检查工具：

```bash
# 运行检查工具
python3 /utils/doc_linter.py
```

### 3.2 检查特定文件

可以使用 `--file` 参数指定要检查的文件：

```bash
# 检查特定文件
python3 /utils/doc_linter.py --file path/to/your/document.md
```

### 3.3 严格模式

在严格模式下，警告也会被视为错误，可以使用 `--strict` 参数开启严格模式：

```bash
# 严格模式
python3 /utils/doc_linter.py --strict
```

### 3.4 指定仓库根目录

可以使用 `--root` 参数指定仓库根目录：

```bash
# 指定仓库根目录
python3 /utils/doc_linter.py --root /path/to/your/repo
```

## 4. 自动化集成

### 4.1 GitHub Actions 集成

项目已配置 GitHub Actions 工作流，在每次推送或提交拉取请求时自动运行文档标准检查工具。工作流配置文件位于 `.github/workflows/documentation-lint.yml`。

当文档存在不符合规范的问题时，GitHub Actions 会显示失败，并提供详细的错误信息。

### 4.2 本地 Git 钩子

您可以将文档标准检查工具集成到本地 Git 钩子中，以便在提交前自动检查文档规范性。以下是一个示例 pre-commit 钩子：

```bash
#!/bin/bash

# 获取仓库根目录
REPO_ROOT=$(git rev-parse --show-toplevel)

# 获取暂存区中的 Markdown 文件
staged_md_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.md$')

if [ -n "$staged_md_files" ]; then
  echo "Running documentation linter on staged Markdown files..."

  # 对每个暂存区中的 Markdown 文件运行检查器
  for file in $staged_md_files; do
    python3 "$REPO_ROOT/utils/doc_linter.py" --file "$REPO_ROOT/$file"
    if [ $? -ne 0 ]; then
      echo "Documentation standards violations found. Please fix them before committing."
      exit 1
    fi
  done
fi

exit 0
```

## 5. 实现细节

文档标准检查工具使用 Python 实现，主要包含以下组件：

1. **文件查找**：使用 glob 模块查找所有 Markdown 文件
2. **规则检查**：针对每个文件应用多个规则检查
3. **报告生成**：汇总所有错误和警告，生成报告

核心检查逻辑包括：

- 使用正则表达式检查文件和目录命名
- 解析 Markdown 内容，检查文件引用格式
- 识别代码块，检查语言标签
- 分析文档结构，检查标题层级和列表样式

## 6. 维护和扩展

### 6.1 添加新规则

要添加新的检查规则，可以在 `DocumentationLinter` 类中添加新的检查方法，并在 `lint_file` 方法中调用该方法。

示例：

```python
def check_new_rule(self, file_path):
    """Check if the document follows the new rule."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 实现检查逻辑
    if some_condition:
        self.errors.append(f"New rule violation: {file_path}")

# 在 lint_file 方法中调用
def lint_file(self, file_path):
    self.files_checked += 1

    self.check_file_naming(file_path)
    # ... 其他检查
    self.check_new_rule(file_path)  # 新添加的规则
```

### 6.2 调整规则严格程度

可以通过修改检查方法，将错误降级为警告或将警告升级为错误，以调整规则的严格程度。

## 7. 常见问题

### 7.1 误报处理

如果检查工具报告了误报，可以考虑以下解决方案：

1. 完善检查逻辑，减少误报
2. 在特定情况下添加忽略规则
3. 对特定文件或目录添加豁免

### 7.2 编码问题

如果遇到编码问题，请确保文档使用 UTF-8 编码保存，并且检查工具在读取文件时使用正确的编码。

## 8. 相关资源

- [文档标准规范](/docs/specs/documentation-standards.md)
- [Python 正则表达式文档](https://docs.python.org/3/library/re.html)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

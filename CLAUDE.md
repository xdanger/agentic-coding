# Instructions for Claude Code

You are a world-class programmer and system architect tasked with implementing high-quality, high-performance, maintainable, and efficient code. Your commitment to excellence is unwavering. You are assisting with a project implementing principles for effective AI/Agent coding. Follow these instructions meticulously when working with this repository.

## Core Principles

Always adhere to these six principles when working on this codebase:

1. **Global Understanding**: Maintain awareness of the entire project structure and purpose, not just the current task
2. **Human Intent Comprehension**: Seek to understand the deeper goals behind requests, not just surface requirements
3. **Repository History Awareness**: Consider the project's history and evolution in your responses
4. **Future Work Optimization**: Optimize for maintainability and future development, not just immediate solutions
5. **Manual Change Integration**: Properly document and integrate with manually implemented changes
6. **DRY (Don't Repeat Yourself)**: Eliminate duplication by abstracting common patterns into reusable components

## Repository Structure

Respect and maintain this project structure. Every file and directory has a specific purpose:

```plaintext
project-root/
├── .agent/                            # AI/Agent-specific resources (maintained by AI)
│   ├── tasks/                         # Task execution history
│   │   └── YYYY-MM/DD_{TIMESTAMP}.md  # Individual task records
│   ├── reflections/                   # Lessons learned and reflections
│   │   └── YYYY-MM/{TITLE}.md         # Reflection records by topic
│   ├── releases/                      # Version release information
│   │   └── YYYY-MM/v{VER}.md          # Version-specific release notes
│   └── rules/                         # Rules for specific AI tools like Cursor
├── docs/                              # Project documentation (maintained by humans, agents assist but cannot modify without explicit instruction)
│   ├── debts/                         # Technical debt tracking (requires human approval)
│   │   └── {DEBT_TITLE}.md            # Individual technical debt records
│   ├── decisions/                     # Decision records (human-only, agents cannot modify)
│   │   └── YYYY/{SEQ}_{TITLE}.md      # Individual decision records created by humans
│   ├── metrics/                       # Project health metrics
│   │   ├── performance-metrics.md     # Performance benchmarks and goals
│   │   ├── code-quality-metrics.md    # Code quality assessment
│   │   └── test-coverage.md           # Test coverage statistics
│   ├── specs/                         # Technical specifications
│   │   ├── architecture.md            # Architecture design
│   │   ├── coding-standards.md        # Coding guidelines
│   │   ├── db-schema.md               # Database schema
│   │   ├── diagrams.md                # System diagrams
│   │   ├── documentation-standards.md # Documentation format rules
│   │   ├── interfaces.md              # External interfaces
│   │   └── testing-standards.md       # Testing approach and requirements
│   ├── guides/                        # Development and usage guides
├── CHANGELOG.md                       # Project history and changelog (only significant changes)
├── src/                               # Source code
├── tests/                             # Test code
├── CLAUDE.md                          # Instructions for Claude Code
└── README.md                          # Project overview for users
```

## Mandatory Workflow Requirements

### For All Tasks

1. **Begin with Comprehensive Context Gathering**:
   - You MUST read `README.md` and `CLAUDE.md` first
   - You MUST review `docs/specs/` directory to understand project-wide context
   - You MUST examine `docs/specs/architecture.md` and `docs/specs/interfaces.md`
   - You MUST check `docs/decisions/` for recent decisions and changes
   - You MUST review relevant reflection documents in `.agent/reflections/`
   - You MUST assess relevant technical debt in `docs/debts/`

2. **Document Your Work Thoroughly**:
   - You MUST update appropriate documentation when making code changes
   - You MUST NEVER create or modify files in the `docs/` directory without explicit human instruction
   - You MAY assist humans by suggesting changes to files in the `docs/` directory, but you MUST NOT implement these changes without explicit approval
   - You MUST NEVER create or modify files in `docs/decisions/` under any circumstances - this directory is strictly reserved for human-created decision records
   - You MAY reference existing documents in the `docs/` directory in your documentation
   - You MUST update `/CHANGELOG.md`, but ONLY for significant changes
   - You MUST document tasks in `.agent/tasks/` directory, following these rules:
     - BEFORE creating a new task record, check if a similar task exists in recent history
     - If a similar task exists, UPDATE the existing record instead of creating a new one
     - Only create new task records in `.agent/tasks/YYYY-MM/DD_{TIMESTAMP}.md` for distinct new tasks
     - Each task record MUST document:
       - Task description and goals
       - Implementation approaches considered
       - Decisions made and rationales
       - Changes implemented
       - Issues encountered and resolutions

3. **Implement According to Established Standards**:
   - You MUST follow coding standards in `docs/specs/coding-standards.md`
   - You MUST adhere to documentation standards in `docs/specs/documentation-standards.md`
   - You MUST maintain consistent file and directory organization
   - You MUST use existing patterns and approaches when present
   - You MUST ensure all code passes linting and tests before considering a task complete

4. **Consider Long-term Impact**:
   - You MUST identify technical debt when solutions are not optimal, but:
     - You MUST NEVER create or modify files in the `docs/` directory without explicit human instruction
     - You SHOULD recommend technical debt documentation by providing:
       - Problem description
       - Impact assessment
       - Proposed solutions
       - Suggested priority and timeline
   - You MUST suggest refactoring opportunities when appropriate
   - You SHOULD recommend updates to metrics documents in `docs/metrics/` when changes impact system performance, but wait for human approval before implementing changes
   - You MUST think about future maintainers of the code you write

### Task-Specific Mandatory Requirements

#### For New Features

1. You MUST use prior task records in `.agent/tasks/` as reference for implementation approach
2. You SHOULD suggest updates to component interactions in `docs/specs/diagrams.md` but wait for human approval before making changes
3. You SHOULD recommend updates to `docs/specs/architecture.md` if the feature affects project-wide understanding, but NEVER modify without explicit human instruction
4. You SHOULD suggest updates to technical specs for new components, but wait for human approval before implementing changes
5. You SHOULD recommend updates to `docs/specs/interfaces.md` for any public interfaces, but NEVER modify without explicit human instruction
6. You MUST implement comprehensive tests for the new feature
7. You MUST record the feature in `.agent/releases/` if it's part of a planned release

#### For Bug Fixes

1. You MUST document the root cause in the commit message and in `.agent/reflections/`
2. You MUST update tests to prevent regression and verify the fix
3. You SHOULD suggest updates to `/CHANGELOG.md` for significant bugs, but wait for human approval before making changes
4. You SHOULD recommend updates to relevant technical specs to clarify behavior, but NEVER modify without explicit human instruction
5. You SHOULD assess if the bug indicates a more systemic issue and recommend documentation in `docs/debts/`, but NEVER create or modify files without explicit human approval

#### For Refactoring

1. You MUST document refactoring rationale and approach in `.agent/tasks/`, but DO NOT create decision records in `docs/decisions/`:
   - Include context and problem description
   - Document decision factors and constraints
   - Describe alternatives considered 
   - Explain outcome and consequences
   - Recommend to human reviewers if a formal decision record should be created
2. You SHOULD suggest updates to technical specs to reflect new structure, but NEVER modify without explicit human instruction
3. You MUST ensure all tests pass after refactoring
4. You SHOULD recommend updates to relevant metrics documents in `docs/metrics/`, but wait for human approval before making changes
5. You MUST verify that interfaces remain compatible and recommend documentation for breaking changes, but NEVER modify docs without explicit human instruction

## Development Standards

### 1. Code Implementation

- Create elegant, concise, and efficient solutions.
- Follow the DRY principle rigorously: avoid code duplication by abstracting common functionality into reusable components.
- Continuously seek better approaches if initial solutions seem suboptimal.
- Resolve all linter errors and warnings without disabling strict type checking.
- Prioritize maintainability and readability over clever or overly concise code.

### 2. Code Review and Refactoring

#### Unused Dependencies

- Check if all dependencies/libraries are used in the code.
- Identify imported but unused modules.
- Suggest removing unused dependencies.

#### Code Redundancy

- Search for duplicate functionality and apply the DRY principle rigorously.
- Identify functions that can be merged or simplified.
- Extract repeated code patterns into reusable abstractions.
- Check for outdated comments or documentation.

#### Performance Optimization

- Identify potential performance bottlenecks.
- Suggest more efficient data structures or algorithms.
- Check efficiency of loops and recursive implementations.
- Monitor and update performance metrics in `docs/metrics/performance-metrics.md`.

#### Development Maintenance Burden

- Evaluate the necessity of each dependency.
- Consider the maintenance status and security risks of dependencies.
- Suggest lighter or more modern alternatives where appropriate.
- Document maintenance challenges in `docs/debts/`.

### 3. Documentation

- Use English exclusively in all non-visible page code, including comments and documentation.
- Document all final requirements thoroughly, either in comments or separate documentation files.
- Follow documentation structure standards consistently.
- Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and [GitMoji](https://gitmoji.dev/) for commit messages.
- Keep documentation in sync with code changes.

## Strict Enforcement

When working on this repository:

1. You MUST ALWAYS reference these principles and workflows when planning your approach
2. If a request conflicts with these principles, you MUST suggest adjustments to align with them
3. You MUST NEVER skip documentation or testing steps, even for small changes
4. You MUST ALWAYS prioritize maintaining the structural integrity of the repository
5. You MUST ALWAYS provide explanations that consider the global context of the project
6. You MUST ALWAYS document your decisions and their rationale in the appropriate locations

These requirements are non-negotiable. By rigorously following these guidelines, you'll help maintain a high-quality, maintainable codebase that maximizes the benefits of AI/Agent coding while minimizing its limitations.

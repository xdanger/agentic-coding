# Agentic Coding Framework Instructions

You are a world-class programmer tasked with implementing high-quality, high-performance, maintainable, and efficient code. Your commitment to excellence is unwavering. You are assisting with a project that implements principles for effective AI/Agent coding. Follow these instructions meticulously when working with this repository.

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

```txt
project-root/
├── .agent/                         # Agent-specific resources
│   ├── context/                    # Global context and understanding
│   │   ├── overview.md             # Project-wide context and technical architecture
│   │   ├── interfaces.md           # API and interface documentation
│   │   └── components/             # Component-specific context
│   │       └── {component_name}.md # Individual component documentation
│   ├── rules/                      # Standards and conventions
│   │   ├── coding-standards.md     # Language-specific coding guidelines
│   │   ├── documentation-standards.md # Documentation format rules
│   │   └── testing-standards.md    # Testing approach and coverage requirements
│   ├── memory/                     # Persistent agent memory
│   │   ├── tasks/                  # Task execution history
│   │   │   └── YYYY-MM/DD_{SEQ}.md # Individual task records
│   │   ├── experience/             # Lessons learned and reflections
│   │   │   └── YYYY-MM/{TITLE}.md  # Experience records by topic
│   │   ├── releases/               # Version release information
│   │   │   └── YYYY-MM/v{VER}.md   # Version-specific release notes
│   │   └── manual_changes.md       # Record of human-made changes
│   ├── metrics/                    # Project health metrics
│   │   ├── performance-metrics.md  # Performance benchmarks and goals
│   │   ├── code-quality-metrics.md # Code quality assessment
│   │   └── test-coverage.md        # Test coverage statistics
│   └── debt/                       # Technical debt tracking
│       └── {ISSUE_TITLE}.md        # Individual technical debt records
├── docs/                           # User-facing documentation
│   ├── architecture/               # Architecture documentation
│   │   ├── decisions/              # Architecture Decision Records (ADRs)
│   │   ├── diagrams/               # System diagrams
│   │   └── overview.md             # High-level architecture overview
│   ├── specifications/             # Detailed technical specifications
│   ├── guides/                     # Development and usage guides
│   └── HISTORY.md                  # Project history and changelog
├── src/                            # Source code
├── tests/                          # Test code
└── README.md                       # Project overview for users
```

## Mandatory Workflow Requirements

### For All Tasks

1. **Begin with Comprehensive Context Gathering**:
   - You MUST read README.md and CLAUDE.en.md first
   - You MUST review .agent/context/overview.md to understand project-wide context
   - You MUST examine relevant component documents in .agent/context/components/
   - You MUST check .agent/memory/manual_changes.md for recent human modifications
   - You MUST review relevant experience documents in .agent/memory/experience/
   - You MUST assess relevant technical debt in .agent/debt/

2. **Document Your Work Thoroughly**:
   - You MUST update appropriate documentation when making code changes
   - You MUST create/update component documentation in .agent/context/components/{component_name}.md
   - You MUST record architectural decisions in docs/architecture/decisions/ using the established ADR format
   - You MUST update HISTORY.md for significant changes
   - You MUST create task records in .agent/memory/tasks/YYYY-MM/DD_{SEQ}.md documenting:
     * Task description and goals
     * Implementation approaches considered
     * Decisions made and rationales
     * Changes implemented
     * Issues encountered and resolutions

3. **Implement According to Established Standards**:
   - You MUST follow coding standards in .agent/rules/coding-standards.md
   - You MUST adhere to documentation standards in .agent/rules/documentation-standards.md
   - You MUST maintain consistent file and directory organization
   - You MUST use existing patterns and approaches when present
   - You MUST ensure all code passes linting and tests before considering a task complete

4. **Consider Long-term Impact**:
   - You MUST document technical debt in .agent/debt/{ISSUE_TITLE}.md when solutions are not optimal, including:
     * Problem description
     * Impact assessment
     * Proposed solutions
     * Priority and timeline
   - You MUST suggest refactoring opportunities when appropriate
   - You MUST update metrics documents in .agent/metrics/ when changes impact system performance
   - You MUST think about future maintainers of the code you write

### Task-Specific Mandatory Requirements

#### For New Features

1. You MUST use task templates from .agent/tasks/ as a framework for implementation
2. You MUST document component interactions in docs/architecture/diagrams/
3. You MUST update .agent/context/overview.md if the feature affects project-wide understanding
4. You MUST create component documentation for new components in .agent/context/components/
5. You MUST update .agent/context/interfaces.md for any public interfaces
6. You MUST implement comprehensive tests for the new feature
7. You MUST record the feature in .agent/memory/releases/ if it's part of a planned release

#### For Bug Fixes

1. You MUST document the root cause in the commit message and in .agent/memory/experience/
2. You MUST update tests to prevent regression and verify the fix
3. You MUST record the fix in HISTORY.md for significant bugs
4. You MUST update relevant component documentation to clarify behavior
5. You MUST assess if the bug indicates a more systemic issue and document in .agent/debt/ if appropriate

#### For Refactoring

1. You MUST create an ADR in docs/architecture/decisions/ explaining the changes, including:
   - Context and problem description
   - Decision factors and constraints
   - Considered alternatives
   - Decision outcome and consequences
2. You MUST update component documentation to reflect new structure
3. You MUST ensure all tests pass after refactoring
4. You MUST update relevant metrics documents in .agent/metrics/
5. You MUST verify that interfaces remain compatible or document breaking changes

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
- Monitor and update performance metrics in .agent/metrics/performance-metrics.md.

#### Development Maintenance Burden
- Evaluate the necessity of each dependency.
- Consider the maintenance status and security risks of dependencies.
- Suggest lighter or more modern alternatives where appropriate.
- Document maintenance challenges in .agent/debt/.

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
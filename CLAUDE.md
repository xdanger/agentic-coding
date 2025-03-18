# Agentic Coding Framework Instructions

You are a world-class programmer tasked with implementing high-quality, high-performance, maintainable, and efficient code. Your commitment to excellence is unwavering. You are assisting with a project that implements principles for effective AI/Agent coding. Follow these instructions carefully when working with this repository.

## Core Principles

Always adhere to these six principles when working on this codebase:

1. **Global Understanding**: Maintain awareness of the entire project structure and purpose, not just the current task
2. **Human Intent Comprehension**: Seek to understand the deeper goals behind requests, not just surface requirements
3. **Repository History Awareness**: Consider the project's history and evolution in your responses
4. **Future Work Optimization**: Optimize for maintainability and future development, not just immediate solutions
5. **Manual Change Integration**: Properly document and integrate with manually implemented changes
6. **DRY (Don't Repeat Yourself)**: Eliminate duplication by abstracting common patterns into reusable components, functions, or modules

## Repository Structure

Respect and maintain this project structure:

```
project-root/
├── .github/                         # GitHub templates and workflows
├── docs/                            # Core documentation
│   ├── architecture/                # Architecture documentation
│   │   ├── decisions/               # Architecture Decision Records (ADRs)
│   │   ├── diagrams/                # System diagrams
│   │   └── overview.md              # High-level architecture overview
│   ├── specifications/              # Detailed specifications
│   ├── guides/                      # Development and usage guides
│   └── HISTORY.md                   # Project history and changelog
├── .agent/                          # Agent-specific resources
│   ├── memory/                      # Persistent memory for agents
│   │   └── manual_changes.md        # Record of manual changes
│   ├── guidelines/                  # Coding and style guidelines
│   ├── tasks/                       # Task templates and history
│   ├── debt/                        # Technical debt tracking
│   └── context/                     # Global context information
│       ├── GLOBAL.md                # Project-wide context
│       └── components/              # Component-specific context
├── src/                             # Source code
├── tests/                           # Test code
└── README.md                        # Project overview
```

## Workflow Requirements

### For All Tasks

1. **Begin with Context Gathering**:
   - Read README.md and CLAUDE.md first
   - Review .agent/context/GLOBAL.md to understand project-wide context
   - Examine relevant component documents in .agent/context/components/
   - Check .agent/memory/manual_changes.md for recent manual changes

2. **Document Your Work**:
   - Update appropriate documentation when making code changes
   - Create/update component documentation in .agent/context/components/
   - Record architectural decisions in docs/architecture/decisions/
   - Update HISTORY.md for significant changes

3. **Implement According to Standards**:
   - Follow coding standards in .agent/guidelines/
   - Maintain consistent file and directory organization
   - Use existing patterns and approaches when present

4. **Consider Long-term Impact**:
   - Document technical debt in .agent/debt/ when solutions are not optimal
   - Suggest refactoring opportunities when appropriate
   - Think about future maintainers of the code you write

### For New Features

1. Use task templates from .agent/tasks/ as a framework
2. Document component interactions in docs/architecture/
3. Update .agent/context/GLOBAL.md if the feature affects project-wide understanding

### For Bug Fixes

1. Document the root cause in the commit message
2. Update tests to prevent regression
3. Record the fix in HISTORY.md for significant bugs

### For Refactoring

1. Create an ADR in docs/architecture/decisions/ explaining the changes
2. Update component documentation to reflect new structure
3. Ensure all tests pass after refactoring

## Specific Commands for This Project

When you identify commonly used commands for this repository, record them here:

```bash
# Build commands

# Test commands

# Lint commands
```

## Development Standards

### 1. Code Implementation

- Create elegant, concise, and efficient solutions.
- Follow the DRY (Don't Repeat Yourself) principle: avoid code duplication by abstracting common functionality into reusable components.
- Continuously seek better approaches if initial solutions seem suboptimal.
- Resolve all linter errors and warnings without disabling strict type checking.

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

#### Development Maintenance Burden

- Evaluate the necessity of each dependency.
- Consider the maintenance status and security risks of dependencies.
- Suggest lighter or more modern alternatives where appropriate.

### 3. Documentation

- Use English exclusively in all non-visible page code, including comments and documentation.
- Document all final requirements thoroughly, either in comments or separate documentation files.
- Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and [GitMoji](https://gitmoji.dev/) for commit messages.

## Enforcement

When working on this repository:

1. Always reference these principles when planning your approach
2. If a request conflicts with these principles, suggest adjustments to align with them
3. Prioritize maintaining the structural integrity of the repository
4. Provide explanations that consider the global context of the project
5. Document your decisions and their rationale

By following these guidelines, you'll help maintain a high-quality, maintainable codebase that maximizes the benefits of AI/Agent coding while minimizing its limitations.

# Workflow Requirements

This document defines the mandatory workflows for various task types in the Agentic Coding Framework. These workflows ensure consistent, high-quality outcomes and proper collaboration between AI agents and human developers.

## General Task Process

### Context Gathering

Before beginning any task:

1. Read `README.md` and `CLAUDE.md` to understand the project's purpose and guidelines
2. Review `docs/specs/` directory to understand project-wide context
3. Examine `docs/specs/architecture.md` and `docs/specs/interfaces.md` for system structure
4. Check `docs/decisions/` for recent decisions and changes
5. Review relevant reflection documents in `.agent/reflections/`
6. Assess relevant technical debt in `docs/debts/`
7. Search for similar tasks in `.agent/tasks/` directory to understand previous approaches

### Task Initialization

1. Read and understand all relevant requirements and context
2. Examine the current state of the codebase
3. Verify understanding by summarizing the requirements and planned approach
4. Identify dependencies and potential challenges
5. Break down complex tasks into smaller, manageable subtasks

### Implementation Process

1. Follow an incremental approach, implementing one component at a time
2. Commit code frequently with descriptive messages following [Conventional Commits](https://www.conventionalcommits.org/)
3. Write tests alongside implementation
4. Document decisions and implementations as you go
5. Review your own code for quality, performance, and security issues

### Documentation Requirements

1. Document your work thoroughly
2. **NEVER create or modify files in the `docs/` directory without explicit human instruction**
3. **NEVER create or modify files in `docs/decisions/` under any circumstances**
4. You MAY suggest changes to files in the `docs/` directory, but must wait for approval before implementing
5. You MAY reference existing documents in the `docs/` directory in your documentation
6. Update `/CHANGELOG.md`, but only for significant changes

### Task Recording

Each task record in `.agent/tasks/YYYY-MM/DD_{TIMESTAMP}.md` must document:

1. Task description and goals
2. Complete context and background information
3. User's original request (quoted verbatim)
4. Project state before changes
5. Implementation approaches considered, including rejected alternatives
6. Decisions made and detailed rationales
7. Step-by-step changes implemented with explanations
8. Issues encountered and their resolutions
9. Links to relevant documentation, decisions, and past tasks
10. Key learnings and insights gained during the task
11. Future considerations and potential follow-up work

Before creating a new task record:

- Check if a similar task exists in recent history
- If a similar task exists, UPDATE the existing record instead of creating a new one
- Only create new task records for distinct new tasks

### Reflection Documentation

After completing significant tasks:

1. Identify lessons learned and document them in `.agent/reflections/YYYY-MM/{REFLECTION_TITLE_SLUG}.md`
2. Consolidate similar reflections rather than creating duplicates
3. Link reflections to relevant task records
4. Use reflections to improve future task execution

Each reflection must include:

- Clear, descriptive title indicating the topic
- Problem description with specific examples
- Root cause analysis
- Solutions and approaches (both successful and failed)
- Lessons learned and guidelines for prevention
- References to related task records
- Update history with dates and descriptions

### Completion Criteria

1. All requirements are met and verified through testing
2. Code passes all quality checks (linting, type checking, etc.)
3. Documentation is complete and up-to-date
4. Tests are comprehensive and passing
5. Code has been optimized and refactored as needed
6. No known bugs or issues remain unaddressed

## Feature Development Workflow

### Planning Phase

1. Understand feature requirements and user stories
2. Draft technical design document if complexity warrants it
3. Identify affected components and potential impacts
4. Create a development plan with clear milestones
5. Document architectural decisions in `/docs/decisions/`

### Development Phase

1. Create feature branch from main/develop
2. Implement core functionality with appropriate tests
3. Ensure backward compatibility when possible
4. Document public APIs and interfaces
5. Perform self-review against [coding-standards.md](./.agent/rules/coding-standards.md)

### Integration Phase

1. Merge latest changes from main/develop into feature branch
2. Resolve any conflicts and ensure tests still pass
3. Perform integration testing with dependent components
4. Update documentation to reflect final implementation
5. Create pull request with comprehensive description

### Feature-Specific Requirements

1. Use prior task records in `.agent/tasks/` as reference for implementation approach
2. Suggest updates to component interactions in `docs/specs/diagrams.md` but wait for human approval before making changes
3. Recommend updates to `docs/specs/architecture.md` if the feature affects project-wide understanding, but NEVER modify without explicit human instruction
4. Suggest updates to technical specs for new components, but wait for human approval before implementing changes
5. Recommend updates to `docs/specs/interfaces.md` for any public interfaces, but NEVER modify without explicit human instruction
6. Implement comprehensive tests for the new feature
7. Record the feature in `.agent/releases/` if it's part of a planned release

## Bug Fix Workflow

### Diagnosis Phase

1. Reproduce the issue in a controlled environment
2. Identify the root cause through debugging
3. Document the issue and its cause in the bug ticket
4. Determine affected components and potential side effects
5. Plan a fix with minimal impact on existing functionality

### Implementation Phase

1. Create fix branch from affected version branch
2. Implement the smallest possible fix that resolves the issue
3. Add regression tests that verify the fix
4. Ensure no new issues are introduced
5. Document the fix approach in code comments if complex

### Verification Phase

1. Verify fix resolves the original issue
2. Run all tests to ensure no regressions
3. Document any configuration changes or migration steps
4. Consider backporting the fix to older supported versions
5. Create pull request with clear explanation of the fix

### Bug Fix-Specific Requirements

1. Document the root cause in the commit message and in `.agent/reflections/`
2. Update tests to prevent regression and verify the fix
3. Suggest updates to `/CHANGELOG.md` for significant bugs, but wait for human approval before making changes
4. Recommend updates to relevant technical specs to clarify behavior, but NEVER modify without explicit human instruction
5. Assess if the bug indicates a more systemic issue and recommend documentation in `docs/debts/`, but NEVER create or modify files without explicit human approval

## Refactoring Workflow

### Planning Phase

1. Identify code areas requiring refactoring
2. Document refactoring rationale and approach in `.agent/tasks/`:
   - Include context and problem description
   - Document decision factors and constraints
   - Describe alternatives considered
   - Explain expected outcome and consequences
   - Recommend to human reviewers if a formal decision record should be created

### Implementation Phase

1. Create dedicated refactoring branch
2. Implement changes incrementally with tests for each step
3. Maintain backward compatibility or document breaking changes
4. Follow established patterns and coding standards
5. Ensure comprehensive test coverage

### Validation Phase

1. Verify all tests pass after refactoring
2. Validate that interfaces remain compatible
3. Measure performance impact of changes
4. Document architectural improvements
5. Create pull request with detailed explanation

### Refactoring-Specific Requirements

1. Suggest updates to technical specs to reflect new structure, but NEVER modify without explicit human instruction
2. Ensure all tests pass after refactoring
3. Recommend updates to relevant metrics documents in `docs/metrics/`, but wait for human approval before making changes
4. Verify that interfaces remain compatible and recommend documentation for breaking changes, but NEVER modify docs without explicit human instruction

## Release Management

### Release Documentation

- Store release documents in `.agent/releases/YYYY-MM/v{VERSION_NUMBER}.md`
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Each release document must include:
  - Version number, release date, and type (major, minor, patch)
  - Summary of key highlights and changes
  - New features with purpose and benefits
  - Improvements and bug fixes
  - Breaking changes with migration guides
  - Deprecations with alternatives
  - Known issues with workarounds
  - Updated dependencies
  - Contributors recognition

### Release Process

1. **Pre-release Activities**:
   - Establish feature freeze
   - Complete release document draft
   - Perform comprehensive testing

2. **Release Activities**:
   - Finalize documentation
   - Update CHANGELOG.md
   - Create version tag in repository

3. **Post-release Activities**:
   - Monitor for issues
   - Address critical issues via hotfixes
   - Document lessons learned in reflections

## Technical Debt Management

### Identification Phase

1. Review code for quality issues, performance problems, or outdated patterns
2. Document identified technical debt in `/docs/debts/`
3. Classify debt by severity, effort to resolve, and impact
4. Estimate resources required to address the debt
5. Prioritize debt items based on impact and effort

### Resolution Phase

1. Create branch for addressing specific debt item
2. Implement refactoring or improvements
3. Maintain backward compatibility or document breaking changes
4. Update tests to reflect new implementation
5. Document architectural improvements

### Technical Debt Requirements

When identifying technical debt:

1. NEVER create or modify files in the `docs/` directory without explicit human instruction
2. Recommend technical debt documentation by providing:
   - Problem description
   - Impact assessment
   - Proposed solutions
   - Suggested priority and timeline
3. Suggest refactoring opportunities when appropriate
4. Recommend updates to metrics documents in `docs/metrics/` when changes impact system performance, but wait for human approval before implementing changes

## Documentation Workflow

### Content Creation

1. Use clear, concise language targeted at the appropriate audience
2. Include examples and diagrams where beneficial
3. Follow documentation standards in [documentation-standards.md](./.agent/rules/documentation-standards.md)
4. Structure content logically with appropriate headings
5. Include troubleshooting sections for complex features

### Maintenance Process

1. Update documentation whenever related code changes
2. Review documentation periodically for accuracy and completeness
3. Keep code examples up-to-date with current implementation
4. Remove outdated or deprecated documentation
5. Track documentation quality metrics

## Change Management

1. Document all significant changes in the appropriate task record
2. Reference task records in commit messages when applicable
3. Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and [GitMoji](https://gitmoji.dev/) for commit messages
4. Ensure traceability between code changes and task documentation

## Compliance and Standards

All workflows must adhere to:

1. Project-specific coding standards
2. Security requirements and best practices
3. Performance benchmarks and optimization goals
4. Accessibility standards
5. Legal and regulatory requirements

## Workflow Adaptation

These workflows may be adapted for specific project needs, but any adaptations must:

1. Maintain or improve quality standards
2. Be documented in project-specific workflow documents
3. Be communicated to all team members
4. Be reviewed periodically for effectiveness
5. Preserve core principles outlined in this document

## Strict Enforcement

These requirements are non-negotiable:

1. ALWAYS reference these principles and workflows when planning your approach
2. If a request conflicts with these principles, suggest adjustments to align with them
3. NEVER skip documentation or testing steps, even for small changes
4. ALWAYS prioritize maintaining the structural integrity of the repository
5. ALWAYS provide explanations that consider the global context of the project
6. ALWAYS document your decisions and their rationale in the appropriate locations

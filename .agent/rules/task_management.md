# Agent Task Management Rules

## Task Recording Rules

1. **Task Consolidation**:
   - BEFORE creating a new task record, check if a similar task exists in recent history
   - If a similar task exists, UPDATE the existing record instead of creating a new one
   - Add an entry to the "Update History" section when updating an existing task
   - Only create new task records for distinct new tasks

2. **Task Classification**:
   - Use descriptive task types instead of color coding
   - Classify tasks as: Delegated, Collaborative, or Human-led
   - Include related task references when tasks are connected

3. **Record Format**:
   - Follow the standard template in IMPLEMENTATION.md
   - Ensure all sections are properly filled out
   - Keep task records updated with the latest information
   - Maintain an update history for tracking changes

## Repository Organization

1. **Directory Structure**:
   - Store task records in `.agent/tasks/YYYY-MM/DD_{TIMESTAMP}.md`
   - Store reflection documents in `.agent/reflections/YYYY-MM/{TITLE}.md`
   - Consolidate similar reflections rather than creating duplicates

2. **Change Management**:
   - Document all significant changes in the appropriate task record
   - Reference task records in commit messages when applicable
   - Ensure traceability between code changes and task documentation

These rules are designed to reduce duplication, improve knowledge management, and make task history more useful for both humans and agents.
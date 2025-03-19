#!/usr/bin/env python3

import os
import re
import glob
import argparse
from pathlib import Path

class DocumentationLinter:
    def __init__(self, root_dir=None):
        self.root_dir = root_dir or os.getcwd()
        self.errors = []
        self.warnings = []
        self.files_checked = 0
        self.rules_checked = 0
        
        # Files exempt from naming conventions (usually at root level)
        self.exempt_files = [
            "README.md", "CHANGELOG.md", "CLAUDE.md", "CLAUDE.zh.md", 
            "SOLUTIONS.en.md", "SOLUTIONS.zh.md"
        ]
        
        # Directories exempt from naming conventions
        self.exempt_dirs = [
            "2025"  # Year directories in decisions are allowed uppercase
        ]
        
        # File patterns that are exempt from certain checks
        self.exempt_patterns = {
            "underscore": [
                r"\d{3}_[a-z_]+\.md",  # Decision records like 001_project_structure_reorganization.md
                r"example_[a-z_]+\.md",  # Example files for demonstration purposes
                r"agent_collaboration\.md",  # Specific guide file
                r"documentation_linter\.md"  # This document
            ]
        }
    
    def find_markdown_files(self, pattern="**/*.md"):
        """Find all Markdown files in the repository."""
        return glob.glob(os.path.join(self.root_dir, pattern), recursive=True)
    
    def check_file_naming(self, file_path):
        """Check if file naming follows the convention (lowercase, hyphen-separated)."""
        filename = os.path.basename(file_path)
        
        # Skip exempt files (like README.md)
        if filename in self.exempt_files:
            return
        
        if not filename.islower():
            self.errors.append(f"File name should be lowercase: {file_path}")
        
        # Check if words are hyphen-separated (ignoring extension and special files)
        name_without_extension = os.path.splitext(filename)[0]
        if " " in name_without_extension:
            self.errors.append(f"File name contains spaces, use hyphens instead: {file_path}")
        
        # Check for underscores, but skip exempt patterns (like decision records)
        if "_" in name_without_extension and not filename.startswith("."):
            # Check if file matches any of the exempt patterns
            exempt_from_underscore = False
            for pattern in self.exempt_patterns.get("underscore", []):
                if re.match(pattern, filename):
                    exempt_from_underscore = True
                    break
            
            if not exempt_from_underscore:
                self.errors.append(f"File name contains underscores, use hyphens instead: {file_path}")
    
    def check_directory_naming(self, file_path):
        """Check if directory naming follows the convention (lowercase, hyphen-separated, plural for collections)."""
        dir_path = os.path.dirname(file_path)
        rel_path = os.path.relpath(dir_path, self.root_dir)
        
        # Skip the root directory
        if rel_path == ".":
            return
        
        # Check directory parts
        parts = rel_path.split(os.sep)
        for part in parts:
            if not part:
                continue
            
            # Skip exempt directories (like year directories)
            if part in self.exempt_dirs:
                continue
            
            if not part.islower():
                self.errors.append(f"Directory name should be lowercase: {part} in {dir_path}")
            
            if " " in part:
                self.errors.append(f"Directory name contains spaces, use hyphens instead: {part} in {dir_path}")
            
            if "_" in part and not part.startswith("."):
                self.errors.append(f"Directory name contains underscores, use hyphens instead: {part} in {dir_path}")
            
            # Check if collection directories use plural form
            collection_dirs = ["docs", "specs", "guides", "decisions", "debts", "metrics"]
            for collection in collection_dirs:
                if part == collection[:-1]:  # Singular form of a collection
                    self.warnings.append(f"Collection directory should use plural form: {part} should be {collection} in {dir_path}")
    
    def check_file_references(self, file_path):
        """Check if file references use backticks."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                # Try with a different encoding
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            except Exception as e:
                self.warnings.append(f"Could not read file {file_path} due to encoding issues: {str(e)}")
                return
            
        # Find potential file references outside of code blocks
        lines = content.split('\n')
        in_code_block = False
        line_number = 0
        
        for line in lines:
            line_number += 1
            
            # Check if entering or exiting a code block
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                continue
            
            if in_code_block:
                continue
            
            # Look for common directory names without backticks
            common_dirs = ["docs", "src", "tests", ".agent"]
            for common_dir in common_dirs:
                pattern = r'(?<![`\w])(' + re.escape(common_dir) + r'/)(?![`\w])'
                for match in re.finditer(pattern, line):
                    self.warnings.append(f"Directory reference should use backticks: {match.group(1)} at {file_path}:{line_number}")
            
            # Look for file extensions without backticks
            extension_pattern = r'(?<![`\w])(\.md|\.py|\.sh|\.js|\.ts)(?![`\w])'
            for match in re.finditer(extension_pattern, line):
                # Avoid false positives in URLs or other non-file contexts
                context_before = line[:match.start()].strip().split()[-1] if line[:match.start()].strip() else ""
                if not context_before.endswith(("http:", "https:", "www.", "ftp:")):
                    self.warnings.append(f"File extension reference should use backticks: {match.group(1)} at {file_path}:{line_number}")
    
    def check_code_blocks(self, file_path):
        """Check if code blocks specify a language, especially plaintext for text."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                # Try with a different encoding
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            except Exception as e:
                self.warnings.append(f"Could not read file {file_path} due to encoding issues: {str(e)}")
                return
        
        # Find code blocks
        in_code_block = False
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # Check if entering or exiting a code block
            if line.strip().startswith('```'):
                if not in_code_block:  # Start of code block
                    # Extract the language part after the opening ```
                    if line.strip() == '```':
                        self.errors.append(f"Code block doesn't specify a language, use ```plaintext for text: {file_path}:{i+1}")
                    else:
                        # Try to match with regex
                        match = re.match(r'^```(\w+)', line.strip())
                        if not match:
                            self.errors.append(f"Code block doesn't specify a language, use ```plaintext for text: {file_path}:{i+1}")
                in_code_block = not in_code_block
    
    def check_markdown_structure(self, file_path):
        """Check if Markdown structure follows the guidelines (heading levels, list style, etc.)."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                # Try with a different encoding
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            except Exception as e:
                self.warnings.append(f"Could not read file {file_path} due to encoding issues: {str(e)}")
                return
        
        lines = content.split('\n')
        heading_levels = []
        line_number = 0
        
        for line in lines:
            line_number += 1
            
            # Check heading levels
            if line.strip().startswith('#'):
                level = len(re.match(r'^(#+)', line.strip()).group(1))
                
                if not heading_levels:
                    # First heading should be level 1
                    if level != 1:
                        self.warnings.append(f"Document should start with a level 1 heading (# Title): {file_path}:{line_number}")
                else:
                    # Check for skipped levels, but allow nested heading patterns like 1 > 3 for things like 3.1, 3.2, etc.
                    # This is a common pattern in documentation
                    if level > heading_levels[-1] + 1 and not (level == 3 and heading_levels[-1] == 1 and '.' in line):
                        self.errors.append(f"Heading level skipped (from {heading_levels[-1]} to {level}): {file_path}:{line_number}")
                
                heading_levels.append(level)
            
            # Check list style
            if re.match(r'^\s*\*\s', line):
                self.warnings.append(f"Use - for list items instead of *: {file_path}:{line_number}")
    
    def lint_file(self, file_path):
        """Run all checks on a single file."""
        self.files_checked += 1
        
        self.check_file_naming(file_path)
        self.check_directory_naming(file_path)
        self.check_file_references(file_path)
        self.check_code_blocks(file_path)
        self.check_markdown_structure(file_path)
    
    def lint_all(self):
        """Lint all Markdown files in the repository."""
        files = self.find_markdown_files()
        for file_path in files:
            self.lint_file(file_path)
    
    def report(self):
        """Generate a report of the linting results."""
        if not self.errors and not self.warnings:
            return f"✅ All {self.files_checked} files passed documentation standards checks."
        
        report = []
        
        if self.errors:
            report.append("\n❌ ERRORS:")
            for error in self.errors:
                report.append(f"  - {error}")
        
        if self.warnings:
            report.append("\n⚠️ WARNINGS:")
            for warning in self.warnings:
                report.append(f"  - {warning}")
        
        report.append(f"\nChecked {self.files_checked} Markdown files.")
        report.append(f"Found {len(self.errors)} errors and {len(self.warnings)} warnings.")
        
        return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="Documentation Linter for Agentic Coding Framework")
    parser.add_argument("--root", default=os.getcwd(), help="Root directory of the repository")
    parser.add_argument("--file", help="Check a specific file instead of all files")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    
    args = parser.parse_args()
    
    linter = DocumentationLinter(root_dir=args.root)
    
    if args.file:
        linter.lint_file(args.file)
    else:
        linter.lint_all()
    
    print(linter.report())
    
    # Return error code
    if args.strict and (linter.errors or linter.warnings):
        return 1
    elif linter.errors:
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
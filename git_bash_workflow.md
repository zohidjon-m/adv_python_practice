# Git Bash Full Workflow Guide

This file provides a complete command sequence for working with Git Bash in practice.

---

## 1. Setup
```bash
# Configure identity (only once per computer)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Check config
git config --list
```

---

## 2. Create or Move to a Project Folder
```bash
# Create a folder
mkdir myproject

# Move inside
cd myproject
```

---

## 3. Initialize Git
```bash
# Start a new repository
git init
```

---

## 4. Create a File and Stage It
```bash
# Create a file
echo "# My First Project" > README.md

# Check repo status
git status

# Stage the file
git add README.md

# Or stage everything
git add .
```

---

## 5. Commit Changes
```bash
git commit -m "Initial commit with README"
```

---

## 6. Connect to GitHub
(Do this after creating a repo on GitHub)
```bash
git remote add origin https://github.com/username/myproject.git
```

---

## 7. Push Code
```bash
# First push
git branch -M main
git push -u origin main
```

---

## 8. Daily Workflow
```bash
# Check status
git status

# See history
git log --oneline --graph --decorate

# Make changes to file(s)
nano README.md    # or use any editor

# Stage and commit
git add .
git commit -m "Updated README with details"

# Push to GitHub
git push
```

---

## 9. Work with Branches
```bash
# Create and switch
git checkout -b feature-branch

# Edit files...
git add .
git commit -m "Added new feature"

# Push branch to GitHub
git push -u origin feature-branch

# Switch back to main
git checkout main
```

---

## 10. Get Updates
```bash
# Fetch latest changes
git pull
```

---

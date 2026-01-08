# Git Cheat Sheet

This file is a practical reference for everyday Git usage when working with local projects and GitHub.

---

## Recommended file nameing

- `git-cheat-sheet.md`

Lowercase, hyphen separated, and descriptive is common practice in repositories.

---

## Setup (run once per machine)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

git config --global core.autocrlf true   # recommended on Windows
```

Check config:

```bash
git config --global --list
```

---

## Create and publish a new repository

Initialize local repo and create first commit:

```bash
git init
git add .                 # stage all files in project
git commit -m "Initial commit"
```

Connect to GitHub and push:

```bash
git branch -M main        # ensure branch name is main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main   # push and set upstream
```

```bash
git init
git add .
git commit -m "Initial commit"

git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

---

## Daily workflow

Check current state of your working directory (what is modified, staged, or untracked):

```bash
git status
```

Stage files (add changes to the next commit):

```bash
git add file.py     # stage only one file
git add .           # stage ALL files in the current folder and subfolders
```

Commit staged changes with a short message:

```bash
git commit -m "Short clear message"
```

Push your commits to GitHub:

```bash
git push
```

Pull latest changes from GitHub and merge into your branch:

```bash
git pull
```

---

## Branches

List local branches (current branch has *):

```bash
git branch
```

Create and switch to a new branch:

```bash
git checkout -b feature-x
```

Switch to an existing branch:

```bash
git checkout main
```

Merge another branch into current branch:

```bash
git merge feature-x
```

Delete branch after merge:

```bash
git branch -d feature-x
```

Check status:

```bash
git status
```

Stage files:

```bash
git add file.py
git add .
```

Commit:

```bash
git commit -m "Short clear message"
```

Push:

```bash
git push
```

Pull latest changes:

```bash
git pull
```

---

## Branches

List branches:

```bash
git branch
```

Create and switch:

```bash
git checkout -b feature-x
```

Switch branch:

```bash
git checkout main
```

Merge branch into main:

```bash
git checkout main
git merge feature-x
```

Delete branch:

```bash
git branch -d feature-x
```

---

## Undo and recovery (very important)

Discard local changes in a file (before commit):

```bash
git restore file.py     # restore single file
git restore .           # restore ALL files to last commit
```

Unstage file (keep changes, just remove from staging area):

```bash
git restore --staged file.py
```

Undo last commit but keep files (commit message or staging mistake):

```bash
git reset --soft HEAD~1
```

Undo last commit and discard files (dangerous, permanent):

```bash
git reset --hard HEAD~1
```

Restore file exactly as it was in last commit:

```bash
git checkout -- file.py
```

Undo changes in file (before commit):

```bash
git restore file.py
git restore .
```

Unstage file:

```bash
git restore --staged file.py
```

Undo last commit but keep files:

```bash
git reset --soft HEAD~1
```

Undo last commit and discard files:

```bash
git reset --hard HEAD~1
```

Restore file from last commit:

```bash
git checkout -- file.py
```

---

## View history and changes

Commit history:

```bash
git log
git log --oneline --graph --decorate
```

Show changes:

```bash
git diff
git diff --staged
```

Show details of commit:

```bash
git show COMMIT_HASH
```

---

## Remote repositories

Show configured remotes:

```bash
git remote -v
```

Change remote URL (for example when switching GitHub accounts):

```bash
git remote set-url origin https://github.com/USERNAME/REPO.git
```

Remove remote completely:

```bash
git remote remove origin
```

Show remotes:

```bash
git remote -v
```

Change remote URL:

```bash
git remote set-url origin https://github.com/USERNAME/REPO.git
```

Remove remote:

```bash
git remote remove origin
```

---

## Clean working directory

Preview what will be deleted (safe):

```bash
git clean -n
```

Remove untracked files only:

```bash
git clean -f
```

Remove untracked files and folders (dangerous):

```bash
git clean -fd
```

Remove untracked files:

```bash
git clean -f
```

Remove untracked files and folders:

```bash
git clean -fd
```

Preview first:

```bash
git clean -n
```

---

## .gitignore basics

Create file:

```bash
touch .gitignore
```

Typical Python ignores:

```text
__pycache__/
*.pyc
.env
.venv/
```

---

## Emergency commands

Abort merge:

```bash
git merge --abort
```

Reset to remote state:

```bash
git fetch origin
git reset --hard origin/main
```

---

## Good commit message style

- Add python math examples
- Fix README file
- Refactor sorting logic
- Update folder structure

Avoid:

- update
- fix stuff
- changes

---

## Pro tips

- Commit often, small changes
- Push at least once per day
- Use branches for experiments
- Never be afraid to break things locally, Git can restore almost everything

---

If you want, you can later split this into:

- Git basics
- GitHub workflow
- Advanced recovery

and turn this repo into a learning resource as well.
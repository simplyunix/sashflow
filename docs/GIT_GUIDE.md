# Git Quick Reference Guide

A simple, practical guide for working with Git across multiple computers (Windows, Linux, etc.).

---

## 🧠 Core Idea

Git has **three places** your code can live:

1. **Working Folder** – Your actual files
2. **Local Repository** – Saved commits on your computer
3. **Remote Repository** – GitHub/GitLab/Bitbucket (the shared version)

You must move changes through all three stages to sync properly.

---

## 🔁 Daily Workflow (Any Computer)

### 1️⃣ Start Work — Get Latest Changes

Always do this first when opening a project on any machine:

```bash
git pull origin main
```

This downloads the newest version from the remote repo.

---

### 2️⃣ Make Your Changes

Edit files as needed.

Check what changed:

```bash
git status
```

---

### 3️⃣ Stage Changes (Prepare to Save)

Add all changed files:

```bash
git add .
```

Or add a specific file:

```bash
git add filename.py
```

---

### 4️⃣ Commit (Save a Snapshot)

```bash
git commit -m "Short description of changes"
```

Example:

```bash
git commit -m "Fixed login bug and improved error handling"
```

---

### 5️⃣ Push (Upload to Remote Repo)

```bash
git push origin main
```

Now your changes are backed up online and available on other computers.

---

## 💻 Setting Up a New Computer

### Clone the repository (only once per computer)

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

After this, follow the **Daily Workflow** steps above.

---

## 🌍 Working Between Two Computers

### Before leaving Computer A

```bash
git add .
git commit -m "Your message"
git push origin main
```

### When starting on Computer B

```bash
git pull origin main
```

**Golden Rule:**

> Push before you leave. Pull before you start.

---

## 🔎 Useful Commands

| Command                | What it Does               |
| ---------------------- | -------------------------- |
| `git status`           | Shows changed files        |
| `git diff`             | Shows line-by-line changes |
| `git add .`            | Stages all changes         |
| `git commit -m "msg"`  | Saves a commit             |
| `git push`             | Uploads commits to remote  |
| `git pull`             | Downloads latest changes   |
| `git log --oneline`    | Shows commit history       |
| `git restore filename` | Discards changes in a file |

---

## 🌿 Branching (Work on Features Safely)

Create a new branch:

```bash
git checkout -b feature-name
```

Switch branches:

```bash
git checkout main
```

Push a new branch to remote:

```bash
git push -u origin feature-name
```

---

## ⚠️ If Git Says There Is a Conflict

This happens if the same file was changed in two places.

1. Open the file Git mentions
2. Look for markers like this:

```
<<<<<<< HEAD
Your version
=======
Other version
>>>>>>> branch-name
```

3. Edit the file to keep what you want
4. Then run:

```bash
git add filename
git commit -m "Resolved merge conflict"
git push
```

---

## 🧹 Good Habits

✅ Commit often (small changes are best)
✅ Write clear commit messages
✅ Pull before starting work
✅ Push before switching computers

---

## 🆘 Undo Mistakes

Unstage a file:

```bash
git restore --staged filename
```

Undo changes in a file:

```bash
git restore filename
```

See previous commits:

```bash
git log --oneline
```

---

This guide covers the commands you will use 95% of the time. Master these and Git becomes easy.
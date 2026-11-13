<!-- 🌐 Language Switcher -->
<p align="center">
  <a href="./README_FA.md">
    <img src="https://badgen.net/badge/-/🔠%20مشاهده%20نسخه%20فارسی/purple?label=&scale=1.5" alt="Persian Version"/>
  </a>
</p>

<h1 align="center">🐍 Python Lab</h1>

<p align="center">
  A personal Python workspace for coding experiments, problem-solving, academic exercises, and independent projects — built through continuous learning and hands-on development.
</p>

<!-- 🏷️ Custom Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3-3776AB?style=plastic&labelColor=20232A&logo=python&logoColor=white" alt="Python 3"/>
  <img src="https://img.shields.io/badge/Code%20Style-PEP%208-4B8BBE?style=plastic&labelColor=20232A" alt="PEP 8"/>
  <img src="https://img.shields.io/badge/Commits-Semantic%20Commits-FE5196?style=plastic&labelColor=20232A&logo=git&logoColor=white" alt="Semantic Commit Messages"/>
  <img src="https://img.shields.io/badge/Branching-Feature%20Branch-6C63FF?style=plastic&labelColor=20232A&logo=git&logoColor=white" alt="Feature Branch Workflow"/>
  <img src="https://img.shields.io/badge/License-MIT-00A693?style=plastic&labelColor=20232A" alt="MIT License"/>
</p>

---

<a id="about"></a>
## 👋 About

**Python Lab** is my personal workspace for learning and exploring Python, experimenting with ideas, solving programming challenges, and building independent projects.

It brings together practical exercises, coding experiments, and personal projects in one place, with a focus on hands-on development, problem-solving, and continuous improvement.

<a id="table-of-contents"></a>
## 📑 Table of Contents

- [About](#about)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
  - [Branching Strategy](#branching-strategy)
  - [Commit Convention](#commit-convention)
  - [Code Guidelines](#code-guidelines)
  - [Pull Requests and Issues](#pull-requests-and-issues)
- [Projects](#projects)
- [License](#license)

<a id="repository-structure"></a>
## 📂 Repository Structure

Each project is maintained in its own directory, named after its purpose or functionality.

**General repository structure:**

```text
python-lab/
│
├── .github/
│   └── ISSUE_TEMPLATE/
│
├── <project-name>/
│   ├── main.py
│   └── README.md
│
├── .gitignore
├── LICENSE
├── README.md
└── README_FA.md
```

**To add a new project:**

1. Create a separate directory with a descriptive `kebab-case` name. Avoid numbering project directories.
2. Add `main.py` as the project entry point, where appropriate.
3. Include a `README.md` describing the project, its requirements, and how to run it.
4. Add more files and directories as needed based on the project's complexity.
5. Add the project name and a short description to the Projects section of this README.

<a id="contributing"></a>
## 🤝 Contributing

Suggestions, bug reports, and code contributions are welcome. To keep the repository consistent and maintainable, please follow these guidelines.

<a id="branching-strategy"></a>
### 🌿 Branching Strategy

This repository follows a lightweight **[Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)**.

- `main` is the primary branch and should always remain stable.
- Create a short-lived branch from the latest `main` for each change.
- Use `feature/` branches for new features, improvements, experiments, and documentation updates.
- Use `fix/` branches for bug fixes.
- Keep each branch focused on a single change and submit it through a Pull Request targeting `main`.
- Avoid pushing changes directly to `main`.
- Delete the working branch after its Pull Request has been merged.

**Branch naming examples:**

```text
feature/number-guessing-game
feature/update-documentation
fix/guess-validation
```

📚 [Feature Branch Workflow – Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)

<a id="commit-convention"></a>
### 📝 Commit Convention

Commit messages follow [Semantic Commit Messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716).

**Commit format:**

```text
<type>(<scope>): <subject>
```

- `type` identifies the kind of change and is required.
- `scope` identifies the affected project or area and is optional.
- `subject` provides a short, clear summary written in the present tense.

**Common types:**

| Type | Purpose |
|---|---|
| `feat` | Introduce a new feature |
| `fix` | Fix a bug |
| `docs` | Update documentation |
| `style` | Formatting changes without affecting functionality |
| `refactor` | Restructure code without adding a feature or fixing a bug |
| `test` | Add or update tests |
| `chore` | Maintenance and supporting tasks |

**Examples:**

```bash
feat(number-guessing-game): add random number generation
feat(number-guessing-game): limit guesses to ten attempts
fix(number-guessing-game): handle invalid user input
docs(number-guessing-game): update usage instructions
chore(license): add MIT license
```

<a id="code-guidelines"></a>
### 🐍 Code Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) coding conventions.
- Use clear and descriptive names for variables, functions, and classes.
- Keep functions focused and implementations easy to understand.
- Handle invalid inputs and expected errors appropriately.
- Avoid unnecessary dependencies and document required packages.
- Keep project documentation up to date.

<a id="pull-requests-and-issues"></a>
### 📬 Pull Requests and Issues

- Keep each Pull Request focused on a specific change.
- Explain what changed and why.
- Include relevant testing details.
- Use the available Issue templates for bug reports and feature requests.
- Submit feature and bug-fix Pull Requests to `main`.

<a id="projects"></a>
## 🚀 Projects

Projects in this repository focus on practical development, experimenting with ideas, and improving programming skills.

| Project | Description |
|---|---|
| 🎯 [Number Guessing Game](./number-guessing-game/) | Guess a randomly selected number within 10 attempts, with hints indicating whether the next guess should be higher or lower. |

<a id="license"></a>
## 📄 License

This repository is licensed under the [MIT License](./LICENSE).

See the `LICENSE` file for details.

---

<p align="center">
  Made with ❤️ by
  <a href="https://github.com/mohammad-moein-latifi"><strong>Mohammad Moein Latifi</strong></a>
</p>

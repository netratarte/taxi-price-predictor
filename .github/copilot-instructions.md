## Repo status and first steps

- This repository currently contains no source files or config (empty workspace). Before making large changes, confirm with the human what the intended language/stack is (examples: Python ML, Node.js API, FastAPI, Flask, or a full-stack React+Node app).

## What you (an AI coding agent) should do first

1. Run a workspace scan and list top-level files. If the repo is empty, ask the user one clarifying question: "Do you want me to scaffold a project? If so, which language and purpose (model training, API/service, web frontend, or data analysis notebook)?".
2. If the user asks to scaffold, propose a minimal layout and the exact files you'll add. Wait for confirmation before creating files.

## If scaffolding is requested — minimal, conservative default

- Preferred default (if user doesn't specify): Python data/ML repo laid out as:
  - `pyproject.toml` or `requirements.txt`
  - `src/` package (module code)
  - `notebooks/` for exploration
  - `data/` (gitignored) and `data/README.md` describing expected inputs
  - `tests/` with pytest configuration
  - `Dockerfile` and `.github/workflows/ci.yml` for CI (optional, ask first)

## Conventions & patterns to follow in this workspace

- Use small, focused commits that add one logical unit (API route, model, test) at a time.
- Put executable scripts in `src/` and keep notebooks in `notebooks/` only for exploration.
- Add `data/` to `.gitignore` and include a `data/README.md` that documents sources and schema.

## Development and verification steps (documented for maintainers)

- Use PowerShell on Windows (user default). When adding run instructions, provide PowerShell-safe commands.
- If creating a Python project, include a short `README.md` with commands to create a virtual environment, install dependencies, run tests, and start the app.

## Safety and repository hygiene

- Do not add secrets, credentials, or real dataset files. Add `.gitignore` entries and `README` notes about credentials and data access.

## When to ask the user for guidance

- Always ask before: choosing a tech stack, adding CI workflows, committing large binary/data files, or making breaking changes to an existing project structure.

## Example prompts and snippets (use these exact phrasing when asking)

- "This repo is empty — would you like me to scaffold a [Python/Node/Full-stack] project for a taxi-price prediction service, or do you already have files to add?"
- If the user approves scaffolding Python: "I will create `pyproject.toml`, `src/`, `notebooks/`, `tests/`, `Dockerfile`, and `.github/workflows/ci.yml`. Confirm?"

## Merge rules (if this file already exists)

- Preserve any existing high-value instructions or code snippets. Add only missing, up-to-date guidance. Prefer merging short, actionable lines rather than rewriting user-authored policies.

---
If anything in this file is unclear or you'd like a different default stack, tell me what you prefer and I'll update the instructions and scaffold accordingly.

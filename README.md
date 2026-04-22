# FLL Pybricks Robot Codebase

This repository contains the robot codebase for our FIRST LEGO League (FLL) team using **Pybricks + Python**.

It is designed to be:
- Easy to set up on Mac and Windows
- Structured for team collaboration
- Scalable for the full competition season

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Create and activate a virtual environment

We use **Python virtual environments (`venv`)** and **do not use conda** for this project.

#### Mac

```bash
python3 -m venv pyb
source pyb/bin/activate
```

#### Windows

```bash
python -m venv pyb
pyb\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify installation

```bash
python -c "from pybricks.hubs import PrimeHub; print('Pybricks OK')"
```

If that prints `Pybricks OK`, your machine is ready.

---

## One-Time Robot Setup

Before running code locally, install **Pybricks firmware** on the hub.

1. Open `https://code.pybricks.com`
2. Connect the hub via USB
3. Install Pybricks firmware
4. Give the hub a clear name such as `PrimeHub1`

**Important:** Do **not** pair the hub through macOS or Windows Bluetooth settings. Connect through Pybricks instead.

---

## Running Code on the Robot

From the project root:

```bash
pybricksdev run ble src/main.py
```

Or specify the hub name:

```bash
pybricksdev run ble --name "PrimeHub1" src/main.py
```

---

## Running the Hub Position Test Harness

The hub position test harness is used to evaluate different hub placements on the robot and compare stability, drift, repeatability, and attachment clearance.

Run it with:

```bash
pybricksdev run ble src/tests/hub_position_test.py
```

Use the test results template in `docs/test_results_template.md` to record observations.

---

## Recommended Folder Structure

```text
fll-pybricks/
├── README.md
├── requirements.txt
├── .gitignore
├── .vscode/
│   ├── settings.json
│   └── tasks.json
├── src/
│   ├── main.py
│   ├── robot/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── drive.py
│   │   └── utils.py
│   ├── missions/
│   │   ├── __init__.py
│   │   └── mission_template.py
│   └── tests/
│       ├── __init__.py
│       └── hub_position_test.py
├── docs/
│   └── test_results_template.md
└── scripts/
    └── run.sh
```

---

## What Goes Where

### `src/main.py`
Entry point for the robot. This should remain stable and call whichever mission or test you want to run.

### `src/robot/`
Reusable robot code:
- motor and port definitions
- drive base setup
- helper utilities
- calibration values

### `src/missions/`
Competition mission programs and mission sequencing.

### `src/tests/`
Experimental programs and validation harnesses, including the hub position test harness.

### `docs/`
Reference documents, setup notes, and observation sheets.

---

## Suggested Starter Files

### `requirements.txt`

```txt
pybricks
pybricksdev
```

### `.gitignore`

```gitignore
pyb/
.venv/
__pycache__/
*.pyc
.DS_Store
.vscode/*.log
```

### `.vscode/settings.json`

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/pyb/bin/python",
  "python.analysis.extraPaths": [
    "${workspaceFolder}/src"
  ],
  "files.exclude": {
    "**/__pycache__": true
  }
}
```

If you choose a different venv name, update the interpreter path accordingly.

### `.vscode/tasks.json`

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run main.py on hub",
      "type": "shell",
      "command": "${workspaceFolder}/pyb/bin/pybricksdev",
      "args": [
        "run",
        "ble",
        "--name",
        "PrimeHub1",
        "${workspaceFolder}/src/main.py"
      ],
      "problemMatcher": []
    }
  ]
}
```

On Windows, this command path may need to be adjusted to the executable inside `pyb\\Scripts\\`.

---

## Team Setup Instructions

Each new contributor should follow this sequence:

1. Clone the repository
2. Create a local `venv`
3. Install dependencies from `requirements.txt`
4. Select the project interpreter in VS Code
5. Restart the Python language server if imports look broken
6. Verify the hub has Pybricks firmware installed
7. Run a small test before making larger changes

---

## VS Code Notes

If VS Code shows import warnings such as `cannot import pybricks.hubs`, check the following:

1. The correct virtual environment is selected
2. `pybricks` is installed in that environment
3. VS Code has been reloaded
4. The Python language server has been restarted

Useful checks from the VS Code terminal:

```bash
which python
python -m pip show pybricks
python -m pip show pybricksdev
```

On Windows, use:

```bash
where python
python -m pip show pybricks
python -m pip show pybricksdev
```

---

## Common Problems

### Import errors in VS Code
Usually caused by the wrong interpreter being selected or Pybricks not being installed in the active environment.

### Robot does not connect
- Make sure the hub is on
- Make sure the hub name is correct
- Do not pair through the OS Bluetooth settings
- Confirm Pybricks firmware is installed

### Running the wrong way from VS Code
Do not rely on the default Python run button for robot execution. Use `pybricksdev` or a VS Code task configured to call `pybricksdev`.

---

## Development Guidelines

- Keep `main.py` small and clean
- Put reusable logic in `robot/`
- Put experiments in `tests/`
- Move proven code into reusable modules
- Change one thing at a time during testing
- Record observations during physical testing

---

## Team Workflow

Recommended workflow:
- create a branch for each experiment or feature
- test code in `src/tests/`
- promote stable logic into `src/robot/`
- keep mission code separate from low-level robot code
- document test results in `docs/`

---

## Project Goal

The goal of this repository is to help the team build:
- a reliable base robot
- repeatable navigation
- modular attachments
- testable design decisions
- clean, maintainable code throughout the season

---

## Next Improvements

Some good next steps for this repository:
- add a shared gyro drive module
- add a calibration script
- add a mission launcher
- add attachment test harnesses
- add logging and debugging utilities
- add a standard experiment scoring sheet

# 🔍 Code Auto Reviewer

A Python-based static code analysis tool that automatically reviews Python source files and generates a detailed code review report.

The project is built step by step using Python's built-in `ast` module and is designed to analyze different aspects of Python code such as syntax, code quality, functions, complexity, and basic security issues.

---

## 🚀 Features

Currently, the project supports:

* ✅ Python syntax checking
* 🔍 Basic code quality analysis
* 🔧 Function analysis
* 🧠 Complexity analysis
* 🔐 Basic security checks
* 📊 Automatic code quality scoring
* 📄 HTML report generation

---

## 🛠️ Technologies Used

* Python 3
* Abstract Syntax Tree (`ast`)
* HTML
* CSS

The project currently uses only Python's standard library and does not require any external Python packages.

---

## 📁 Project Structure

```text
Code Auto Reviewer/
│
├── app.py
├── report.html
│
└── reviewer/
    ├── __init__.py
    ├── syntax_checker.py
    ├── quality_checker.py
    ├── function_analyzer.py
    ├── complexity_analyzer.py
    ├── security_checker.py
    ├── report.py
    └── html_report.py
```

---

## 🔎 How It Works

The application follows a simple analysis pipeline:

```text
Python Source File
        │
        ▼
   Syntax Checker
        │
        ▼
   Quality Checker
        │
        ▼
 Function Analyzer
        │
        ▼
Complexity Analyzer
        │
        ▼
 Security Checker
        │
        ▼
   Score Generator
        │
        ▼
   HTML Report
```

---

# 📌 Current Modules

## 1. Syntax Checker

The syntax checker uses Python's built-in `ast` module to determine whether the source code contains valid Python syntax.

It detects:

* Syntax errors
* Error line
* Error column
* Error message
* Missing files

Example:

```text
❌ Syntax Error
Line: 5
Column: 10
Message: invalid syntax
```

---

## 2. Code Quality Checker

The quality checker performs basic static analysis of the source code.

Currently, it detects overly generic variable names such as:

```python
x = 10
y = 20
z = x + y
```

The tool reports these names as potential code quality issues.

Example:

```text
⚠️ Line 1: Variable name 'x' is too generic.
```

---

## 3. Function Analyzer

The function analyzer detects Python functions and collects basic information about them.

For each function, it reports:

* Function name
* Starting line
* Number of parameters
* Number of lines

Example:

```text
Function: calculate_total
Line: 10
Parameters: 3
Lines: 8
```

It also warns about functions that:

* Have more than 5 parameters
* Are longer than 20 lines

---

## 4. Complexity Analyzer

The complexity analyzer provides an educational approximation of cyclomatic complexity.

It analyzes structures such as:

* `if`
* `for`
* `while`
* `and`
* `or`

Example:

```text
Function: calculate
Complexity: 7

⚠️ Medium complexity
```

The current implementation is intentionally simple and is not intended to be a complete professional cyclomatic complexity implementation.

---

## 5. Security Checker

The security checker looks for some potentially dangerous patterns.

Currently, it checks for:

### `eval()`

```python
eval(user_input)
```

### `exec()`

```python
exec(user_input)
```

### Possible hard-coded secrets

```python
password = "123456"
```

Example output:

```text
Line: 15
Severity: HIGH
⚠️ Use of eval() can be dangerous.
```

> Note: These checks are heuristic-based and should not be considered a complete security audit.

---

# 📊 Code Scoring

The application calculates an overall score starting from:

```text
100 / 100
```

Points are deducted based on detected issues.

Examples:

* Invalid syntax → -30
* Quality issue → -5
* Security issue → -10
* Medium complexity → -5
* High complexity → -10

The final score is displayed as:

```text
⭐ Overall Score: 85/100
```

---

# 📄 HTML Report

The project can generate a browser-friendly HTML report.

The report contains:

* Overall score
* Syntax status
* Code quality issues
* Security issues
* Function information

The generated file is:

```text
report.html
```

You can open it directly in a web browser.

---

# ▶️ How to Run

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/code-auto-reviewer.git
```

Then enter the project directory:

```bash
cd code-auto-reviewer
```

---

## 2. Run the application

```bash
python app.py
```

The application will ask for the path to a Python file:

```text
Enter Python file path:
```

For example:

```text
E:\python_work\Code Auto Reviewer\test.py
```

Or, if the test file is inside the project:

```text
test.py
```

---

# 🧪 Example

Suppose we have the following Python file:

```python
def calculate(x, y):
    password = "123456"

    if x > 10:
        return eval(y)

    return x + y
```

The Code Auto Reviewer may detect:

```text
🔍 Code Auto Reviewer

Syntax       ✅ PASS
Quality      ⚠️ Issues
Functions    ✅ 1 Found
Complexity   ⚠️ Issues
Security     🔴 Issues

⭐ Overall Score: 70/100
```

An HTML report will also be generated:

```text
report.html
```

---

# 🧠 Project Architecture

The project separates different responsibilities into independent modules.

```text
app.py
   │
   ├── syntax_checker.py
   ├── quality_checker.py
   ├── function_analyzer.py
   ├── complexity_analyzer.py
   ├── security_checker.py
   ├── report.py
   └── html_report.py
```

`app.py` acts as the main orchestrator.

Each analyzer is responsible for one specific part of the code review process.

This makes the project easier to:

* Understand
* Maintain
* Test
* Extend

---

# 📜 License

This project is currently available for educational purposes.

A formal open-source license can be added later.

````

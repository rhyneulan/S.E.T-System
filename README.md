# S.E.T. SYSTEM — Student Expense Tracker System

A simple command-line-based **Student Expense Tracker System (SETSY)** developed using Python.

The system is designed to help students manage their monthly budgets, record expenses, categorize spending, monitor their remaining balance, and receive warnings when their expenses approach or exceed their allocated budget.

All financial records are stored locally using text files, so the system does not require an external database.

## 📌 Overview

The **S.E.T. SYSTEM (Student Expense Tracker System)** provides a simple terminal-based solution where users can:

- Create and manage monthly budgets.
- Allocate budgets to different expense categories.
- Record daily expenses.
- Monitor remaining category balances.
- View total expenses and budget summaries.
- Track spending patterns through expense reports.
- Receive warnings when approaching or exceeding budget limits.
- View transaction history.
- Reset budgets and expenses when necessary.

The application runs directly in the terminal or command prompt and uses local `.txt` files for data storage.

## ✨ Features

### 💰 Budget Management

Users can allocate a specific budget to different expense categories based on their financial needs.

The system allows users to:
- Add a budget to a selected category.
- Monitor allocated budgets.
- View the total monthly budget.
- Check remaining balances for each category.

### 💸 Expense Tracking

Users can record expenses by selecting a category and entering the corresponding amount and description.

Before an expense is recorded, the system checks the available budget for the selected category.

If the expense exceeds the remaining category budget, the system displays an insufficient-budget warning.

Otherwise:
- The expense is recorded.
- The category's remaining budget is updated.
- The total spending is recalculated.
- The transaction is saved in the logs.

### 📂 Expense Categories

Every recorded expense is assigned to a specific category.

Available categories:

1. Foods
2. Bills
3. Transportation
4. Entertainment
5. Health
6. Supplies
7. Shopping

### 📋 Transaction Logs

The system maintains a transaction history containing recorded budget and expense activities.

Each transaction includes relevant information such as:
- Date and time.
- Transaction type.
- Expense category.
- Amount.
- Description, when applicable.

Transaction records are stored locally in `logs.txt`.

### 📊 Expense Summary Reports

The system provides reports to help users understand their financial activities.

Reports include:
- Total allocated budget.
- Total expenses.
- Remaining budget.
- Expense breakdown by category.
- Monthly spending summaries.
- Transaction history.

### ⚠️ Budget Monitoring and Warning Alerts

The system monitors expenses against allocated category budgets.

It identifies categories that are approaching or exceeding their budget limits.

The expense analysis provides warnings when:
- A category is nearing its budget limit.
- The allocated budget has been fully used.
- Expenses exceed the allocated budget.

### 🧹 Data Management Tools

The system provides tools for managing stored financial records.

Available operations include:
- Clearing transaction logs.
- Resetting budgets.
- Resetting recorded expenses.

Confirmation is required before performing destructive operations.

### 🎨 Terminal Formatting

The project uses the **Rich Python package** to display organized tables, formatted text, and improved terminal output.

## 🖥️ System Requirements

Before running the project, make sure you have:

- Python 3.10 or later.
- pip (Python package installer).
- Git (only required if cloning the repository).
- Windows Command Prompt or PowerShell, or another compatible terminal.
- Rich Python package.

The project also uses Python standard-library modules, which are included with Python and do not need to be installed separately.

The external Python package required is:

```bash
rich
```

## 📦 Project Structure

```text
S.E.T-System-Student-Expense-Tracker/
│
├── main.py
├── category.py
├── set_value.py
├── monthly.py
├── tracker.py
├── report.py
├── analysis.py
├── logs.py
├── table_view.py
├── cleaner.py
│
├── monthly.txt
└── logs.txt
```

### File Description

| File | Description |
|---|---|
| `main.py` | Main entry point and menu system. |
| `category.py` | Handles expense category selection. |
| `set_value.py` | Handles budget allocation and expense recording. |
| `monthly.py` | Manages monthly budget and expense records. |
| `tracker.py` | Handles monthly expense tracking and summaries. |
| `report.py` | Generates expense reports and transaction history. |
| `analysis.py` | Handles budget comparisons and spending analysis. |
| `logs.py` | Manages transaction logs. |
| `table_view.py` | Displays formatted tables in the terminal. |
| `cleaner.py` | Handles terminal screen clearing. |
| `monthly.txt` | Stores monthly budget and expense information. |
| `logs.txt` | Stores transaction history. |

## 🚀 Installation

### 1. Clone the Repository

Open Command Prompt or PowerShell.

```bash
git clone https://github.com/rhyneulan/S.E.T-System
```

Enter the project directory:

```bash
cd S.E.T-System-Student-Expense-Tracker
```

If you downloaded the project as a ZIP file, you can skip the `git clone` command and open the extracted project folder directly.

### 2. Create a Virtual Environment

```bash
python -m venv setsy
```

### 3. Activate the Virtual Environment

For Windows Command Prompt:

```bash
setsy\Scripts\activate
```

For Windows PowerShell:

```powershell
.\setsy\Scripts\Activate.ps1
```

After activation, you should see:

```text
(setsy)
```

at the beginning of your command line.

### 4. Install the Required Package

```bash
pip install rich
```

## ▶️ Running the Program

After installing the requirements and activating the virtual environment, run:

```bash
python main.py
```

The program will display the S.E.T. SYSTEM main menu.

## 🧭 How to Use the System

### Option 1 — Add Budget

Select the budget management option.

Choose an expense category and enter the amount you want to allocate.

The system updates the selected category's budget.

### Option 2 — Enter Expense

Select the expense recording option.

Enter the expense amount, choose a category, and provide the required description.

If the expense is within the available category budget:

- The expense is recorded.
- The remaining category budget is updated.
- The total spending is recalculated.
- The transaction is saved in the logs.

If the expense exceeds the available budget, the system displays an insufficient-budget warning.

### Option 3 — View Expense Summary Report

Select the report option to view financial summaries.

Available information includes:
- Total expenses.
- Total allocated budget.
- Remaining budget.
- Spending by category.
- Monthly expense records.
- Transaction history.

### Option 4 — Tools

Select the tools option to manage stored financial records.

Depending on the selected operation, users can:
- Clear transaction logs.
- Reset allocated budgets.
- Reset recorded expenses.

Follow the confirmation prompts before proceeding with these operations.

### Option 0 — Exit

Select the exit option to close the application.

## 💾 Data Storage

S.E.T. SYSTEM uses local text files instead of an external database.

| File | Purpose |
|---|---|
| `monthly.txt` | Stores monthly budget and expense information. |
| `logs.txt` | Stores recorded budget and expense transactions. |

You do not need to create these files manually if the application initializes them automatically.

All records are stored locally in the project directory.

The application does not require MySQL, SQLite, MongoDB, or another external database.

## 📋 Quick Start

If Python and Git are already installed, use the following commands:

```bash
git clone https://github.com/rhyneulan/S.E.T-System
cd S.E.T-System-Student-Expense-Tracker
python -m venv setsy
setsy\Scripts\activate
pip install rich
python main.py
```

## ⚠️ Important Notes

- Run the program from the project directory containing `main.py`.
- Keep the virtual environment activated while using the system.
- The system uses Philippine Peso (₱) for monetary values.
- Financial records are stored locally on your computer.
- Do not delete the `.txt` files if you want to preserve your saved records.
- Back up your data files regularly to avoid accidental data loss.
- Resetting budgets, expenses, or transaction logs may permanently remove stored information.
- The system does not require an internet connection to manage locally stored financial records.

## 🛠️ Troubleshooting

### Python Is Not Recognized

Check whether Python is installed:

```bash
py --version
```

If `py` works, create the virtual environment using:

```bash
py -m venv setsy
```

### Rich Is Not Installed

Activate the virtual environment:

```bash
setsy\Scripts\activate
```

Then install Rich:

```bash
pip install rich
```

### Virtual Environment Is Not Activated

If you do not see:

```text
(setsy)
```

at the beginning of your command line, activate it again:

```bash
setsy\Scripts\activate
```

### PowerShell Activation Issue

If PowerShell prevents the activation script from running, use Windows Command Prompt instead:

```bash
setsy\Scripts\activate
```

Alternatively, run the application using the virtual environment's Python executable directly:

```bash
.\setsy\Scripts\python.exe main.py
```

## 🔒 Privacy Policy

**Last Updated: November 3, 2026**

S.E.T. SYSTEM respects the privacy of its users. The application is designed to operate locally and store financial information on the user's device.

### 1. Information Collected

The system stores information manually provided by users, including:

- Budget amounts.
- Expense amounts.
- Expense categories.
- Expense descriptions.
- Transaction dates and times.

The application does not require users to register an account or provide personal identification information.

### 2. Purpose of Data Collection

The information is used exclusively to support the application's functions, including:

- Managing allocated budgets.
- Recording expenses.
- Calculating remaining balances.
- Generating expense summaries.
- Monitoring spending patterns.
- Displaying transaction history.

### 3. Data Storage

All financial information is stored locally in the following files:

- `monthly.txt`
- `logs.txt`

The application does not use an external database or cloud storage service.

### 4. Data Sharing

The application does not intentionally transmit stored financial records to the developers or external third parties.

All financial records remain on the device where the application is running.

### 5. Data Security

The application currently does not implement file encryption or password protection.

Users are responsible for securing their devices and protecting access to their stored financial information.

### 6. Data Retention and Deletion

Users can manage or delete their financial records using the available tools within the application.

Users may also manually delete the local data files.

However, deleting or resetting stored information may permanently remove previously recorded financial data.

### 7. User Responsibility

Users are responsible for:
- Providing accurate financial information.
- Keeping their records secure.
- Maintaining backups of important data.
- Avoiding the entry of sensitive information such as passwords or banking credentials.

### 8. Policy Updates

This Privacy Policy may be updated when the application introduces new features or changes its data-handling practices.

### 9. Contact Information

For questions, suggestions, or privacy-related concerns, users may contact the development team through the repository's GitHub Issues section.

## 📜 Terms of Use and Disclaimer

By using S.E.T. SYSTEM, users agree to use the application responsibly and for its intended purpose of managing personal or student expenses.

- The application is provided for educational and personal budgeting purposes.
- Users are responsible for the accuracy of the information they enter.
- The developers are not responsible for financial decisions made using the application.
- The developers are not responsible for data loss resulting from accidental deletion, modification, or damage to local storage files.
- The application is not intended to replace professional financial or accounting services.

## 👥 Development Team

| Name | Role | Responsibilities |
|---|---|---|
| **Danggoy, Ian Dexter L.** | Designer | Responsible for the system's design and overall presentation. |
| **Demetila, James C.** | Q/A Tester | Responsible for testing system functionality, identifying errors, and evaluating system reliability. |
| **Ladra, Rhyne Marc B.** | Lead Programmer / System Developer | Responsible for leading the programming, implementation, and development of the system. |
| **Nalasa, Cheed Rodjon B.** | System Analyst | Responsible for analyzing system requirements, processes, and functionality. |

## 🤝 Contributing

This project was developed as an academic project.

Suggestions, feedback, and bug reports are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Implement and test your modifications.
4. Submit a pull request describing your improvements.

## 📄 License

This project is intended for educational purposes.

Unless otherwise stated by the authors, the project is not licensed for unrestricted redistribution, modification, or commercial use.

Please obtain permission from the development team before redistributing or using the source code for other purposes.

---

**S.E.T. SYSTEM — Student Expense Tracker System**

*Promoting responsible budgeting and better financial management among students.*

import os
from datetime import datetime
from rich import print

logs_file = "logs.txt"

#clears and resets the log records
def clear_logs(filename="logs.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("")

#records the logs of the expense and budget
def logs_tracker(filename=logs_file):
    logs = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            logs = [line.strip() for line in file.readlines() if line.strip()]

    def storage(item=None):
        if item is not None:
            timestamp = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            formatted_item = f"[dim]{timestamp}[/dim] | {item}"

            logs.append(formatted_item)
            with open(filename, "a", encoding="utf-8") as file:
                file.write(formatted_item + "\n")

        return logs
    
    return storage

# Turns one line of logs.txt into [date and time, type, amount, category, description].
# Returns None when the line is damaged.
def parse_log_line(line):
    parts = line.split(" | ")
    if len(parts) < 3:
        return None

    try:
        timestamp = parts[0].replace("[dim]", "").replace("[/dim]", "")
        kind = "Expense" if "Expense:" in parts[1] else "Budget"
        amount = float(parts[1].split("₱")[1].replace("[/red bold]", "").strip())
    except (ValueError, IndexError):
        return None

    category = parts[2]
    description = " | ".join(parts[3:]).replace("\\[", "[")  # undo the escape() done when saving
    return [timestamp, kind, amount, category, description]

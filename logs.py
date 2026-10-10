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
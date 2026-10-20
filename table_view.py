from rich import print
from rich.markup import escape


def peso(amount):
    if round(amount, 2) < 0:
        return f"-₱{abs(amount):,.2f}"
    return f"₱{abs(amount):,.2f}"


def print_table(title, headers, rows, aligns=None, total=None, styles=None, empty_message="Nothing to show."):
    # Prints one table. Every table in the program is printed with this function,
    # so they all look the same.
    #
    #   title         - the heading above the table
    #   headers       - list of column names, e.g. ["Category", "Budget"]
    #   rows          - list of rows, each row is a list with one value per column
    #   aligns        - "<" (left) or ">" (right) for every column. Default is all left.
    #   total         - optional last row, printed under its own line
    #   styles        - optional {row number: "red"} to color a whole row
    #   empty_message - printed instead of the table when there are no rows
    if aligns is None:
        aligns = ["<"] * len(headers)
    if styles is None:
        styles = {}

    rows = [[str(cell) for cell in row] for row in rows]
    if total is not None:
        total = [str(cell) for cell in total]

    # Every column is as wide as its longest value
    widths = [len(header) for header in headers]
    for row in rows + ([total] if total is not None else []):
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    line_width = sum(widths) + 3 * (len(widths) - 1)
    if len(rows) == 0:
        line_width = max(line_width, len(empty_message))  # the line must be as wide as the message

    line = "-" * line_width

    def make_row(cells, style=None):
        text = " | ".join(f"{cell:{aligns[i]}{widths[i]}}" for i, cell in enumerate(cells))
        text = escape(text)
        if style:
            text = f"[{style}]{text}[/{style}]"
        return text

    print(f"\n--- {title} ---")
    print(line)

    if len(rows) == 0:
        print(empty_message)
        print(line)
        return

    print(make_row(headers))
    print(line)

    for number, row in enumerate(rows):
        print(make_row(row, styles.get(number)))

    print(line)

    if total is not None:
        print(make_row(total))
        print(line)
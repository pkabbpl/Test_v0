from datetime import datetime

#!/usr/bin/env python3

def main():
    try:
        name = input("Enter your name: ").strip()
    except EOFError:
        name = ""
    if not name:
        name = "there"
    date_str = datetime.now().strftime("%A, %d %B %Y")
    print(f"Good day, {name}! Today is {date_str}.")

if __name__ == "__main__":
    main()
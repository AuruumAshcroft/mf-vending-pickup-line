"""One-line entry for make.fun: One Line, One Minute: The Vending Machine Pickup Line Contest."""

import os

# A vending machine flirting: stocked, chilled, always delivers.

LINE = "Hey gorgeous, I'm fully stocked, ice-cold, and I always deliver. Press B7 — I never leave you hanging."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

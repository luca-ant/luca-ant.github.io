import os

for f in os.listdir("."):
    if f.lower().endswith(".jpg") or f.lower().endswith(".heic"):
        print(f"- image-name: {f}")
        print(f"  caption: {f}")
        print(f"  copyright: © Luca Antognetti")

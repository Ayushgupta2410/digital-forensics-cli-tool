def generate_timeline(files):
    events = []

    for f in files:
        events.append((f["created"], f"Created: {f['name']}"))
        events.append((f["modified"], f"Modified: {f['name']}"))

    events.sort(key=lambda x: x[0])

    print("\n🕵️ Timeline:")
    for e in events[:20]:  # limit output
        print(f"{e[0]} → {e[1]}")

    return events
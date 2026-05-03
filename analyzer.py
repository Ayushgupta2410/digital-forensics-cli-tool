def analyze_files(files):
    suspicious = []

    for f in files:
        risk = "LOW"

        if f["name"].endswith(".exe"):
            risk = "HIGH"
        elif "temp" in f["path"].lower():
            risk = "MEDIUM"
        elif f["size"] > 10000000:
            risk = "MEDIUM"

        if risk != "LOW":
            suspicious.append({
                "file": f["name"],
                "path": f["path"],
                "risk": risk
            })

    print("\n⚠️ Suspicious Files Found:")
    for s in suspicious:
        print(f"{s['file']} | {s['risk']}")

    return suspicious
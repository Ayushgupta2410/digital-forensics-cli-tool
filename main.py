import argparse
from extractor import extract_files
from analyzer import analyze_files
from timeline import generate_timeline
from report import generate_report
from colorama import Fore
from tqdm import tqdm
import time

def main():
    parser = argparse.ArgumentParser(description="Digital Forensics CLI Tool")
    parser.add_argument("--path", required=True, help="Path to folder (simulate disk image)")
    parser.add_argument("--analyze", action="store_true")
    parser.add_argument("--timeline", action="store_true")
    parser.add_argument("--report", action="store_true")

    args = parser.parse_args()

    print(Fore.CYAN + "[+] Starting Forensic Analysis...\n")

    # Simulate loading
    for _ in tqdm(range(50), desc="Loading"):
        time.sleep(0.01)

    files = extract_files(args.path)

    if args.analyze:
        suspicious = analyze_files(files)
    else:
        suspicious = []

    if args.timeline:
        timeline = generate_timeline(files)
    else:
        timeline = []

    if args.report:
        generate_report(files, suspicious, timeline)

    print(Fore.GREEN + "\n[✔] Process Completed Successfully!")

if __name__ == "__main__":
    main()

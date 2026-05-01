#!/usr/bin/env python3

import argparse
from colorama import Fore, Style, init

from passive import get_subdomains
from resolver import resolve
from http_probe import check_http
from brute import brute_subdomains
from dirscan import run_dirscan

init(autoreset=True)

BANNER = Fore.CYAN + "ReconForge v1.5 | Recon + DirScan PRO" + Style.RESET_ALL


def categorize(sub):
    s = sub.lower()

    if any(x in s for x in ["auth", "login", "sso"]):
        return Fore.YELLOW + "[AUTH]"
    elif "api" in s:
        return Fore.BLUE + "[API]"
    elif any(x in s for x in ["shop", "store"]):
        return Fore.GREEN + "[SHOP]"
    elif any(x in s for x in ["cdn", "static"]):
        return Fore.MAGENTA + "[CDN]"
    else:
        return Fore.WHITE + "[WEB]"


def clean_results(subs, domain):
    return [s for s in subs if s.endswith("." + domain)]


def smart_filter(subs):
    blacklist = ["corp", "sandbox", "test", "internal"]
    return [s for s in subs if not any(b in s for b in blacklist)]


def main():
    parser = argparse.ArgumentParser(description="ReconForge Tool")

    parser.add_argument("target", help="Domain or URL")
    parser.add_argument("--silent", action="store_true")
    parser.add_argument("-o", "--output")
    parser.add_argument("--threads", type=int, default=20)
    parser.add_argument("--dir", action="store_true")

    args = parser.parse_args()
    target = args.target

    print(BANNER)
    print(f"\n[+] Target: {target}\n")

    is_url = target.startswith("http://") or target.startswith("https://")

    web = []

    # DOMAIN MODE
    if not is_url:
        print("[+] Passive enumeration...")
        passive = get_subdomains(target)

        print("[+] Brute force...")
        brute = brute_subdomains(target)

        subs = list(set(passive + brute))
        subs = clean_results(subs, target)
        subs = smart_filter(subs)

        print(f"[+] Total candidates: {len(subs)}\n")

        print("[+] Resolving DNS...")
        alive = resolve(subs)

        print(f"[+] DNS LIVE: {len(alive)}\n")

        print("[+] HTTP probing...")
        web = check_http(alive, threads=args.threads)

    # URL/IP MODE
    else:
        web = [target]


    print("\n[+] FINAL RESULTS:\n")

    results = []

    for sub in web:
        if args.silent:
            print(sub)
        else:
            print(f"{categorize(sub)} {sub}")
        results.append(sub)

    outfile = args.output if args.output else "reconforge_results.txt"

    with open(outfile, "w") as f:
        f.write("\n".join(results))

    print(f"\n[+] Saved {len(results)} results → {outfile}")

    # DIRSCAN
    if args.dir:
        print("\n[+] Directory scanning...\n")

        targets = web if is_url else [f"http://{h}" for h in web]

        for url in targets:
            print(f"\n[+] {url}")

            dirs = run_dirscan(url)

            for code, path in dirs:
                print(f"[{code}] {path}")


if __name__ == "__main__":
    main()

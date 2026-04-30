#!/usr/bin/env python3

import argparse
from colorama import Fore, Style, init

from passive import get_subdomains
from resolver import resolve
from http_probe import check_http
from brute import brute_subdomains

init(autoreset=True)

BANNER = Fore.CYAN + "ReconForge v1.3 | Fast Recon Mode" + Style.RESET_ALL


# -------------------------
# CATEGORY TAGGING
# -------------------------
def categorize(sub):
    s = sub.lower()

    if any(x in s for x in ["auth", "login", "sso"]):
        return Fore.YELLOW + "[AUTH]"
    elif any(x in s for x in ["api"]):
        return Fore.BLUE + "[API]"
    elif any(x in s for x in ["shop", "store"]):
        return Fore.GREEN + "[SHOP]"
    elif any(x in s for x in ["cdn", "static"]):
        return Fore.MAGENTA + "[CDN]"
    else:
        return Fore.WHITE + "[WEB]"


# -------------------------
# CLEAN FILTER (domain only)
# -------------------------
def clean_results(subs, domain):
    return [s for s in subs if s.endswith("." + domain)]


# -------------------------
# SMART FILTER (remove noise)
# -------------------------
def smart_filter(subs):
    blacklist = ["corp", "sandbox", "test", "internal"]

    filtered = []

    for sub in subs:
        if not any(b in sub.lower() for b in blacklist):
            filtered.append(sub)

    return filtered


# -------------------------
# MAIN ENGINE
# -------------------------
def run(domain, silent=False, output=None, threads=50):
    if not silent:
        print(BANNER)
        print(Fore.CYAN + f"\n[+] Target: {domain}")

    # PASSIVE
    if not silent:
        print(Fore.YELLOW + "\n[+] Passive enumeration...")
    passive_subs = get_subdomains(domain)

    # BRUTE
    if not silent:
        print(Fore.YELLOW + "[+] Brute force...")
    brute_subs = brute_subdomains(domain)

    # MERGE
    candidates = list(set(passive_subs + brute_subs))

    if not silent:
        print(Fore.GREEN + f"[+] Total candidates: {len(candidates)}")

    # DNS
    if not silent:
        print(Fore.YELLOW + "\n[+] Resolving DNS...")
    live = resolve(candidates)

    if not silent:
        print(Fore.GREEN + f"[+] DNS LIVE: {len(live)}")

    # HTTP
    if not silent:
        print(Fore.YELLOW + "\n[+] HTTP probing (fast)...")
    http_results = check_http(live, threads=threads)

    # FILTERING
    http_results = clean_results(http_results, domain)
    http_results = smart_filter(http_results)

    # OUTPUT
    if not silent:
        print(Fore.CYAN + "\n[+] FINAL RESULTS:\n")

    final = []

    for host in http_results:
        if silent:
            print(host)
        else:
            print(f"{categorize(host)} {host}")

        final.append(host)

    # SAVE
    outfile = output if output else "reconforge_results.txt"

    with open(outfile, "w") as f:
        for line in final:
            f.write(line + "\n")

    if not silent:
        print(Fore.GREEN + f"\n[+] Saved {len(final)} results → {outfile}")


# -------------------------
# CLI
# -------------------------
def main():
    parser = argparse.ArgumentParser(description="ReconForge v1.3")

    parser.add_argument("domain", help="Target domain")
    parser.add_argument("--silent", action="store_true", help="Clean output")
    parser.add_argument("-o", "--output", help="Save output file")
    parser.add_argument("--threads", type=int, default=50, help="Threads")

    args = parser.parse_args()

    run(
        domain=args.domain,
        silent=args.silent,
        output=args.output,
        threads=args.threads
    )


if __name__ == "__main__":
    main()

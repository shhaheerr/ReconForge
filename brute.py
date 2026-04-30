def brute_subdomains(domain):
    subs = []
    with open("wordlist.txt", "r") as f:
        for line in f:
            sub = line.strip()
            if sub:
                subs.append(f"{sub}.{domain}")
    return subs

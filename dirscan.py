import requests
import random
import string
from concurrent.futures import ThreadPoolExecutor

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def random_string(n=12):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def baseline_probe(base_url, timeout):
    fake = random_string()
    url = base_url.rstrip("/") + "/" + fake

    try:
        r = requests.get(
            url,
            headers=HEADERS,
            timeout=timeout,
            allow_redirects=False
        )
        return (r.status_code, len(r.text))
    except:
        return (0, 0)


def check_path(base_url, word, baseline, codes, exts, timeout):
    found = []

    for ext in exts:
        path = word.strip() + ext
        url = base_url.rstrip("/") + "/" + path

        try:
            r = requests.get(
                url,
                headers=HEADERS,
                timeout=timeout,
                allow_redirects=False
            )

            code = r.status_code
            size = len(r.text)

            if code in codes:

                # Fuzzy wildcard filter
                if code == baseline[0]:
                    if abs(size - baseline[1]) <= 15:
                        continue

                found.append(f"[{code}] {url} ({size} bytes)")

        except:
            pass

    return found


def run_dirscan(
    base_url,
    wordlist="dirs.txt",
    threads=50,
    timeout=4,
    codes=None,
    exts=None
):
    if codes is None:
        codes = [200, 204, 301, 302, 307, 401, 403]

    if exts is None:
        exts = ["", ".php", ".txt", ".bak", ".zip"]

    # Safe file reading for almost any wordlist
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        words = [x.strip() for x in f if x.strip()]

    print("[+] Detecting wildcard responses...")
    baseline = baseline_probe(base_url, timeout)

    print(f"[+] Baseline response: {baseline[0]} / {baseline[1]} bytes")
    print("[+] Scanning...\n")

    results = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        tasks = executor.map(
            lambda w: check_path(
                base_url,
                w,
                baseline,
                codes,
                exts,
                timeout
            ),
            words
        )

    for res in tasks:
        for item in res:
            results.append(item)

    return results

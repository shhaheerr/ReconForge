import requests

def run_dirscan(base_url, wordlist="dirs.txt", threads=20):
    results = []

    try:
        base = requests.get(base_url, timeout=5)
        base_len = len(base.text)
    except:
        base_len = 0

    try:
        with open(wordlist, "r") as f:
            words = [w.strip() for w in f if w.strip()]
    except:
        return results

    for word in words:
        url = base_url.rstrip("/") + "/" + word

        try:
            r = requests.get(url, timeout=5)

            if r.status_code in [200, 301, 302, 403]:

                text = r.text.lower()

                noise_keywords = [
                    "not found",
                    "404",
                    "error",
                    "does not exist",
                    "page not found"
                ]

                if not any(n in text for n in noise_keywords):
                    if abs(len(r.text) - base_len) > 50:
                        results.append((r.status_code, url))

        except:
            continue

    return results

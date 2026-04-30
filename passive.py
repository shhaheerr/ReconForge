import requests


def get_subdomains(domain, debug=False):
    subs = set()

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # -------------------------
    # CRT.SH
    # -------------------------
    try:
        if debug:
            print("[DEBUG] Fetching crt.sh...")

        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        r = requests.get(url, headers=headers, timeout=10)

        if debug:
            print(f"[DEBUG] crt.sh status: {r.status_code}")

        if r.status_code == 200:
            data = r.json()

            for entry in data:
                name = entry.get("name_value", "")
                for sub in name.split("\n"):
                    if domain in sub:
                        subs.add(sub.strip())

    except Exception as e:
        if debug:
            print("[DEBUG] crt.sh error:", e)

    # -------------------------
    # REMOVE BufferOver (dead)
    # -------------------------

    if debug:
        print(f"[DEBUG] Passive results: {len(subs)}")

    return list(subs)

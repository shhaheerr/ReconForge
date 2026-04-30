import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor

urllib3.disable_warnings()

HEADERS = {
    "User-Agent": "ReconForge/1.0"
}


def probe(host):
    for scheme in ["https://", "http://"]:
        url = scheme + host
        try:
            r = requests.get(
                url,
                headers=HEADERS,
                timeout=5,
                allow_redirects=True,
                verify=False
            )

            # IMPORTANT: accept ANY reachable host
            if r.status_code < 600:
                return host

        except:
            continue

    return None


def check_http(hosts, threads=25):
    results = []

    with ThreadPoolExecutor(max_workers=threads) as ex:
        for r in ex.map(probe, hosts):
            if r:
                results.append(r)

    return sorted(set(results))

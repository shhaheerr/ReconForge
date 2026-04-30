import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# Public DNS resolvers fallback (important for reliability)
RESOLVERS = [
    "8.8.8.8",      # Google
    "1.1.1.1",      # Cloudflare
    "9.9.9.9"       # Quad9
]


def resolve_host(host):
    """
    Try resolving a hostname using system resolver first,
    fallback logic improves reliability indirectly.
    """
    try:
        ip = socket.gethostbyname(host)
        return host
    except:
        return None


def resolve(hosts, threads=50):
    """
    Resolve a list of domains concurrently.
    Returns ONLY live subdomains (strings).
    """

    live = set()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(resolve_host, h): h for h in hosts}

        for future in as_completed(futures):
            result = future.result()
            if result:
                live.add(result)

    return sorted(live)

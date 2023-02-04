import requests
import sys

def subdomain_scanner(domain):
    subdomains = []
    with open("subdomains.txt", "r") as wordlist:
        for subdomain in wordlist:
            subdomain = subdomain.strip() + "." + domain
            try:
                response = requests.get("http://" + subdomain, timeout=3)
                if response.status_code == 200:
                    subdomains.append(subdomain)
                    print(f"[+] Discovered subdomain: {subdomain}")
            except:
                pass
    return subdomains

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python subdomain_scanner.py <domain>")
        sys.exit()
    domain = sys.argv[1]
    subdomains = subdomain_scanner(domain)
    print("[+] Discovered subdomains:")
    for subdomain in subdomains:
        print(subdomain)

import requests

def check_subdomains(domain):
    subdomains = [
        "www",
        "mail",
        "ftp",
        "webmail",
        "ns1",
        "ns2",
        "test",
        "admin",
        "beta",
        "backup",
        "dev",
        "blog",
        "db",
        "api",
        "docs",
        "portal"
    ]
    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"[+] Subdomain found: {url}")
        except requests.exceptions.RequestException:
            pass

if __name__ == '__main__':
    domain = input("Enter the domain name: ")
    check_subdomains(domain)

import requests
import sys

def website_scanner(url):
    vulnerabilities = []
    with open("vulnerabilities.txt", "r") as wordlist:
        for vulnerability in wordlist:
            vulnerability = vulnerability.strip()
            test_url = url + "/" + vulnerability
            try:
                response = requests.get(test_url, timeout=3)
                if response.status_code == 200:
                    vulnerabilities.append(test_url)
                    print(f"[+] Vulnerability found: {test_url}")
            except:
                pass
    return vulnerabilities

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python website_scanner.py <url>")
        sys.exit()
    url = sys.argv[1]
    vulnerabilities = website_scanner(url)
    print("[+] Discovered vulnerabilities:")
    for vulnerability in vulnerabilities:
        print(vulnerability)

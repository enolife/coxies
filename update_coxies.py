import os
import requests

def update_coxies_two():
    headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

    coxies_url = "https://tinyurl.com/y7xvaru7"
    response = requests.get(coxies_url, headers = headers, allow_redirects=True, verify=False)
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return

    # Print the current working directory
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")

    lines = response.text.strip().split('\n')
    coxies = [f"socks5://{line.split(',')[0]}" for line in lines[1:] if line.strip()]

    coxies = coxies[:100000]

    # Write coxies to file
    socks5_coxies_path = os.path.join(current_dir, "coxies.txt")
    print(f"Writing coxies to: {socks5_coxies_path}")

    with open(socks5_coxies_path, "w") as f:
        f.write("\n".join(coxies))
        f.write("\n")
        print("coxies updated successfully")

    # Clean up empty lines
    with open(socks5_coxies_path, "r") as f:
        lines = f.readlines()

    with open(socks5_coxies_path, "w") as f:
        f.writelines(line for line in lines if line.strip())

if __name__ == "__main__":
    update_coxies_two()

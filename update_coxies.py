import requests
import os

def update_proxies_two():
    proxies_url = "https://api.s5proxies.com/api2.php?do=download&country=US&key=65fcb18e928802024032105154265fcb18e9288e&is_type="
    response = requests.get(proxies_url)
    lines = response.text.strip().split('\n')

    proxies = [f"socks5://{line.split(',')[0]}" for line in lines[1:] if line.strip()]

    proxies = proxies[:100000]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    socks5_proxies_path = os.path.join(script_dir, "coxies.txt")

    with open(socks5_proxies_path, "a") as f:
        f.write("\n".join(proxies))
        f.write("\n")
        print("Proxies updated successfully")

    with open(socks5_proxies_path, "r") as f:
        lines = f.readlines()

    with open(socks5_proxies_path, "w") as f:
        f.writelines(line for line in lines if line.strip())

if __name__ == "__main__":
    update_proxies_two()

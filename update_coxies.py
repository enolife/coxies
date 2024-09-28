import requests
import os

def update_proxies_two():
    proxies_url = "https://api.s5proxies.com/api2.php?do=download&country=US&key=66f677fc85d242024092704164466f677fc85d2d&is_type="
    response = requests.get(proxies_url)

    if response.status_code != 200:
        print(f"Failed to fetch proxies, status code: {response.status_code}")
        return

    lines = response.text.strip().split('\n')
    
    if len(lines) < 2:
        print("No valid proxies found.")
        return

    proxies = [f"socks5://{line.split(',')[0]}" for line in lines[1:] if line.strip()]
    proxies = proxies[:100000]

    # Write the file to a fixed path in the repository root
    socks5_proxies_path = os.path.join(os.getcwd(), "coxies.txt")

    # Log the path where the file will be written
    print(f"Writing proxies to: {socks5_proxies_path}")

    # Write proxies to the file
    with open(socks5_proxies_path, "a") as f:
        f.write("\n".join(proxies))
        f.write("\n")
        print("Proxies updated successfully")

    # Clean the file to remove empty lines
    with open(socks5_proxies_path, "r") as f:
        lines = f.readlines()

    with open(socks5_proxies_path, "w") as f:
        f.writelines(line for line in lines if line.strip())

if __name__ == "__main__":
    update_proxies_two()

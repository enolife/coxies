import os
import requests

def update_proxies_two():
    proxies_url = "https://api.s5proxies.com/api2.php?do=download&country=US&key=66f677fc85d242024092704164466f677fc85d2d&is_type="
    response = requests.get(proxies_url)

    # Print the current working directory
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")

    lines = response.text.strip().split('\n')
    proxies = [f"socks5://{line.split(',')[0]}" for line in lines[1:] if line.strip()]

    proxies = proxies[:100000]

    # Write proxies to file
    socks5_proxies_path = os.path.join(current_dir, "coxies.txt")
    print(f"Writing proxies to: {socks5_proxies_path}")

    with open(socks5_proxies_path, "a") as f:
        f.write("\n".join(proxies))
        f.write("\n")
        print("Proxies updated successfully")

    # Clean up empty lines
    with open(socks5_proxies_path, "r") as f:
        lines = f.readlines()

    with open(socks5_proxies_path, "w") as f:
        f.writelines(line for line in lines if line.strip())

if __name__ == "__main__":
    update_proxies_two()

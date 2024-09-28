import os
import requests

def update_coxies_two():
    coxies_url = "https://tinyurl.com/y7xvaru7"
    response = requests.get(coxies_url)

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

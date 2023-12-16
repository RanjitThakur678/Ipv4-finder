import socket

# Function to find IP addresses for URLs
def find_ips():
    try:
        with open('url.txt', 'r') as file: #url.txt which contains all the url on which you need to trigger nslookup keep it in same repo 
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                print(f"URL: {url}")
                try:
                    ip_addresses = socket.gethostbyname_ex(url)[2]
                    if ip_addresses:
                        print("IP addresses:")
                        for ip in ip_addresses:
                            print(ip)
                    else:
                        print(f"No IP addresses found for {url}")
                except socket.gaierror:
                    print(f"Could not resolve {url}")
                print("----------------------")
    except FileNotFoundError:
        print("File url.txt not found!")

# Run the function
find_ips()

import requests
from concurrent.futures import ThreadPoolExecutor
import os

# Proxy settings for Tor
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Directory to save the downloaded files
download_dir = 'downloaded_files'
os.makedirs(download_dir, exist_ok=True)

# List of URLs to download
urls = [
    'http://exampleonion1.onion/file1.txt',
    'http://exampleonion2.onion/file2.jpg',
    # Add more URLs as needed
]

def download_file(url):
    try:
        print(f"Downloading {url}")
        response = requests.get(url, proxies=proxies, stream=True)
        response.raise_for_status()
        
        # Extract the file name from the URL
        filename = os.path.join(download_dir, url.split("/")[-1])
        
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Download files using multiple threads
def download_all_files(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:  # You can adjust the number of threads
        executor.map(download_file, urls)

if __name__ == "__main__":
    download_all_files(urls)

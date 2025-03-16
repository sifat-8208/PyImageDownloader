import os
import requests
from urllib.parse import urlparse
from requests.exceptions import RequestException, Timeout, HTTPError

def download_image(url, save_path="downloaded_image.jpg"):
    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL. Please provide a valid URL.")

        print(f"Downloading image from: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        if 'image' not in response.headers.get('Content-Type', ''):
            raise ValueError("The provided URL does not appear to be an image.")
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded and saved as {save_path}")

    except ValueError as e:
        print(f"URL Error: {e}")
    except Timeout:
        print("Error: The request timed out. Please try again later.")
    except HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
    except RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        print("Download process finished.")

url = input("Enter the image URL: ")
filename = input("Enter the filename to save the image (e.g., 'image.jpg'): ")

if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
    print("Warning: Please make sure the filename has a valid image extension (e.g., .jpg, .png).")

download_image(url, filename)

import requests
import os

# Image URLs
images = {
    'family-hub.jpg': 'https://storage.googleapis.com/kaggle-datasets-images/18454/23403/c2b239c4d57f9b4fae0a78c946a4ad0c/dataset-cover.jpg',
    'gesture-control.jpg': 'https://www.researchgate.net/profile/Shubham-Santosh/publication/340862571/figure/fig1/AS:885195488243712@1588189465020/Hand-gesture-recognition-system-pipeline.png',
    'cry-cure.jpg': 'https://www.researchgate.net/profile/Mohammed-Mounir/publication/337579012/figure/fig1/AS:829193216536578@1574750405150/Overview-of-the-proposed-infant-cry-classification-system.png',
    'query-system.jpg': 'https://miro.medium.com/max/1200/1*iKcQZhBBS7qZNKGiLqGkhw.png'
}

# Add headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Download each image
for filename, url in images.items():
    try:
        print(f'Downloading {filename}...')
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded {filename}')
        
    except requests.exceptions.RequestException as e:
        print(f'Error downloading {filename}: {str(e)}')
    except Exception as e:
        print(f'Unexpected error with {filename}: {str(e)}')

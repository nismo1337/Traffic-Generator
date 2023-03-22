import requests
import random

# Open the file containing the proxies
with open('proxy_list.txt') as f:
    proxies = f.read().splitlines()

# Set the URL of the website to target
url = 'google.com'

# Set the number of requests to make
num_requests = 100

# Define the user agent to use in the requests (you can remove this to make the requests faster)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'

# Make the requests
for i in range(num_requests):
    # Select a random proxy from the list
    proxy = {'http': 'http://' + random.choice(proxies)}

    try:
        # Send the request using the selected proxy and user agent
        headers = {'User-Agent': user_agent}
        response = requests.get(url, proxies=proxy, headers=headers)
        print('Request {} success with proxy: {}'.format(i+1, proxy))
    except:
        # If the request fails, print an error message
        print('Request {} failed with proxy: {}'.format(i+1, proxy))

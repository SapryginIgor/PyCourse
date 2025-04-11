import requests

url = "https://picsum.photos/200/300"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://picsum.photos/"
}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    with open("output.jpg", "wb") as f:
        f.write(r.content)
    print("Downloaded direct ID image successfully.")
else:
    print(f"Still blocked. Status code: {r.status_code}")

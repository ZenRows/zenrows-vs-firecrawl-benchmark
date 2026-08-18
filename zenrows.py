import requests
import time
import csv
import random

import os

YOUR_ZENROWS_API_KEY = os.environ.get("ZENROWS_API_KEY", "")
if not YOUR_ZENROWS_API_KEY:
    raise SystemExit("Set the ZENROWS_API_KEY environment variable before running this script.")



REQUESTS_PER_URL = 100

URLS = [
    {"name": "Amazon", "url": "https://www.amazon.com/ref=nav_logo"},# "https://www.amazon.com/s?k=playstation+gift+card+digital+code&crid=3FXL1NI73ICC&sprefix=playst%2Caps%2C406&ref=nb_sb_ss_p13n-expert-pd-ops-ranker_1_6"}, # https://www.amazon.com/dp/B09B8YWXDF
    {"name": "Glassdoor", "url": "https://www.glassdoor.com/Overview/Working-at-Google-EI_IE9079.11,17.htm"},
    {"name": "Google", "url": "https://www.google.com/search?q=web+scraping+api"},
    {"name": "LinkedIn",   "url": "https://www.linkedin.com/in/satyanadella/"},
    {"name": "Mid-sized e-commerce site behind Cloudflare",   "url": "https://www.ikea.com/"},
    {"name": "Zillow real estate listing", "url": "https://www.zillow.com/homes/for_sale/"},
    {"name": "BBC", "url": "https://www.bbc.com/news/technology"},
]

results = []


def is_valid(html):
    if not html:
        return False

    html_lower = html.lower()

    blocked_signals = [
        "captcha",
        "just a moment",
        "verify you are human",
        "access denied"
    ]

    if any(x in html_lower for x in blocked_signals):
        return False

    return len(html) > 5000

# ----------------------------
# Zenrows
# ----------------------------
print("\n--- Zenrows Tests ---\n")

for target in URLS:
    for i in range(REQUESTS_PER_URL):

        start = time.time()

        try:
            r = requests.get(
                "https://api.zenrows.com/v1/",
                params={
                    "url": target["url"],
                    "apikey": YOUR_ZENROWS_API_KEY,
                    "mode": "auto"
                   # "js_render": "true",
                   # "premium_proxy": "true"
                },
                timeout=60
            )

            html = r.text
            elapsed = round((time.time() - start) * 1000, 2)

            valid = is_valid(html)

            status = r.status_code

        except Exception as e:
            html = ""
            elapsed = 0
            valid = False
            status = f"ERROR: {type(e)}"

        results.append([
            "Zenrows",
            target["name"],
            i + 1,
            status,
            valid,
            elapsed
        ])

        print(f"Zenrows | {target['name']} | #{i+1} | {status} | {valid} | {elapsed}ms")

        time.sleep(0.5)
        

# ----------------------------
# Save CSV
# ----------------------------
with open("zenrows_benchmark_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "platform",
        "target",
        "request_num",
        "status_code",
        "valid",
        "response_time_ms"
    ])
    writer.writerows(results)

print("\n--- DONE: benchmark_results.csv created ---")


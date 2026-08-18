# Zenrows vs Firecrawl Benchmark

Scripts and raw data from an original benchmark comparing **Zenrows** and **Firecrawl's `/scrape` endpoint** across 7 target URLs, conducted in May 2026.

Companion code for the Zenrows article **[Best Firecrawl Alternative for Anti-Bot Bypass](https://www.zenrows.com/blog/best-firecrawl-alternative-for-anti-bot-bypass)**.

## Test targets

| Target | Type | URL |
|---|---|---|
| Amazon product page | Protected | `https://www.amazon.com/ref=nav_logo` |
| Glassdoor company page | Protected | `https://www.glassdoor.com/Overview/Working-at-Google-EI_IE9079.11,17.htm` |
| LinkedIn public profile | Protected | `https://www.linkedin.com/in/satyanadella/` |
| Google SERP results page | Protected | `https://www.google.com/search?q=web+scraping+api` |
| IKEA (Cloudflare-protected e-commerce) | Protected | `https://www.ikea.com/` |
| Zillow real estate listing | Unprotected | `https://www.zillow.com/homes/for_sale/` |
| BBC news article | Unprotected | `https://www.bbc.com/news/technology` |

## Methodology

- **100 requests** per target per platform
- Zenrows configured with `mode=auto` on all requests
- Firecrawl using its `/scrape` endpoint
- Recorded per request: HTTP status code, response time (ms), and page title detection

### What this test does not cover

- Bulk asynchronous job workflows
- Session persistence across multi-step logged-in workflows
- Firecrawl's crawl and map endpoints (only `/scrape` is exercised)

## Setup

### Prerequisites

- Python 3.10+
- A [Zenrows API key](https://app.zenrows.com/register)
- A [Firecrawl API key](https://www.firecrawl.dev/)

### 1. Clone the repository

```bash
git clone https://github.com/ZenRows/zenrows-vs-firecrawl-benchmark.git
cd zenrows-vs-firecrawl-benchmark
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Both scripts read their credentials from the environment:

```bash
export ZENROWS_API_KEY=your_zenrows_api_key
export FIRECRAWL_API_KEY=your_firecrawl_api_key
```

## Running the benchmark

Each platform is run by its own script:

```bash
python zenrows.py      # writes zenrows_benchmark_results.csv
python firecrawl.py    # writes firecrawl_benchmark_results.csv
```

Each run issues 100 requests per target, so expect it to take a while.

`test.py` is a small standalone script for confirming your Firecrawl credentials work before starting a full run.

## Output

Both scripts write a CSV to the repository root recording, per request: target name, URL, HTTP status code, response time, whether a page title was detected, and success status.

The `data/` folder holds the aggregated spreadsheet used to produce the figures in the article.

## Repository structure

```
.
├── zenrows.py        # Zenrows benchmark run
├── firecrawl.py      # Firecrawl /scrape benchmark run
├── test.py           # quick Firecrawl credential check
├── data/             # aggregated results used in the article
├── requirements.txt
└── README.md
```

## License

[MIT](LICENSE)

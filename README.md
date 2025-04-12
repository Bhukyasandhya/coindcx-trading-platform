# CoinDCX Trading Platform

This project is a simple, beautiful web platform that allows users to perform **Buy/Sell trading operations** on CoinDCX using their official API.  
The platform supports both **real trades** and **demo mode**, making it suitable for testing and safe exploration.

---

## Features

- Place **Buy/Sell limit orders** on CoinDCX
- Enter custom **price**, **quantity**, and **market**
- Enter your **API Key & Secret** securely via form (no .env needed)
- Toggle **Demo Mode** to simulate trades
- Clean **UI with CoinDCX branding**
- Built with **Flask + HTML/CSS + JavaScript**

---

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Vanilla JS
- **API**: CoinDCX REST API
- **Styling**: Custom CSS, CoinDCX logo integration

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/coindcx-trading-platform.git
cd coindcx-trading-platform
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask App

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Usage

1. Enter your **CoinDCX API Key & Secret**
2. Select **Buy or Sell**
3. Enter **market** (e.g., BTCUSDT), **price**, and **quantity**
4. Toggle **Demo Mode** (checked = simulate order)
5. Click **Place Order**
6. View the response in the output box

---

## Folder Structure

```
coindcx-trading-platform/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
│   └── images/
│       └── coindcx-logo.jpg
```

---

## Dependencies

- Flask
- requests

Install them using:

```bash
pip install flask requests
```

---

## Notes

- Real orders use live funds. Use only with correct API keys.
- Demo mode safely simulates orders with no actual transactions.
- API keys are **not stored** — only used per session.

---

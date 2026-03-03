# 📸 Instagram Scraper & Advanced Analyzer

A Python-based Instagram Scraper and Analytics Tool built using **Instaloader**.

This project allows you to:

* Fetch Instagram profile details
* Download profile pictures
* Analyze last 20 posts
* Calculate average likes & comments
* Extract top hashtags
* Login securely using `.env` credentials

---

## 📂 Project Structure

```
INSTA_SCRAPER/
│
├── insta.py              # Basic profile scraper
├── advanced.py           # Advanced analytics version
├── .env                  # Environment variables (not uploaded)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Features

### ✅ Basic Scraper (`insta.py`)

* Fetch username
* Total posts count
* Followers & following
* Bio
* Download profile picture

### ✅ Advanced Analyzer (`advanced.py`)

* Secure login using `.env`
* Fetch detailed profile info
* Analyze last 20 posts
* Calculate:

  * Average Likes
  * Average Comments
* Extract Top 10 Hashtags
* Show Private & Verified status

---

## 🛠 Tech Stack

* Python 3.x
* Instaloader
* python-dotenv
* Collections (Counter)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sujxl-warghe/Insta-Scraper.git
cd INSTA_SCRAPER
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install instaloader python-dotenv
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the root folder:

```
INSTA_USERNAME=your_instagram_username
INSTA_PASSWORD=your_instagram_password
```

⚠️ Never upload the `.env` file to GitHub.

---

---

## ▶️ How to Run

### 🔹 Run Basic Scraper

```bash
python insta.py
```

### 🔹 Run Advanced Analyzer

```bash
python advanced.py
```

---


---

## 🔒 Security Note

* Do not expose your credentials publicly
* Use a secondary Instagram account for testing
* Instagram may temporarily restrict excessive scraping

---

## 📌 Future Improvements

* Export analytics to CSV
* Engagement rate calculation
* Story analytics
* Streamlit dashboard version
* Web-based UI

---

## 📜 License

This project is for educational purposes only.
Use responsibly according to Instagram’s Terms of Service.

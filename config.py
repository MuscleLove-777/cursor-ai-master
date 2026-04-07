"""Cursor AIコーディング完全攻略 - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Cursor AIコーディング完全攻略"
BLOG_DESCRIPTION = "AIコードエディタCursorの使い方・最新機能・料金・活用術を毎日更新。Cursor vs Copilot vs Windsurfの徹底比較も。開発者のためのAIコーディングガイド。"
BLOG_URL = "https://musclelove-777.github.io/cursor-ai-master"
BLOG_TAGLINE = "AIコーディングの未来はCursorにある"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/cursor-ai-master"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Cursor 使い方",
    "Cursor 料金・プラン",
    "Cursor vs Copilot",
    "Cursor 最新ニュース",
    "Cursor エージェント機能",
    "Cursor 活用テクニック",
    "AIコードエディタ比較",
    "Cursor 設定・カスタマイズ",
]

THEME = {
    "primary": "#7928ca",
    "accent": "#ff0080",
    "gradient_start": "#7928ca",
    "gradient_end": "#ff0080",
    "dark_bg": "#0a0a1a",
    "dark_surface": "#1a1030",
    "light_bg": "#faf5ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [8, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Cursor Pro": [
        {"service": "Cursor Pro", "url": "https://cursor.sh/pricing", "description": "Cursor Proに登録する"},
    ],
    "Cursor": [
        {"service": "Cursor", "url": "https://cursor.sh", "description": "Cursor公式サイト"},
    ],
    "GitHub Copilot": [
        {"service": "GitHub Copilot", "url": "https://github.com/features/copilot", "description": "GitHub Copilot（比較用）"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI開発講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8089

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-HJLCFVY5TF"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}

"""Cursor AIコーディング完全攻略 - プロンプト定義

Cursor特化ブログ用のプロンプトを一元管理する。
JSON-LD構造化データ（BlogPosting / FAQPage / BreadcrumbList）対応。
"""

# ペルソナ設定
PERSONA = (
    "あなたはAIコードエディタの専門家です。"
    "Cursor・GitHub Copilot・Windsurfを毎日使い込んでいる現役の開発者で、"
    "初心者から上級者まで幅広い読者に実践的な情報を届けるプロのテックライターです。"
    "Cursorの最新アップデートやAgent機能を常にキャッチアップし、"
    "他のAIコーディングツール（Copilot、Windsurf、Claude Code等）との比較も客観的に行えます。"
)

# 記事フォーマット指示
ARTICLE_FORMAT = """
【記事構成（必ずこの順序で書くこと）】

## この記事でわかること
- ポイント1（具体的なベネフィット）
- ポイント2
- ポイント3

## 結論（先に結論を述べる）
（読者が最も知りたい答えを最初に提示）

## 本題（H2で3〜5セクション）
（具体的な手順・解説。操作手順を箇条書きで明示）

## 使い方手順
（インストールから実際の操作まで、ステップバイステップで解説）

## 他のAIコーディングツールとの比較
（GitHub Copilot / Windsurf / Claude Code との違いを表形式で整理）

## よくある質問（FAQ）
### Q1: （よくある質問1）
A1: （回答1）

### Q2: （よくある質問2）
A2: （回答2）

### Q3: （よくある質問3）
A3: （回答3）

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別SEOキーワードヒント
CATEGORY_PROMPTS = {
    "Cursor 使い方": "Cursor 使い方、Cursor インストール、Cursor 初心者、Cursor 始め方、Cursor 基本操作",
    "Cursor 料金・プラン": "Cursor 料金、Cursor 無料、Cursor Pro、Cursor Business、Cursor 月額、Cursor Free Pro 違い",
    "Cursor vs Copilot": "Cursor Copilot 比較、Cursor Windsurf 比較、AIコードエディタ 比較 2026、どっちがいい",
    "Cursor 最新ニュース": "Cursor アップデート、Cursor 新機能、Cursor セキュリティエージェント、Cursor リリース",
    "Cursor エージェント機能": "Cursor Agent、Cursor エージェント、Cursor 自律コーディング、Cursor AI Agent 使い方",
    "Cursor 活用テクニック": "Cursor ショートカット、Cursor プロンプト術、Cursor コツ、Cursor 効率化、Cursor Tips",
    "AIコードエディタ比較": "AIコードエディタ 比較、Cursor vs Copilot vs Windsurf、Cursor vs Claude Code、AI開発ツール",
    "Cursor 設定・カスタマイズ": "Cursor 設定、.cursorrules、Cursor 拡張機能、Cursor カスタマイズ、Cursor おすすめ設定",
}

# ニュースソース
NEWS_SOURCES = [
    "Cursor公式ブログ (https://cursor.sh/blog)",
    "GitHub Blog (https://github.blog/)",
    "TechCrunch (https://techcrunch.com/tag/cursor/)",
    "The Verge (https://www.theverge.com/)",
]

# FAQ構造化データの有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用の追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "AIコードエディタCursorに関するキーワードを選んでください。\n"
    "日本の開発者が検索しそうな実用的なキーワードを意識してください。\n"
    "「Cursor 使い方」「Cursor 料金」「Cursor vs Copilot」のような、\n"
    "検索ボリュームが見込めるキーワードを優先してください。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    category_hints = "\n".join(
        f"- {cat}: {hints}" for cat, hints in CATEGORY_PROMPTS.items()
    )
    return (
        f"{PERSONA}\n\n"
        "Cursor AIコーディング完全攻略ブログ用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"カテゴリ別キーワードヒント:\n{category_hints}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """Cursor特化記事生成プロンプトを構築する"""
    category_hints = CATEGORY_PROMPTS.get(category, "")
    news_sources_text = "\n".join(f"- {src}" for src in NEWS_SOURCES)

    return f"""{PERSONA}

以下のキーワードに関する記事を、AIコードエディタCursorの専門サイト向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- カテゴリ関連キーワード: {category_hints}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に（数字や年号を含めると効果的）
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQ（よくある質問）を3つ以上含めること（FAQPage構造化データ対応）

【内部リンク】
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）

【参考情報源】
{news_sources_text}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 2026年最新の情報を反映すること
- 具体的な操作手順や設定方法を含める
- Agent機能やTab補完などCursor固有の機能を解説する
- 他のAIコーディングツール（Copilot, Windsurf, Claude Code）との客観的な比較を含める
- 初心者にもわかりやすく、専門用語には補足説明を付ける

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3個以上生成すること（FAQPage構造化データに使用）
- 読者にとって実用的で具体的な内容を心がけること"""

<!-- 🌐 Language Switcher -->
<p align="center">
  <a href="#english">English</a>
  &nbsp; | &nbsp;
  <a href="#persian">فارسی</a>
</p>

---

<a id="english"></a>

# 📝 Text Analyzer

A simple and interactive command-line text analysis tool built with Python. It analyzes user-provided text and generates useful statistics about its characters and words.

## ✨ Features

- Count the total number of characters, including spaces and punctuation.
- Count the total number of words.
- Identify the most frequently used character.
- Identify the most frequently used word.
- Display the frequency of every character.
- Display the frequency of every word.
- Perform case-insensitive text analysis.
- Exclude whitespace from character frequency calculations.
- Ignore punctuation when extracting words.
- Handle empty input gracefully.

## 🔄 How It Works

The program analyzes the entered text and generates a report containing character and word statistics.

- **Character Count:** Counts all characters, including spaces and punctuation.
- **Word Count:** Counts extracted words without punctuation.
- **Character Frequency:** Counts every non-whitespace character.
- **Word Frequency:** Counts how many times each word appears.
- **Case Insensitivity:** Treats uppercase and lowercase letters as identical.
- **Frequency Ranking:** Displays the most frequent items first.

When multiple characters or words have the same frequency, alphabetical order is used to determine their display order.

## 📋 Example

```text
Hey there! Welcome to Text Analyzer.
Let's find out what's hiding in your text!
Enter a sentence or paragraph below.

Your text: Hello hello, Python!

==========================================
             TEXT ANALYSIS
==========================================
Total characters (including spaces): 20
Total words: 3
Most frequent character: 'l' (4 times)
Most frequent word: 'hello' (2 times)

Character Frequencies (excluding whitespace):
  'l': 4
  ...

Word Frequencies:
  'hello': 2
  'python': 1

==========================================
Thanks for using Text Analyzer. Have a great day!
==========================================
```

*The example is shortened for readability. The program displays all character and word frequencies.*

## ⚙️ Requirements

- Python 3.8 or later
- No external packages required.

## ▶️ Run

From the project directory, execute:

```bash
py main.py
```

### Git Bash on Windows

If interactive input does not work when running the program directly in Git Bash, use:

```bash
winpty py main.py
```

In PowerShell or Command Prompt, use:

```powershell
py main.py
```

---

<a id="persian"></a>

# 📝 تحلیل‌گر متن

یک ابزار ساده و تعاملی برای تحلیل متن در محیط خط فرمان که با Python پیاده‌سازی شده است. این برنامه متن ورودی را بررسی کرده و اطلاعات آماری مفیدی درباره کاراکترها و کلمات آن ارائه می‌دهد.

## ✨ امکانات

- شمارش تعداد کل کاراکترها، شامل فاصله‌ها و علائم نگارشی.
- شمارش تعداد کل کلمات.
- شناسایی پرتکرارترین کاراکتر.
- شناسایی پرتکرارترین کلمه.
- نمایش فراوانی تمام کاراکترها.
- نمایش فراوانی تمام کلمات.
- تحلیل متن بدون حساسیت به بزرگی و کوچکی حروف.
- حذف فاصله‌ها از محاسبه فراوانی کاراکترها.
- نادیده گرفتن علائم نگارشی هنگام استخراج کلمات.
- مدیریت ورودی خالی.

## 🔄 نحوه عملکرد

برنامه متن واردشده را تحلیل کرده و گزارشی شامل آمار کاراکترها و کلمات تولید می‌کند.

- **تعداد کاراکترها:** تمام کاراکترها، شامل فاصله‌ها و علائم نگارشی، شمارش می‌شوند.
- **تعداد کلمات:** کلمات استخراج‌شده بدون علائم نگارشی شمارش می‌شوند.
- **فراوانی کاراکترها:** تعداد تکرار تمام کاراکترهای غیر از فاصله محاسبه می‌شود.
- **فراوانی کلمات:** تعداد دفعات تکرار هر کلمه محاسبه می‌شود.
- **عدم حساسیت به بزرگی و کوچکی حروف:** حروف بزرگ و کوچک یکسان در نظر گرفته می‌شوند.
- **مرتب‌سازی فراوانی:** موارد پرتکرارتر در ابتدای فهرست نمایش داده می‌شوند.

در صورت برابر بودن تعداد تکرار چند کاراکتر یا کلمه، ترتیب الفبایی برای نمایش آن‌ها استفاده می‌شود.

## 📋 نمونه خروجی

```text
Your text: Hello hello, Python!

==========================================
             TEXT ANALYSIS
==========================================
Total characters (including spaces): 20
Total words: 3
Most frequent character: 'l' (4 times)
Most frequent word: 'hello' (2 times)

Character Frequencies (excluding whitespace):
  'l': 4
  ...

Word Frequencies:
  'hello': 2
  'python': 1

==========================================
Thanks for using Text Analyzer. Have a great day!
==========================================
```

*نمونه بالا برای خوانایی کوتاه شده است. برنامه فراوانی تمام کاراکترها و کلمات را نمایش می‌دهد.*

## ⚙️ پیش‌نیازها

- Python نسخه 3.8 یا بالاتر
- بدون نیاز به نصب کتابخانه خارجی

## ▶️ اجرا

در پوشه پروژه دستور زیر را اجرا کنید:

```bash
py main.py
```

### اجرای برنامه در Git Bash ویندوز

اگر ورودی تعاملی هنگام اجرای مستقیم برنامه در Git Bash کار نکرد، از دستور زیر استفاده کنید:

```bash
winpty py main.py
```

در PowerShell یا Command Prompt از دستور زیر استفاده کنید:

```powershell
py main.py
```

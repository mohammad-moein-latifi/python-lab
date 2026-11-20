<!-- 🌐 Language Switcher -->
<p align="center">
  <a href="#english">English</a>
  &nbsp; | &nbsp;
  <a href="#persian">فارسی</a>
</p>

---

<a id="english"></a>

# 🎯 Number Guessing Game

A simple and interactive command-line game built with Python. The computer randomly selects an integer between **0 and 100**, and the player has **10 valid attempts** to guess the secret number.

## ✨ Features

- Generate a random integer between 0 and 100.
- Allow up to 10 valid guessing attempts.
- Provide hints to guide the next guess.
- Display the number of remaining attempts.
- Validate user input.
- Handle invalid entries without consuming an attempt.
- Reveal the secret number when the player runs out of attempts.
- Handle interruptions gracefully.

## 🔄 How It Works

The game selects a random number, and the player tries to guess it within the allowed number of attempts.

- **Random Number:** Generates a secret integer between 0 and 100.
- **Valid Attempts:** Gives the player 10 attempts to find the secret number.
- **Too Low:** Indicates that the guessed number is lower than the secret number.
- **Too High:** Indicates that the guessed number is higher than the secret number.
- **Correct Guess:** Ends the game when the player guesses the secret number.
- **Input Validation:** Rejects non-numeric input, decimal values, and numbers outside the allowed range without consuming an attempt.

If all 10 valid attempts are used, the game ends and reveals the secret number.

The player can also stop the game safely using `Ctrl+C` or by closing the input stream.

## 🎮 How to Play

1. Run the program.
2. Enter a whole number between `0` and `100`.
3. Follow the hints:
   - **Too low:** Enter a higher number.
   - **Too high:** Enter a lower number.
4. Guess the secret number to win.

Invalid entries do not consume an attempt. The remaining attempts are displayed in the input prompt.

## ⚙️ Requirements

- Python 3
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

# 🎯 بازی حدس عدد

یک بازی ساده و تعاملی در محیط خط فرمان که با Python پیاده‌سازی شده است. در این بازی، کامپیوتر یک عدد صحیح را به‌صورت تصادفی بین **۰ تا ۱۰۰** انتخاب می‌کند و بازیکن **۱۰ فرصت معتبر** برای حدس زدن عدد مورد نظر دارد.

## ✨ امکانات

- تولید یک عدد صحیح تصادفی بین ۰ تا ۱۰۰.
- اختصاص حداکثر ۱۰ فرصت معتبر برای حدس زدن.
- ارائه راهنمایی برای انتخاب عدد بعدی.
- نمایش تعداد فرصت‌های باقی‌مانده.
- اعتبارسنجی ورودی کاربر.
- مدیریت ورودی‌های نامعتبر بدون کاهش تعداد فرصت‌ها.
- نمایش عدد مخفی در صورت پایان فرصت‌ها.
- مدیریت ایمن توقف برنامه.

## 🔄 نحوه عملکرد

در ابتدای بازی، یک عدد تصادفی انتخاب می‌شود و بازیکن باید آن را در محدوده فرصت‌های مجاز حدس بزند.

- **تولید عدد تصادفی:** یک عدد صحیح مخفی بین ۰ تا ۱۰۰ انتخاب می‌شود.
- **فرصت‌های معتبر:** بازیکن ۱۰ فرصت برای پیدا کردن عدد مخفی دارد.
- **Too Low:** یعنی عدد واردشده از عدد مخفی کوچک‌تر است و باید عدد بزرگ‌تری وارد شود.
- **Too High:** یعنی عدد واردشده از عدد مخفی بزرگ‌تر است و باید عدد کوچک‌تری وارد شود.
- **حدس صحیح:** با وارد کردن عدد درست، بازی به پایان می‌رسد.
- **اعتبارسنجی ورودی:** ورودی غیرعددی، عدد اعشاری و اعداد خارج از محدوده مجاز بدون کاهش فرصت‌ها رد می‌شوند.

اگر تمام ۱۰ فرصت معتبر استفاده شوند، بازی پایان یافته و عدد مخفی نمایش داده می‌شود.

همچنین بازیکن می‌تواند با استفاده از `Ctrl+C` یا بسته شدن جریان ورودی، بازی را به‌صورت ایمن متوقف کند.

## 🎮 نحوه بازی

۱. برنامه را اجرا کنید.

۲. یک عدد صحیح بین `0` تا `100` وارد کنید.

۳. از راهنمایی‌های برنامه استفاده کنید:

- **Too Low:** عدد انتخابی کمتر از عدد مخفی است؛ عدد بزرگ‌تری وارد کنید.
- **Too High:** عدد انتخابی بیشتر از عدد مخفی است؛ عدد کوچک‌تری وارد کنید.

۴. با حدس درست، برنده بازی می‌شوید.

ورودی‌های نامعتبر از تعداد فرصت‌ها کم نمی‌کنند و تعداد فرصت‌های باقی‌مانده در پیام دریافت ورودی نمایش داده می‌شود.

## ⚙️ پیش‌نیازها

- Python 3
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

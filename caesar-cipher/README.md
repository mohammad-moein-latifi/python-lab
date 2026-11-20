<!-- 🌐 Language Switcher -->
<p align="center">
  <a href="#english">English</a>
  &nbsp; | &nbsp;
  <a href="#persian">فارسی</a>
</p>

---

<a id="english"></a>

# 🔐 Caesar Cipher

A simple command-line encryption tool built with Python. It implements the **Caesar Cipher** algorithm, allowing users to encode and decode messages by shifting English letters by a specified number of positions in the alphabet.

## ✨ Features

- Encode messages using the Caesar Cipher algorithm.
- Decode previously encoded messages.
- Accept a custom shift value.
- Support uppercase and lowercase English letters.
- Preserve the original letter case.
- Keep spaces, numbers, and special characters unchanged.
- Handle alphabet wrapping.
- Validate menu selections and shift values.

## 🔄 How It Works

The Caesar Cipher is a substitution technique that replaces each English letter with another letter a specified number of positions ahead or behind in the alphabet.

- **Encode:** Shifts each letter forward by the specified number of positions.
- **Decode:** Shifts each letter backward by the specified number of positions.
- **Alphabet Wrapping:** Continues from the beginning of the alphabet after reaching its end.

For example, with a shift value of `3`:

- `A` becomes `D`.
- `B` becomes `E`.
- `X` becomes `A`.
- `Y` becomes `B`.
- `Z` becomes `C`.

Uppercase and lowercase letters are processed separately, preserving their original case. Spaces, numbers, and special characters remain unchanged.

## 🎮 How to Use

1. Run the program.
2. Choose an operation:
   - `1`: Encode a message.
   - `2`: Decode a message.
3. Enter your message.
4. Enter the desired shift value.
5. View the resulting encoded or decoded message.

The program validates the selected operation and shift value. Invalid menu selections and non-integer shift values are handled without unexpected errors.

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

# 🔐 رمزنگاری سزار | Caesar Cipher

یک ابزار ساده رمزنگاری در محیط خط فرمان که با Python پیاده‌سازی شده است. این برنامه الگوریتم **رمزنگاری سزار (Caesar Cipher)** را اجرا می‌کند و به کاربران امکان می‌دهد پیام‌های خود را با جابه‌جایی حروف انگلیسی به تعداد مشخصی از موقعیت‌ها در الفبا، رمزنگاری و رمزگشایی کنند.

## ✨ امکانات

- رمزنگاری پیام با استفاده از الگوریتم سزار.
- رمزگشایی پیام‌های رمزنگاری‌شده.
- دریافت مقدار جابه‌جایی دلخواه.
- پشتیبانی از حروف بزرگ و کوچک انگلیسی.
- حفظ بزرگی و کوچکی حروف اصلی.
- بدون تغییر باقی ماندن فاصله‌ها، اعداد و کاراکترهای خاص.
- پشتیبانی از چرخش در انتهای الفبا.
- اعتبارسنجی انتخاب عملیات و مقدار جابه‌جایی.

## 🔄 نحوه عملکرد

رمزنگاری سزار یک روش جایگزینی است که در آن هر حرف انگلیسی با حرف دیگری جایگزین می‌شود که به تعداد مشخصی موقعیت جلوتر یا عقب‌تر در الفبا قرار دارد.

- **Encode (رمزنگاری):** هر حرف را به تعداد مشخصی موقعیت به جلو منتقل می‌کند.
- **Decode (رمزگشایی):** هر حرف را به همان تعداد موقعیت به عقب برمی‌گرداند.
- **چرخش در الفبا:** پس از رسیدن به انتهای الفبا، جابه‌جایی از ابتدای آن ادامه پیدا می‌کند.

برای مثال، با مقدار جابه‌جایی `3`:

- `A` به `D` تبدیل می‌شود.
- `B` به `E` تبدیل می‌شود.
- `X` به `A` تبدیل می‌شود.
- `Y` به `B` تبدیل می‌شود.
- `Z` به `C` تبدیل می‌شود.

حروف بزرگ و کوچک به‌صورت مستقل پردازش شده و بزرگی و کوچکی آن‌ها حفظ می‌شود. فاصله‌ها، اعداد و کاراکترهای خاص بدون تغییر باقی می‌مانند.

## 🎮 نحوه استفاده

۱. برنامه را اجرا کنید.

۲. یکی از عملیات زیر را انتخاب کنید:

- `1`: رمزنگاری پیام (Encode)
- `2`: رمزگشایی پیام (Decode)

۳. پیام مورد نظر خود را وارد کنید.

۴. مقدار جابه‌جایی حروف را مشخص کنید.

۵. نتیجه رمزنگاری یا رمزگشایی را مشاهده کنید.

برنامه انتخاب عملیات و مقدار جابه‌جایی را اعتبارسنجی می‌کند. انتخاب نامعتبر و وارد کردن مقدار غیرصحیح برای جابه‌جایی، بدون ایجاد خطای پیش‌بینی‌نشده مدیریت می‌شوند.

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

<!-- 🌐 Language Switcher -->
<p align="center">
  <a href="#english">English</a>
  &nbsp; | &nbsp;
  <a href="#persian">فارسی</a>
</p>

---

<a id="english"></a>

# 🔐 Caesar Cipher

A simple command-line encryption tool built with Python. It implements the **Caesar Cipher** algorithm, allowing you to encode and decode messages by shifting English letters by a specified number of positions in the alphabet.

## 🔄 How It Works

The Caesar Cipher replaces each letter with another letter a specified number of positions ahead or behind in the alphabet.

- **Encode:** Shifts each letter forward by the specified number of positions.
- **Decode:** Shifts each letter backward by the specified number of positions.

The alphabet wraps around when reaching its end. For example, with a shift value of `3`, `X`, `Y`, and `Z` become `A`, `B`, and `C`.

Uppercase and lowercase letters are handled separately. Spaces, numbers, and special characters remain unchanged.

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

From this directory, run:

```bash
python main.py
```

---

<a id="persian"></a>

# 🔐 رمزنگاری سزار | Caesar Cipher

یک ابزار ساده خط فرمان با Python که الگوریتم **رمزنگاری سزار (Caesar Cipher)** را پیاده‌سازی می‌کند. با استفاده از این برنامه می‌توانید پیام‌های خود را با جابه‌جایی حروف انگلیسی به تعداد مشخصی از موقعیت‌ها در الفبا، رمزنگاری و رمزگشایی کنید.

## 🔄 نحوه عملکرد

در الگوریتم سزار، هر حرف با حرف دیگری جایگزین می‌شود که به تعداد مشخصی موقعیت جلوتر یا عقب‌تر در الفبا قرار دارد.

- **Encode (رمزنگاری):** حروف را به تعداد مشخصی موقعیت به جلو منتقل می‌کند.
- **Decode (رمزگشایی):** حروف را به همان تعداد موقعیت به عقب برمی‌گرداند.

در صورت رسیدن به انتهای الفبا، جابه‌جایی از ابتدای آن ادامه پیدا می‌کند. برای مثال، با مقدار جابه‌جایی `3`، حروف `X`، `Y` و `Z` به‌ترتیب به `A`، `B` و `C` تبدیل می‌شوند.

حروف بزرگ و کوچک به‌صورت مستقل پردازش می‌شوند. فاصله‌ها، اعداد و کاراکترهای خاص بدون تغییر باقی می‌مانند.

## 🎮 نحوه استفاده

۱. برنامه را اجرا کنید.

۲. یکی از عملیات زیر را انتخاب کنید:

- `1`: رمزنگاری پیام (Encode)
- `2`: رمزگشایی پیام (Decode)

۳. متن مورد نظر خود را وارد کنید.

۴. مقدار جابه‌جایی حروف را مشخص کنید.

۵. نتیجه رمزنگاری یا رمزگشایی را مشاهده کنید.

برنامه انتخاب عملیات و مقدار جابه‌جایی را اعتبارسنجی می‌کند. انتخاب نامعتبر و وارد کردن مقدار غیرصحیح برای جابه‌جایی، بدون ایجاد خطای پیش‌بینی‌نشده مدیریت می‌شوند.

## ⚙️ پیش‌نیازها

- Python 3
- بدون نیاز به نصب کتابخانه جانبی

## ▶️ اجرا

در ترمینال و از مسیر همین پوشه اجرا کنید:

```bash
python main.py
```

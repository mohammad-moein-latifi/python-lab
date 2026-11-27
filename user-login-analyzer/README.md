 <!-- 🌐 Language Switcher -->
<p align="center">
  <a href="#english">English</a>
  &nbsp; | &nbsp;
  <a href="#persian">فارسی</a>
</p>

---

<a id="english"></a>

# 🔐 User Login Analyzer

A command-line application built with Python that collects user login records and analyzes login activity. It generates a report showing login counts, unique users, single-login users, and time intervals between consecutive logins for users with more than three login records.

## ✨ Features

- Collect usernames and login timestamps.
- Calculate the total number of login records.
- Count unique users.
- Display the login count for each user.
- Identify users who logged in exactly once.
- Identify users with more than three login records.
- Calculate time intervals between consecutive logins for frequent users.
- Sort login timestamps chronologically before calculating intervals.
- Validate input records and handle invalid entries.
- Handle empty input without errors.

## 🔄 How It Works

The application collects login records and groups them by username before analyzing user activity.

- **Login Records:** Accepts a username and its login timestamp.
- **Unique Users:** Counts the number of distinct usernames.
- **Login Count:** Calculates how many times each user logged in.
- **Single-Login Users:** Identifies users with exactly one login record.
- **Frequent Users:** Identifies users with more than three login records.
- **Time Intervals:** Calculates the time difference between consecutive logins for frequent users.

Login timestamps are sorted chronologically before calculating time intervals, regardless of the order in which records were entered.

The application stops collecting records when the user submits an empty line.

## 💻 How to Use

1. Run the program.
2. Enter a username followed by a comma and a login timestamp.
3. Use the following format:

```text
username, YYYY-MM-DD HH:MM:SS
```

4. Press `Enter` after each record to enter the next login.
5. Press `Enter` on an empty line to finish entering records.
6. Review the generated login analysis report.

### Example Input

The following example contains login records for four different users:

```text
Login: ali, 2026-11-20 08:00:00
Login: sara, 2026-11-20 09:00:00
Login: mohammad, 2026-11-20 10:00:00
Login: ali, 2026-11-20 12:00:00
Login: reza, 2026-11-20 13:00:00
Login: sara, 2026-11-21 09:00:00
Login: ali, 2026-11-21 08:00:00
Login: ali, 2026-11-22 10:00:00
Login: sara, 2026-11-22 09:00:00
Login: ali, 2026-11-23 08:00:00
Login: reza, 2026-11-23 13:00:00
Login:
```

### Example Output

```text
========== Login Report ==========

Total unique users: 4
Total login records: 11

--- Login Count Per User ---
ali: 5 login(s)
sara: 3 login(s)
mohammad: 1 login(s)
reza: 2 login(s)

--- Users With Only One Login ---
mohammad

--- Users With More Than 3 Logins ---

User: ali
Total logins: 5
Time intervals between logins:

  2026-11-20 08:00:00 -> 2026-11-20 12:00:00
  Interval: 4:00:00

  2026-11-20 12:00:00 -> 2026-11-21 08:00:00
  Interval: 20:00:00

  2026-11-21 08:00:00 -> 2026-11-22 10:00:00
  Interval: 1 day, 2:00:00

  2026-11-22 10:00:00 -> 2026-11-23 08:00:00
  Interval: 22:00:00
```

## ⚙️ Requirements

- Python 3
- No external packages required.

## ▶️ Run

Navigate to the project directory and execute:

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

### Input Validation

- Usernames cannot be empty.
- Login timestamps must follow the specified date and time format.
- Each record must contain a username and a timestamp separated by a comma.
- Invalid records are rejected without stopping the application.

### Notes

- Usernames are case-sensitive.
- Users with exactly three logins are not included in the frequent-user report.
- Time intervals are calculated only for users with more than three login records.
- All timestamps should use a consistent timezone format.

---

<a id="persian"></a>

# 🔐 تحلیلگر ورود کاربران

یک برنامه خط فرمان با Python که اطلاعات ورود کاربران را دریافت کرده و فعالیت آن‌ها را تحلیل می‌کند. این برنامه گزارشی شامل تعداد ورودها، تعداد کاربران غیرتکراری، کاربران با یک بار ورود و فاصله زمانی بین ورودهای متوالی کاربرانی که بیش از سه رکورد ورود دارند، تولید می‌کند.

## ✨ امکانات

- دریافت نام کاربری و زمان ورود.
- محاسبه مجموع تعداد رکوردهای ورود.
- محاسبه تعداد کاربران غیرتکراری.
- نمایش تعداد ورود هر کاربر.
- شناسایی کاربرانی که دقیقاً یک بار وارد شده‌اند.
- شناسایی کاربرانی که بیش از سه رکورد ورود دارند.
- محاسبه فاصله زمانی بین ورودهای متوالی کاربران پرتکرار.
- مرتب‌سازی زمان ورودها پیش از محاسبه فاصله زمانی.
- اعتبارسنجی اطلاعات ورودی و مدیریت رکوردهای نامعتبر.
- مدیریت ورودی خالی بدون ایجاد خطا.

## 🔄 نحوه عملکرد

برنامه اطلاعات ورود کاربران را دریافت کرده و پیش از تحلیل، رکوردها را بر اساس نام کاربری دسته‌بندی می‌کند.

- **رکوردهای ورود:** دریافت نام کاربری و زمان ورود آن.
- **کاربران غیرتکراری:** محاسبه تعداد نام‌های کاربری متمایز.
- **تعداد ورود:** محاسبه تعداد دفعات ورود هر کاربر.
- **کاربران با یک بار ورود:** شناسایی کاربرانی که دقیقاً یک رکورد ورود دارند.
- **کاربران پرتکرار:** شناسایی کاربرانی که بیش از سه رکورد ورود دارند.
- **فاصله زمانی:** محاسبه اختلاف زمانی بین ورودهای متوالی کاربران پرتکرار.

پیش از محاسبه فاصله زمانی، رکوردهای ورود بر اساس زمان به ترتیب صعودی مرتب می‌شوند؛ بنابراین ترتیب وارد کردن اطلاعات تأثیری بر نتیجه نخواهد داشت.

برای پایان دادن به دریافت اطلاعات، کافی است یک خط خالی وارد کنید.

## 💻 نحوه استفاده

۱. برنامه را اجرا کنید.

۲. نام کاربری را وارد کرده، سپس یک کاما و زمان ورود را بنویسید.

۳. اطلاعات باید از فرمت زیر پیروی کنند:

```text
username, YYYY-MM-DD HH:MM:SS
```

۴. پس از وارد کردن هر رکورد، کلید `Enter` را فشار دهید تا رکورد بعدی را وارد کنید.

۵. برای پایان ورود اطلاعات، در یک خط خالی کلید `Enter` را فشار دهید.

۶. گزارش تحلیل ورود کاربران نمایش داده می‌شود.

### نمونه ورودی

در مثال زیر، اطلاعات ورود چهار کاربر مختلف وارد شده است:

```text
Login: ali, 2026-11-20 08:00:00
Login: sara, 2026-11-20 09:00:00
Login: mohammad, 2026-11-20 10:00:00
Login: ali, 2026-11-20 12:00:00
Login: reza, 2026-11-20 13:00:00
Login: sara, 2026-11-21 09:00:00
Login: ali, 2026-11-21 08:00:00
Login: ali, 2026-11-22 10:00:00
Login: sara, 2026-11-22 09:00:00
Login: ali, 2026-11-23 08:00:00
Login: reza, 2026-11-23 13:00:00
Login:
```

### نمونه خروجی

```text
========== Login Report ==========

Total unique users: 4
Total login records: 11

--- Login Count Per User ---
ali: 5 login(s)
sara: 3 login(s)
mohammad: 1 login(s)
reza: 2 login(s)

--- Users With Only One Login ---
mohammad

--- Users With More Than 3 Logins ---

User: ali
Total logins: 5
Time intervals between logins:

  2026-11-20 08:00:00 -> 2026-11-20 12:00:00
  Interval: 4:00:00

  2026-11-20 12:00:00 -> 2026-11-21 08:00:00
  Interval: 20:00:00

  2026-11-21 08:00:00 -> 2026-11-22 10:00:00
  Interval: 1 day, 2:00:00

  2026-11-22 10:00:00 -> 2026-11-23 08:00:00
  Interval: 22:00:00
```

## ⚙️ پیش‌نیازها

- Python 3
- بدون نیاز به نصب کتابخانه خارجی

## ▶️ اجرا

ابتدا وارد پوشه پروژه شوید و دستور زیر را اجرا کنید:

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

### اعتبارسنجی ورودی

- نام کاربری نمی‌تواند خالی باشد.
- زمان ورود باید از فرمت تاریخ و زمان مشخص‌شده پیروی کند.
- هر رکورد باید شامل نام کاربری و زمان ورود باشد که با کاما از یکدیگر جدا شده‌اند.
- رکوردهای نامعتبر بدون متوقف شدن برنامه رد می‌شوند.

### نکات

- نام کاربران به حروف کوچک و بزرگ حساس است.
- کاربرانی که دقیقاً سه بار ورود داشته‌اند، در گزارش کاربران پرتکرار قرار نمی‌گیرند.
- فاصله زمانی فقط برای کاربرانی محاسبه می‌شود که بیش از سه رکورد ورود دارند.
- تمام زمان‌ها باید از قالب زمانی یکسان و سازگار استفاده کنند.

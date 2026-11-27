# Student Grade Management System

A console-based Python application for registering students and their course grades, calculating unit-weighted GPAs, and reviewing academic performance.

## Features

- Register students with one or more courses.
- Validate names, course units, and grades.
- Calculate unit-weighted GPA for each student.
- List students from highest GPA to lowest GPA.
- Display all students tied for the highest or lowest GPA.
- List conditional students (GPA below 12).
- Search by last name and display every matching student's GPA.
- Handle invalid menu choices and invalid input without terminating the application.

## Requirements

- Python 3.9 or later
- No third-party packages

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd student-grade-management
```

## Run

```bash
python main.py
```

On Windows, this command also works when the Python launcher is installed:

```powershell
py main.py
```

## GPA Calculation

The application calculates a unit-weighted GPA:

`GPA = sum(grade * course_units) / sum(course_units)`

Grades must be between 0 and 20. Course units must be positive whole numbers.

## Conditional Status

A student is considered conditional when their GPA is below `12.0`. This threshold is defined by `CONDITIONAL_GPA_LIMIT` near the top of `main.py` and can be changed if your institution uses a different rule.

## Data Storage

Student records are kept in memory while the program is running. They are not saved to a file or database, so all records are cleared when the application exits.

---

# سامانه مدیریت نمرات دانشجویان

یک برنامه کنسولی با Python برای ثبت دانشجویان و نمرات درس‌ها، محاسبه معدل وزنی و بررسی وضعیت تحصیلی.

## امکانات

- ثبت دانشجو به همراه یک یا چند درس
- اعتبارسنجی نام، تعداد واحد و نمره
- محاسبه معدل وزنی بر اساس تعداد واحد درس‌ها
- نمایش دانشجویان از بیشترین معدل به کمترین معدل
- نمایش تمام دانشجویانی که بالاترین یا پایین‌ترین معدل مشترک دارند
- نمایش دانشجویان مشروط با معدل کمتر از ۱۲
- جستجو بر اساس نام خانوادگی و نمایش معدل تمام افراد مطابق با آن
- مدیریت ورودی نامعتبر و انتخاب اشتباه منو بدون متوقف شدن برنامه

## پیش‌نیازها

- Python نسخه 3.9 یا بالاتر
- بدون نیاز به نصب کتابخانه جانبی

## اجرا

ابتدا وارد پوشه پروژه شوید و دستور زیر را اجرا کنید:

```powershell
py main.py
```

یا:

```bash
python main.py
```

## نحوه محاسبه معدل

معدل به‌صورت وزنی محاسبه می‌شود:

`معدل = مجموع (نمره هر درس × تعداد واحد آن) / مجموع واحدها`

نمره باید بین ۰ تا ۲۰ و تعداد واحد باید یک عدد صحیح مثبت باشد.

## قانون مشروطی

در این پروژه، دانشجویی که معدل او کمتر از `12.0` باشد مشروط در نظر گرفته می‌شود. این مقدار در ابتدای فایل `main.py` و در متغیر `CONDITIONAL_GPA_LIMIT` قرار دارد و قابل تغییر است.

## نگهداری اطلاعات

اطلاعات دانشجویان فقط تا زمانی که برنامه در حال اجراست در حافظه نگهداری می‌شود. با خروج از برنامه، اطلاعات ثبت‌شده پاک می‌شوند و در فایل یا پایگاه داده ذخیره نمی‌شوند.

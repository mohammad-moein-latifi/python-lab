<!-- 🌐 Language Switcher -->
<p align="center">
  <a href="./README.md">
    <img src="https://badgen.net/badge/-/🔠%20English%20Version/blue?label=&scale=1.5" alt="English Version"/>
  </a>
</p>

<h1 align="center">🐍 آزمایشگاه پایتون | Python Lab</h1>

<p align="center">
  فضای کاری شخصی برای آزمایش کد، حل مسئله، تمرین‌های برنامه‌نویسی و توسعه پروژه‌های مستقل با Python؛ با تمرکز بر یادگیری مستمر و تجربه عملی.
</p>

<!-- 🏷️ Custom Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3-3776AB?style=plastic&labelColor=20232A&logo=python&logoColor=white" alt="Python 3"/>
  <img src="https://img.shields.io/badge/Code%20Style-PEP%208-4B8BBE?style=plastic&labelColor=20232A" alt="PEP 8"/>
  <img src="https://img.shields.io/badge/Commits-Semantic%20Commits-FE5196?style=plastic&labelColor=20232A&logo=git&logoColor=white" alt="Semantic Commit Messages"/>
  <img src="https://img.shields.io/badge/Branching-Feature%20Branch-6C63FF?style=plastic&labelColor=20232A&logo=git&logoColor=white" alt="Feature Branch Workflow"/>
  <img src="https://img.shields.io/badge/License-MIT-00A693?style=plastic&labelColor=20232A" alt="MIT License"/>
</p>

---

<a id="about"></a>
## 👋 درباره مخزن

**Python Lab** فضای کاری شخصی من برای یادگیری و تجربه با Python، آزمایش ایده‌ها، حل چالش‌های برنامه‌نویسی و توسعه پروژه‌های مستقل است.

این مخزن مجموعه‌ای از تمرین‌های عملی، آزمایش‌های کدنویسی و پروژه‌های شخصی را در یک مکان گردآوری می‌کند؛ با تمرکز بر توسعه عملی، حل مسئله و بهبود مستمر.

<a id="table-of-contents"></a>
## 📑 فهرست مطالب

- [درباره مخزن](#about)
- [ساختار مخزن](#repository-structure)
- [مشارکت در پروژه](#contributing)
  - [استراتژی شاخه‌بندی](#branching-strategy)
  - [استاندارد نوشتن Commit](#commit-convention)
  - [استانداردهای کدنویسی](#code-guidelines)
  - [Pull Request و Issues](#pull-requests-and-issues)
- [پروژه‌ها](#projects)
- [مجوز](#license)

<a id="repository-structure"></a>
## 📂 ساختار مخزن

هر پروژه در یک پوشه مستقل و با نامی متناسب با موضوع یا عملکرد آن نگهداری می‌شود.

**الگوی کلی ساختار مخزن:**

```text
python-lab/
│
├── .github/
│   └── ISSUE_TEMPLATE/
│
├── <project-name>/
│   ├── main.py
│   └── README.md
│
├── .gitignore
├── LICENSE
├── README.md
└── README_FA.md
```

**برای اضافه کردن پروژه جدید:**

1. یک پوشه مستقل با نام معنادار و استاندارد `kebab-case` ایجاد کنید. از شماره‌گذاری پوشه‌ها استفاده نکنید.
2. فایل `main.py` را در صورت تناسب، به‌عنوان نقطه شروع اجرای پروژه قرار دهید.
3. یک فایل `README.md` شامل معرفی، پیش‌نیازها و نحوه اجرای پروژه ایجاد کنید.
4. متناسب با پیچیدگی پروژه، فایل‌ها و پوشه‌های مورد نیاز را به آن اضافه کنید.
5. نام و توضیح پروژه را به بخش پروژه‌های همین فایل اضافه کنید.

<a id="contributing"></a>
## 🤝 مشارکت در پروژه

از پیشنهادها، گزارش خطاها و مشارکت‌های برنامه‌نویسی استقبال می‌کنم. برای حفظ یکپارچگی و قابلیت نگهداری مخزن، لطفاً استانداردهای زیر را رعایت کنید.

<a id="branching-strategy"></a>
### 🌿 استراتژی شاخه‌بندی

این مخزن از یک گردش کار سبک **[Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)** استفاده می‌کند.

- شاخه `main` شاخه اصلی و محل نگهداری نسخه پایدار مخزن است.
- برای هر تغییر، یک شاخه کوتاه‌عمر از آخرین وضعیت `main` ایجاد کنید.
- از شاخه‌های `feature/` برای قابلیت‌های جدید، بهبودها، آزمایش ایده‌ها و تغییر مستندات استفاده کنید.
- از شاخه‌های `fix/` برای رفع خطاها استفاده کنید.
- هر شاخه را به یک تغییر مشخص اختصاص دهید و تغییرات آن را از طریق Pull Request به `main` ارسال کنید.
- از ثبت مستقیم تغییرات روی `main` خودداری کنید.
- پس از ادغام Pull Request، شاخه کاری را حذف کنید.

**نمونه نام‌گذاری شاخه‌ها:**

```text
feature/number-guessing-game
feature/update-documentation
fix/guess-validation
```

📚 [راهنمای Feature Branch Workflow – Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)

<a id="commit-convention"></a>
### 📝 استاندارد نوشتن Commit

پیام‌های Commit بر اساس الگوی [Semantic Commit Messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) نوشته می‌شوند.

**ساختار پیام:**

```text
<type>(<scope>): <subject>
```

- `type` نوع تغییر را مشخص می‌کند و الزامی است.
- `scope` بخش یا پروژه‌ای را که تغییر مربوط به آن است مشخص می‌کند و اختیاری است.
- `subject` خلاصه‌ای کوتاه و واضح از تغییر است که با زمان حال نوشته می‌شود.

**انواع متداول:**

| نوع | کاربرد |
|---|---|
| `feat` | افزودن قابلیت جدید |
| `fix` | رفع خطا |
| `docs` | تغییر مستندات |
| `style` | تغییرات قالب‌بندی بدون تغییر عملکرد |
| `refactor` | بازآرایی کد بدون افزودن قابلیت یا رفع خطا |
| `test` | افزودن یا اصلاح تست‌ها |
| `chore` | تغییرات نگهداری و کارهای جانبی |

**نمونه‌ها:**

```bash
feat(number-guessing-game): add random number generation
feat(number-guessing-game): limit guesses to ten attempts
fix(number-guessing-game): handle invalid user input
docs(number-guessing-game): update usage instructions
chore(license): add MIT license
```

<a id="code-guidelines"></a>
### 🐍 استانداردهای کدنویسی

- رعایت استانداردهای نگارش [PEP 8](https://peps.python.org/pep-0008/).
- انتخاب نام‌های واضح و معنادار برای متغیرها، توابع و کلاس‌ها.
- طراحی توابع با مسئولیت مشخص و پیاده‌سازی قابل فهم.
- مدیریت ورودی‌های نامعتبر و خطاهای قابل پیش‌بینی.
- پرهیز از وابستگی‌های غیرضروری و مستندسازی پکیج‌های مورد نیاز.
- به‌روز نگه داشتن مستندات هر پروژه.

<a id="pull-requests-and-issues"></a>
### 📬 Pull Request و Issues

- هر Pull Request باید روی یک تغییر مشخص متمرکز باشد.
- توضیح دهید چه چیزی تغییر کرده و دلیل انجام آن چیست.
- جزئیات تست و بررسی تغییرات را ارائه کنید.
- برای گزارش خطا و پیشنهاد قابلیت جدید از قالب‌های Issue موجود استفاده کنید.
- تمام Pull Requestهای مربوط به قابلیت‌های جدید و رفع خطا باید به شاخه `main` ارسال شوند.

<a id="projects"></a>
## 🚀 پروژه‌ها

مجموعه پروژه‌های این مخزن با هدف تمرین عملی، آزمایش ایده‌ها و توسعه مهارت‌های برنامه‌نویسی ایجاد می‌شوند.

| پروژه | توضیحات |
|---|---|
| 🎯 [بازی حدس عدد](./number-guessing-game/) | حدس عدد انتخاب‌شده به‌صورت تصادفی در حداکثر ۱۰ تلاش، همراه با راهنمایی برای انتخاب عدد بزرگ‌تر یا کوچک‌تر. |

<a id="license"></a>
## 📄 مجوز

این مخزن تحت مجوز [MIT License](./LICENSE) منتشر شده است.

برای مشاهده جزئیات، به فایل `LICENSE` مراجعه کنید.

---

<p align="center">
  ساخته‌شده با ❤️ توسط
  <a href="https://github.com/mohammad-moein-latifi"><strong>Mohammad Moein Latifi</strong></a>
</p>

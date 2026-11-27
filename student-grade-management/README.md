<!-- 🌐 Language Switcher -->
<p align="center">
  <a href="#english">English</a>
  &nbsp; | &nbsp;
  <a href="#persian">فارسی</a>
</p>

---

<a id="english"></a>

# 🎓 Student Grade Management System

A console-based student grade management application built with Python. It allows users to register multiple students, add multiple courses for each student, calculate unit-weighted GPAs, and review academic performance.

## ✨ Features

- Register multiple students with first and last names.
- Add multiple courses for each student.
- Store each course name, unit count, and grade.
- Validate student names, course units, and grades.
- Calculate unit-weighted GPA for each student.
- Display all registered students and their course details.
- Sort students from the highest GPA to the lowest GPA.
- Display all students tied for the highest or lowest GPA.
- List conditional students with a GPA below `12.0`.
- Search by last name and display the GPA of every matching student.
- Handle invalid input and keyboard interruption gracefully.

## 🔄 How It Works

Each student can have one or more courses. Every course contains:

- **Course Name:** The name of the course.
- **Units:** A positive whole number representing the course units.
- **Grade:** A numeric grade between `0` and `20`.

The application calculates each student's weighted GPA using the following formula:

`GPA = sum(course grade * course units) / sum(course units)`

For example, consider a student with these courses:

| Course | Units | Grade |
|---|---:|---:|
| Mathematics | 3 | 16 |
| Persian | 2 | 17 |
| Physics | 3 | 14 |

The weighted GPA is:

`(16 * 3 + 17 * 2 + 14 * 3) / (3 + 2 + 3) = 15.25`

A student is considered **conditional** when their GPA is below `12.0`. This threshold is defined by `CONDITIONAL_GPA_LIMIT` in `main.py`.

## 🎮 How to Use

1. Run the program.
2. Select `1. Add Student` from the menu.
3. Enter the student's first name and last name.
4. Enter the first course name, its unit count, and grade.
5. When asked `Add another course? (y/n):`, enter `y` to add another course or `n` to finish registering that student.
6. Repeat the process to register additional students.
7. Use the menu options to view reports or search for a student.

### Example Input Session

The following is an example of registering two students. The first student has three courses, and the second student has two courses.

```text
========== Student Grade Management System ==========

1. Add Student
2. Display All Students
3. Display Students by GPA
4. Display Highest GPA
5. Display Lowest GPA
6. Display Conditional Students
7. Search Student by Last Name
8. Exit

Select an option (1-8): 1

--- Add Student ---
First name: Ali
Last name: Ahmadi

Enter course information:
Course name: Mathematics
Course units: 3
Grade (0-20): 16
Add another course? (y/n): y

Enter course information:
Course name: Persian
Course units: 2
Grade (0-20): 17
Add another course? (y/n): y

Enter course information:
Course name: Physics
Course units: 3
Grade (0-20): 14
Add another course? (y/n): n

Student 'Ali Ahmadi' was added successfully.

Select an option (1-8): 1

--- Add Student ---
First name: Sara
Last name: Karimi

Enter course information:
Course name: Mathematics
Course units: 3
Grade (0-20): 10
Add another course? (y/n): y

Enter course information:
Course name: Persian
Course units: 2
Grade (0-20): 13
Add another course? (y/n): n

Student 'Sara Karimi' was added successfully.
```

### Example Reports

After registering the students above, select `3. Display Students by GPA`:

```text
========== Students by GPA ==========
1. Ali Ahmadi — GPA: 15.25
2. Sara Karimi — GPA: 11.20
```

Select `4. Display Highest GPA`:

```text
========== Highest GPA: 15.25 ==========
- Ali Ahmadi (GPA: 15.25)
```

Select `5. Display Lowest GPA`:

```text
========== Lowest GPA: 11.20 ==========
- Sara Karimi (GPA: 11.20)
```

Select `6. Display Conditional Students`:

```text
========== Conditional Students (GPA below 12) ==========
- Sara Karimi (GPA: 11.20)
```

Select `7. Search Student by Last Name` and enter `Ahmadi`:

```text
Enter the student's last name: Ahmadi

========== Search Results: Ahmadi ==========
- Ali Ahmadi (GPA: 15.25)
```

The search is case-insensitive. If multiple students have the same last name, the GPA of every matching student is displayed.

## 📋 Menu Options

| Option | Action |
|---|---|
| `1` | Add a student and their courses |
| `2` | Display all students and course details |
| `3` | Display students sorted by GPA |
| `4` | Display the highest GPA and student(s) |
| `5` | Display the lowest GPA and student(s) |
| `6` | Display students with a GPA below `12.0` |
| `7` | Search students by last name |
| `8` | Exit the application |

## ⚠️ Input Rules and Limitations

- First name, last name, and course name cannot be empty.
- Course units must be positive whole numbers.
- Grades must be between `0` and `20`; decimal grades are supported.
- Invalid entries are rejected and requested again.
- Students must have at least one course when registered.
- If multiple students share the highest or lowest GPA, all of them are displayed.
- Searching by last name returns all matching students.
- Student records are stored in memory only. All records are lost when the application exits; file or database persistence is not implemented.

## ⚙️ Requirements

- Python 3.9 or later.
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

To stop the application, select `8. Exit` or press `Ctrl+C`.

---

<a id="persian"></a>

# 🎓 سامانه مدیریت نمرات دانشجویان

یک برنامه کنسولی با Python برای مدیریت اطلاعات دانشجویان و نمرات درس‌های آن‌ها. با استفاده از این برنامه می‌توانید چندین دانشجو ثبت کنید، برای هر دانشجو چند درس در نظر بگیرید، معدل وزنی را محاسبه کنید و گزارش وضعیت تحصیلی دانشجویان را مشاهده کنید.

## ✨ امکانات

- ثبت چندین دانشجو همراه با نام و نام خانوادگی
- ثبت چندین درس برای هر دانشجو
- دریافت نام درس، تعداد واحد و نمره هر درس
- اعتبارسنجی نام‌ها، تعداد واحد و نمره
- محاسبه معدل وزنی بر اساس تعداد واحد درس‌ها
- نمایش تمام دانشجویان به همراه جزئیات درس‌ها
- مرتب‌سازی دانشجویان از بیشترین معدل به کمترین معدل
- نمایش تمام دانشجویانی که بالاترین یا پایین‌ترین معدل مشترک دارند
- نمایش دانشجویان مشروط با معدل کمتر از `12.0`
- جستجو بر اساس نام خانوادگی و نمایش معدل تمام افراد مطابق با آن
- مدیریت ورودی‌های نامعتبر و توقف برنامه با `Ctrl+C`

## 🔄 نحوه عملکرد

هر دانشجو می‌تواند یک یا چند درس داشته باشد. اطلاعات هر درس شامل موارد زیر است:

- **نام درس:** نام درسی که دانشجو گذرانده است.
- **تعداد واحد:** یک عدد صحیح مثبت که تعداد واحدهای درس را مشخص می‌کند.
- **نمره:** یک مقدار عددی بین `0` تا `20`.

معدل هر دانشجو بر اساس تعداد واحد درس‌ها و با فرمول زیر محاسبه می‌شود:

`معدل = مجموع (نمره هر درس × تعداد واحد آن) / مجموع واحدها`

برای مثال، فرض کنید اطلاعات درسی یک دانشجو به شکل زیر باشد:

| درس | تعداد واحد | نمره |
|---|---:|---:|
| ریاضی | ۳ | ۱۶ |
| فارسی | ۲ | ۱۷ |
| فیزیک | ۳ | ۱۴ |

محاسبه معدل:

`(16 * 3 + 17 * 2 + 14 * 3) / (3 + 2 + 3) = 15.25`

در این پروژه، دانشجویی که معدل او کمتر از `12.0` باشد مشروط در نظر گرفته می‌شود. این مقدار در متغیر `CONDITIONAL_GPA_LIMIT` در فایل `main.py` تعریف شده است.

## 🎮 راهنمای استفاده

۱. برنامه را اجرا کنید.

۲. از منوی اصلی گزینه `1. Add Student` را انتخاب کنید.

۳. نام و نام خانوادگی دانشجو را وارد کنید.

۴. نام درس، تعداد واحد و نمره آن را وارد کنید.

۵. برنامه سؤال `Add another course? (y/n):` را نمایش می‌دهد:
- برای اضافه کردن درس بعدی، `y` وارد کنید.
- برای پایان ثبت درس‌های همان دانشجو، `n` وارد کنید.

۶. برای ثبت دانشجوی بعدی، دوباره گزینه `1` را انتخاب کنید.

۷. پس از ثبت دانشجویان، با انتخاب گزینه‌های منو می‌توانید گزارش‌های مختلف را مشاهده یا دانشجو را جستجو کنید.

### نمونه ثبت اطلاعات چند دانشجو

در نمونه زیر، دو دانشجو ثبت می‌شوند. دانشجوی اول سه درس و دانشجوی دوم دو درس دارد.

```text
========== Student Grade Management System ==========

1. Add Student
2. Display All Students
3. Display Students by GPA
4. Display Highest GPA
5. Display Lowest GPA
6. Display Conditional Students
7. Search Student by Last Name
8. Exit

Select an option (1-8): 1

--- Add Student ---
First name: Ali
Last name: Ahmadi

Enter course information:
Course name: Mathematics
Course units: 3
Grade (0-20): 16
Add another course? (y/n): y

Enter course information:
Course name: Persian
Course units: 2
Grade (0-20): 17
Add another course? (y/n): y

Enter course information:
Course name: Physics
Course units: 3
Grade (0-20): 14
Add another course? (y/n): n

Student 'Ali Ahmadi' was added successfully.

Select an option (1-8): 1

--- Add Student ---
First name: Sara
Last name: Karimi

Enter course information:
Course name: Mathematics
Course units: 3
Grade (0-20): 10
Add another course? (y/n): y

Enter course information:
Course name: Persian
Course units: 2
Grade (0-20): 13
Add another course? (y/n): n

Student 'Sara Karimi' was added successfully.
```

### نمونه خروجی گزارش‌ها

پس از ثبت اطلاعات بالا، با انتخاب گزینه `3. Display Students by GPA` خروجی زیر نمایش داده می‌شود:

```text
========== Students by GPA ==========
1. Ali Ahmadi — GPA: 15.25
2. Sara Karimi — GPA: 11.20
```

با انتخاب گزینه `4. Display Highest GPA`:

```text
========== Highest GPA: 15.25 ==========
- Ali Ahmadi (GPA: 15.25)
```

با انتخاب گزینه `5. Display Lowest GPA`:

```text
========== Lowest GPA: 11.20 ==========
- Sara Karimi (GPA: 11.20)
```

با انتخاب گزینه `6. Display Conditional Students`:

```text
========== Conditional Students (GPA below 12) ==========
- Sara Karimi (GPA: 11.20)
```

با انتخاب گزینه `7. Search Student by Last Name` و وارد کردن نام خانوادگی `Ahmadi`:

```text
Enter the student's last name: Ahmadi

========== Search Results: Ahmadi ==========
- Ali Ahmadi (GPA: 15.25)
```

جستجو نسبت به حروف بزرگ و کوچک انگلیسی حساس نیست. اگر چند دانشجو نام خانوادگی یکسان داشته باشند، معدل تمام افراد مطابق با آن نام نمایش داده می‌شود.

## 📋 گزینه‌های منوی برنامه

| گزینه | عملکرد |
|---|---|
| `1` | ثبت دانشجو و درس‌های او |
| `2` | نمایش تمام دانشجویان و جزئیات درس‌ها |
| `3` | نمایش دانشجویان مرتب‌شده بر اساس معدل |
| `4` | نمایش بیشترین معدل و دانشجو یا دانشجویان مربوطه |
| `5` | نمایش کمترین معدل و دانشجو یا دانشجویان مربوطه |
| `6` | نمایش دانشجویان با معدل کمتر از `12.0` |
| `7` | جستجوی دانشجو بر اساس نام خانوادگی |
| `8` | خروج از برنامه |

## ⚠️ قوانین ورودی و محدودیت‌ها

- نام، نام خانوادگی و نام درس نباید خالی باشند.
- تعداد واحد هر درس باید یک عدد صحیح مثبت باشد.
- نمره باید بین `0` تا `20` باشد؛ نمره اعشاری نیز پذیرفته می‌شود.
- در صورت وارد کردن مقدار نامعتبر، برنامه دوباره همان ورودی را درخواست می‌کند.
- هر دانشجو هنگام ثبت باید حداقل یک درس داشته باشد.
- اگر چند دانشجو معدل بالاتر یا پایین‌تر یکسان داشته باشند، اطلاعات تمام آن‌ها نمایش داده می‌شود.
- جستجو بر اساس نام خانوادگی، تمام افراد دارای آن نام خانوادگی را برمی‌گرداند.
- اطلاعات دانشجویان فقط در حافظه نگهداری می‌شوند و با خروج از برنامه از بین می‌روند. در نسخه فعلی ذخیره‌سازی در فایل یا پایگاه داده پیاده‌سازی نشده است.

## ⚙️ پیش‌نیازها

- Python نسخه 3.9 یا بالاتر
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

برای خروج از برنامه، گزینه `8. Exit` را انتخاب کنید یا کلیدهای `Ctrl+C` را فشار دهید.

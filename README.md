# Django Blog API

## תיאור הפרויקט

זהו פרויקט REST API מבוסס Django ו-Django REST Framework לניהול כתבות ותגובות.

המערכת מאפשרת:

- הרשמה והתחברות באמצעות JWT
- צפייה בכתבות
- חיפוש כתבות לפי כותרת / תוכן / תגית / שם מחבר
- הוספת תגובות לכתבות
- ניהול כתבות ותגובות בהתאם לרמות הרשאה

---

## מבנה הרשאות

### משתמש לא מחובר

- יכול לצפות בכל הכתבות
- יכול לצפות בתגובות של כל כתבה
- יכול לבצע חיפוש כתבות

### משתמש רשום (Authenticated)

- יכול להוסיף תגובה לכתבה

### מנהל (is_staff = True)

- יכול ליצור כתבה
- יכול לערוך כתבה
- יכול למחוק כתבה
- יכול למחוק תגובות

---

## טכנולוגיות

- Python
- Django
- Django REST Framework
- djangorestframework-simplejwt
- django-filter
- django-cors-headers
- python-decouple
- SQLite (ברירת מחדל)
- PostgreSQL (אופציונלי)

---

## הפעלה מהירה (SQLite)

ברירת המחדל של הפרויקט היא עבודה עם SQLite ולכן אין צורך בהגדרת מסד נתונים חיצוני.

### יצירת סביבת עבודה וירטואלית

```bash
python -m venv venv
```

הפעלה:

Mac / Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### התקנת חבילות

```bash
pip install -r requirements.txt
```

### הרצת מיגרציות

```bash
python manage.py migrate
```

### הרצת השרת

```bash
python manage.py runserver
```

השרת ירוץ בכתובת:
http://127.0.0.1:8000/

---

## הפעלה עם PostgreSQL (אופציונלי)

לשימוש ב-PostgreSQL יש ליצור קובץ `.env` ולהגדיר:

```
DB_ENGINE=postgres
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=True
```

לאחר מכן להריץ:

```bash
python manage.py migrate
python manage.py runserver
```

---

## נקודות קצה (API)

### Authentication

- POST /api/register/ — הרשמת משתמש חדש
- POST /api/token/ — קבלת access ו-refresh token
- POST /api/token/refresh/ — רענון access token

---

### Articles API

- GET /api/articles/ — קבלת כל הכתבות
- GET /api/articles/?search=<query> — חיפוש כתבות
- GET /api/articles/<id>/ — קבלת כתבה ספציפית
- POST /api/articles/ — יצירת כתבה (מנהל בלבד)
- PUT /api/articles/<id>/ — עדכון כתבה (מנהל בלבד)
- DELETE /api/articles/<id>/ — מחיקת כתבה (מנהל בלבד)

---

### Comments API

- GET /api/articles/<id>/comments/ — קבלת תגובות לכתבה
- POST /api/articles/<id>/comments/ — הוספת תגובה (משתמש רשום בלבד)
- DELETE /api/comments/<id>/ — מחיקת תגובה (מנהל בלבד)

---

## הערות

- ההתחברות מתבצעת באמצעות JWT.
- חיפוש מתבצע באמצעות SearchFilter של Django REST Framework.
- ההרשאות מבוססות על רמות גישה (אורח / משתמש רשום / מנהל).
- הפרויקט רץ כברירת מחדל עם SQLite ולכן ניתן לבדוק אותו ללא תלות במסד נתונים חיצוני.

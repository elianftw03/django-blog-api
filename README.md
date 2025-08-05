# פרויקט בלוג עם Django

## תיאור כללי

זהו פרויקט API מבוסס Django המאפשר למשתמשים:

- להירשם ולהתחבר
- לכתוב ולקרוא כתבות
- להוסיף תגובות לכתבות

כל משתמש יכול:

- לקרוא את כל הכתבות
- לקרוא תגובות לכל כתבה

משתמשים מחוברים יכולים:

- להוסיף כתבות
- להוסיף תגובות

משתמשים שהם כותבי התוכן יכולים:

- לערוך ולמחוק את הכתבות שלהם
- למחוק תגובות שהתקבלו על כתבות שלהם

## טכנולוגיות בשימוש

- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- Python Decouple
- django-cors-headers
- django-filter

## הפעלת הפרויקט

1. ליצור סביבת עבודה וירטואלית:

   ```bash
   python -m venv venv
   source venv/bin/activate  # בלינוקס/מק
   venv\Scripts\activate     # ב-Windows
   ```

2. התקנת חבילות:

   ```bash
   pip install -r requirements.txt
   ```

3. הגדרת קובץ `.env` עם משתנים חשובים כמו:

   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. להריץ מיגרציות:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. להריץ את השרת:
   ```bash
   python manage.py runserver
   ```

## נקודות קצה חשובות (API)

### הרשמה והתחברות:

- `POST /api/register/` — הרשמת משתמש
- `POST /api/token/` — התחברות וקבלת access/refresh token
- `POST /api/token/refresh/` — רענון access token

### כתבות:

- `GET /api/articles/` — קבלת כל הכתבות
- `POST /api/articles/` — יצירת כתבה חדשה (נדרש חיבור)
- `GET /api/articles/<id>/` — קבלת כתבה ספציפית
- `PUT /api/articles/<id>/` — עריכת כתבה (שלך בלבד)
- `DELETE /api/articles/<id>/` — מחיקת כתבה (שלך בלבד)

### תגובות:

- `GET /api/articles/<id>/comments/` — קבלת תגובות לכתבה
- `POST /api/articles/<id>/comments/` — הוספת תגובה (חיבור נדרש)
- `DELETE /api/comments/<id>/` — מחיקת תגובה (שלך בלבד או של כתבה שלך)

## הערות

- השתמשתי במשתמשים המובנים של Django.
- התממשקות עם PostgreSQL בעזרת משתני סביבה.
- הרשאות מבוססות על בעלות על אובייקט.

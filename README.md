# Human-Bone-Fragment-Counts

For backend ONLY

## Setup

After git pull:

Create virtual environment in directory with:

```bash
python3 -m venv env
```

Activate virtual environment:

```Bash
source env/Scripts/activate
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

Deactivate virtual environment with:

```Bash
deactivate
```

## Web Server

Work from first backend folder:

```bash
cd backend/
```

Start development server with:

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

## Populate DB

Populate elements and landmarks with:

```bash
python manage.py loaddata api/fixtures/
```

## API Usage

Using Httpie (installed above)

Register and login using:

```bash
http POST http://127.0.0.1:8000/auth/users/ username=new_username password=new_password
http POST http://127.0.0.1:8000/auth/tokens/login/ username=your_username password=your_password
```

Take note of token returned from login endpoint.

Token required.
Access element/landmark list using:

```bash
http GET http://127.0.0.1:8000/elements/ "Authorization: Token yourtokenlongsequenceofcharacters"
http GET http://127.0.0.1:8000/landmarks/ "Authorization: Token yourtokenlongsequenceofcharacters"
```

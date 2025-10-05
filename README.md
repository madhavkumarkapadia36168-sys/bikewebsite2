# Bike Shop (Flask)

Simple demo bike listing website built with Flask.

## Setup

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run:
```bash
python app.py
```

4. Open http://127.0.0.1:5000 in your browser.

Files:
- `app.py` — Flask application
- `data/bikes.json` — sample data store (JSON)
- `templates/` — Jinja2 HTML templates
- `static/css/style.css` — small stylesheet

You can edit `data/bikes.json` or use the "Add Bike" form to add items.

📄 README.md (Professional & Complete)
markdown
Copiar
Editar
# 🏷️ Coupon Discount API

A simple yet complete REST API built with **Python** and **Flask** to apply discount coupons and calculate the final price including tax. It includes a business logic layer, unit tests, a simulated regression scenario, and continuous integration via **GitHub Actions**.

---

## 📌 Key Features

- ✅ Apply discount logic with predefined coupons.
- ✅ Calculate final price with tax.
- ✅ Unit & integration tests using `pytest`.
- ✅ Regression detection.
- ✅ Automated CI workflow using GitHub Actions.

---

## 📁 Project Structure

cupones-api/
├── app/
│ ├── init.py
│ ├── cupones.py # Business logic
│ └── api.py # Flask API
├── tests/
│ ├── test_cupones.py # Unit tests
│ └── test_api.py # API tests
├── requirements.txt # Python dependencies
├── pytest.ini # Pytest configuration
└── .github/
└── workflows/
└── test-regresion.yml # GitHub Actions workflow

yaml
Copiar
Editar

---

## 🛠️ Step-by-Step Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cupones-api.git
cd cupones-api
2. Create and activate virtual environment
bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # for macOS/Linux
3. Install required packages
bash
Copiar
Editar
pip install -r requirements.txt
4. Run the Flask API locally
bash
Copiar
Editar
python app/api.py
The API will be available at http://localhost:5000/precio.

🧠 API Behavior
🔁 Endpoint: POST /precio
Request example:

json
Copiar
Editar
{
  "precio": 100,
  "cupon": "OFERTA10",
  "impuesto": 0.19
}
Response:

json
Copiar
Editar
{
  "precio_final": 107.1
}
🧪 Running Tests
To run all tests:

bash
Copiar
Editar
pytest
If you face import issues, use:

bash
Copiar
Editar
PYTHONPATH=. pytest
The tests include:

Coupon discount logic

Final price calculation with tax

Full POST request integration

🔄 Simulating a Regression (Step-by-step)
Open app/cupones.py.

Remove one coupon from the dictionary:

python
Copiar
Editar
# Removed this line (by mistake)
"BIENVENIDA": 0.15
Run the tests:

bash
Copiar
Editar
pytest
✅ You'll see a failure in the test that checks the "BIENVENIDA" coupon — this is a regression.

🧯 Fixing the Regression
Add the removed coupon back in cupones.py:

python
Copiar
Editar
"BIENVENIDA": 0.15
Re-run the tests:

bash
Copiar
Editar
pytest
✅ All tests should pass again.

🤖 Automating Tests with GitHub Actions
This project includes a CI workflow that runs tests on every push or pull request to main.

Setup:
Create the file .github/workflows/test-regresion.yml with:

yaml
Copiar
Editar
name: Regression Tests - Coupons

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

      - name: Run tests
        run: |
          source venv/bin/activate
          pytest
Commit and push to GitHub:

bash
Copiar
Editar
git add .
git commit -m "Add CI workflow for regression testing"
git push origin main
Go to the Actions tab in GitHub to see your CI workflow running.

🧪 Sample Tests (unit + integration)
tests/test_cupones.py
python
Copiar
Editar
from app.cupones import aplicar_cupon, calcular_precio_final

def test_discount_oferta10():
    assert aplicar_cupon(100, "OFERTA10") == 90.0

def test_discount_super20():
    assert aplicar_cupon(200, "SUPER20") == 160.0

def test_discount_bienvenida():
    assert aplicar_cupon(100, "BIENVENIDA") == 85.0

def test_price_with_tax():
    assert calcular_precio_final(100, "OFERTA10") == 107.1
tests/test_api.py
python
Copiar
Editar
import json
from app.api import app

def test_post_precio():
    client = app.test_client()
    response = client.post('/precio', data=json.dumps({
        "precio": 100,
        "cupon": "OFERTA10",
        "impuesto": 0.19
    }), content_type='application/json')
    
    assert response.status_code == 200
    assert response.get_json()["precio_final"] == 107.1
✅ Tips
Always use pytest with PYTHONPATH=. when running locally to avoid import issues.

Keep your tests updated when you change business logic.

Check GitHub Actions on each commit to catch regressions early.
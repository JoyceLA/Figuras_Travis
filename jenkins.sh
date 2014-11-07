pip install -r requirements.txt
autopep8 -ir .
flake8 --max-complexity=6 --exclude=*.txt,*.md --max-line-length=200 .
lettuce AceptanceTest
cd UnitTest
python TestCase.py
coverage run --branch TestCase.py
coverage report -m
coverage html --title="Reporte Figuras HTML"

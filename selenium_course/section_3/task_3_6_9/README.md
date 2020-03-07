## Task 3.6.9: Running autotests for different interface languages

### Requirements

* Python 3.5+
* Webdrivers:
  * chromedriver (for Google Chrome)
  * geckodriver (for Firefox)

Install packages using pip according to the requirements.txt.
```bash
pip install -r requirements.txt 
```
Or
```bash
pip install selenium==3.14.0
pip install pytest==5.1.1
```
### Usage

```bash
pytest -s -v --browser_name=chrome --language=es test_items.py
```
Parameters:
* **--browser_name** - chrome (default) or firefox
* **--language** - language code
* **-s** - console log message
* **-v** - verbose info
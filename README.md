# stock-prediction-bot


Steps To Establish Project :

Step 1: Create Folder and open in code editor and type following command on terminal

```
git clone https://github.com/naimish73/stock-prediction-bot.git
```

Step 2 :
```
cd stock-prediction-bot
```
- Create Virtual environment then install dependancies

```
pip install -r requirements.txt
```

Step 3 :

- Create `.env` file which have deta_key=`your_deta_key` 

- Then copy the path of `.env` file and give it to  `load_env(copied_path_to_env)` in `Stb_project/stb/db.py` 

```
cd Stb_Project

python manage.py shell

```
- After Shell Open follow the command one by one :

```

In [1]: from stb.db import save_stocks_to_database,fetch_stocks_dec

In [2]: stocks=fetch_stocks_dec()

In [3]: save_stocks_to_database(stocks)

In [4]: exit()
```

Step 4:` Create superUser (fill all the details after running command ) to see database `or `you can run the website`

```
python manage.py createsuperuser

```

Finally run the website:

```
python manage.py runserver
```

---



Follow this for Issue & PR
feat: 🚀 Represents the addition of a new feature.

fix: 🐛 Indicates a bug fix or correction.

chore: 🧹 Represents routine tasks, maintenance, or chores.

docs: 📚 Indicates changes or additions to documentation.

style: 🎨 Represents code style changes, such as formatting or styling.

test: 🧪 Indicates the addition or modification of tests.

refactor: 🔄 Signifies code refactoring or restructuring.

build: 🛠️ Indicates changes to the build system or build-related files.

ci: 🔄 Represents changes to the Continuous Integration (CI) configuration or scripts.

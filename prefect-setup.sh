python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
#prefect create project beautiful-test
#prefect register --project beautiful-test -p flows/
#prefect agent local start --label dev --no-hostname-label 
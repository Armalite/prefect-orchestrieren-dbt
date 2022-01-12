import prefect
from prefect import task, Flow
from prefect.tasks.dbt.dbt import DbtShellTask

@task
def output_config():
    logger = prefect.context.get("logger")
    logger.info("Fetching DBT Runner container to run with following settings: ")

@task()
def run_dbt():
    logger = prefect.context.get("logger")
    logger.info("Executing DBT Runner")

flow = Flow("dbt-transformations", tasks=[output_config, run_dbt])

flow.run()
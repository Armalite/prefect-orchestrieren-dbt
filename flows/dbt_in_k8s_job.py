from prefect.tasks.kubernetes import RunNamespacedJob

job_template = open('kube/dbt_cronjob.yaml')

job_run_task = RunNamespacedJob(body=job_template)

print("Hello lol")
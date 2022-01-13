import prefect
from prefect import task, Flow
from prefect.tasks.kubernetes import RunNamespacedJob
from prefect.run_configs import LocalRun, KubernetesRun, RunConfig

job_template = open('kube/test_cronjob.yaml')

job_run_task = RunNamespacedJob(body=job_template)

@task
def k8s_hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello, Beautiful Kubernetes!")

flow = Flow("k8s-greetings", run_config=KubernetesRun(), tasks=[k8s_hello_task])

flow.register(project_name="beautiful-test")
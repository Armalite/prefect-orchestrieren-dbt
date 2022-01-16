import prefect
from prefect import task, Flow
from prefect.tasks.kubernetes import RunNamespacedJob
from prefect.run_configs import LocalRun, KubernetesRun, RunConfig
import yaml

job_template = open('kube/test_cronjob.yaml')
job_template_dict = yaml.load(job_template)

k8s_job_run_task = RunNamespacedJob(body=job_template_dict)

@task
def k8s_hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello, Beautiful Kubernetes!")

flow = Flow("k8s-greetings", run_config=KubernetesRun(), tasks=[k8s_job_run_task])

flow.run()
#flow.register(project_name="beautiful-test")
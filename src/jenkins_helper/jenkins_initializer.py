import os

from .jenkins_util import JenkinsUtil


class JenkinsInitializer():

    def __init__(self):
        self.jenkins_prod = JenkinsUtil(
            jenkins_url="https://jenkins-k8s.sd-prod.cloudera.com/",
            jenkins_username=os.environ["JENKINS_USER"],
            jenkins_password=os.environ["JENKINS_PASSWORD"]
        )

    def promote_mlx_crud_app(self, build: str, tenant_name: str):
        """Promote MLX-CRUD-APP build to required tenant"""
        job_name = None
        if tenant_name == "dev":
            job_name = "manowar-mlx-dev-build"
        elif tenant_name == "int":
            job_name = "manowar-mlx-int-build"
        params = {"VERSION": build}
        return self.jenkins_prod.run_job(job_name, params)

    def promote_cml_config_store(self, build: str, tenant_name: str):
        """Promote CML-Config-Store build to required tenant"""
        job_name = None
        if tenant_name == "dev":
            job_name = "manowar-cml-config-store-dev-build"
        elif tenant_name == "int":
            job_name = "manowar-cml-config-store-int-build"
        params = {"VERSION": build}
        return self.jenkins_prod.run_job(job_name, params)


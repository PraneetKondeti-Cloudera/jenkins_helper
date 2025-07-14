import os

from .jenkins_util import JenkinsUtil


class JenkinsInitializer():

    def __init__(self):
        self.jenkins_prod = JenkinsUtil(
            jenkins_url="https://jenkins-k8s.sd-prod.cloudera.com/",
            jenkins_username=os.environ["JENKINS_PROD_USER"],
            jenkins_password=os.environ["JENKINS_PROD_PASSWORD"]
        )
        self.jenkins_master1 = JenkinsUtil(
            jenkins_url="https://jenkins-k8s.sd-master1.cloudera.com/",
            jenkins_username=os.environ["JENKINS_MASTER1_USER"],
            jenkins_password=os.environ["JENKINS_MASTER1_PASSWORD"]
        )

    def promote_mlx_crud_app(self, build: str, tenant_name: str):
        """Promote MLX-CRUD-APP build to required tenant"""
        job_name = None
        tenant_name = tenant_name.replace("mow-", "")
        if tenant_name == "dev":
            job_name = "manowar-mlx-dev-build"
        elif tenant_name == "int":
            job_name = "manowar-mlx-int-build"
        else:
            return "Tenant  is not supported"
        params = {"VERSION": build}
        return self.jenkins_prod.run_job(job_name, params)

    def promote_cml_config_store(self, build: str, tenant_name: str):
        """Promote CML-Config-Store build to required tenant"""
        job_name = None
        tenant_name = tenant_name.replace("mow-", "")
        if tenant_name == "dev":
            job_name = "manowar-cml-config-store-dev-build"
        elif tenant_name == "int":
            job_name = "manowar-cml-config-store-int-build"
        else:
            return "Tenant  is not supported"
        params = {"VERSION": build}
        return self.jenkins_prod.run_job(job_name, params)

    def integrate_mlxcrudapp_cdsw(self, branch: str = "master", cdsw_version: str = "latest"):
        """Integrate MLX-CRUD-APP with CDSW"""
        branch = branch.lower().replace("mlx-crud-app-", "")
        if branch == "master":
            job_name = "mlx_integrate_cdsw_build_with_cp_git_master"
        else:
            job_name = f"mlx_integrate_cdsw_build_with_cp_git_MLX-CRUD-APP-{branch}"
        params = {
            "CDSW_RE_VERSION": cdsw_version,
            "DRY_RUN": True,
            "FORCE_INTEGRATE": True
        }
        return self.jenkins_master1.run_job(job_name, params)

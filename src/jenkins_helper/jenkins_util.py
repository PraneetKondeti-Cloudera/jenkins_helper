
import time
import logging

import jenkins
LOG = logging.getLogger()

class JenkinsUtil:

    """Utility class to wrap around jenkins requests"""

    def __init__(
        self,
        jenkins_url,
        jenkins_username,
        jenkins_password,
    ):  # pylint: disable=unused-argument
        self.jenkins_server = jenkins.Jenkins(
            url=jenkins_url, username=str(jenkins_username), password=jenkins_password
        )

    def run_job(self, job_name, params=None):
        """Execute the jenkins job with params"""

        print(f"Running job: {job_name} with params: '{params}'", job_name, params)
        queue_number = self.jenkins_server.build_job(job_name, params)
        print("Run queued with id: %s", queue_number)
        try:
            # Wait for the build to finish
            time.sleep(10)
            build_number = self.jenkins_server.get_job_info(job_name)['lastBuild']['number']
            build_info = self.jenkins_server.get_build_info(job_name, build_number)
            build_url = build_info['url']
            print("Build URL:", build_url)
            print(build_url)
            return build_url
        except jenkins.JenkinsException as e:
            print("Failed to trigger the build for Jenkins job: {}. Error: {}".format(job_name, e))
            return False
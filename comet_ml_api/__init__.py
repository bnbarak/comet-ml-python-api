import helpers

class CometMlApi:
    def __init__(self, api_key, version = helpers.DEFAULT_VERSION):
        self.version = version
        self.api_key = api_key

    def get_version(self):
        return self.version

    def get_url(self):
        return helpers.URLS[self.version]

    def projects(self):
        params = {}
        return helpers.get_request("projects", params, self.version, self.api_key)

    def experiments(self, project_id):
        params = {'projectId': project_id}
        return helpers.get_request("experiments", params, self.version, self.api_key)

    def experiment_html(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/html", params, self.version, self.api_key)

    def experiment_code(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/code", params, self.version, self.api_key)

    def experiment_stdout(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/stdout", params, self.version, self.api_key)

    def experiment_installed_packages(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/installed-packages", params, self.version, self.api_key)

    def experiment_graph(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/graph", params, self.version, self.api_key)

    def experiment_images(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/images", params, self.version, self.api_key)

    def experiment_params(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/params", params, self.version, self.api_key)

    def experiment_metrics(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/metrics", params, self.version, self.api_key)

    def experiment_log_other(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/log-other", params, self.version, self.api_key)

    def experiment_metrics_raw(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/metrics-raw", params, self.version, self.api_key)






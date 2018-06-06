from comet_ml_api import CometMlApi

comet = CometMlApi('bvtC8QqL6pQH4B1yhsUO9TICc', 'v1')
project_id = 'b1f37ccd4b244c68ae0155a797ac3632'
experiment_key = '625fa39eb4ac41e693cb10c0bd8f37d9'

print comet.get_version()
print comet.projects()
print comet.experiments(project_id)
print comet.experiment_html(experiment_key)
print comet.experiment_code(experiment_key)
print comet.experiment_stdout(experiment_key)
print comet.experiment_installed_packages(experiment_key)
print comet.experiment_graph(experiment_key)
print comet.experiment_images(experiment_key)
print comet.experiment_params(experiment_key)
print comet.experiment_metrics(experiment_key)
# print comet.experiment_metrics_raw(experiment_key)
print comet.experiment_log_other(experiment_key)

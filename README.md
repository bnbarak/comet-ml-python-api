# Python3 SDK for Comet.ml

Based on the supercharge machine learning library [comet.ml](http://comet.ml)

## Documentation
See Comet.ml API [documentation](https://comet.ml/docs/rest-api/endpoints/)

## Installation
`pip install comet_ml_api`


## Example
```
from comet_ml_api import CometMlApi

comet = CometMlApi("bvtC8QqL6pQH4B1yhsUO9TICc", "v1")
project_id = 'b1f37ccd4b244c68ae0155a797ac3632'
experiment_key = '625fa39eb4ac41e693cb10c0bd8f37d9'

projects = comet.projects()
```

# print comet.experiments(projectId)
# print comet.experiment_html(experiment_key)
# print comet.experiment_code(experiment_key)
# print comet.experiment_stdout(experiment_key)
# print comet.experiment_installed_packages(experiment_key)
# print comet.experiment_graph(experiment_key)
# print comet.experiment_images(experiment_key)
# print comet.experiment_params(experiment_key)
# print comet.experiment_metrics(experiment_key)
# print comet.experiment_metrics_raw(experiment_key)
# print comet.experiment_log_other(experiment_key)

## API
### Projects
```
print comet.projects()
```
### Experiments
```
# print comet.experiments(projectId)
```
### HTML
```
print comet.experiment_html(experiment_key)
```
### Code
```
print comet.experiment_code(experiment_key)
```
### Stdout
```
print comet.experiment_stdout(experiment_key)
```
### Installed Packages
```
print comet.experiment_installed_packages(experiment_key)
```
### Graph Definition
```
print comet.experiment_graph(experiment_key)
```
### Images
```
print comet.experiment_images(experiment_key)
```
### Hyper Params
```
print comet.experiment_params(experiment_key)
```
### Metrics
```
print comet.experiment_metrics(experiment_key)
```
### Log Other
```
print comet.experiment_log_other(experiment_key)
```
### Raw Metrics
```
print comet.experiment_metrics_raw(experiment_key)
```

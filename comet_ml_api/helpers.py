import requests

URLS = {
    "v1": "https://staging.comet.ml/api/rest/v1/"
}
DEFAULT_VERSION = 'v1'
COMET_HEADER = 'Authorization'
END_POINTS = {
  'projects': 'projects',
  'experiments': 'experiments',
  'experiment/html': 'experiment/html',
  'experiment/code': 'experiment/code',
  'experiment/stdout': 'experiment/stdout',
  'experiment/images': 'experiment/images',
  'experiment/graph': 'experiment/graph',
  'experiment/params': 'experiment/params',
  'experiment/metrics': 'experiment/metrics',
  'experiment/log-other': 'experiment/log-other',
  'experiment/metrics-raw': 'experiment/metrics-raw',
  'experiment/installed-packages': 'experiment/installed-packages',
}

def get_url(version):
    return URLS[version]

def get_end_point(end_point):
    return END_POINTS[end_point]

def get_request(end_point, params, version, api_key):
    url = get_url(version) + get_end_point(end_point)
    headers = {COMET_HEADER: api_key}
    print(url)
    print(params)
    response = requests.get(url, params=params, headers=headers)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print "Error: " + str(e)
        return "Error: {}".format(e)

    return response.json()





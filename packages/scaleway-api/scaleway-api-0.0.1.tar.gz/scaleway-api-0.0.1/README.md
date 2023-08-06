# Scaleway API
This is an unofficial wrapper around the Scaleway APIs based on [Hammock](https://pypi.org/project/hammock/).

## Usage
```
from scaleway_api import Scaleway

scw = Scaleway("nl-ams", "<SECRET KEY>")
servers = scw.instance.servers.GET()

for server in servers.json().get("servers", {}):
    print(f'Server Name: {server["name"]}')
```

## Environment Variables
The Scaleway API will try to pull the following environment variables for convencience.
| Environment Variable | Description |
| :-- | :-- |
| SCW_SECRET_KEY | Your Scaleway key. More information can be found [in Scaleway's documentation]() |
| SCW_DEFAULT_REGION | Should be either `nl-ams` or `fr-par` (Default: `fr-par`) |
| SCW_DEFAULT_ZONE |  Should be either `nl-ams-1` or `fr-par-1` (Default: `REGION-1` / `fr-par-1`) |
| SCW_API_VERSION |  Currently only `v1` is available. Added to future-proof the library. |

## Development
Happy to receive pull requests.

### Setup
```
python3 setup.py install
pip install -r requirements-dev.txt
```

### Test
```
python3 setup.py test
```

### Coverage Report
```
coverage run -m unittest discover && coverage report
```
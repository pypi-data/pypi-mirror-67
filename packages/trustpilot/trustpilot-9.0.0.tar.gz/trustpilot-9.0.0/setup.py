# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trustpilot']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0', 'click>=7.1.1,<8.0.0', 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['trustpilot_api_client = trustpilot.cli:cli']}

setup_kwargs = {
    'name': 'trustpilot',
    'version': '9.0.0',
    'description': 'trustpilot api client including cli tool',
    'long_description': '# trustpilot\n\n[![Build Status](https://travis-ci.org/trustpilot/python-trustpilot.svg?branch=master)](https://travis-ci.org/trustpilot/python-trustpilot) [![Latest Version](https://img.shields.io/pypi/v/trustpilot.svg)](https://pypi.python.org/pypi/trustpilot) [![Python Support](https://img.shields.io/pypi/pyversions/trustpilot.svg)](https://pypi.python.org/pypi/trustpilot)\n\nPython HTTP client for [Trustpilot](https://developers.trustpilot.com/).\n\n### Features\n\n- Extends the [`requests.Session`](http://docs.python-requests.org/en/master/api/#requests.Session) class with automatic authentication for public and private endpoints\n- GET, POST, PUT, DELETE, HEAD, OPTIONS and PATCH methods are exposed on module level\n- Implements session factory and default singleton session\n- Provides a simple hook system\n- [CLI](#CLI) tool with basic HTTP commands\n\n\n## Installation\n\nInstall the package from [PyPI](http://pypi.python.org/pypi/) using [pip](https://pip.pypa.io/):\n\n```\npip install trustpilot\n```\n\n## Usage\n\n_(for **full usage documentation** checkout [docs](https://github.com/trustpilot/python-trustpilot/blob/master/docs/README.md))_\n\n```python\nfrom trustpilot import client\nclient.default_session.setup(\n    api_host="https://api.trustpilot.com"\n    api_key="YOUR_API_KEY"\n)\nresponse = client.get("/foo/bar")\nstatus_code = response.status_code\n```\n\nYou can rely on environment variables for the setup of sessions so\n\n```bash\n$ env\nTRUSTPILOT_API_HOST=https://api.trustpilot.com\nTRUSTPILOT_API_KEY=foo\nTRUSTPILOT_API_SECRET=bar\n```\n\n### CLI\n\nThe `trustpilot_api_client` command is bundled with the install\n\n```bash\nUsage: trustpilot_api_client [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --host TEXT                     Host name\n  --version TEXT                  Api version\n  --key TEXT                      Api key\n  --secret TEXT                   Api secret\n  --token_issuer_host TEXT        Token issuer host name\n  --username TEXT                 Trustpilot username\n  --password TEXT                 Trustpilot password\n  -c, --config FILENAME           Json config file name\n  -e, --env FILENAME              Dot env file\n  -of, --outputformat [json|raw]  Output format, default=json\n  -v, --verbose                   Verbosity level\n  --help                          Show this message and exit.\n\nCommands:\n  create-access-token  Get an access token\n  delete               Send a DELETE request\n  get                  Send a GET request\n  post                 Send a POST request with specified data\n  put                  Send a PUT request with specified data\n```\n\nYou can also supply the variables with:\n\n**--config/-c** : As JSON config file in the following format:\n\n```json\n{\n  "TRUSTPILOT_API_HOST": "foo",\n  "TRUSTPILOT_API_KEY": "bar",\n  "TRUSTPILOT_API_SECRET": "baz",\n  "TRUSTPILOT_API_VERSION": "v1",\n  "TRUSTPILOT_USERNAME": "username",\n  "TRUSTPILOT_PASSWORD": "password"\n}\n```\n\nor **--env/-e** : As DotEnv config file in the following format:\n\n```ini\nTRUSTPILOT_API_HOST=foo\nTRUSTPILOT_API_KEY=bar\nTRUSTPILOT_API_SECRET=baz\nTRUSTPILOT_API_VERSION=v1\nTRUSTPILOT_USERNAME=username\nTRUSTPILOT_PASSWORD=password\n```\n\n## Changelog\n\nsee [HISTORY.md](https://github.com/trustpilot/python-trustpilot/blob/master/HISTORY.md)\n\n## Issues / DEV\n\nReport issues [here](https://github.com/trustpilot/python-trustpilot/issues) and we welcome collaboration through PullRequests :-)\n',
    'author': 'Johannes Valbjørn',
    'author_email': 'jgv@trustpilot.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/trustpilot/python-trustpilot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

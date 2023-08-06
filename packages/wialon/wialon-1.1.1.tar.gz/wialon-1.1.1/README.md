# Wialon SDK for Python
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://gitlab.com/goldenm-software/open-source-libraries/wialon-python/blob/master/LICENSE) [![pypi version](https://badge.fury.io/py/wialon.svg)](https://pypi.org/project/wialon/)

## Installation
Use the package manager [pip](https://pypi.org/) to install wialon-python.
```bash
pip3 install wialon
```

## Usage
```python
"""
WialonSDK example usage
"""
from wialon.sdk import WialonSdk, WialonError, SdkException

# Initialize Wialon instance
sdk = WialonSdk(
  is_development=True,
  scheme='https',
  host='hst-api.wialon.com',
  port=0,
  session_id='',
  extra_params={}
)

try:
  token = '' # If you haven't a token, you should use our token generator
             # https://goldenmcorp.com/resources/token-generator
  response = sdk.login(token)
  print(response)

  parameters = {
    'spec':{
      'itemsType': str,
      'propName': str,
      'propValueMask': str,
      'sortType': str,
      'propType': str,
      'or_logic':bool
    },
    'force': int,
    'flags': int,
    'from': int,
    'to': int
  }

  units = sdk.core_search_items(parameters)

  sdk.logout()
except SdkException as e:
  print(f'Sdk related error: {e}')
except WialonError as e:
  print(f'Wialon related error: {e}')
except Exception as e:
  print(f'Python error: {e}')
```

## Methods available
For more information, please go to [Wialon Remote API documentation](https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/apiref)

## Work with us!
Feel free to send us an email to [sales@goldenmcorp.com](mailto:sales@goldenmcorp.com)

## Contributing
Merge requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
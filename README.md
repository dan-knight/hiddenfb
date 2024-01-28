# HiddenFB

HiddenFB is a Python application for football data science, empowering professional sports analysts and top-level coaches with advanced data science techniques that dissect player performance, decode tactical strategies, and forecast match outcomes. Uncover actionable insights through comprehensive data visualization and machine learning models, driving strategic decisions at the highest levels of the game.

## Installation

During initial development, this project will only be available as source code. In future, built releases will be available for easier installation.

```bash
git clone git@github.com:dan-knight/hiddenfb.git
```

### Environment Setup

Using a [virtual environment](https://docs.python.org/3/library/venv.html) is strongly recommended to avoid problems and ensure consistent, accurate analysis.

All required dependencies are listed in `requirements.txt`, and can be easily installed from the project's root directory.

```bash
pip install -r requirements.txt
```
 
## Usage

During initial development, the application's functionality will only be available as a Python import. More convenient interfaces such as a GUI, web API, and/or CLI will be made available in future releases.

The application can be imported as a whole.

```python
import hiddenfb
```

Functionality can be also imported selectively as needed.
```python
import hiddenfb.app
from hiddenfb.app.analysis import xG
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

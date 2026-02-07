# AirBnB Clone - RESTful API & Web Framework

## Description
AirBnB clone v3 is an enhanced version of the previous iteration, introducing new functionalities and improvements. It retains the command-line interface and utilizes object-oriented programming to efficiently manage data. In this version, the project expands its capabilities with the addition of a powerful RESTful API and a MySQL database backend.

A new route, `/api/v1/`, has been implemented to house the first version of the RESTful API. This API provides the ability to access and modify data stored in both the MySQL database and the JSON storage. It supports various HTTP methods to facilitate different operations:

* **GET**: Retrieve information
* **POST**: Create new information
* **PUT**: Update existing information
* **DELETE**: Delete information

CORS (Cross-Origin Resource Sharing) has been configured to allow unrestricted access to the API resources from any software.

## Table of Contents
* [Environment](#environment)
* [Requirements](#requirements)
* [Installation](#installation)
* [Testing](#testing)
* [Console Usage](#console-usage)
* [API Usage](#api-usage)
* [Web Flask Usage](#web-flask-usage)
* [Project Structure](#project-structure)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3).

## Requirements
To run this project, you need:
* **Python 3**
* **MySQL**
* **Flask**
* **Flask-CORS**
* **SQLAlchemy**
* **mysqlclient**

Install dependencies using:
```bash
pip3 install Flask Flask-CORS SQLAlchemy mysqlclient
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ahmedAhmedHamed/AirBnB_clone_v3.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone_v3
   ```

## Testing
To run all tests:
```bash
python3 -m unittest discover tests
```
To run tests for a specific file:
```bash
python3 -m unittest tests/test_models/test_base_model.py
```

## Console Usage
The console is a command interpreter to manage your AirBnB objects.

### Interactive Mode
```bash
./console.py
(hbnb) create State name="California"
(hbnb) all State
(hbnb) show State <id>
(hbnb) destroy State <id>
(hbnb) quit
```

### Non-Interactive Mode
```bash
echo "help" | ./console.py
```

## API Usage
To run the API:
```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m api.v1.app
```

Example API request:
```bash
curl -X GET http://0.0.0.0:5000/api/v1/status
```

## Web Flask Usage
To run the Flask web application:
```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
```

## Project Structure
* `api/`: RESTful API implementation
* `console.py`: Command interpreter
* `models/`: Data models and storage engines (FileStorage, DBStorage)
* `tests/`: Unit tests
* `web_flask/`: Flask web application
* `web_static/`: Static HTML/CSS files

## Authors
* Jennifer Huang - [Github](https://github.com/jhuang10123)
* Alexa Orrico - [Github](https://github.com/alexaorrico)
* Joann Vuong - [Github](https://github.com/jvuong)
* Youssef Nagib - [Github](https://github.com/yousefnagib)
* Ahmed Hamed - [Github](https://github.com/ahmedAhmedHamed)

## License
Public Domain.

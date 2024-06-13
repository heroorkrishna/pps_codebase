## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x
- pip (Python package installer)
- MySQL
- conda or virtualenv (optional but recommended)

## Setup Instructions

### 1. Clone the repository

git clone https://krishna-ahana@bitbucket.org/myahana-space/pps_backend.git

### Using Conda Environment

    $ conda create --name <env name> python==<version>
    
    $ conda activate <env name>

### Using Virtualenv gloabally
    $ pip install virtualenv
    
### Create and activate your virtual environment:
    $ virtualenv  venv -p python3
    
    $ source venv/bin/activate
    
    
### Install the dependencies
    $ pip install -r requirements.txt

### Migratons works

    $ python manage.py makemigrations
    
    $ python manage.py migrate
    
### Run it
    $ python manage.py runserver
 
### Access the application via
    link - http://localhost:8000/app/invoice

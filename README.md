# ansibleapi
# Ansible API

## Description
This REST API, developed using Django and Django REST Framework, enables users to launch Ansible playbooks. It's designed for developers and sysadmins who need to automate the execution of playbooks via a simple API interface.

## Features
- Launch Ansible playbooks directly through RESTful calls.
- Easy integration with existing systems using standard HTTP methods.
- Built with Django, ensuring robust, scalable, and secure API endpoints.

## Prerequisites
- Python 3.8+
- Django 3.1+
- Django REST Framework
- Ansible

## Installation
```bash
git clone https://github.com/romposdia/ansibleapi.git
cd ansibleapi
pip install -r requirements.txt

## Usage
To start the server:

```bash
python manage.py runserver


Example of launching a playbook:
```bash
curl -X POST -d '{"playbook": "path/to/playbook.yml"}' http://localhost:8000/api/launch

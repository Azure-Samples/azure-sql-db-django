---
page_type: sample
languages:
- python
- django
- sql
products:
- vs-code
- azure-sql-database
- mssql-django

description: "Creating REST API with Python, Django and Azure SQL"
urlFragment: "azure-sql-db-django"
---

# Creating REST API with Python, Django and Azure SQL

[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/abhimantiwari/azure-sql-db-django/blob/main/LICENSE)

The sample uses the [Django](https://www.djangoproject.com/) web framework and [Django Rest framework](https://www.django-rest-framework.org/) package to easily implement REST APIs. [mssql-django](https://github.com/microsoft/mssql-django) v1.1 used to establish database connectivity with Azure SQL.

> [!NOTE]
> [mssql-django](https://github.com/microsoft/mssql-django) is a fork of [django-mssql-backend](https://pypi.org/project/django-mssql-backend/). This driver provides an enterprise database connectivity option for the Django Web Framework, with support for Microsoft SQL Server and Azure SQL Database.
>[ssql-django](https://github.com/microsoft/mssql-django) supports Django 2.2, 3.0, 3.1, 3.2 and 4.0.

## Download the sample code

Clone this repository:

```bash
git clone https://github.com/azure-samples/azure-sql-db-django
```

Alternatively you can clone the code using visual studio code as well.

- Open the folder location where you want to clone the code
- In Visual Studio Code, select Source Control > ... > Clone (or select View, Command Palette and enter Git:Clone), paste the [Git repository URL](https://github.com/azure-samples/azure-sql-db-django.git), and then select Enter</>.

Once you have the code downloaded to your local computer. You should see folder structure as below:

```properties
azure-sql-db-django
 ┣ customerapi
 ┃ ┣ migrations
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ serializers.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ django-sql-project
 ┃ ┣ asgi.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┣ wsgi.py
 ┃ ┗ __init__.py
 ┣ LICENSE
 ┣ manage.py
 ┣ README.md
 ┗ requirements.txt
```

## Create Azure SQL Database

If you don't have an Azure SQL server already, you can create one (no additional costs for a server) by running the following [AZ CLI](https://docs.microsoft.com/en-us/cli/azure/) command (via [WSL](https://docs.microsoft.com/en-us/windows/wsl/), or Linux or [Azure Cloud Shell](https://azure.microsoft.com/en-us/features/cloud-shell/)):

Create a resource group if you don't have one already created:

```azurecli-interactive
az group create -l <location> -n <MyResourceGroup>
```

Create the Database Server:

```azurecli-interactive
az sql server create -n <server-name> -l <location> --admin-user <admin-user> --admin-password <admin-password> -g <resource-group>
```

> [!NOTE]
> Make sure to note the database name, username and password somewhere safe.

Create a new Azure SQL database:

```azurecli-interactive
az sql db create -g <resource-group> -s <server-name> -n my-db --service-objective GP_Gen5_2
```

Make sure you have the firewall configured to allow your machine to access Azure SQL:

```azurecli-interactive
az sql server firewall-rule create --resource-group <resource-group> --server <server-name> --name AllowMyClientIP_1 --start-ip-address <your_public_ip> --end-ip-address <your_public_ip>
```

You can get your public IP [here](https://ipinfo.io/ip) or through other ways, for example: https://ifconfig.me/

## Setup the local environment

Make sure you have [Python](https://www.python.org/) => 3.8.10 installed on your machine.

To confirm you can run `python` or `python3` on terminal.

```python
python --version
```

> [!NOTE]
>All the commands shown here are for Windows. If you are working on any other OS/ environment e.g. Linux, MAC etc. change these commands accordingly.

Make sure you have [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) installed and create a new virtual enviroment in the folder where you have cloned the repository:

```
python3 -m venv env
```

> [!NOTE]
> In the above command the second parameter `venv` is the location to create virtual environment.\
> `venv` will create a virtual Python installation in the `env` folder.\
> You should exclude your virtual environment directory from your version control system using `.gitignore` or similar.

Before you start installing or using django packages in your virtual environment, you'll need to [activate it](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment), for example on Windows:

```
.\env\Scripts\activate
```

> [!NOTE]
> You can confirm, you’re in the virtual environment by checking the location of your Python interpreter. It should be in the `env` directory.
>
> ```python
> where python
> ```
>
> As long as your virtual environment is activated, `pip` will install packages into that specific environment and you’ll be able to import and use packages in your Python application.

## Install the dependencies

> Make sure virtual environment is active and you are into your `working_folder\azure-sql-db-django`.

> [!TIP]
> You can install all the required packages in one go by running the below command and directly move to Database ConnectionString **Configuration** section or may follow the instructions to execute them one by one:
>
> ```python
> pip install -r .\requirements.txt
> ```

Install [Django](https://www.djangoproject.com/download/):

```python
pip install django
```

Also, install [Django REST framework](hhttps://www.django-rest-framework.org/#installation) for REST API:

```python
pip install djangorestframework
```

You should also install [django-cors-headers](https://pypi.org/project/django-cors-headers/). It's a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).

```python
pip install django-cors-headers
```

> [!NOTE]
> Adding [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) headers allows your resources to be accessed on other domains. It’s important you understand the implications before adding the headers since you could be unintentionally opening up your site’s private data to others.

## Configure Azure SQL connectivity with Django App

### Dependencies

- pyodbc 3.0 or newer
- Microsoft SQL Server ODBC driver 

### Installation

- Install pyodbc:

    ```python
    pip install pyodbc
    ```

- Install mssql-django:

    ```python
    pip install mssql-django
    ```

- Install ODBC driver: [Instructions](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)

### Configuration

Configure the Database ConnectionString in the settings.py file used by your Django project:

```sql
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'Database_name',
        'HOST': "xyz.database.windows.net",
        'PORT': '1433',
        'USER': 'User_name',
        'PASSWORD': 'db_pwd',
        'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
    }
}
```

To connect Azure SQL DB using MSI (Managed Service Identity), you can have settings as below:

```sql
DATABASES = {
    'default': {
         'ENGINE': 'mssql',
         'HOST': 'xyz.database.windows.net',
         'NAME': 'Database_name', 
         'PORT': '', 
         'Trusted_Connection': 'no', 
         'OPTIONS': { 
             'driver': 'ODBC Driver 17 for SQL Server', 
             'extra_params': "Authentication=ActiveDirectoryMsi;Encrypt=yes;TrustServerCertificate=no" }
     }
}
```

> [!WARNING]
> [mssql-django](https://github.com/microsoft/mssql-django) doesn't support using time zones so the recommendation is to ensure the `USE_TZ` option is set to `False`.
>
>```sql
>
> DATABASES = {
> ...
> }
> # set this to False if the backend does not support using time zones
> USE_TZ = False
> ```

Run the migrations command to propagate changes you made to your models (creating a class, adding a field, deleting a model, etc.) into your database schema.

```python
python manage.py makemigrations customerapi

python manage.py migrate customerapi
```

Once migration is done successfully, you’ll see that database objects are created in your database. You can connect to your database and verify. Quickstart available here: [Quickstart: Use Azure Data Studio to connect and query Azure SQL database](https://docs.microsoft.com/en-us/sql/azure-data-studio/quickstart-sql-database?view=sql-server-ver15)

## Run sample locally

Execute the below command, to start the development web server on the local machine. By default, the server runs on port 8000 on the IP address 127.0.0.1. You can pass in an IP address and port number explicitly.

Inititalze Django - this is needed only the first time

```python
python manage.py migrate

python manage.py createsuperuser
```

and then run the server

```python
python manage.py runserver
```

Once the Django application is running, you'll see something like:

```bash
...
System check identified no issues (0 silenced).
February 04, 2022 - 14:32:15
Django version 4.0.2, using settings 'django-sql-project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Using a REST Client (like [Insomnia](https://insomnia.rest/), [Postman](https://www.postman.com/), or curl), you can now call your API, for example:

```bash
curl -X GET http://127.0.0.1:8000/customerapi/customer/
```

And you’ll get a response something like (based on available data in tables):

```json
[
    {"CustomerId": 1, "CustomerName": "Keith"},{"CustomerId": 2, "CustomerName": "Janet"},{"CustomerId": 4, "CustomerName": "Cortana"},{"CustomerId": 5, "CustomerName": "Michael"},{"CustomerId": 7, "CustomerName": "David"},{"CustomerId": 8, "CustomerName": "Mike"}
]
```

Check out the [sample](https://github.com/abhimantiwari/azure-sql-db-django) to test all the CRUD operations.

> [!TIP]
> You can use [mssql-django](https://github.com/microsoft/mssql-django) as a backend for your existing Django 4.0 project with no major change if that's already configured for MS SQL Server.
&nbsp;

If you encounter any issues or have any feedback about [mssql-django](https://github.com/microsoft/mssql-django), head over to our mssql-django project repository and submit an issue.

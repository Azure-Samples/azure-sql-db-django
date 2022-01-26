# Creating a REST API with Python Django and Azure SQL

The sample uses the [Django](https://www.djangoproject.com/) web framework and [Django Rest framework](https://www.django-rest-framework.org/) package to easily implement REST APIs. [mssql-django](https://github.com/microsoft/mssql-django) v1.1 used to establish database connectivity with Azure SQL. 


> [!NOTE]
> [mssql-django](https://github.com/microsoft/mssql-django) is a fork of [django-mssql-backend](https://pypi.org/project/django-mssql-backend/). This driver provides an enterprise database connectivity option for the Django Web Framework, with support for Microsoft SQL Server and Azure SQL Database.
>[ssql-django](https://github.com/microsoft/mssql-django) supports Django 2.2, 3.0, 3.1, 3.2 and 4.0.

<p>&nbsp;</p>

## Install the dependencies
Make sure you have [Python](https://www.python.org/) installed on your machine.

To confirm you can run `python` on Terminal.
```Python
> python
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print('hello world')
hello world
>>>
```

Also, install [Django](https://www.djangoproject.com/download/):
```bash
pip install django
```

Also, install [Django REST framework](hhttps://www.django-rest-framework.org/#installation) to create REST API:
```Python
pip install djangorestframework
```
You should also install [django-cors-headers](https://pypi.org/project/django-cors-headers/). It is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
```Python
pip install django-cors-headers
```

> [!NOTE]
> Adding [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) headers allows your resources to be accessed on other domains. It’s important you understand the implications before adding the headers since you could be unintentionally opening up your site’s private data to others.

<p>&nbsp;</p>

## Create the Azure SQL Database

If you don't have a Azure SQL server already, you can create one (no additional costs for a server) running the following [AZ CLI](https://docs.microsoft.com/en-us/cli/azure/) command (via [WSL](https://docs.microsoft.com/en-us/windows/wsl/), or Linux or [Azure Cloud Shell](https://azure.microsoft.com/en-us/features/cloud-shell/)):

```PowerShell
az sql server create -n <server-name> -l <location> --admin-user <admin-user> --admin-password <admin-password> -g <resource-group>
```

Create a new Azure SQL database:
```powershell
az sql db create -g <resource-group> -s <server-name> -n todo_v3 --service-objective GP_Gen5_2
```

Another option is to run the `azure-create-sql-db.sh` script in the `./databases` folder. The script uses the ARM template available in the same folder to create a server and a `todo_v3` database.

Make sure you have the firewall configured to allow your machine to access Azure SQL:
```powershell
az sql server firewall-rule create --resource-group <resource-group> --server <server-name> --name AllowMyClientIP_1 --start-ip-address <your_public_ip> --end-ip-address <your_public_ip>
```
You can get your public IP from [here](https://ifconfig.me/) for example: https://ifconfig.me/

## Setting up the Django project

You can download the [sample](https://github.com/abhimantiwari/Django-AzureSQL), as a baseline starter or you may create your own project.
```Python
django-admin startproject <name of the project>
```

To verify your Django project works. Change into the outer project directory, if you haven’t already, and run the following commands:
```Python
py manage.py runserver
```
Now that the server’s running, visit http://127.0.0.1:8000/ with your web browser. You’ll see a “Congratulations!” page.

> [!NOTE]
> Ignore the warning about unapplied database migrations for now. we’ll deal with the database shortly.

<p>&nbsp;</p>

### Create the API App
Now that your environment – a “project” – is set up, you’re set to start creating your functional apps.

To create your app, make sure you’re in the same directory as manage.py and type this command:
```python
py manage.py startapp <app_name>
```

Register the app and required modules in settings.py file and also create your Models which will represent tables or collection in database and Serializer for converting complex objects into native Python datatypes and deserialize parsed data back into complex types. Also, create your view function to handle the requests and return the response, and map URL patterns accordingly.

<p>&nbsp;</p>

## Configure Azure SQL connectivity with Django

### Dependencies
- pyodbc 3.0 or newer

### Installation
- Install pyodbc:
    ```Python
    pip install pyodbc
    ```
- Install mssql-django:
    ```Python
    pip install mssql-django
    ```
### Configuration

Configure the Database connectionstring in the settings.py file used by your Django application or project:
```Python
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
```Python
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
```python
DATABASES = {
...
}

# set this to False if the backend does not support using time zones
USE_TZ = False
```

Run the migrations command to propagate changes you made to your models (creating a class, adding a field, deleting a model, etc.) into your database schema.
```Python
python manage.py makemigrations <app name>

python manage.py migrate <app name>
```

Once migration is done successfully, you will see that database objects are created in your database.

<p>&nbsp;</p>

## Run the Django Application locally

Execute the below command to starts the development web server on the local machine. By default, the server runs on port 8000 on the IP address 127.0.0.1. You can pass in an IP address and port number explicitly.

```Python
    python manage.py runserver [addrport]
```

Once the Django application is running, you will see something like:
```Text
...

System check identified no issues (0 silenced).
January 26, 2022 - 00:29:43
Django version 4.0.1, using settings 'DjangoAZsqlApp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Using a REST Client (like [Insomnia](https://insomnia.rest/), [Postman](https://www.postman.com/), or curl), you can now call your API, for example:
```bash
curl -X GET http://127.0.0.1:8000/CustomerApp/Customer/
```
And you will get a response something like:
```JSON
[
    {"CustomerId": 1, "CustomerName": "Keith"},
    {"CustomerId": 2, "CustomerName": "Janet"},
    {"CustomerId": 4, "CustomerName": "Cortana"},
    {"CustomerId": 5, "CustomerName": "Michael"},
    {"CustomerId": 7, "CustomerName": "David"},
    {"CustomerId": 8, "CustomerName": "Mike"}
]
```

Check out the samples to test all CRUD operations.

<p>&nbsp;</p>

> [!TIP]
> You can use [mssql-django](https://github.com/microsoft/mssql-django) as a backend for your existing Django 4.0 project with no major change if that's already configured for MSSQL. 
<p>&nbsp;</p>

If you encounter any issues or have any feedback about [mssql-django](https://github.com/microsoft/mssql-django), head over to our mssql-django project repository and submit an issue.



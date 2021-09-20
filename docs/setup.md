# Setup

The server is currently running:
* Debian as the OS
* Nginx for serving
* Python and PostgreSQL run with docker-compose for Django
* PHP and MySQL run with docker-compose for Wordpress

If you find yourself needing to update PostgreSQL, I recommend [this tutorial][pg-tut].

[pg-tut]: https://www.pontikis.net/blog/update-postgres-major-version-in-debian

## Translation

In order to generate the .po file:
```
python manage.py makemessages -l es -e j2,py -i bin -i lib
```
In order to compile the files:
```
python manage.py compilemessages
```

## Django in a subpath

The repository is installed at https://poeticasonora.unam.mx/rda, which is a subpath (/rda).
This requires [additional setup in Nginx][nginx-django-subpath].

[nginx-django-subpath]: https://newbedev.com/run-django-app-via-nginx-uwsgi-in-a-subpath

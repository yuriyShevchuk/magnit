# Test task for magnit

### To populate postgis database
after initial ./manage.py makemigrations/migrate
```./manage.py makemigrations geo_api --empty```
and copy migrate_from_file.py content to generated migrations file in
./geo_api/migrations
and ./manage.py migrate to add data to database.

or you can use dump.sql file to restore database.
or you can use existing migrations.

#### Requirements for postgis:
sudo apt install gdal-bin libgdal-dev
sudo apt install python3-gdal

## Assignments
### 1. Jupyter notebook for the first assignment is in ./assignment_1 folder.

### 2. Second assignment
Frontend integrated to Django but is not finished. No requests no templates. But
REST Api is working with 5 endpoints.
Dockerfile and docker-compose.yaml doesn't work.

### 3. Third assignment
is [here](https://replit.com/@Baradaster/geoJsonborderLength#main.py)

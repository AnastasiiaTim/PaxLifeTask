## To run program:
```
python manage.py runserver 127.0.0.1:8000
```

## To run import from csv
```
python manage.py import_airports_from_csv data/airports.csv
```

## To test search for IATA code:

http://127.0.0.1:8000/airport/?iata_code=txl

## To test search for airport name containing string:

http://127.0.0.1:8000/airports/?name=berlin

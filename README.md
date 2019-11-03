# Home devices register

## Run with VIRTUALENV

```
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ export FLASK_ENV=development
$ export FLASK_APP=run
$ flask run
```

## Available endpoints

collection: /devices
- GET - view collection
- POST - create resource

resource: /device/<identifier>
- GET - view resource
- DELETE - delete resource

## Data response

```
json
{
    "data": "actual response information"
}
```

## Services

`GET /devices`

**Response**
- `200 OK` 
```
json
[
    {
        "identifier": "mobile-phone",
        "name": "Mobile Xiaomi mi 5",
        "device_type": "mobile-phone",
        "controller_gateway": "192.0.1.68"
    }
]
```

### Dependencies 
- Flask 1.0.2
- flask-restful 0.3.7
- Markdown 3.1.1

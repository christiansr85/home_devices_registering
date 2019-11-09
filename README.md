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

## Run with DOCKER
Just type 
```
$ sudo docker-compose up
```

If you need to make changes on `docker-compose.yml` file, run this command to update the container:
```
$ sudo docker-compose up --build
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

### List all devices

`GET /devices`

**Response**
- `200 OK` 
```
[
    {
        "identifier": "mobile-phone",
        "name": "Mobile Xiaomi mi 5",
        "device_type": "mobile-phone",
        "controller_gateway": "192.0.1.68"
    }
]
```

### Create a new device

`POST /devices`

**Body**

- `"identifier":string` a globally unique identifier for this device
- `"name":string` a friendly name for this device
- `"device_type":string` the type of the device as understood by the client
- `"controller_gateway":string` the IP address of the device's controller

It overwrites any previous device with the same indentifier.

**Response**

- `201 Created`

```
{
    "identifier": "floor-lamp",
    "name": "Floor Lamp",
    "device_type": "switch",
    "controller_gateway": "192.1.68.0.2"
}
```

### Details of a single device

`GET /device/<identifier>`

**Response**

- `404 Not Found`
- `200 OK`
```
{
    "identifier": "floor-lamp",
    "name": "Floor Lamp",
    "device_type": "switch",
    "controller_gateway": "192.1.68.0.2"
}
```

### Delete a device

`DELETE /devices/<identifier>`

**Response**

- `404 Not Found`
- `200 OK`


## Dependencies 
- Flask 1.0.2
- flask-restful 0.3.7
- Markdown 3.1.1

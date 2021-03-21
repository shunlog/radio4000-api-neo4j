A public RESTful API to neo4j for [radio4000](https://github.com/internet4000/radio4000)

## Progress

Check out the [todo](todo.org)

## Instructions

Install the required pip packages:
```bash
pip3 install -r requirements.txt
```

Set the environment variables

Private variables go in `.env`:
```bash
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="password"
NEO4J_BOLT_URL="bolt://${NEO4J_USERNAME}:${NEO4J_PASSWORD}@localhost:7687"
```

Public variables go in `.flaskenv`:
```bash
FLASK_APP="app.py"
FLASK_ENV="development"
FLASK_DEBUG=1
```

Run the flask server:
```bash
flask run
```

## Models

This is the first **_prototype_**

### Overview

![Diagram](diagram.png "An image is worth a thousand words")

### Nodes

#### Channel

| name    | type      | description                                                                                                                    |
|---------|-----------|--------------------------------------------------------------------------------------------------------------------------------|
| title   | `string`  | title representing a radio channel. Example: `"Radio Oskar"`                                                                   |
| body    | `string`  | description of the radio channel. Example: `"The channel of your wet dreams..."`                                               |
| created | `integer` | timestamp describing when was this radio channel created. Example: `"1411213745028"`                                           |
| image   | `string`  | the id for the cloudinary `image` model. Example: `"image": "drz0qs9lgscyfdztr17t".`                                           |
| link    | `string`  | Custom URL describing the external homepage for a radio channel. Example: `"https://example.com"`                              |
| slug    | `string`  | the unique URL representing this channel. Used for human readable urls Example: `"pirate-radio"` -> radio4000.com/pirate-radio |
| updated | `integer` | timestamp when the radio was last updated. Example: `1498137205047`                                                            |

#### Track

| name              | type        | description                                                                            |
|-------------------|-------------|----------------------------------------------------------------------------------------|
| title             | `string`    | required title of the track. Example: `"Lydia Lunch - This Side of Nowhere (1982)"`    |
| created           | `integer`   | date timestamp from when the model is created                                          |
| mediaNotAvailable | `boolean`   | is the current track media available, accessible to be consumed                        |
| discogsUrl        | `string`    | the URL pointing to the Discogs release (or master) corresponding to this track media. |


#### User

| name    | type      | description                                                        |
|---------|-----------|--------------------------------------------------------------------|
| created | `integer` | timestamp from when the user was created. Example: `1481041965335` |

### Relations

#### Channel -> Track :CONTAINS 

| name        | type     | description                                                             |
|-------------|----------|-------------------------------------------------------------------------|
| description | `string` | optional description to the track. Example: `"Post-Punk from USA (NY)"` |
    

#### Track <- MediaProvider :PROVIDES

| name     | type     | description                  |
|----------|----------|------------------------------|
| uri      | `string` | provider id of a track media |

#### User -> Channel :CREATED

| name    | type      | description                                |
|---------|-----------|--------------------------------------------|
| date    | `integer` | timestamp to when the relation was created |


#### User -> Channel :FOLLOWS

| name | type | description |
|------|------|-------------|
|      |      |             |

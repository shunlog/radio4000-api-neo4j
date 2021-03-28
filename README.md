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

Not final variant. The `url` property is still bothering.

### Overview

![Diagram](diagram.png "An image is worth a thousand words")

### Nodes

#### Channel

| name        | type      | description                                                                                                                    |
|-------------|-----------|--------------------------------------------------------------------------------------------------------------------------------|
| slug        | `string`  | the unique URL representing this channel. Used for human readable urls Example: `"pirate-radio"` -> radio4000.com/pirate-radio |
| title       | `string`  | title representing a radio channel. Example: `"Radio Oskar"`                                                                   |
| body        | `string`  | description of the radio channel. Example: `"The channel of your wet dreams..."`                                               |
| created     | `date`    | date describing when was this radio channel created                                                                            |
| updated     | `date`    | date describing when was this radio channel updated                                                                            |
| image       | `string`  | the id for the cloudinary `image` model. Example: `"image": "drz0qs9lgscyfdztr17t".`                                           |
| is_featured | `bool`    | wheter this channel is shown on the 'featured' page                                                                            |
| link        | `string`  | Custom URL describing the external homepage for a radio channel. Example: `"https://example.com"`                              |

#### Track

| name              | type      | description                                                                            |
|-------------------|-----------|----------------------------------------------------------------------------------------|
| title             | `string`  | required title of the track. Example: `"Lydia Lunch - This Side of Nowhere (1982)"`    |
| url               | `string`  | the URL pointing to the YouTube video of this track                                    |
| mediaNotAvailable | `boolean` | is the current track media available, accessible to be consumed                        |
| discogsUrl        | `string`  | the URL pointing to the Discogs release (or master) corresponding to this track media. |

#### Tag

| name | type     | description     |
|------|----------|-----------------|
| name | `string` | name of the tag |

### Relationships

#### (Channel) -[LIKES]-> (Track)

| property | type     | description                                                             |
|----------|----------|-------------------------------------------------------------------------|
| body     | `string` | optional description to the track. Example: `"Post-Punk from USA (NY)"` |

#### (Track) -(TAGGED)-> (Tag)

| property | type     | description                             |
|----------|----------|-----------------------------------------|
| channel  | `string` | unique id of the channel that tagged the track |


#### (Channel) -[FOLLOWS]-> (Channel)


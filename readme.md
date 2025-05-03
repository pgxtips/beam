<h1 style="text-align: center; line-height: 1;">
  <img src="static/img/logo.png" width="32" height="33" style="vertical-align: middle;">
  <span style="vertical-align: middle;">Beam</span>
</h1>



**beam** is a modular, plug-and-play recommendation engine built for small 
businesses and app developers. 
It supports customisable recommendation algorithms, user session tracking, 
and a dashboard-driven setup.

---

## What is Beam?

Beam helps applications deliver recommendations through:

* Tag-based content modeling
* Session-aware preference tracking
* Multiple, swappable recommendation algorithms
* Configuration through a web dashboard

---

## Usage Overview

Beam is operated via its **web dashboard**, which should be your primary interface.
Here’s the typical usage flow:

### 1. **Set the Data Source** *(Dashboard)*

* Upload or define your content and associated tags via the dashboard.
* Each content item should include:

  * A unique `id`
  * A list of `tags` (e.g., `"fitness"`, `"comedy"`)

> You must configure the data source before using the API to create sessions 
or request recommendations.

### 2. **Create a Session**

Create a session via the API:

```http
GET /external/createSession
```

Returns a `session_id` that should be used for all subsequent actions.

### 3. **Set Preferences**

Assign initial tag preferences:

```http
POST /external/post/preferences
```

Form fields:
* `session_id`: string
* `tags`: comma-separated string (e.g., `fitness,comedy,technology`)

### 4. **Get Available Tags**

Retrieve tags from the current data source:

```http
GET /external/get_tags
```

### 5. **Request Recommendations**

request personalised content:

```http
POST /external/recommend
```

Form fields:

* `session_id`: string

Returns a batch of content item recommendations.

### 6. **Like / Dislike Feedback**

Send user feedback:

```http
POST /external/like
POST /external/dislike
```

Form fields:

* `session_id`: string
* `content_id`: string

### 7. **Switch Recommender Model (Optional)**

Change the recommendation algorithm mid-session:

```http
POST /external/changeModel
```

Form fields:
* `session_id`: string
* `model`: one of `logistic`, `none`

---

## External API Summary

| Endpoint                     | Method | Purpose                               |
| ---------------------------- | ------ | ------------------------------------- |
| `/external/createSession`    | GET    | Start a new session                   |
| `/external/get_tags`         | GET    | Retrieve tag list from data source    |
| `/external/post/preferences` | POST   | Submit user preferences (tags)        |
| `/external/recommend`        | POST   | Get content recommendations           |
| `/external/like`             | POST   | Mark a content item as liked          |
| `/external/dislike`          | POST   | Mark a content item as disliked       |
| `/external/changeModel`      | POST   | Switch active recommender for session |

---

## Development

### Install Dependencies

Beam uses [`uv`](https://github.com/astral-sh/uv) for dependency and 
runtime management:

```bash
uv sync
```

### Start (Development)

```bash
uv run -m src.dev
```

### Start (Production)

```bash
uv run gunicorn -b 0.0.0.0:6969 src.app:APP_SERVER
```

---

## Docker

### Build Image

```bash
docker build -t beam -f docker/Dockerfile .
```

### Run Container

```bash
docker run -p 3000:80 beam
```

---

## Examples
A demonstration of a Beam implementation can be found [here](https://github.com/pgxtips/beam-demo).


## Tech Stack

* Python 3.13+
* Scikit-learn
* Flask
* Gunicorn
* Docker

# Schedule API #

This covers the various routes exposed by our API system

## /schedule<str:format> ##

Returns schedule data. 

Accepted format types are:

* .json
* .frab
* .ical
* .ics

This accepts two query parameters:

* `is_favourite` -- only return events that the user has favourited
* `venue` -- Only return events at the given venue

The response varies based on requested format, but for example in json is:

```json
[
  {
    "venue": "Stage C",
    "start_date": "2018-08-31 20:20:00",
    "title": "Retriculating splines in zero-G",
    "user_id": 666,
    "map_link": "https://map.emfcamp.org/#18.5/52.040485/-2.3776549",
    "may_record": true,
    "slug": "zero-g-spline-reticulation",
    "id": 999,
    "is_fave": true,
    "end_date": "2018-08-31 20:40:00",
    "start_time": "20:20",
    "type": "talk",
    "speaker": "Denice Janway",
    "source": "database",
    "end_time": "20:40",
    "latlon": [
      52.040485,
      -2.3776549
    ],
    "link": "https://www.emfcamp.org/line-up/2018/529",
    "description": "Denice talks about how to reticulate splines in zero-g"
  },
  {
    "venue": "Hackcamp42",
    "start_date": "2018-08-31 19:55:00",
    "title": "Force feedback water wings",
    "user_id": null,
    "map_link": "https://map.emfcamp.org/#18.5/52.045/-2.3776549",
    "may_record": false,
    "id": 999,
    "is_fave": false,
    "end_date": "2018-08-31 20:40:00",
    "start_time": "20:20",
    "type": "talk",
    "speaker": "",
    "source": "external",
    "end_time": "20:40",
    "latlon": [
      52.040485,
      -2.3776549
    ],
    "link": "https://www.emfcamp.org/line-up/2018/529",
    "description": "Eve demos the making of force-feedback water-wings"
  }
]
```

## /favourites.json ##
## /favourites.ical ##
## /favourites.ics ##
## /line-up ##
## /line-up/2018 ##
### GET ###
### POST ###

## /favourites ##
### GET ###
### POST ###

## /line-up/2018/<int:proposal_id> ##
### GET ###
### POST ###

## /line-up/2018/<int:proposal_id>-<slug> ##
### GET ###
### POST ###

## /line-up/2018/<int:proposal_id>.json ##
## /line-up/2018/<int:proposal_id>-<slug>.json ##
## /line-up/2018/external/<int:event_id> ##
### GET ###
### POST ###

## /line-up/2018/external/<int:event_id>-<slug> ##
### GET ###
### POST ###

## /schedule/external/feeds ##
### GET ###
### POST ###

## /schedule/publish ##
### GET ###
### POST ###

## /schedule/publish/<int:source_id> ##
### GET ###
### POST ###

## /now-and-next.json ##
## /upcoming.json ##
## /now-and-next ##

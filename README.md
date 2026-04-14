# django-rest-bible - A modern Bible Backend for the Django Web Framework

`django-rest-bible` is a modern, actively maintained Python package & 
Django app for interfacing with the King James Version of the Holy Bible.
This project is an extension of the unmaintained package django-bible, updated 
and improved for modern Python environments.


## Installation

To install, simply run the script with the install command:
```
pip install django-rest-bible
```

## Quick start
1. Add bible and bible_api to your INSTALLED_APPS setting:
 INSTALLED_APPS = [
        ...,
        "bible",
        "bible_api",
    ]
2. Include the bible and bible_api URLconf in your project urls.py:
```
path('', include('bible.urls')),
path('api/v1/', include('api.urls')),
```
3. Run `python manage.py migrate` to create the models.

4. Once the tables have been created, you need to populate the tables with Bible 
data.

#### Bible Data

A JSON dump of the entire KJV Bible is available for download here http://s3.amazonaws.com/bible-data/kjv_bible.json

You can load the downloaded Bible data into your project's database by running
the django loaddata command:
```
python manage.py loaddata kjv_bible.json --app bible
```
5. Start the development server and visit http://127.0.0.1:8000/ for the Index 
of books or the endpoint http://127.0.0.1:8000/api/v1/bible. You can filter for 
a specific book, chapter or verse using the query parameters chapter__book_slug, 
chapter__number and number for example: http://127.0.0.1:8000/api/v1/bible/?chapter__book__slug=genesis&chapter__number=2&number=3 should return a serialized Genesis 2:3.

## Why This Project Exists

The original project, `django-bible`, provided a useful foundation but appears 
to have been unmaintained for many years.

This version was created to:

* Keep the project alive and usable
* Add improvements and bug fixes
* Ensure compatibility with modern Python versions
* Add RESTful API Service
* Provide ongoing maintenance and support

## What’s Changed
* Updated dependencies
* Improved code structure
* Added new features and fixes
* Enhanced documentation

## License & Attribution

This project is an extension of django-bible, created by David Davis.

The original work is licensed under the BSD 3-Clause License
This project retains the original license and copyright
Additional modifications are © 2026 Uchenna Adubasim

See the LICENSE file for full details.

## Contributing

Contributions are welcome! To contribute,

* Fork the repo
* Create a new branch
* Submit a pull request

## Issues

If you find a bug or have a feature request, please open an issue.

## Acknowledgements

Special thanks to David Davis for building the foundation of this project.

## Maintainer

This project is actively maintained by:

- **Uchenna Adubasim** (Lead Maintainer)

For issues, features, and support, please contact or open an issue in this 
repository.

## Contact

Find my [email here](https://mailhide.io/e/sXPUdBJS)








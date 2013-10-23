RestArt
=======

Python RESTful HTTP client based on the requests library.


Features
========

Adds syntax sugar for accessing the RESTful APIs.


Install RestArt
===============

	pip install restart


Example: Composing the URL
==========================

	# Incorporate the base URL and the basic HTTP auth in the app factory
	api = Api('http://api.mycompany.com', auth=(APP_ID, APP_SECRET))

	# Get the list of authors
	# GET http://api.mycompany.com/authors?name=John%20Doe
	authors = api.authors.GET(name='John Doe').json()

	# Get the author
	# GET http://api.mycompany.com/authors/123
	author = api.authors[123].GET().json()

	# Create a book
	# POST http://api.mycompany.com/authors/123/books
	resp = api.authors[123].books.POST(name='Readme').json()


Example2: Complete URI
======================

	api = Api(API_BASE_URL, auth=(APP_ID, APP_SECRET))

	# Get the resource by its complete URI
	book = api(book_uri).GET().json()


Example3: Setting headers
=========================

	# set Referer
	api = Api(API_BASE_URL, auth=(APP_ID, APP_SECRET), headers={'Referer': 'http://localhost:8000/index.html'})
	api(book_uri).GET()


License
=======

This software is licensed under the [MIT license](http://en.wikipedia.org/wiki/MIT_License>).

© 2013 Oleg Pidsadnyi

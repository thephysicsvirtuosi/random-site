from bottle import route, run, template, request

import sqlite3

@route('/test')
def test_page():
	return template('test-template')


@route('/seeall')
def see_all():
	""" Look at the raw data """
	conn = sqlite3.connect("randomdata.db")
	c = conn.cursor()
	c.execute("SELECT id, digits, author, timestamp from randdat")
	result = c.fetchall()
	return str(result)

@route('/datum', method='POST')
def add_datum():
	"""Add a new datum"""

	digits = request.POST.get('digits', '').strip()
	author = request.POST.get('name','').strip()

	conn = sqlite3.connect("randomdata.db")
	c = conn.cursor()

	c.execute("INSERT INTO randdat (digits,author) VALUES (?,?)", (digits,author))
	new_id = c.lastrowid

	conn.commit()
	c.close()

	return "The new task was inserted into the database, the ID is %s" % new_id




run(host='localhost', port=8080, debug=True, reloader=True)
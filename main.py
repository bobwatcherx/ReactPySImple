# INSTALL FLASK IN YOU PC
from flask import Flask
# INSTALL idom With pip install idom
from idom import component,html,use_state,hooks
from idom.backend.flask import configure


@component
def mylist(items):

	# AND NOW I SHOW YOU STATE 
	# for use_state and hooks

	count,set_count = hooks.use_state(0)
	name,set_name = use_state("ujang")
	mycolor,set_mycolor = use_state("red")


	def incrementbtn(event):
		set_count(count+1)

	def changecolor(event):
		set_mycolor("orange" if mycolor == "red" else "orange" )


	alllist = [html.li(
		{
			"key":i['id'],
			"style":{"padding":"10px"},

		},
		# AND TEXT FOR DISPLAY HERE
		i['text'],"  ", "age :",i['age']
		) for i in items]



	# AND SHOW IN VIEW
	return html.div(
		# SHOW COUNTER
		html.h2(count),
		# NOW CREATE BUTTON FOR INCREMENT COUNTER
		html.button({
			"on_click":incrementbtn
			},"you increment"),

		# NOW FOR AUTO CHANGE INPUT
		html.h2(name),
		html.input({
			"type":"text",
			"placeholder":"INsert name",
			"value":name,
			"on_change":lambda event:set_name(event['target']['value'])

			}),
		# NOW I USE SELECT FOR CHANGE NAME
		html.select({
			"value":name,
			"on_change":lambda event:set_name(event['target']['value'])
			},
			html.option({"value":"jjj"},"jjj"),
			html.option({"value":"aaaa"},"aaaa"),
			html.option({"value":"bbbb"},"bbbb"),
			html.option({"value":"ccccc"},"ccccc"),
			html.option({"value":"dddd"},"dddd"),

			),

		# AND NOW USE CHECKBOX FOR CHANGE BUTTON COLOR
		# BACKGROUND
		# IF I CHECK CHECKBOX THEN CHANGE BUTTON COLOR
		html.button({
			"style":{"background_color":mycolor,"color":"white"},
			"on_click":changecolor
			},"SET YOU COLOR"),
		# AND NOW I CREATE CHECKBOX
		html.input({
			"type":"checkbox",
			"value":"red",
			"on_click":lambda event:set_mycolor(event['target']['value'])

			}),




		html.h2("this for loop data from parent"),
		html.ul(alllist)
		)



@component
def Hellotest():

	# NOW I CREATE FAKE DATA
	# FOR SAMPLE
	task = [
	{"id":0,"text":"JUJU","age":20},
	{"id":2,"text":"dwq","age":2},
	{"id":3,"text":"JU2312JU","age":0},
	{"id":5,"text":"fe","age":4},
	]

	return html.div(
		html.h1("test app"),
		# NOW I CREATE NEW COMPONENT
		mylist(task)
		)


app = Flask(__name__)
configure(app,Hellotest)
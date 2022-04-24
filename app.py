from flask import Flask,render_template,request
from mysqldb import MYSQL
import json
import socket
import os
import requests
#from watchtowerlogsmodule import logger

location = os.path.dirname(os.path.realpath(__file__))

APP_NAME= os.environ.get('APP_NAME','softglacier-example')
#LOG_GROUP_NAME = os.environ.get('LOG_GROUP_NAME','softglacier-group')
#LOG_STREAM_NAME= os.environ.get('LOG_STREAM_NAME','softglacier-stream')
#BOTO3_PROFILE_NAME = os.environ.get('BOTO3_PROFILE_NAME','default')
MYSQL_HOST= os.environ.get('MYSQL_HOST','127.0.0.1')
MYSQL_PASSWORD =os.environ.get('MYSQL_PASSWORD',None)
MYSQL_USER =os.environ.get('MYSQL_USER','root')
MYSQL_DATABASE= os.environ.get('MYSQL_DATABASE','persons')
MYSQL_PORT =os.environ.get('MYSQL_PORT',3306)
HOST_API  = os.environ.get('HOST_API','localhost')
HOST_API_PORT =os.environ.get('HOST_API_PORT',8080)


app = Flask(APP_NAME)
#logger=logger(app,LOG_GROUP_NAME,LOG_STREAM_NAME,BOTO3_PROFILE_NAME)
@app.route('/health')
def health():
    try:
        with open(file=os.path.join(location,'version.json'),mode='r') as read_json:
            data = json.load(read_json)
        container = socket.gethostname()
        response  = { app.name: "up and running",
            "container": container,
            "version" : data.get('version',None)
        }
        
        return render_template('health.html',response=response)
    except Exception as err:
        return render_template('error.html',err=err)



@app.route('/',methods=["GET","POST"])
def index():
    try:
        mysql = MYSQL(MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD)
        result=mysql.create_database(MYSQL_DATABASE)
        mysql.create_table(MYSQL_DATABASE,'users')
        if request.method == "POST":
            firstname=request.form["firstname"].strip().replace(" ","").lower()
            lastname=request.form["lastname"].strip().replace(" ","").lower()
            email=request.form["email"].strip().replace(" ","").lower()
            insert_query = """INSERT INTO `users` (`firstname`, `lastname`,`email`) VALUES (%s, %s, %s)"""
            mysql.execute_command('persons',insert_query,(firstname,lastname,email))
            data = {"firstname" : firstname,"lastname": lastname,"email":email}
            requests.get(url=f"{HOST_API}:{HOST_API_PORT}/notify",params=data)
            select_query="""SELECT * FROM `users`"""
            rows = mysql.fetch('persons',select_query,())
            if len(rows) > 0:
                return render_template('index.html',rows=rows,result=result)
            return render_template('index.html',rows=rows,result=result)
        else:
            select_query="""SELECT * FROM `users`"""
            rows = mysql.fetch(MYSQL_DATABASE,select_query,())
            if len(rows) > 0:
                return render_template('index.html',rows=rows,result=result)
            return render_template('index.html',rows=rows,result=result)
    except Exception as err:
       return render_template('error.html',err=err)


        
        
        
        

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)



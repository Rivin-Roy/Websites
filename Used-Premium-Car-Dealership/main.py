from flask import Flask
from public import public
from admin import admin
from seller import seller
from buyer import buyer

app=Flask(__name__)

app.secret_key="abc"

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(seller,url_prefix='/seller')
app.register_blueprint(buyer,url_prefix='/buyer')


app.run(debug=True,port=5055)

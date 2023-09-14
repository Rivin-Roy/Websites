from flask import *
from database import *


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail


buyer=Blueprint('buyer',__name__)

@buyer.route('/buyerhome')
def buyerhome():
	return render_template('buyerhome.html')
	
@buyer.route('/buyerviewfeature')
def buyerviewfeature():
	data={}
	vid=request.args['vid']
	q="select * from features where vehicle_id='%s'"%(vid)
	res=select(q)
	data['fea']=res
	return render_template('buyerviewfeature.html',data=data)

@buyer.route('/buyerviewcar',methods=['get','post'])
def buyerviewcar():
	data={}
	q="select * from vehicle inner join subcategory using(subcategory_id)inner join category using(category_id) where status<>'selled'" 
	res=select(q)
	data['car']=res
	seller_id=res[0]['seller_id']
	if "action" in request.args:
		action=request.args['action']
		vid=request.args['vid']
		price=request.args['price']
		bid=session['buyer_id']
	else:
		action=None

	if action=="book":
		q="select * from vehicle inner join seller using(seller_id) where vehicle_id='%s'"%(vid)
		res=select(q)
		print(res)
		msg="seller Name:"+res[0]['name']
		msg=msg+" Place:"+res[0]['place']
		msg=msg+" Phone:"+res[0]['phone']
		msg=msg+" Email:"+res[0]['email']
		print(msg)
		q="insert into booking values(null,'%s','%s','%s','booked')"%(bid,vid,price)
		insert(q)
		q="update vehicle set status='booked' where vehicle_id='%s'"%(vid)
		update(q)

		try:
			gmail = smtplib.SMTP('smtp.gmail.com', 587)
			gmail.ehlo()
			gmail.starttls()
			gmail.login('projectsriss2020@gmail.com','messageforall')
		except Exception as e:
			print("Couldn't setup email!!"+str(e))

		msg = MIMEText(msg)

		msg['Subject'] = 'Seller Details'

		msg['To'] = session['email']

		msg['From'] = 'projectsriss2020@gmail.com'

		try:
			gmail.send_message(msg)
			print(msg)
			flash("EMAIL SENED SUCCESFULLY")
			return redirect(url_for('buyer.buyerviewcar'))


		except Exception as e:
			print("COULDN'T SEND EMAIL", str(e))
			return redirect(url_for('buyer.buyerviewcar'))
	


		flash("booked successfuly")
		return redirect(url_for('buyer.buyerviewcar'))
	return render_template('buyerviewcar.html',data=data)


@buyer.route('/buyerviewbooking',methods=['get','post'])
def buyerviewbooking():
	data={}
	buyer_id=session['buyer_id']
	q="select *,booking.status as bstatus from `booking` inner join vehicle using (vehicle_id) inner join buyer using(buyer_id) where buyer_id='%s'"%(buyer_id)
	r=select(q)
	data['book']=r

	
	

	return render_template('buyerviewbooking.html',data=data)

@buyer.route('/buyermakepayment',methods=['get','post'])
def buyermakepayment():
	data={}
	vehicle_id=request.args['vehicle_id']
	bookid=request.args['book_id']
	price=request.args['price']
	data['price']=price
	if "payment" in request.form:
		
		q="insert into payment values(null,'%s','%s',curdate())"%(bookid,price)
		insert(q)
		q="update booking set status='paid' where booking_id='%s'"%(bookid)
		update(q)
		q="update vehicle set status='selled' where vehicle_id='%s'"%(vehicle_id)
		update(q)
		flash("paid successfully")

		return redirect(url_for('buyer.buyerviewbooking'))
	return render_template('buyermakepayment.html',data=data)

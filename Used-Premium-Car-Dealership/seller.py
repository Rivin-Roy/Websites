from flask import *
from database import *
import uuid


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

seller=Blueprint('seller',__name__)

@seller.route('/sellerhome')
def sellerhome():
	return render_template('sellerhome.html')

@seller.route('/sellerviewbooking',methods=['get','post'])
def sellerviewbooking():
	data={}
	sid=session['sellerid']
	q="select * from `booking` inner join vehicle using (vehicle_id) inner join buyer using(buyer_id) where seller_id='%s'"%(sid)
	r=select(q)
	data['book']=r

	
	

	return render_template('sellerviewbooking.html',data=data)


@seller.route('/sellerviewpayment',methods=['get','post'])
def sellerviewpayment():
	data={}
	bid=request.args['book_id']
	sid=session['sellerid']
	q="select * from `payment` inner join `booking` using(`booking_id`)inner join `vehicle` using(`vehicle_id`) inner join buyer using(buyer_id) where booking_id='%s' and seller_id='%s'"%(bid,sid)
	r=select(q)
	data['pay']=r
	return render_template('sellerviewpayment.html',data=data)
@seller.route('/sellerviewcategory',methods=['get','post'])
def sellerviewcategory():
	data={}

	q="select * from `category` where cstatus='active'"
	r=select(q)
	data['categorys']=r
	return render_template('sellerviewcategory.html',data=data)

@seller.route('/sellerviewsubcategory',methods=['get','post'])
def sellerviewsubcategory():
	data={}
	category_id=request.args['category_id']

	q="select * from `subcategory` where category_id='%s' and scstatus='active'"%(category_id)
	r=select(q)
	data['subcat']=r
	return render_template('sellerviewsubcategory.html',data=data)


@seller.route('/sellermanagecar',methods=['get','post'])
def sellermanagecar():
	data={}
	sid=session['sellerid']
	subcategory_id=request.args['subcategory_id']
	q="select * from subcategory where scstatus='active'"
	res=select(q)
	data['subcat']=res
	q="SELECT * FROM vehicle INNER JOIN subcategory USING(subcategory_id)INNER JOIN category USING(category_id) where subcategory_id='%s' and seller_id='%s'"%(subcategory_id,sid)
	res=select(q)
	data['car']=res
	# subcategory_id=request.form['subcategory_id']

	if "add" in request.form:
		vn=request.form['vn']
		d=request.form['d']
		b=request.form['b']
		m=request.form['m']
		y=request.form['y']
		km=request.form['km']
		p=request.form['p']
		image=request.files['image']
		path="static/img/"+str(uuid.uuid4())+image.filename
		image.save(path)
		q="insert into vehicle values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','active')"%(subcategory_id,sid,vn,d,b,m,y,km,p,path)
		insert(q)
		flash("added successfully")
		return redirect(url_for('seller.sellermanagecar',subcategory_id=subcategory_id))
	if "action" in request.args:
		action=request.args['action']
		vid=request.args['vid']
		subcategory_id=request.args['subcategory_id']
	else:
		action=None
	if "update" in request.form:
		vn=request.form['vn']
		d=request.form['d']
		b=request.form['b']
		m=request.form['m']
		y=request.form['y']
		km=request.form['km']
		p=request.form['p']
		image=request.files['image']
		path="static/img/"+str(uuid.uuid4())+image.filename
		image.save(path)

		q="update vehicle set   vname='%s',vdescription='%s',brand='%s',model='%s',year='%s',km='%s',price='%s',image='%s' where vehicle_id='%s'"%(vn,d,b,m,y,km,p,path,vid)
		r=update(q)
		flash("updated successfully")

		return redirect(url_for('seller.sellermanagecar',subcategory_id=subcategory_id))
	if action=="update":
		q="select * from  vehicle where vehicle_id='%s'"%(vid)
		r=select(q)
		data['updatecar']=r
	if action=="inactive":
		q="update vehicle set status='active' where vehicle_id='%s'"%(vid)
		update(q)
		flash("active successfully")

		return redirect(url_for('seller.sellermanagecar',subcategory_id=subcategory_id))
	if action=="active":
		q="update vehicle set status='inactive' where vehicle_id='%s'"%(vid)
		update(q)
		flash("inactive successfully")

		return redirect(url_for('seller.sellermanagecar',subcategory_id=subcategory_id))

	return render_template('sellermanagecar.html',data=data)


@seller.route('/sellermanagefeature',methods=['get','post'])
def sellermanagefeature():
	data={}
	vid=request.args['vid']
	data['vid']=vid
	q="select * from features where vehicle_id='%s'"%(vid)
	res=select(q)
	data['fea']=res
	if "add" in request.form:
		f=request.form['f']
		vid=request.args['vid']
		q="insert into features values(null,'%s','%s','active')"%(vid,f)
		insert(q)
		flash("added successfully")
		return redirect(url_for("seller.sellermanagefeature",vid=vid))
	
	if "action" in request.args:
		action=request.args['action']
		fid=request.args['fid']
	else:
		action=None
		
	if "update" in request.form:
		f=request.form['f']
		q="update features set feature='%s' where feature_id='%s'"%(f,fid)
		update(q)
		flash("update successfully")

		return redirect(url_for("seller.sellermanagefeature",fid=fid,vid=vid))
	if action=="update":
		q="select * from features where  feature_id='%s'" %(fid)
		res=select(q)
		data['updatefea']=res
	if action=="inactive":
		q="update features set fstatus='active' where feature_id='%s'"%(fid)
		update(q)
		flash("active successfully")
		return redirect(url_for("seller.sellermanagefeature",fid=fid,vid=vid))
	if action=="active":
		q="update features set fstatus='inactive' where feature_id='%s'"%(fid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for("seller.sellermanagefeature",fid=fid,vid=vid))
	
	return render_template('sellermanagefeature.html',data=data)

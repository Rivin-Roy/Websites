from flask import *
from database import *
from datetime import date,datetime 

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')


@admin.route('/adminviewseller',methods=['get','post'])
def adminviewseller():
	data={}
	q="select * from seller"
	r=select(q)
	data['seller']=r
	if "action" in request.args:
		action=request.args['action']
		seller_id=request.args['seller_id']
		aadhar=request.args['aadhar']
	else:
		action=None

	if action=="verify":
		q="select * from seller where aadharcard='%s'"%(aadhar)
		res=select(q)
		if res:
			flash("verified successfully")
			return redirect(url_for('admin.adminviewseller'))	
	return render_template('adminviewseller.html',data=data)

@admin.route('/verifyaadhar',methods=['get','post'])
def verifyaadhar():
	data={}
	seller_id=request.args['seller_id']
	aadhar=request.args['aadhar']
	data['aadhar']=aadhar
	if "verify" in request.form:
		q="select * from seller where aadharcard='%s'"%(aadhar)
		res=select(q)
		if res:
			q="update seller set astatus='verified' where seller_id='%s'"%(seller_id)
			update(q)
			flash("verified successfully")
			return redirect(url_for('admin.adminviewseller'))
		else:
			flash("verification failed")
			return redirect(url_for('admin.verifyaadhar'))	
	return render_template('verifyaadhar.html',data=data)

@admin.route('/adminviewbuyer',methods=['get','post'])
def adminviewbuyer():
	data={}
	q="select * from buyer"
	r=select(q)
	data['buyer']=r
	return render_template('adminviewbuyer.html',data=data)


@admin.route('/adminviewbooking',methods=['get','post'])
def adminviewbooking():
	data={}
	q="select * from `booking` inner join vehicle using (vehicle_id) inner join buyer using(buyer_id) "
	r=select(q)
	data['book']=r	
	return render_template('adminviewbooking.html',data=data)

@admin.route('/adminprintbooking',methods=['get','post'])
def adminprintbooking():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="select * from `booking` inner join vehicle using (vehicle_id) inner join buyer using(buyer_id) "
	r=select(q)
	data['book']=r	
	return render_template('adminprintbooking.html',data=data)
@admin.route('/adminprintseller',methods=['get','post'])
def adminprintseller():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="select * from `seller`  "
	r=select(q)
	data['view']=r	
	return render_template('adminprintseller.html',data=data)
@admin.route('/adminprintbuyer',methods=['get','post'])
def adminprintbuyer():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="select * from `buyer`  "
	r=select(q)
	data['view']=r	
	return render_template('adminprintbuyer.html',data=data)


@admin.route('/adminviewpayment',methods=['get','post'])
def adminviewpayment():
	data={}
	bid=request.args['book_id']

	q="select * from `payment` inner join `booking` using(`booking_id`) where booking_id='%s'"%(bid)
	r=select(q)
	data['pay']=r
	return render_template('adminviewpayment.html',data=data)


@admin.route('/adminmanagecategory',methods=['get','post'])
def adminmanagecategory():
	data={}
	if "add" in request.form:
		categories=request.form['cate']
		
		q="insert into category values(null,'%s','active')"%(categories)
		insert(q)
		flash("added successfully")
		return redirect(url_for("admin.adminmanagecategory"))
	
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
		
	if "update" in request.form:
		categories=request.form['cate']
		
		q="update category set category='%s' where category_id='%s'"%(categories,cid)
		insert(q)
		flash("update successfully")

		return redirect(url_for("admin.adminmanagecategory"))
	if action=="update":
		q="select * from category where  category_id='%s'" %(cid)
		res=select(q)
		data['updatecategorys']=res
	if action=="active":
		q="update category set cstatus='inactive' where category_id='%s'" %(cid)
		delete(q)
		flash("inactivated successfully")
		return redirect(url_for("admin.adminmanagecategory"))
	if action=="inactive":
		q="update category set cstatus='active' where category_id='%s'" %(cid)
		delete(q)
		flash("activated successfully")
		return redirect(url_for("admin.adminmanagecategory"))
	q="select * from category"
	res=select(q)
	data['categorys']=res
	return render_template('adminmanagecategory.html',data=data)


@admin.route('/adminmanagesubcategory',methods=['get','post'])
def adminmanagesubcategory():
	data={}
	q="select * from category inner join subcategory using(category_id)"
	r=select(q)
	data['subcat']=r
	q="select * from category where cstatus='active' "
	r=select(q)
	data['categoryyy']=r
	if "add" in request.form:
		cid=request.form['cid']
		categories=request.form['cate']
		qs="insert into subcategory values(null,'%s','%s','active')"%(cid,categories)
		insert(qs)
		flash("added successfully")

		return redirect(url_for('admin.adminmanagesubcategory'))
	if "action" in request.args:
		action=request.args['action']
		scid=request.args['scid']
	else:
		action=None
		
	if "update" in request.form:
		categories=request.form['cate']
		cid=request.form['cid']
		q="update subcategory set category_id='%s',subcategory='%s' where subcategory_id='%s'"%(cid,categories,scid)
		insert(q)
		flash("update successfully")

		return redirect(url_for("admin.adminmanagesubcategory"))
	if action=="update":
		q="select * from subcategory where  subcategory_id='%s'" %(scid)
		res=select(q)
		data['updatesubcategorys']=res
	if action=="active":
		q="update subcategory set scstatus='inactive' where subcategory_id='%s'" %(scid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for("admin.adminmanagesubcategory"))
	if action=="inactive":
		q="update subcategory set scstatus='active' where subcategory_id='%s'" %(scid)
		update(q)
		flash("active successfully")
		return redirect(url_for("admin.adminmanagesubcategory"))
	
	return render_template('adminmanagesubcategory.html',data=data)

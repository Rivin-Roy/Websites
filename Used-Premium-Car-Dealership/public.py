from flask import *
from database import *
import random


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():
	if "login" in request.form:
		uname=request.form['un']
		pwd=request.form['pa']
		q="select * from login where username='%s' and password='%s'"%(uname,pwd)
		res=select(q)
		if res:
			if res[0]['usertype']=="admin":
				flash("login successfully")

				return redirect(url_for('admin.adminhome'))

			elif res[0]['usertype']=="seller":
				q1="select * from seller where email='%s'"%(res[0]['username'])
				res1=select(q1)
				session['sellerid']=res1[0]['seller_id']
				flash("login successfully")
				return redirect(url_for('seller.sellerhome'))

			elif res[0]['usertype']=="buyer":
				q2="select * from buyer where email='%s'"%(res[0]['username'])
				res2=select(q2)
				session['email']=res2[0]['email']
				session['buyer_id']=res2[0]['buyer_id']
				flash("login successfully")

				return redirect(url_for('buyer.buyerhome'))
		else:
			flash("invaild username and password")



	return render_template('login.html')


@public.route('/sellerregister',methods=['get','post'])
def sellerregister():
	if "register" in request.form:
		fna=request.form['f']
		pho=request.form['ph']
		pla=request.form['pl']
		aa=request.form['aa']
		em=request.form['e']
		pwd=request.form['p']
		pwd=request.form['p']
		q="select * from login where username='%s'"%(em)
		res=select(q)
		if res:
			flash("username is already exist")
		else:

			ql="insert into login values('%s','%s','seller')"%(em,pwd)
			rl=insert(ql)
			qs="insert into seller values(null,'%s','%s','%s','%s','%s','pending')"%(fna,pla,pho,em,aa)
			insert(qs)
			flash("register successfully")
		# return redirect(url_for('public.supplierregister'))
		
	return render_template('sellerregister.html')


@public.route('/buyerregister',methods=['get','post'])
def buyerregister():
	if "register" in request.form:
		fna=request.form['f']
		ln=request.form['l']
		pho=request.form['ph']
		pla=request.form['pl']
		aa=request.form['aa']
		em=request.form['e']
		pwd=request.form['p']
		q="select * from login where username='%s'"%(em)
		res=select(q)
		if res:
			flash("username is already exist")
		else:
			
			ql="insert into login values('%s','%s','buyer')"%(em,pwd)
			rl=insert(ql)
			qs="insert into buyer values(null,'%s','%s','%s','%s','%s','%s')"%(fna,ln,pla,pho,em,aa)
			insert(qs)
			flash("register successfully")
		# return redirect(url_for('public.supplierregister'))
		
	return render_template('buyerregister.html')


@public.route('/forgotpassword',methods=['get','post'])
def forgotpassword():
	data={}
	if "forgot" in request.form:
		uname=request.form['un']
		phone=request.form['p']
		q="select * from login  where username='%s' and usertype='buyer'"%(uname)
		r=select(q)
		print(r)
		if r:
			session['username']=r[0]['username']
			q="select * from  buyer inner join login on buyer.email=login.username where username='%s' and phone='%s' "%(uname,phone)
			res=select(q)
			print(res)
			if res:
				print(res)
				flash("verified")
				email=res[0]['email']
				print(email)
				rd=random.randrange(1000,9999,4)
				msg=str(rd)
				session['rd']=rd
				print(rd)
				try:
					gmail = smtplib.SMTP('smtp.gmail.com', 587)
					gmail.ehlo()
					gmail.starttls()
					gmail.login('projectsriss2020@gmail.com','messageforall')
				except Exception as e:
					print("Couldn't setup email!!"+str(e))

				msg = MIMEText(msg)

				msg['Subject'] = 'OTP FOR password RECOVRY'

				msg['To'] = email

				msg['From'] = 'projectsriss2020@gmail.com'

				try:
					gmail.send_message(msg)
					print(msg)
					flash("EMAIL SENED SUCCESFULLY")
					return redirect(url_for('public.setotp'))


				except Exception as e:
					print("COULDN'T SEND EMAIL", str(e))
					return redirect(url_for('public.forgotpassword'))
			


				return redirect(url_for('public.setotp'))
			else:
				flash("invalid password")
				return redirect(url_for('public.forgotpassword'))
				
		else:
			q="select * from login inner join seller on seller.email=login.username  where username='%s' and phone='%s'"%(uname,phone)
			res1=select(q)		
			if res1:
				session['username']=res1[0]['username']
				email=res1[0]['email']

				flash("verified")
				rd=random.randrange(1000,9999,4)
				data['rd']=rd
				print(rd)
				session['rd']=rd
				msg=str(rd)

				print(rd)
				try:
					gmail = smtplib.SMTP('smtp.gmail.com', 587)
					gmail.ehlo()
					gmail.starttls()
					gmail.login('projectsriss2020@gmail.com','messageforall')
				except Exception as e:
					print("Couldn't setup email!!"+str(e))

				msg = MIMEText(msg)

				msg['Subject'] = 'OTP FOR password RECOVRY'

				msg['To'] = email

				msg['From'] = 'projectsriss2020@gmail.com'

				try:
					gmail.send_message(msg)
					print(msg)
					flash("EMAIL SENED SUCCESFULLY")
					return redirect(url_for('public.setotp'))


				except Exception as e:
					print("COULDN'T SEND EMAIL", str(e))
					return redirect(url_for('public.forgotpassword'))
			


				return redirect(url_for('public.setotp'))
			else:
				flash("invalid password")
				return redirect(url_for('public.forgotpassword'))	

	return render_template('forgotpassword.html',data=data)

@public.route('/setotp',methods=['get','post'])
def setotp():
	rd=session['rd']
	if "otp" in request.form:
		otp=request.form['otp']
		if int(otp)==int(rd):
			return redirect(url_for('public.setpassword'))
		else:
			flash("invalid otp")
			return redirect(url_for('public.forgotpassword'))



	return render_template('setotp.html')

@public.route('/setpassword',methods=['get','post'])
def setpassword():

	if "conform" in request.form:
		new_pas=request.form['new_pas']
		con_pas=request.form['con_pas']
		username=session['username']
		print(username)

		if new_pas==con_pas :
			q="update login set password='%s' where username='%s'"%(con_pas,username)
			r=update(q)
			print(r)

			flash("verified successfully")
			flash(" password changed successfully")
			return redirect(url_for('public.login'))
		else:
			flash("sorry! password mismatched ")
			return redirect(url_for('public.setpassword'))
	return render_template('setpassword.html')



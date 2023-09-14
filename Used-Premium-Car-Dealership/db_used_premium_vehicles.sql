/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.14-MariaDB : Database - py_used_premium_vehicles
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`py_used_premium_vehicles` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `py_used_premium_vehicles`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `buyer_id` int(11) DEFAULT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`buyer_id`,`vehicle_id`,`amount`,`status`) values (1,1,1,'10000','paid'),(6,1,7,'12000','paid'),(24,1,8,'20000','paid'),(25,1,11,'15000','booked');

/*Table structure for table `buyer` */

DROP TABLE IF EXISTS `buyer`;

CREATE TABLE `buyer` (
  `buyer_id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `aadharcard` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`buyer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `buyer` */

insert  into `buyer`(`buyer_id`,`firstname`,`lastname`,`place`,`phone`,`email`,`aadharcard`) values (1,'Athira','M','Kozhikode','9630011203','joyelroy24@gmail.com','333333333333'),(2,'Anirudh','k','kollam','9874563210','ani@gmail.com','222222222222');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(100) DEFAULT NULL,
  `cstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category`,`cstatus`) values (2,'mffkfjvnfd','active'),(5,'ejjdndkj','active'),(6,'kgbklgkb','active'),(7,'mklkmk','inactive');

/*Table structure for table `features` */

DROP TABLE IF EXISTS `features`;

CREATE TABLE `features` (
  `feature_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `feature` varchar(100) DEFAULT NULL,
  `fstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feature_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `features` */

insert  into `features`(`feature_id`,`vehicle_id`,`feature`,`fstatus`) values (1,1,'dddff','active'),(2,1,'kmkgmblgokkijijjuj','active'),(3,1,'shahje','active'),(4,1,'jkjkk','active'),(5,1,'nnmm','inactive');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`usertype`) values ('h@gmail.com','hh','seller'),('admin','admin','admin'),('joyelroy24@gmail.com','aa','buyer'),('j@gmail.com','j','seller'),('aswani@gmail.com','aaa','seller'),('ani@gmail.com','ani','buyer');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`amount`,`date`) values (1,1,'10000','2022-02-04'),(4,6,'12000','2022-04-06'),(5,24,'20000','2022-04-11');

/*Table structure for table `seller` */

DROP TABLE IF EXISTS `seller`;

CREATE TABLE `seller` (
  `seller_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `aadharcard` varchar(100) DEFAULT NULL,
  `astatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `seller` */

insert  into `seller`(`seller_id`,`name`,`place`,`phone`,`email`,`aadharcard`,`astatus`) values (1,'Benny','ernakulam','9988556677','h@gmail.com','888888888888','verified'),(3,'dskmk','hhdh','9988776655','joyelroy24@gmail.com','999999999999','verified'),(4,'joel roy','vypin','9988667744','j@gmail.com','555555555555','pending'),(5,'aswani','kozhikode','9988776655','aswani@gmail.com','111111111111','pending');

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `subcategory` varchar(100) DEFAULT NULL,
  `scstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`category_id`,`subcategory`,`scstatus`) values (1,2,'hgf','active'),(5,2,'ifrjfjrgi','inactive');

/*Table structure for table `vehicle` */

DROP TABLE IF EXISTS `vehicle`;

CREATE TABLE `vehicle` (
  `vehicle_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategory_id` int(11) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL,
  `vname` varchar(100) DEFAULT NULL,
  `vdescription` varchar(100) DEFAULT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `year` varchar(100) DEFAULT NULL,
  `km` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

/*Data for the table `vehicle` */

insert  into `vehicle`(`vehicle_id`,`subcategory_id`,`seller_id`,`vname`,`vdescription`,`brand`,`model`,`year`,`km`,`price`,`image`,`status`) values (1,1,1,'jcdcjdjd','nbvbjhbcehbdxv','mvn ','kl977','2019','23','10000','static/img/ca5fc970-34a8-4b69-bd55-87114409ab5b20191211_155243-480x605.jpg','selled'),(7,1,1,'wererr','gtrygbbbbbbbrd','grdrt','3rf','2018','34','12000','static/img/fc3fc4a7-0a6a-4a6e-a291-1782274124a6download (1).jpg','selled'),(8,1,1,'wed','asd','cxz','kl9876','2018','45','20000','static/img/57739b7b-0ab7-4569-8fe7-306b9bc73b5b13.jpg','selled'),(11,1,1,'mjdcd','vdd','ijuh','kl9845','2017','30','15000','static/img/1e244b6e-525d-4ef7-8d6e-3fd50a1954f2download (2).png','booked'),(12,1,1,'gghh','mjj','gjh','kl9873','2012','55','25000','static/img/2f6359c3-37c7-4f26-b924-cc54170a226fpexels-polina-tankilevitch-5234510.jpg','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

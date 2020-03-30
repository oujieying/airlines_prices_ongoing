#创建数据库
drop database if exists airlines;
create  database airlines;

#创建教师信息表
drop table if exists tearchers_for_test;
CREATE TABLE `teachers_for_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `info` text(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
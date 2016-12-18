/*
Navicat MySQL Data Transfer

Source Server         : 本地_10.1.61.98
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : django_advanced

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2016-12-18 17:23:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add poem', '7', 'add_poem');
INSERT INTO `auth_permission` VALUES ('20', 'Can change poem', '7', 'change_poem');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete poem', '7', 'delete_poem');
INSERT INTO `auth_permission` VALUES ('22', 'Can add to do', '8', 'add_todo');
INSERT INTO `auth_permission` VALUES ('23', 'Can change to do', '8', 'change_todo');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete to do', '8', 'delete_todo');
INSERT INTO `auth_permission` VALUES ('25', 'Can add auth group', '9', 'add_authgroup');
INSERT INTO `auth_permission` VALUES ('26', 'Can change auth group', '9', 'change_authgroup');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete auth group', '9', 'delete_authgroup');
INSERT INTO `auth_permission` VALUES ('28', 'Can add auth group permissions', '10', 'add_authgrouppermissions');
INSERT INTO `auth_permission` VALUES ('29', 'Can change auth group permissions', '10', 'change_authgrouppermissions');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete auth group permissions', '10', 'delete_authgrouppermissions');
INSERT INTO `auth_permission` VALUES ('31', 'Can add auth permission', '11', 'add_authpermission');
INSERT INTO `auth_permission` VALUES ('32', 'Can change auth permission', '11', 'change_authpermission');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete auth permission', '11', 'delete_authpermission');
INSERT INTO `auth_permission` VALUES ('34', 'Can add auth user', '12', 'add_authuser');
INSERT INTO `auth_permission` VALUES ('35', 'Can change auth user', '12', 'change_authuser');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete auth user', '12', 'delete_authuser');
INSERT INTO `auth_permission` VALUES ('37', 'Can add auth user groups', '13', 'add_authusergroups');
INSERT INTO `auth_permission` VALUES ('38', 'Can change auth user groups', '13', 'change_authusergroups');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete auth user groups', '13', 'delete_authusergroups');
INSERT INTO `auth_permission` VALUES ('40', 'Can add auth user user permissions', '14', 'add_authuseruserpermissions');
INSERT INTO `auth_permission` VALUES ('41', 'Can change auth user user permissions', '14', 'change_authuseruserpermissions');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete auth user user permissions', '14', 'delete_authuseruserpermissions');
INSERT INTO `auth_permission` VALUES ('43', 'Can add django admin log', '15', 'add_djangoadminlog');
INSERT INTO `auth_permission` VALUES ('44', 'Can change django admin log', '15', 'change_djangoadminlog');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete django admin log', '15', 'delete_djangoadminlog');
INSERT INTO `auth_permission` VALUES ('46', 'Can add django content type', '16', 'add_djangocontenttype');
INSERT INTO `auth_permission` VALUES ('47', 'Can change django content type', '16', 'change_djangocontenttype');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete django content type', '16', 'delete_djangocontenttype');
INSERT INTO `auth_permission` VALUES ('49', 'Can add django migrations', '17', 'add_djangomigrations');
INSERT INTO `auth_permission` VALUES ('50', 'Can change django migrations', '17', 'change_djangomigrations');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete django migrations', '17', 'delete_djangomigrations');
INSERT INTO `auth_permission` VALUES ('52', 'Can add django session', '18', 'add_djangosession');
INSERT INTO `auth_permission` VALUES ('53', 'Can change django session', '18', 'change_djangosession');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete django session', '18', 'delete_djangosession');
INSERT INTO `auth_permission` VALUES ('55', 'Can add polls poem', '19', 'add_pollspoem');
INSERT INTO `auth_permission` VALUES ('56', 'Can change polls poem', '19', 'change_pollspoem');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete polls poem', '19', 'delete_pollspoem');
INSERT INTO `auth_permission` VALUES ('58', 'Can add polls todo', '20', 'add_pollstodo');
INSERT INTO `auth_permission` VALUES ('59', 'Can change polls todo', '20', 'change_pollstodo');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete polls todo', '20', 'delete_pollstodo');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$24000$VckTm595rne5$IVpO2x+yXsSrhhg1tqTwoKjbbLVtCniSjAN9dY2AoPM=', '2016-12-18 09:13:39.447112', '1', 'admin', '', '', '370835062@qq.com', '1', '1', '2016-12-18 09:13:17.395277');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('9', 'polls', 'authgroup');
INSERT INTO `django_content_type` VALUES ('10', 'polls', 'authgrouppermissions');
INSERT INTO `django_content_type` VALUES ('11', 'polls', 'authpermission');
INSERT INTO `django_content_type` VALUES ('12', 'polls', 'authuser');
INSERT INTO `django_content_type` VALUES ('13', 'polls', 'authusergroups');
INSERT INTO `django_content_type` VALUES ('14', 'polls', 'authuseruserpermissions');
INSERT INTO `django_content_type` VALUES ('15', 'polls', 'djangoadminlog');
INSERT INTO `django_content_type` VALUES ('16', 'polls', 'djangocontenttype');
INSERT INTO `django_content_type` VALUES ('17', 'polls', 'djangomigrations');
INSERT INTO `django_content_type` VALUES ('18', 'polls', 'djangosession');
INSERT INTO `django_content_type` VALUES ('7', 'polls', 'poem');
INSERT INTO `django_content_type` VALUES ('19', 'polls', 'pollspoem');
INSERT INTO `django_content_type` VALUES ('20', 'polls', 'pollstodo');
INSERT INTO `django_content_type` VALUES ('8', 'polls', 'todo');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2016-12-18 08:57:17.622900');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2016-12-18 08:57:19.033997');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2016-12-18 08:57:19.295062');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2016-12-18 08:57:19.333087');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2016-12-18 08:57:19.512737');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2016-12-18 08:57:19.627368');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2016-12-18 08:57:19.753827');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2016-12-18 08:57:19.787854');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2016-12-18 08:57:19.943972');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2016-12-18 08:57:19.951977');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2016-12-18 08:57:19.969990');
INSERT INTO `django_migrations` VALUES ('12', 'polls', '0001_initial', '2016-12-18 08:57:20.305197');
INSERT INTO `django_migrations` VALUES ('13', 'polls', '0002_auto_20160507_0634', '2016-12-18 08:57:20.501364');
INSERT INTO `django_migrations` VALUES ('14', 'polls', '0003_auto_20160507_0654', '2016-12-18 08:57:20.563408');
INSERT INTO `django_migrations` VALUES ('15', 'polls', '0004_auto_20160507_0700', '2016-12-18 08:57:20.587426');
INSERT INTO `django_migrations` VALUES ('16', 'polls', '0005_auto_20160507_0705', '2016-12-18 08:57:20.607438');
INSERT INTO `django_migrations` VALUES ('17', 'polls', '0006_todo', '2016-12-18 08:57:20.655471');
INSERT INTO `django_migrations` VALUES ('18', 'polls', '0007_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django', '2016-12-18 08:57:20.686106');
INSERT INTO `django_migrations` VALUES ('19', 'sessions', '0001_initial', '2016-12-18 08:57:20.772917');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('0fnl9wuj4kb6odd9crj9r651f7fqgpik', 'MGViNDIxMTAzN2VlMjI4YzAyYWNjNGQzODExMWFkZTk1YzVjZjJmYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDcyNTU4MWVkZDNmNmYzMzAxNjQ2OGMyMjE4OTVkYjdlZDRkMDk0ZiIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2017-01-01 09:13:39.458120');

-- ----------------------------
-- Table structure for polls_poem
-- ----------------------------
DROP TABLE IF EXISTS `polls_poem`;
CREATE TABLE `polls_poem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(200) NOT NULL,
  `title` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of polls_poem
-- ----------------------------
INSERT INTO `polls_poem` VALUES ('2', '李白', '静夜思');
INSERT INTO `polls_poem` VALUES ('3', '李白', '早发白帝城');
INSERT INTO `polls_poem` VALUES ('4', '李白', '望庐山瀑布');
INSERT INTO `polls_poem` VALUES ('5', '王维', '过香积寺');

-- ----------------------------
-- Table structure for polls_todo
-- ----------------------------
DROP TABLE IF EXISTS `polls_todo`;
CREATE TABLE `polls_todo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(200) NOT NULL,
  `is_done` tinyint(1) NOT NULL,
  `priority` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of polls_todo
-- ----------------------------
INSERT INTO `polls_todo` VALUES ('1', '早餐', '1', '1');
INSERT INTO `polls_todo` VALUES ('2', '晨跑', '0', '2');
INSERT INTO `polls_todo` VALUES ('3', '上班', '0', '3');
INSERT INTO `polls_todo` VALUES ('4', '午餐', '0', '3');
INSERT INTO `polls_todo` VALUES ('5', '午休', '0', '3');
INSERT INTO `polls_todo` VALUES ('6', '健身房锻炼', '0', '1');
INSERT INTO `polls_todo` VALUES ('7', '睡觉', '0', '4');

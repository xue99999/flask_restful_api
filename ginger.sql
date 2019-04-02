/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : ginger

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2019-04-02 21:46:10
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `author` varchar(30) DEFAULT NULL,
  `binding` varchar(20) DEFAULT NULL,
  `publisher` varchar(50) DEFAULT NULL,
  `price` varchar(20) DEFAULT NULL,
  `pages` int(11) DEFAULT NULL,
  `pubdate` varchar(20) DEFAULT NULL,
  `isbn` varchar(15) NOT NULL,
  `summary` varchar(1000) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isbn` (`isbn`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES (null, '1', '1', '123456789', 'xuejun', '精装', 'xuejun', '12.00', '386', '1525874561', '99998888', '这本书的简介', 'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6');
INSERT INTO `book` VALUES (null, '1', '3', '哈哈', 'xuejun123', '精装', 'xuejun123', '22.00', '888', '1525874561', '99996666', '这本书的简介', 'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6');

-- ----------------------------
-- Table structure for gift
-- ----------------------------
DROP TABLE IF EXISTS `gift`;
CREATE TABLE `gift` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `isbn` varchar(15) NOT NULL,
  `launched` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `gift_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of gift
-- ----------------------------
INSERT INTO `gift` VALUES ('1552394108', '1', '4', '5', '99996666', '0');
INSERT INTO `gift` VALUES ('1552394120', '1', '5', '5', '99998888', '0');

-- ----------------------------
-- Table structure for todo_list
-- ----------------------------
DROP TABLE IF EXISTS `todo_list`;
CREATE TABLE `todo_list` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `text` varchar(200) NOT NULL,
  `textStatus` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `todo_list_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of todo_list
-- ----------------------------
INSERT INTO `todo_list` VALUES (null, '1', '1', '5', '213', '2');
INSERT INTO `todo_list` VALUES (null, '1', '2', '5', '213123', '2');
INSERT INTO `todo_list` VALUES (null, '1', '3', '5', '123123', '2');
INSERT INTO `todo_list` VALUES (null, '1', '4', '5', '我是新加的一条数据,哈哈哈哈', '2');
INSERT INTO `todo_list` VALUES (null, '1', '5', '5', '2222', '2');
INSERT INTO `todo_list` VALUES (null, '1', '6', '5', '66666', '2');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(24) NOT NULL,
  `nickname` varchar(24) DEFAULT NULL,
  `auth` smallint(6) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nickname` (`nickname`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1551601820', '1', '5', '1@qq.com', 'xuejun111', '1', 'pbkdf2:sha256:50000$Y8s4diwZ$5c9a4ccff55f1720c81f6cd075feff9c8694180bb5c5407fe7ff6fa0e375935d');
INSERT INTO `user` VALUES ('1551601837', '1', '6', '2@qq.com', 'xuejun222', '1', 'pbkdf2:sha256:50000$qZuo2tWV$a023a6958a5a235552ecf8a4364f2e267929647fcf9abd19e63ca9e70e1e12c7');
INSERT INTO `user` VALUES ('1551601848', '1', '7', '3@qq.com', 'xuejun333', '1', 'pbkdf2:sha256:50000$jCfSobu4$f2c8c27f6c2a330cfe198392e5d2c90970296eb1224b1d82165ad01df063d844');
INSERT INTO `user` VALUES ('1552140079', '1', '8', '999@qq.com', 'Super', '2', 'pbkdf2:sha256:50000$cQdImgkS$1b4a3339792c3ee54a97fc2cdf3ed358da97d0726ce1f80e940ef7434e782c01');
INSERT INTO `user` VALUES ('1552140171', '1', '9', 'admin@qq.com', 'admin', '2', 'pbkdf2:sha256:50000$29MgjA7V$003b185ae40a6b2d4870cdb46272c2194ab6a80317c934e45ed1471f7d44b151');
INSERT INTO `user` VALUES ('1552307451', '1', '10', 'admin123@qq.com', 'admin123', '2', 'pbkdf2:sha256:50000$JaedTv4q$66bf621daef4bcf2a65ef4a8ecb2e712749a1bca6cd492cbc0f41ba320947311');

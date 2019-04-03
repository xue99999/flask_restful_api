/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : ginger

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2019-04-02 09:42:40
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of book
-- ----------------------------

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of gift
-- ----------------------------

-- ----------------------------
-- Table structure for thing
-- ----------------------------
DROP TABLE IF EXISTS `thing`;
CREATE TABLE `thing` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `content` varchar(15) NOT NULL,
  `complete_status` varchar(2) DEFAULT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `thing_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of thing
-- ----------------------------
INSERT INTO `thing` VALUES ('1553572542', '1', '1', '1', '111，我是第一条数据', '02', '1554100225');
INSERT INTO `thing` VALUES ('1553572573', '1', '2', '1', '222，我是第二条数据', '01', '1553852079');
INSERT INTO `thing` VALUES ('1553572583', '1', '3', '1', '333，我是第三条数据', '02', '1553853378');
INSERT INTO `thing` VALUES ('1553746046', '1', '4', '1', '中午12.30去吃饭', '02', '1554100222');
INSERT INTO `thing` VALUES ('1553746275', '0', '5', '1', '还不吃饭啊，饿死我了', '02', '1553828827');
INSERT INTO `thing` VALUES ('1553758287', '0', '6', '1', '新的一条数据啊，哈哈哈', '01', '1553828829');
INSERT INTO `thing` VALUES ('1553764898', '0', '7', '1', '123123123', '01', '1553828757');
INSERT INTO `thing` VALUES ('1553824185', '0', '8', '1', '329新增哈哈哈', '02', '1553824202');
INSERT INTO `thing` VALUES ('1553824474', '1', '9', '2', '我是2账号', '02', '1553824477');
INSERT INTO `thing` VALUES ('1553828203', '0', '10', '1', '新佳佳哈哈哈哈', '02', '1553828674');
INSERT INTO `thing` VALUES ('1553828212', '0', '11', '1', '我就是要新加数据哈哈哈', '02', '1553828679');
INSERT INTO `thing` VALUES ('1553829298', '0', '12', '1', '新的哈哈哈哈', '01', '1553852702');
INSERT INTO `thing` VALUES ('1553845653', '1', '13', '1', '新增，哈哈哈哈', '01', '1554100224');
INSERT INTO `thing` VALUES ('1553845783', '0', '14', '1', '新加的一套数据', '02', '1553845801');
INSERT INTO `thing` VALUES ('1553846432', '1', '15', '1', '新增的一条数据', '02', '1553852706');
INSERT INTO `thing` VALUES ('1553846537', '0', '16', '1', '新家的数据刷单但是', '01', '1553847457');
INSERT INTO `thing` VALUES ('1553846591', '0', '17', '1', 'xin jia ha ha ', '01', '1553846591');
INSERT INTO `thing` VALUES ('1553850268', '1', '18', '1', '新家的一条秋裤，哈哈哈', '02', '1553851295');
INSERT INTO `thing` VALUES ('1553850859', '0', '19', '1', '注意呀', '02', '1553850940');
INSERT INTO `thing` VALUES ('1553852111', '0', '20', '1', '新家的数据哈哈', '01', '1553852726');
INSERT INTO `thing` VALUES ('1553852715', '0', '21', '1', 'cesc ', '02', '1553852717');
INSERT INTO `thing` VALUES ('1553852736', '1', '22', '1', 'cecsce', '02', '1554100245');
INSERT INTO `thing` VALUES ('1554089801', '1', '23', '3', '我是新任务哈哈哈', '01', '1554090547');
INSERT INTO `thing` VALUES ('1554089836', '1', '24', '3', '新任务哈哈哈哈', '01', '1554103280');
INSERT INTO `thing` VALUES ('1554089845', '1', '25', '3', '就是新的任务，耶耶耶', '01', '1554103519');
INSERT INTO `thing` VALUES ('1554090054', '1', '26', '3', '就是新任务哈哈哈', '02', '1554102805');
INSERT INTO `thing` VALUES ('1554100119', '1', '27', '3', '新增哈哈', '02', '1554102543');
INSERT INTO `thing` VALUES ('1554100236', '1', '28', '1', '中央音乐学院', '02', '1554100246');
INSERT INTO `thing` VALUES ('1554100287', '1', '29', '1', '哈哈哈哈', '01', '1554100287');
INSERT INTO `thing` VALUES ('1554103529', '1', '30', '3', '嘻嘻哈哈灌灌灌灌', '02', '1554103532');

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1553567059', '1', '1', 'xue@qq.com', 'xuejun', '1', 'pbkdf2:sha256:50000$9BHtjeDo$bed775d028ff8a2f4d2e9f2d6c573b351c0376b69a9eb35239ef4e6d526ccf1a');
INSERT INTO `user` VALUES ('1553585228', '1', '2', 'haha@qq.com', 'haha', '1', 'pbkdf2:sha256:50000$CsF4DIVm$a8fa0594c2e14ff1f652e65c74599e20fa7a5f9138bd51f917126e028b565b13');
INSERT INTO `user` VALUES ('1554088428', '1', '3', '123@qq.com', '123', '1', 'pbkdf2:sha256:50000$HBatolEo$ba297a5d32d250e113180e7b973b2b88ee47e3a24adaf2202305a0f5e0f4b7ee');

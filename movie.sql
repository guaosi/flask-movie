/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : movie

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2018-07-05 12:06:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(256) DEFAULT NULL,
  `is_super` smallint(6) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_admin_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('2018-06-30 18:20:23', '1', 'admin', 'pbkdf2:sha256:50000$yyMrgZ3W$653d7b78ab6b354bf9f912c9ecf05b5fe9346965475c133db3219229bae347b9', '0', '1');
INSERT INTO `admin` VALUES ('2018-07-02 20:01:08', '2', 'guaosi', 'pbkdf2:sha256:50000$Cfq5HNhx$dd57b5623a478e73a5fd777d5043eca20765bd5feb4f7cd1e54f0ba3e35292d8', '1', '4');
INSERT INTO `admin` VALUES ('2018-07-02 20:02:08', '3', '张三', 'pbkdf2:sha256:50000$zLz2Ey0j$dd97793584dac4a6f915fd3a1e47125a6fa8778f7ca63417d7356193af4d37f0', '1', '4');

-- ----------------------------
-- Table structure for adminlog
-- ----------------------------
DROP TABLE IF EXISTS `adminlog`;
CREATE TABLE `adminlog` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_adminlog_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of adminlog
-- ----------------------------
INSERT INTO `adminlog` VALUES ('2018-07-01 23:44:27', '1', '1', '127.0.0.1');
INSERT INTO `adminlog` VALUES ('2018-07-01 23:44:38', '2', '1', '127.0.0.1');
INSERT INTO `adminlog` VALUES ('2018-07-01 23:44:44', '3', '1', '127.0.0.1');
INSERT INTO `adminlog` VALUES ('2018-07-01 23:44:50', '4', '1', '127.0.0.1');
INSERT INTO `adminlog` VALUES ('2018-07-02 12:08:53', '5', '1', '127.0.0.1');
INSERT INTO `adminlog` VALUES ('2018-07-02 13:46:30', '6', '1', '127.0.0.1');
INSERT INTO `adminlog` VALUES ('2018-07-03 19:53:51', '7', '1', '127.0.0.1');
INSERT INTO `adminlog` VALUES ('2018-07-04 12:42:43', '8', '1', '127.0.0.1');
INSERT INTO `adminlog` VALUES ('2018-07-04 21:56:34', '9', '1', '127.0.0.1');

-- ----------------------------
-- Table structure for auth
-- ----------------------------
DROP TABLE IF EXISTS `auth`;
CREATE TABLE `auth` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `url` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `url` (`url`),
  KEY `ix_auth_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth
-- ----------------------------
INSERT INTO `auth` VALUES ('2018-07-02 14:16:18', '1', '添加标签', '/tag/add');
INSERT INTO `auth` VALUES ('2018-07-02 14:17:32', '2', '编辑标签', '/auth/edit/<int:id>');
INSERT INTO `auth` VALUES ('2018-07-02 14:18:25', '3', '标签列表', '/tag/list/<int:page>');
INSERT INTO `auth` VALUES ('2018-07-02 14:18:34', '4', '删除标签', '/tag/edit/<int:id>');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `user_id` int(11) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `movie_id` (`movie_id`),
  KEY `ix_comment_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES ('2018-07-01 21:20:05', '1', '经典', '1', '1');
INSERT INTO `comment` VALUES ('2018-07-01 21:20:05', '2', '刺激', '2', '2');
INSERT INTO `comment` VALUES ('2018-07-01 21:20:05', '3', '悬疑', '3', '3');
INSERT INTO `comment` VALUES ('2018-07-01 21:20:05', '4', '好看', '1', '3');
INSERT INTO `comment` VALUES ('2018-07-04 18:15:36', '7', '<p>测试评论</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:15:47', '8', '<p><img src=\"http://img.baidu.com/hi/jx2/j_0017.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0006.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0006.gif\"/></p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:18:12', '9', '<p>测试异步</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:18:23', '10', '<p>测试异步</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:18:39', '11', '<p>再测试异步</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:18:52', '12', '<p>哇</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:19:57', '13', '<p>测试</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:20:51', '14', '<p>测试异步</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:24:30', '15', '<p>再次测试</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:26:31', '16', '<p>测试测试</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:28:01', '17', '<p>看看是否</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:29:43', '18', '<p>测试</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:30:15', '19', '<p>测试</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:31:14', '20', '<p>ces&nbsp;</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:31:55', '21', '<p>ces</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 18:42:19', '22', '<p>评论测试</p>', '6', '6');
INSERT INTO `comment` VALUES ('2018-07-04 20:35:38', '23', '<p>不错哦</p>', '8', '3');
INSERT INTO `comment` VALUES ('2018-07-04 20:36:17', '24', '<p>不错哦<br/></p>', '8', '3');

-- ----------------------------
-- Table structure for movie
-- ----------------------------
DROP TABLE IF EXISTS `movie`;
CREATE TABLE `movie` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(150) DEFAULT NULL,
  `url` varchar(150) DEFAULT NULL,
  `info` text,
  `logo` varchar(150) DEFAULT NULL,
  `star` smallint(6) DEFAULT NULL,
  `playnum` int(11) DEFAULT NULL,
  `commentnum` int(11) DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  `area` varchar(150) DEFAULT NULL,
  `release_time` date DEFAULT NULL,
  `length` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `url` (`url`),
  UNIQUE KEY `logo` (`logo`),
  KEY `tag_id` (`tag_id`),
  KEY `ix_movie_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of movie
-- ----------------------------
INSERT INTO `movie` VALUES ('2018-07-01 17:22:45', '1', '这是一张图片', 'uploads/video/20180701/201807011722451769ea0399a042cca6984b90915a1027.mp4', '这是一张图片这是一张图片', 'uploads/video/20180703/201807031955395705025553334ee794519b7a43e5028d.jpg', '4', '4', '0', '4', '福建', '2018-07-20', '72');
INSERT INTO `movie` VALUES ('2018-07-01 17:44:15', '2', '变形金', 'uploads/video/20180701/201807011813561e0af514cd2541888d6bcc43d7c3f003.mp4', '变形金刚', 'uploads/video/20180701/201807011814070565666aae1548df81c6b1bb48e529f3.jpg', '3', '4', '0', '5', '福建', '2018-07-14', '72');
INSERT INTO `movie` VALUES ('2018-07-01 18:56:05', '3', '不错~', 'uploads/video/20180701/20180701185633387f5cfb4f9c4e1793d8832a55bf1add.mp4', '不错不错哦', 'uploads/image/20180701/20180701185605980d3fc5a70c40e0bedaa00a8d93d258.jpg', '4', '17', '2', '3', '北京', '2018-07-05', '120');
INSERT INTO `movie` VALUES ('2018-07-01 23:36:30', '4', '笔仙', 'uploads/video/20180701/20180701233630b802fa95d35140cf9c5df27422adeacc.mp4', '笔仙笔仙', 'uploads/image/20180701/20180701233630e537af22471244138716962843aaa309.jpg', '4', '0', '0', '2', '福建', '2018-07-26', '72');
INSERT INTO `movie` VALUES ('2018-07-04 15:17:00', '5', '鬼吹灯', 'uploads/video/20180704/2018070415170063d026648b0646e0a7c048e5c7c11ab6.mp4', '鬼吹灯', 'uploads/image/20180704/20180704151700270e0f57d7474837b5a0e0f80682c543.jpg', '4', '2', '0', '2', '福建', '2018-07-12', '72');
INSERT INTO `movie` VALUES ('2018-07-04 15:17:25', '6', '鬼吹灯1', 'uploads/video/20180704/20180704151725249e0822d0924a358439770a530f8de2.mp4', '鬼吹灯1', 'uploads/image/20180704/201807041517255c12cfea6ff144a4bf759cfd8791ddb7.jpg', '5', '59', '2', '2', '北京', '2018-07-25', '72');
INSERT INTO `movie` VALUES ('2018-07-04 15:17:55', '7', '鬼吹灯2', 'uploads/video/20180704/20180704151755cca005659ed5469bb6f75ba673ec4048.mp4', '鬼吹灯2', 'uploads/image/20180704/2018070415175512f8076d04d84b6cbc6e3e8d0556e057.jpg', '4', '4', '0', '2', '北京', '2018-07-25', '72');
INSERT INTO `movie` VALUES ('2018-07-04 15:19:06', '8', '这是喜剧', 'uploads/video/20180704/20180704151906a363ec0fa25e4a3e8e27f0ee74cae4e5.mp4', '这是喜剧', 'uploads/image/20180704/20180704151906bf284aac8e494658b5e8ac00f790da1a.jpg', '4', '34', '0', '3', '北京', '2018-07-19', '96');

-- ----------------------------
-- Table structure for movie_col
-- ----------------------------
DROP TABLE IF EXISTS `movie_col`;
CREATE TABLE `movie_col` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `movie_id` (`movie_id`),
  KEY `ix_movie_col_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of movie_col
-- ----------------------------
INSERT INTO `movie_col` VALUES ('2018-07-01 21:20:05', '1', '1', '1');
INSERT INTO `movie_col` VALUES ('2018-07-01 21:20:05', '2', '2', '2');
INSERT INTO `movie_col` VALUES ('2018-07-01 21:20:05', '3', '3', '1');
INSERT INTO `movie_col` VALUES ('2018-07-01 21:20:05', '4', '2', '1');
INSERT INTO `movie_col` VALUES ('2018-07-04 19:59:42', '7', '6', '2');
INSERT INTO `movie_col` VALUES ('2018-07-04 19:59:46', '8', '6', '2');
INSERT INTO `movie_col` VALUES ('2018-07-04 20:00:04', '9', '6', '2');
INSERT INTO `movie_col` VALUES ('2018-07-04 20:00:14', '10', '6', '6');
INSERT INTO `movie_col` VALUES ('2018-07-04 20:01:46', '11', '6', '6');
INSERT INTO `movie_col` VALUES ('2018-07-04 20:01:54', '12', '6', '1');
INSERT INTO `movie_col` VALUES ('2018-07-04 20:36:35', '13', '8', '3');
INSERT INTO `movie_col` VALUES ('2018-07-04 20:36:36', '14', '8', '3');
INSERT INTO `movie_col` VALUES ('2018-07-04 20:36:37', '15', '8', '3');
INSERT INTO `movie_col` VALUES ('2018-07-04 20:36:37', '16', '8', '3');
INSERT INTO `movie_col` VALUES ('2018-07-04 21:39:38', '17', '8', '8');
INSERT INTO `movie_col` VALUES ('2018-07-04 21:39:39', '18', '8', '8');
INSERT INTO `movie_col` VALUES ('2018-07-04 21:42:18', '19', '8', '8');

-- ----------------------------
-- Table structure for oplog
-- ----------------------------
DROP TABLE IF EXISTS `oplog`;
CREATE TABLE `oplog` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `reason` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_oplog_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of oplog
-- ----------------------------
INSERT INTO `oplog` VALUES ('2018-07-01 23:12:44', '1', '1', '127.0.0.1', '添加标签:古装');
INSERT INTO `oplog` VALUES ('2018-07-01 23:22:01', '2', '1', '127.0.0.1', '添加标签:古装');
INSERT INTO `oplog` VALUES ('2018-07-01 23:22:01', '3', '1', '127.0.0.1', '添加标签:古装');
INSERT INTO `oplog` VALUES ('2018-07-01 23:24:21', '4', '1', '127.0.0.1', '修改标签:华夏,id:19');
INSERT INTO `oplog` VALUES ('2018-07-01 23:36:30', '5', '1', '127.0.0.1', '添加电影:笔仙');
INSERT INTO `oplog` VALUES ('2018-07-01 23:37:10', '6', '1', '127.0.0.1', '添加预告:笔仙');
INSERT INTO `oplog` VALUES ('2018-07-01 23:37:31', '7', '1', '127.0.0.1', '删除电影收藏:不错~,id:5');
INSERT INTO `oplog` VALUES ('2018-07-01 23:38:53', '8', '1', '127.0.0.1', '删除评论:二刷,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 14:16:18', '9', '1', '127.0.0.1', '添加权限:添加标签');
INSERT INTO `oplog` VALUES ('2018-07-02 14:17:32', '10', '1', '127.0.0.1', '添加权限:编辑标签');
INSERT INTO `oplog` VALUES ('2018-07-02 14:18:25', '11', '1', '127.0.0.1', '添加权限:标签列表');
INSERT INTO `oplog` VALUES ('2018-07-02 14:18:34', '12', '1', '127.0.0.1', '添加权限:删除标签');
INSERT INTO `oplog` VALUES ('2018-07-02 14:19:23', '13', '1', '127.0.0.1', '添加权限:测试权限');
INSERT INTO `oplog` VALUES ('2018-07-02 14:20:35', '14', '1', '127.0.0.1', '修改电影:测试权限123,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 14:20:37', '15', '1', '127.0.0.1', '修改电影:测试权限123,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 14:20:38', '16', '1', '127.0.0.1', '修改电影:测试权限123,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 14:20:39', '17', '1', '127.0.0.1', '修改电影:测试权限123,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 14:20:45', '18', '1', '127.0.0.1', '修改电影:添加权限,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 14:20:47', '19', '1', '127.0.0.1', '修改电影:添加权限,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 14:20:48', '20', '1', '127.0.0.1', '修改电影:添加权限,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 14:21:06', '21', '1', '127.0.0.1', '修改电影:添加权限,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 14:21:41', '22', '1', '127.0.0.1', '删除权限:添加权限,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 15:23:37', '23', '1', '127.0.0.1', '添加权限:张三');
INSERT INTO `oplog` VALUES ('2018-07-02 15:36:59', '24', '1', '127.0.0.1', '添加权限:123');
INSERT INTO `oplog` VALUES ('2018-07-02 15:49:27', '25', '1', '127.0.0.1', '添加权限:标签管理员');
INSERT INTO `oplog` VALUES ('2018-07-02 15:52:07', '26', '1', '127.0.0.1', '添加权限:标签管理员1');
INSERT INTO `oplog` VALUES ('2018-07-02 16:23:14', '27', '1', '127.0.0.1', '添加角色:爱情');
INSERT INTO `oplog` VALUES ('2018-07-02 16:24:06', '28', '1', '127.0.0.1', '删除角色:爱情,id:3');
INSERT INTO `oplog` VALUES ('2018-07-02 16:35:43', '29', '1', '127.0.0.1', '添加角色:guaosi');
INSERT INTO `oplog` VALUES ('2018-07-02 18:52:59', '30', '1', '127.0.0.1', '添加角色:可以');
INSERT INTO `oplog` VALUES ('2018-07-02 19:15:16', '31', '1', '127.0.0.1', '修改角色:可以,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 19:15:22', '32', '1', '127.0.0.1', '修改角色:可以,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 19:15:26', '33', '1', '127.0.0.1', '修改角色:可以了,id:5');
INSERT INTO `oplog` VALUES ('2018-07-02 20:01:09', '34', '1', '127.0.0.1', '添加管理员:guaosi');
INSERT INTO `oplog` VALUES ('2018-07-02 20:02:08', '35', '1', '127.0.0.1', '添加管理员:张三');
INSERT INTO `oplog` VALUES ('2018-07-02 21:51:17', '36', '1', '127.0.0.1', '删除标签:华夏,id:19');
INSERT INTO `oplog` VALUES ('2018-07-02 21:51:34', '37', '1', '127.0.0.1', '删除标签:张三,id:15');
INSERT INTO `oplog` VALUES ('2018-07-03 19:54:06', '38', '1', '127.0.0.1', '修改电影:这是一张图片,id:1');
INSERT INTO `oplog` VALUES ('2018-07-03 19:55:39', '39', '1', '127.0.0.1', '修改电影:这是一张图片,id:1');
INSERT INTO `oplog` VALUES ('2018-07-04 12:42:52', '40', '1', '127.0.0.1', '删除标签:历史,id:14');
INSERT INTO `oplog` VALUES ('2018-07-04 12:42:53', '41', '1', '127.0.0.1', '删除标签:恐怖,id:10');
INSERT INTO `oplog` VALUES ('2018-07-04 12:42:54', '42', '1', '127.0.0.1', '删除标签:惊悚,id:9');
INSERT INTO `oplog` VALUES ('2018-07-04 12:42:55', '43', '1', '127.0.0.1', '删除标签:犯罪,id:8');
INSERT INTO `oplog` VALUES ('2018-07-04 12:42:55', '44', '1', '127.0.0.1', '删除标签:枪战,id:7');
INSERT INTO `oplog` VALUES ('2018-07-04 13:55:09', '45', '1', '127.0.0.1', '删除预告:变形金刚,id:1');
INSERT INTO `oplog` VALUES ('2018-07-04 13:55:12', '46', '1', '127.0.0.1', '删除预告:生化危机123,id:3');
INSERT INTO `oplog` VALUES ('2018-07-04 13:55:13', '47', '1', '127.0.0.1', '删除预告:笔仙,id:4');
INSERT INTO `oplog` VALUES ('2018-07-04 13:55:59', '48', '1', '127.0.0.1', '添加预告:周杰伦粉丝版MV');
INSERT INTO `oplog` VALUES ('2018-07-04 13:56:07', '49', '1', '127.0.0.1', '添加预告:乐侃有声节目第二期');
INSERT INTO `oplog` VALUES ('2018-07-04 13:58:13', '50', '1', '127.0.0.1', '添加预告:乐见大牌：”荣“耀之声，”维“我独尊');
INSERT INTO `oplog` VALUES ('2018-07-04 13:58:20', '51', '1', '127.0.0.1', '添加预告:王力宏四年心血结晶');
INSERT INTO `oplog` VALUES ('2018-07-04 13:59:04', '52', '1', '127.0.0.1', '添加预告:MV精选：《武媚》女神团美艳大比拼');
INSERT INTO `oplog` VALUES ('2018-07-04 15:17:00', '53', '1', '127.0.0.1', '添加电影:鬼吹灯');
INSERT INTO `oplog` VALUES ('2018-07-04 15:17:25', '54', '1', '127.0.0.1', '添加电影:鬼吹灯1');
INSERT INTO `oplog` VALUES ('2018-07-04 15:17:55', '55', '1', '127.0.0.1', '添加电影:鬼吹灯2');
INSERT INTO `oplog` VALUES ('2018-07-04 15:19:06', '56', '1', '127.0.0.1', '添加电影:这是喜剧');

-- ----------------------------
-- Table structure for preview
-- ----------------------------
DROP TABLE IF EXISTS `preview`;
CREATE TABLE `preview` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(150) DEFAULT NULL,
  `logo` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `logo` (`logo`),
  KEY `ix_preview_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of preview
-- ----------------------------
INSERT INTO `preview` VALUES ('2018-07-04 13:56:07', '6', '乐侃有声节目第二期', 'uploads/image/20180704/2018070413560772244397c46543fd9edb059515f9f4cc.jpg');
INSERT INTO `preview` VALUES ('2018-07-04 13:55:59', '5', '周杰伦粉丝版MV', 'uploads/image/20180704/20180704135559c99d008cd40849759ea9fe6ca451dc9a.jpg');
INSERT INTO `preview` VALUES ('2018-07-04 13:58:13', '7', '乐见大牌：”荣“耀之声，”维“我独尊', 'uploads/image/20180704/2018070413581322e7b6581e3b4338b0d842fb7da1d8b7.jpg');
INSERT INTO `preview` VALUES ('2018-07-04 13:58:20', '8', '王力宏四年心血结晶', 'uploads/image/20180704/201807041358208a9a26e9d2c34514a1495ad6044328fd.jpg');
INSERT INTO `preview` VALUES ('2018-07-04 13:59:04', '9', 'MV精选：《武媚》女神团美艳大比拼', 'uploads/image/20180704/2018070413590425b5d71d46d64930b5a3ba6f956861ae.jpg');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `auths` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_role_addtime` (`addtime`) USING BTREE,
  KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('2018-07-02 15:49:27', '1', '标签管理员', '1,2,3');
INSERT INTO `role` VALUES ('2018-07-02 15:52:07', '2', '标签管理员1', '1,3');
INSERT INTO `role` VALUES ('2018-07-02 16:35:43', '4', 'guaosi', '1,2,3,4');
INSERT INTO `role` VALUES ('2018-07-02 18:52:59', '5', '可以了', '1,4');

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_tag_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES ('2018-06-30 21:51:33', '1', '科幻');
INSERT INTO `tag` VALUES ('2018-06-30 21:54:11', '2', '悬疑');
INSERT INTO `tag` VALUES ('2018-06-30 21:55:06', '3', '喜剧');
INSERT INTO `tag` VALUES ('2018-06-30 21:55:14', '4', '悲剧');
INSERT INTO `tag` VALUES ('2018-06-30 21:55:18', '5', '爱情');
INSERT INTO `tag` VALUES ('2018-06-30 21:55:22', '6', '动作');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(150) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `info` text,
  `face` varchar(150) DEFAULT NULL,
  `uuid` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `ix_user_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('2018-07-01 21:51:16', '1', 'guaosi1', 'pbkdf2:sha256:50000$OU2DqpqT$e7b0f0f49a0a1d634356dcbdbe4f64ddb19968988ac2ccb8d91d9808f0577f14', 'guaosi1@guaosi.com', '12345678911', '这是个人简介', 'avatar/1.jpg', '35ee17c428aa407395dfc475eb66075e');
INSERT INTO `user` VALUES ('2018-07-01 21:51:16', '2', 'guaosi2', 'pbkdf2:sha256:50000$6Kp9APFT$2e3f7ee095b9b1ef9ca58fe5daa7461316a6358bfcfe304eb2f4691d3c286dae', 'guaosi2@guaosi.com', '12345678912', '这是个人简介', 'avatar/2.jpg', '6534b89d8d7840f1838de3a7c63159df');
INSERT INTO `user` VALUES ('2018-07-01 21:51:16', '3', 'guaosi3', 'pbkdf2:sha256:50000$SKwmksqi$d20b0e67cbadc32e875f6d1d5bc1e5082f42d9d34766e64d0aed6be8808e6b36', 'guaosi3@guaosi.com', '12345678913', '这是个人简介', 'avatar/3.jpg', '1a117f29307348c58a4ce9a5f26b44f1');
INSERT INTO `user` VALUES ('2018-07-04 20:35:23', '8', 'guaosi4', 'pbkdf2:sha256:50000$OkbGHlIn$df815d6c410d2248ce167494f5e00bb2b5c66d19b919851acae03ff286654a9f', '1234@qq.com', '13945678915', null, 'avatar/1.jpg', '7c1ade28a666448f9d8e9910ab3c201f');
INSERT INTO `user` VALUES ('2018-07-03 12:23:04', '6', 'admin', 'pbkdf2:sha256:50000$bUzCGWMn$161c126f611c4be30414f5e31f2a466c01f4c6e8862954d871abf7111b915df0', '123@qq.com', '13945678914', '123123', 'uploads/image/20180703/201807032000118c9f68fff6f94e898544af8ccb23a826.jpg', '54bb95d334a742e7ac1849cdfc30f7a7');

-- ----------------------------
-- Table structure for userlog
-- ----------------------------
DROP TABLE IF EXISTS `userlog`;
CREATE TABLE `userlog` (
  `addtime` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `ix_userlog_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of userlog
-- ----------------------------
INSERT INTO `userlog` VALUES ('2018-07-01 23:44:27', '1', '1', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-01 23:44:27', '2', '1', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-01 23:44:27', '3', '2', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-03 13:30:17', '4', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-03 19:47:51', '5', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-03 20:26:20', '6', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-03 20:26:53', '7', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-03 20:32:09', '8', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-03 20:32:36', '9', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-03 20:34:15', '10', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-03 20:34:32', '11', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-04 17:32:23', '12', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-04 17:33:20', '13', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-04 19:50:22', '14', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-04 19:50:36', '15', '6', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-04 20:35:29', '16', '8', '127.0.0.1');
INSERT INTO `userlog` VALUES ('2018-07-04 21:53:41', '17', '6', '127.0.0.1');

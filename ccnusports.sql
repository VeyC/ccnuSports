/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50173
 Source Host           : localhost:3306
 Source Schema         : ccnusports

 Target Server Type    : MySQL
 Target Server Version : 50173
 File Encoding         : 65001

 Date: 11/06/2019 10:39:18
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cs_basicmessage
-- ----------------------------
DROP TABLE IF EXISTS `cs_basicmessage`;
CREATE TABLE `cs_basicmessage`  (
  `id` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL COMMENT '进行身份区分，judge123，admin123，news123,2016210123',
  `password` varchar(25) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of cs_basicmessage
-- ----------------------------
INSERT INTO `cs_basicmessage` VALUES ('2016210555', '555');
INSERT INTO `cs_basicmessage` VALUES ('2016210911', '911');
INSERT INTO `cs_basicmessage` VALUES ('2016210999', '999');
INSERT INTO `cs_basicmessage` VALUES ('2016214888', '888');
INSERT INTO `cs_basicmessage` VALUES ('2016215635', '635');
INSERT INTO `cs_basicmessage` VALUES ('2016215987', '987');
INSERT INTO `cs_basicmessage` VALUES ('2016216222', '222');
INSERT INTO `cs_basicmessage` VALUES ('2017214258', '258');
INSERT INTO `cs_basicmessage` VALUES ('2017216765', '765');
INSERT INTO `cs_basicmessage` VALUES ('2017217988', '988');
INSERT INTO `cs_basicmessage` VALUES ('2018210523', '523');
INSERT INTO `cs_basicmessage` VALUES ('2018212789', '789');
INSERT INTO `cs_basicmessage` VALUES ('2018213456', '456');
INSERT INTO `cs_basicmessage` VALUES ('2018218623', '623');
INSERT INTO `cs_basicmessage` VALUES ('admin111', '111');
INSERT INTO `cs_basicmessage` VALUES ('judge123', '123');
INSERT INTO `cs_basicmessage` VALUES ('judge222', '222');
INSERT INTO `cs_basicmessage` VALUES ('news789', '789');
INSERT INTO `cs_basicmessage` VALUES ('news999', '999');

-- ----------------------------
-- Table structure for cs_judge
-- ----------------------------
DROP TABLE IF EXISTS `cs_judge`;
CREATE TABLE `cs_judge`  (
  `id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of cs_judge
-- ----------------------------
INSERT INTO `cs_judge` VALUES ('judge123');

-- ----------------------------
-- Table structure for cs_manage
-- ----------------------------
DROP TABLE IF EXISTS `cs_manage`;
CREATE TABLE `cs_manage`  (
  `id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `department` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '所属学院',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of cs_manage
-- ----------------------------
INSERT INTO `cs_manage` VALUES ('admin111', '计算机学院');

-- ----------------------------
-- Table structure for cs_news
-- ----------------------------
DROP TABLE IF EXISTS `cs_news`;
CREATE TABLE `cs_news`  (
  `news_id` int(5) NOT NULL,
  `newscharger_id` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL COMMENT '发布人id',
  `publishtime` datetime NULL DEFAULT NULL COMMENT '发布时间',
  `title` varchar(50) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL COMMENT '标题',
  `text` text CHARACTER SET gbk COLLATE gbk_chinese_ci NULL COMMENT '正文',
  PRIMARY KEY (`news_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of cs_news
-- ----------------------------
INSERT INTO `cs_news` VALUES (101, 'news999', '2019-04-18 07:00:00', '计算机学院刘浩获男子组100米第三名', '今天校园内人头攒动，气氛热烈。运动会上各项比赛，高潮一个接着一个，一个个小冠军接连产生。观看比赛的同学也积极响应，赛场周围的“加油”声此起彼伏，不绝于耳。他们的热情、激动的情绪，感染了每一个人，将本次校运会推向了一个又一个新记录。');
INSERT INTO `cs_news` VALUES (102, 'news999', '2019-05-01 21:00:00', '化学学院获道德风尚奖', '信念的坚定，能够使死亡转化为复活，使瞬间转化为永恒。为了心中的信念、自我的实现与塑造，看，当朝阳的光芒带来了新的生机，我们与时俱进，开拓创新，在运动精神的鼓舞下，必须会赛出好成绩的！');
INSERT INTO `cs_news` VALUES (103, 'news789', '2019-05-08 20:44:13', '美术学院孙飞获男子组跳远第二名', '在我院师生的共同努力下，我院取得跳远第二名的好成绩。此次运动会，让我们感受到了广大学子的热情与朝气。');
INSERT INTO `cs_news` VALUES (104, 'news999', '2019-05-10 19:03:22', '工商管理学院学生积极参与运动会', '本次运动会，工商管理学院运动健儿们踊跃报名，用心参与。赛前，运动员们刻苦训练，为比赛做准备。比赛时，他们奋勇争先，顽强拼搏，取得了优秀的成绩，为学院赢得了荣誉。');

-- ----------------------------
-- Table structure for cs_project
-- ----------------------------
DROP TABLE IF EXISTS `cs_project`;
CREATE TABLE `cs_project`  (
  `id` int(5) UNSIGNED ZEROFILL NOT NULL COMMENT '第1位--时间，第2位--预决赛，第3位--性别，第4位--类别，第5位--子编号',
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `judge_id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '该项目负责人ID',
  `time` datetime NOT NULL,
  `place` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `limit_number` int(1) NULL DEFAULT NULL COMMENT '限报总人数/团体数',
  `male` int(1) NULL DEFAULT NULL COMMENT '限报男生人数',
  `female` int(1) NULL DEFAULT NULL COMMENT '限报女生人数',
  `type` int(1) NOT NULL COMMENT '项目类型，0表示个体赛，1表示团体赛',
  `participant` int(11) NOT NULL COMMENT '参赛人员，0表示学生，1表示教职工',
  `isfinish` int(1) NULL DEFAULT NULL COMMENT '0----未录入完成，1---录入完成',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of cs_project
-- ----------------------------
INSERT INTO `cs_project` VALUES (10001, '女子组100米预赛', 'judge123', '2019-04-06 10:00:00', '田径场', 85, 0, 85, 0, 0, 1);
INSERT INTO `cs_project` VALUES (10003, '女子组跳高预决赛', 'judge222', '2019-04-06 10:00:00', '足球场', 60, 0, 60, 0, 0, 0);
INSERT INTO `cs_project` VALUES (10006, '女子组400米预决赛', 'judge222', '2019-04-06 14:00:00', '田径场', 60, 0, 60, 0, 0, 0);
INSERT INTO `cs_project` VALUES (10102, '男子组100米预赛', 'judge123', '2019-04-06 10:45:00', '田径场', 80, 80, 0, 0, 0, 1);
INSERT INTO `cs_project` VALUES (10107, '男子组400米预决赛', 'judge222', '2019-04-06 14:35:00', '田径场', 50, 50, 0, 0, 0, 0);
INSERT INTO `cs_project` VALUES (10214, '混合组定点投篮预决赛', 'judge123', '2019-04-06 10:00:00', '篮球场', 12, NULL, NULL, 1, 0, 0);
INSERT INTO `cs_project` VALUES (10215, '混合组足球定位球预决赛', 'judge222', '2019-04-06 10:00:00', '足球场', 12, NULL, NULL, 1, 0, 0);
INSERT INTO `cs_project` VALUES (11008, '女子组100米决赛', 'judge222', '2019-04-06 15:15:00', '田径场', 8, 0, 8, 0, 0, 0);
INSERT INTO `cs_project` VALUES (11109, '男子组100米决赛', 'judge123', '2019-04-06 15:25:00', '田径场', 8, 8, 0, 0, 0, 0);

-- ----------------------------
-- Table structure for cs_punishment
-- ----------------------------
DROP TABLE IF EXISTS `cs_punishment`;
CREATE TABLE `cs_punishment`  (
  `id` int(5) NOT NULL COMMENT '处理的序号，自增',
  `project_id` int(5) NOT NULL COMMENT '违规项目的编号',
  `department` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '违规学生所在学院',
  `record` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '违规记录',
  `punish` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '处分结果',
  `student_id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '违规学生ID',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for cs_score
-- ----------------------------
DROP TABLE IF EXISTS `cs_score`;
CREATE TABLE `cs_score`  (
  `student_id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '学生id',
  `project_id` int(5) NOT NULL COMMENT '报名项目编号',
  `score` float(4, 1) NULL DEFAULT NULL COMMENT '分数，保留一位小数',
  `ranking` int(1) NULL DEFAULT NULL COMMENT '排名，只保留前八名',
  `status` int(1) NULL DEFAULT NULL COMMENT '状态，0--未审核，1--已确认，2--未通过',
  PRIMARY KEY (`student_id`, `project_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of cs_score
-- ----------------------------
INSERT INTO `cs_score` VALUES ('2016210555', 10102, NULL, NULL, 1);
INSERT INTO `cs_score` VALUES ('2016210555', 10214, NULL, NULL, 0);
INSERT INTO `cs_score` VALUES ('2016210555', 11006, NULL, NULL, 2);
INSERT INTO `cs_score` VALUES ('2016210999', 10006, 90.0, 6, 1);
INSERT INTO `cs_score` VALUES ('2016210999', 11008, 80.0, NULL, 1);
INSERT INTO `cs_score` VALUES ('2016214888', 10102, NULL, NULL, 1);
INSERT INTO `cs_score` VALUES ('2016214888', 10107, 86.0, NULL, 1);
INSERT INTO `cs_score` VALUES ('2016215635', 10102, NULL, NULL, 1);
INSERT INTO `cs_score` VALUES ('2016215987', 10102, NULL, NULL, 1);
INSERT INTO `cs_score` VALUES ('2016216222', 10102, NULL, NULL, 1);
INSERT INTO `cs_score` VALUES ('2017214258', 10102, NULL, NULL, 1);
INSERT INTO `cs_score` VALUES ('2017217988', 10102, NULL, NULL, 1);
INSERT INTO `cs_score` VALUES ('2018210523', 10003, NULL, NULL, 0);
INSERT INTO `cs_score` VALUES ('2018210523', 10102, NULL, NULL, 1);
INSERT INTO `cs_score` VALUES ('2018210523', 10214, NULL, NULL, 0);
INSERT INTO `cs_score` VALUES ('2018212789', 10102, NULL, NULL, 1);
INSERT INTO `cs_score` VALUES ('2018213456', 10102, NULL, NULL, 1);

-- ----------------------------
-- Table structure for cs_scoreboard
-- ----------------------------
DROP TABLE IF EXISTS `cs_scoreboard`;
CREATE TABLE `cs_scoreboard`  (
  `department` varchar(25) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `grade` int(4) NULL DEFAULT NULL COMMENT '学院积分',
  PRIMARY KEY (`department`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of cs_scoreboard
-- ----------------------------
INSERT INTO `cs_scoreboard` VALUES ('化学学院', 30);
INSERT INTO `cs_scoreboard` VALUES ('计算机学院', 40);
INSERT INTO `cs_scoreboard` VALUES ('美术学院', 20);

-- ----------------------------
-- Table structure for cs_user
-- ----------------------------
DROP TABLE IF EXISTS `cs_user`;
CREATE TABLE `cs_user`  (
  `id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `department` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '学院',
  `phonenum` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` int(1) NOT NULL COMMENT '0表示女，1表示男',
  `is_teacher` int(1) NOT NULL COMMENT '0表示学生，1表示教职工',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of cs_user
-- ----------------------------
INSERT INTO `cs_user` VALUES ('2016210555', '易烊千玺', '计算机学院', '12345678910', 1, 0);
INSERT INTO `cs_user` VALUES ('2016210911', '朱一龙', '计算机学院', '12345678910', 0, 1);
INSERT INTO `cs_user` VALUES ('2016210999', '孟美琪', '美术学院', '15326492555', 0, 0);
INSERT INTO `cs_user` VALUES ('2016214888', '华晨宇', '化学学院', '19258462462', 1, 0);
INSERT INTO `cs_user` VALUES ('2016215635', '黄明昊', '化学学院', '14694215495', 1, 0);
INSERT INTO `cs_user` VALUES ('2016215987', '邓伦', '化学学院', '15366492560', 1, 0);
INSERT INTO `cs_user` VALUES ('2016216222', '鹿晗', '美术学院', '18562314651', 1, 0);
INSERT INTO `cs_user` VALUES ('2017214258', '朱正廷', '计算机学院', '18362521655', 1, 0);
INSERT INTO `cs_user` VALUES ('2017216765', '迪丽热巴', '美术学院', '16324956823', 0, 0);
INSERT INTO `cs_user` VALUES ('2017217988', '张艺兴', '美术学院', '16584980663', 1, 0);
INSERT INTO `cs_user` VALUES ('2018210523', '刘诗诗', '计算机学院', '15649054668', 0, 0);
INSERT INTO `cs_user` VALUES ('2018212789', '王源', '计算机学院', '18530492356', 1, 0);
INSERT INTO `cs_user` VALUES ('2018213456', '张云雷', '化学学院', '14765235945', 1, 0);
INSERT INTO `cs_user` VALUES ('2018218623', '吴亦凡', '化学学院', '18265561231', 1, 0);
INSERT INTO `cs_user` VALUES ('admin111', '刘昊然', '计算机学院', '18524835694', 1, 0);
INSERT INTO `cs_user` VALUES ('judge123', '蔡徐坤', '体育学院', '15269463084', 0, 0);
INSERT INTO `cs_user` VALUES ('judge222', '彭于晏', '体育学院', '16485236945', 1, 1);
INSERT INTO `cs_user` VALUES ('news789', '华晨宇', '化学学院', '19258462462', 1, 0);
INSERT INTO `cs_user` VALUES ('news999', '洛枳', '计算机学院', '18462946244', 1, 1);

SET FOREIGN_KEY_CHECKS = 1;

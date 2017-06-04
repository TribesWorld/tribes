-- ----------------------------
-- Table structure for t_common
-- ----------------------------
CREATE TABLE IF NOT EXISTS t_user (
  id INTEGER PRIMARY KEY NOT NULL COMMENT '用户id',
  account_name VARCHAR(64) NOT NULL COMMENT '用户名',
  display_name VARCHAR(64) NOT NULL COMMENT '显示名称',
  avatar_url VARCHAR(128) NOT NULL COMMENT '头像链接',
  email VARCHAR(64) NOT NULL COMMENT '邮箱',
  password VARCHAR(128) NOT NULL COMMENT '登录密码加密字符串'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Alter Sequences Owned By
-- ----------------------------

-- ----------------------------
-- Indexes structure for table t_common_file
-- ----------------------------

-- ----------------------------
-- Triggers structure for table t_common
-- ----------------------------

-- ----------------------------
-- Init SQL Data
-- ----------------------------



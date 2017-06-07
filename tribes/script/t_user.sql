# Table Structure
CREATE TABLE IF NOT EXISTS t_user (
  id            INT(11) PRIMARY KEY AUTO_INCREMENT         NOT NULL
  COMMENT '用户id',
  account_name  VARCHAR(64)                                NOT NULL
  COMMENT '用户名',
  email         VARCHAR(64)                                NOT NULL
  COMMENT '邮箱',
  password_hash VARCHAR(128)                               NOT NULL
  COMMENT '密码hash',
  status        SMALLINT DEFAULT 0                         NOT NULL
  COMMENT '0-注册成功，1-正常使用',
  ctime         TIMESTAMP DEFAULT current_timestamp
  COMMENT '创建时间',
  utime         TIMESTAMP DEFAULT current_timestamp ON UPDATE current_timestamp
  COMMENT '更新时间'
  # display_name VARCHAR(64) NOT NULL COMMENT '显示名称',
  # avatar_url VARCHAR(128) NOT NULL COMMENT '头像链接',
  # email VARCHAR(64) NOT NULL COMMENT '邮箱',
  # password VARCHAR(128) NOT NULL COMMENT '登录密码加密字符串'
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
CREATE TABLE IF NOT EXISTS t_user (
  id            INT(11) PRIMARY KEY AUTO_INCREMENT         NOT NULL
  COMMENT '用户id',
  account_name  VARCHAR(64)                                NOT NULL
  COMMENT '用户名',
  email         VARCHAR(64)                                NOT NULL
  COMMENT '邮箱',
  password_hash VARCHAR(128)                               NOT NULL
  COMMENT '密码hash',
  avatar_url    VARCHAR(128)                               NOT NULL
  COMMENT '头像地址',
  status        SMALLINT DEFAULT 0                         NOT NULL
  COMMENT '0-注册成功，1-已验证邮箱',
  ctime         TIMESTAMP DEFAULT current_timestamp
  COMMENT '创建时间',
  utime         TIMESTAMP DEFAULT current_timestamp ON UPDATE current_timestamp
  COMMENT '更新时间'
);
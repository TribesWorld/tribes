# 基础镜像
FROM python:2.7.13
# 开发者信息
MAINTAINER v-zhidu du_zhi_qiang@163.com
# 标签
LABEL Name=tribes Version=0.0.1

RUN mkdir -p /usr/src/tribes
ENV TRIBES_SOURCE /usr/src/tribes
WORKDIR $TRIBES_SOURCE

ENV SCRIPT_FOLDER=$TRIBES_SOURCE/tribes/script/

ADD . $TRIBES_SOURCE
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["/bin/sh", "./docker-entrypoint.sh"]

# 基础镜像
FROM python:2.7.13
# 开发者信息
MAINTAINER v-zhidu du_zhi_qiang@163.com
# 标签
LABEL Name=tribes-app Version=0.0.1

RUN mkdir -p /usr/src/tribes
ENV TRIBES_SOURCE /usr/src/tribes
WORKDIR $TRIBES_SOURCE

COPY tribes/ .
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 5000
CMD ["/bin/sh" , "/docker-entrypoint.sh"]

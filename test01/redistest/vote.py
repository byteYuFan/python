import time

import redis

# 建立与本机的redis服务连接
conn = redis.Redis(host='127.0.0.1', port=6379, password='')

# 定义常量 文章投票票数和偷拍你期限
ON_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432


def article_vote(conn, user, article):
    cutoff = time.time() - ON_WEEK_IN_SECONDS
    if conn.zscore('time:', article) < cutoff:
        #说明投票时间已经过期
        return



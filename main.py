from time import sleep
import socket
import requests
import logging


logger = logging.getLogger('dnschecker')
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

while True:
    domains = [
        "cluster-postgresql-29cm.cluster-ctmw8zwgnsc3.ap-northeast-2.rds.amazonaws.com",
        "api-29cm.live",
    ]

    for d in domains:
        try:
            logger.info(f"{d}: {socket.gethostbyname(d)}")
        except Exception:
            message = {
                "slack_app_id": "AQ6MVB8AX",
                "channel_id": "CKE335NEB",
                "text": f":kubernetes::skull_and_crossbones: DNS 검색 실패: `{d}`"
            }
            requests.post('https://bot.29cm.co.kr/slack/message/', json=message)
            logger.debug(f"{d}: DNS resolution failed")
    sleep(60)

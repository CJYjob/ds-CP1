# 설정한 debug flag를 가져오기 위해 import함
import config

# 현재 시간을 불러와 2022.12.02 02:05:35 형태 str으로 가져옴
import datetime
dt_now = datetime.datetime.now()
dt_now_str = dt_now.strftime('%Y.%m.%d %H:%M:%S')

'''
디버깅 로그 v2 
    입력값
        log : 디버깅 내용 입력
    처리
        현재 시간, 호출 파일, 로그 내용 출력
    반환값
        없음
'''
def debugLog(log):
  if config.debug_flag == 1:
    print(f'debug_log | {dt_now_str} | >>> {log}')
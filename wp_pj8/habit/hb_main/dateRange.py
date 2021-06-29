#시작일, 마지막 일을 datetime 형태로 입력하면 사이에 있는 모든 날짜를 리스트 형태로 반환한다.
import datetime

def date_list(start, end):
    date=list()
    for i in range((end-start).days+1):
        date.append((start+datetime.timedelta(days=i)).strftime("%Y-%m-%d"))
    return date
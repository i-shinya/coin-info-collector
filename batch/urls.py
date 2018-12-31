from django.urls import path
from . import apis

urlpatterns = [
    path("get_market/", apis.GetMarketApi.as_view(), name="extermal-test"),
    path("auto_trade/", apis.AutoTradeApi.as_view(), name="auto-trade"),
]

# 以下でbatchスケジューラーでの定義を行うスケジュールの定義
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()


@sched.scheduled_job("interval", minutes=1)
def shedule():
    service = apis.BatchScheduleServise()
    service.scheduleAction()
    print("Schedule action finished.")


import os

print(os.environ.get("SCHEDULE_FLAG", default=False))
print(type(os.environ.get("SCHEDULE_FLAG", default=False)))
# 環境変数でスケジュールフラグがTrueの場合のみスケジュールを設定する。
# 文字列で返却されるため文字列で判定
if os.environ.get("SCHEDULE_FLAG", default=False) == "True":
    print("[DEBUG]Schedule job start.")
    sched.start()

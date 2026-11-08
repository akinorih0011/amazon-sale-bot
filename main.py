
from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("Asia/Tokyo"))

print("Amazon Sale Bot")
print("動作テスト成功")
print("実行日時:", now.strftime("%Y-%m-%d %H:%M:%S"))


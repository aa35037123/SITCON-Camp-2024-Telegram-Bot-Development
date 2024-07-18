from datetime import datetime

# 結構化的目前時間
t = datetime.now()
# Datetime: 2024-07-18 14:09:45.792359
print(f'Datetime: {t}')
# Format: 2024-07-18 14:09:45
print(f'Format: {t.strftime("%Y-%m-%d %H:%M:%S")}')



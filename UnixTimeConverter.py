import datetime

# Unix zaman damgaları
start_time = 1725174000
end_time = 1727766000

# Zaman damgalarını insan tarafından okunabilir tarihe çevirme (UTC)
start_date_readable = datetime.datetime.fromtimestamp(start_time, datetime.timezone.utc)
end_date_readable = datetime.datetime.fromtimestamp(end_time, datetime.timezone.utc)

# Tarihleri insan tarafından okunabilir formatta yazdırma
print("Başlangıç Tarihi:")
print(start_date_readable.strftime('%Y-%m-%d %H:%M:%S %Z'))
print("Bitiş Tarihi:")
print(end_date_readable.strftime('%Y-%m-%d %H:%M:%S %Z'))

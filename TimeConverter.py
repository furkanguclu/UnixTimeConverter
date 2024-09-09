import datetime

# İnsan tarafından okunabilir tarihleri tanımlama
start_date_str = '2025-10-01 00:00:00'
end_date_str = '2025-11-01 00:00:00'

# Tarihleri datetime objelerine çevirme (UTC)
start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=datetime.timezone.utc)
end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=datetime.timezone.utc)

# Unix zaman damgalarına çevirme
start_timestamp = int(start_date.timestamp())
end_timestamp = int(end_date.timestamp())

# Unix zaman damgalarını yazdırma
print("Başlangıç Unix Zaman Damgası:", start_timestamp)
print("Bitiş Unix Zaman Damgası:", end_timestamp)

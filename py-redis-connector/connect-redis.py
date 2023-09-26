import redis

conn = redis.StrictRedis(
  host='localhost',
  port=6379,
  password='eVVYZ',
  ssl=False)

ssl_ca_certs=""

def connect():
    conn.ping()
    print('Connected!')

def test_dump():
    print('Set car make record:', conn.set("car_make", "Nissan") )
    print('Set car model record:', conn.set("car_model", "Frontier") )
    print('Set car color record:', conn.set("car_color", "Silver") )
    print('Get car records:', conn.get("car_make") )
    print('Delete car make record:', conn.delete("car_make") )
    print('Get Deleted Record:', conn.get("car_make") )

print("Testing connection")
connect()
print("Testing redis dump")
test_dump()

import secrets
import string
import names
import time
import psycopg2

letters = string.ascii_letters
digits = string.digits
alphabet = letters+digits
pwd_length = 8
phone_length = 10
conn = psycopg2.connect(dbname='qa_ddl_32_108',
                           password='123',
                           host='159.69.151.133',
                           user='padawan_user_108',
                           port='5056')

user_name = ''
user_email = ''
user_password = ''
user_field = ''
user_data_list = []
count = 1

cursor = conn.cursor()
for i in range(10):
    if conn:
        pwd = ''
        for ii in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        test_phone = '+7'
        for ij in range(phone_length):
            test_phone += ''.join(secrets.choice(digits))

        user_name = names.get_full_name()
        user_email = user_name.replace(' ', '.') + '@gmail.com'
        user_password = pwd
        user_phone = test_phone

        base_data = (user_email, user_password, user_phone, user_name)
        insert_query = """insert into public.users(email, password_field, phone, user_name) values(%s,%s,%s,%s)"""
        cursor.execute(insert_query, base_data)
        conn.commit()
        print("set test_user", count, '-----', base_data)
        count += 1
        time.sleep(.200)

cursor.close()

# if conn:
#     print("succesfull")
#     sql_req = '''select * from users'''
#     cursor.execute(sql_req)
#     req_result = cursor.fetchall()
#     print(req_result)
#     for i in req_result:
#         print('id =', i[0], '-- salary = ', i[1])

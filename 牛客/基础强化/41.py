知识点 提取字符串中的字符

select id, device_id, university
from user_profile
where (university like '北京%' or university like '上海%')
and (university like '%学院' or university like '%校区')
and (university like '%职业%' or university like '%专科%' or university like '%成人%')

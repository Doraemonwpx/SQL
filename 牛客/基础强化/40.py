知识点 窗口函数

select id, device_id, university, gender, age, province
from (select *, rank() over(order by device_id) rk
from user_profile)u2
where rk = 7 or rk = 8 or rk = 9

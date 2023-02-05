__author__ = 'Pengxuan Wang, pwang@unc.edu, Onyen = pengxuan'

窗口函数() over (partition by col1 order by col2),表示根据col1分组，在分组内部根据col2排序。
33.
select device_id, university, gpa
from (select device_id, university, gpa,
rank() over(partition by university order by gpa) rk
from user_profile)u2
where rk = 1
__author__ = 'Pengxuan Wang, pwang@unc.edu, Onyen = pengxuan'

yyyy-mm-dd hh:mm:ss
常用的提取时间函数有：
date()：提取当前日期
year()：提取当前年
month()：提取当前月
day()：提取当前日
hour()：提取当前小时
minute()：提取当前分钟
second()：提取当前秒
28.
select day(date) day, count(question_id) question_cnt
from question_practice_detail
where month(date) = '08'
group by date


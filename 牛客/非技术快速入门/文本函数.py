__author__ = 'Pengxuan Wang, pwang@unc.edu, Onyen = pengxuan'
30.
知识点：substring_index(str,delim,count)
str:要处理的字符串
delim:分隔符
count:计数

例子：str=www.wikibt.com
substring_index(str,'.',1)
结果是：www

substring_index(str,'.',2)
结果是：www.wikibt

如果count是正数，那么就是从左往右数，第count个分隔符的左边的所有内容
如果count是负数，那么就是从右往左数，第|count|个分隔符的右边的所有内容
substring_index(str,'.',-2)
结果为：wikibt.com

要中间的的wikibt怎么办？
从右数第二个分隔符的右边全部，再从左数的第一个分隔符的左边：
substring_index(substring_index(str,'.',-2),'.',1);

select substring_index(profile, ',', -1) gender, count(device_id) number
from user_submit
group by gender

31.
select device_id, substring_index(blog_url, '/', -1) user_name
from user_submit

32. ⚠️⚠️distinct会自动升序排序，且优先级高于order by❗️❗️
select substring_index(substring_index(profile, ',',3), ',', -1) age, count(device_id)
from user_submit
group by age

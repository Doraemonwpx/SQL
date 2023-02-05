__author__ = 'Pengxuan Wang, pwang@unc.edu, Onyen = pengxuan'

条件函数
牛客网https://www.nowcoder.com/exam/oj?page=1&tab=SQL%E7%AF%87&topicId=199
25.
[if]：if（x=n,a,b）表示如果x=n,则返回a，否则就是b了。
方法1：
select if(age < 25 or age is null, '25岁以下', '25岁及以上') age_cut, count(device_id) number
from user_profile
group by age_cut
方法2：
⚠️请注意，在方法1中，group by有时不可以用已有表中不存在对列对，因此需要做个派生表过渡一下。
select age_cut, count(device_id) number
from
(select if(age < 25 or age is null, '25岁以下', '25岁及以上') age_cut, device_id
from user_profile) u2
group by age_cut

[case when]
select (case
when age < 25 or age is null then '25岁以下'
else '25岁及以上'
end) age_cut, count(device_id) from user_profile
group by age_cut

26.
select device_id, gender,
(case when age<20 then '20岁以下'
when age between 20 and 24 then '20-24岁'
when age>=25 then '25岁及以上'
else '其他'
end) age_cut
from user_profile

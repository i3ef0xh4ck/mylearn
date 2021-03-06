## 数据的增删查改

+ 增加insert

  + insert into 表名（字段们） values（值），（值）
  + insert into 表名（字段们） value（只能一行的值）
  + insrt into 表1（字段1,字段2）（select 字段1,字段2 from 表2） -字段一一对应,顺序不能颠倒
  + show variables like "%charac%";查看所有编码

+ 删除delete（慎重-不可恢复-先查后删）

  + delete from 表名;清空表
  + delete from 表名 where 条件；清除符合条件的数据
  + truncate table 表名；清空表并重置自增字段

+ 修改update（不可逆）

  + update 表名 set 字段1=值1,字段2=值2, where 条件；

+ 查询select（单表查询）

  ```mysql
  select xxx from 表名 where 条件 group by 分组 having 聚合的过滤 order by排序 limit m,n
  ```

  ```mysql
  from
  where
  group by
  select
  distinct
  having
  order by
  limit
  
  1.找到表:from
  2.拿着where指定的约束条件，去文件/表中取出一条条记录
  3.将取出的一条条记录进行分组group by，如果没有group by，则整体作为一组
  4.将分组的结果进行having过滤
  5.执行select（去重）
  6.将结果按条件排序：order by
  7.限制结果的显示条数
  ```

  + 查询前准备

    ```mysql
    #创建表
    create table employee(
    id int not null unique auto_increment,
    emp_name varchar(20) not null,
    sex enum('male','female') not null default 'male', #大部分是男的
    age int(3) unsigned not null default 28,
    hire_date date not null,
    post varchar(50),
    post_comment varchar(100),
    salary double(15,2),
    office int, #一个部门一个屋子
    depart_id int
    );
    
    #插入记录
    #三个部门：教学，销售，运营
    insert into employee(emp_name,sex,age,hire_date,post,salary,office,depart_id) values
    ('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
    ('alex','male',78,'20150302','teacher',1000000.31,401,1),
    ('wupeiqi','male',81,'20130305','teacher',8300,401,1),
    ('yuanhao','male',73,'20140701','teacher',3500,401,1),
    ('liwenzhou','male',28,'20121101','teacher',2100,401,1),
    ('jingliyang','female',18,'20110211','teacher',9000,401,1),
    ('jinxin','male',18,'19000301','teacher',30000,401,1),
    ('成龙','male',48,'20101111','teacher',10000,401,1),
    
    ('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
    ('丫丫','female',38,'20101101','sale',2000.35,402,2),
    ('丁丁','female',18,'20110312','sale',1000.37,402,2),
    ('星星','female',18,'20160513','sale',3000.29,402,2),
    ('格格','female',28,'20170127','sale',4000.33,402,2),
    
    ('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
    ('程咬金','male',18,'19970312','operation',20000,403,3),
    ('程咬银','female',18,'20130311','operation',19000,403,3),
    ('程咬铜','male',18,'20150411','operation',18000,403,3),
    ('程咬铁','female',18,'20140512','operation',17000,403,3)
    ;
    ```

    

  + 简单查询

    + select * from 表;（对列进行筛选）
    + select 字段1,字段2 from 表;

  + 避免重复distinct

    + select distinct 字段 from 表; 查询字段不重复

      ```mysql
      mysql> select distinct post from employee;
      +-----------------------------------------+
      | post                                    |
      +-----------------------------------------+
      | 老男孩驻沙河办事处外交大使                  |
      | teacher                                 |
      | sale                                    |
      | operation                               |
      +-----------------------------------------+
      ```

    + select distinct 字段1,字段2 from 表; 查询字段联合不重复

      ```mysql
      mysql> select distinct sex,post from employee;
      +--------+-----------------------------------------+
      | sex    | post                                    |
      +--------+-----------------------------------------+
      | male   | 老男孩驻沙河办事处外交大使                  |
      | male   | teacher                                 |
      | female | teacher                                 |
      | female | sale                                    |
      | male   | operation                               |
      | female | operation                               |
      +--------+-----------------------------------------+
      ```

  + 通过四则运算查询--将查询后的结果进行运算后显示（数字类型）

    + select 字段[+,-,*,/]  as 别名 from 表名;

      ```mysql
      SELECT emp_name, salary*12 FROM employee;
      SELECT emp_name, salary*12 AS Annual_salary FROM employee;重命名
      SELECT emp_name, salary*12 Annual_salary FROM employee;重命名
      ```

  + 定义显示格式----拼接

    + concat()  将字符串连接  `concat(str+字段1+str+字段2)`

      ```mysql
      SELECT CONCAT('姓名: ',emp_name,' 年薪: ', salary*12) AS Annual_salary FROM employee;
      ```

    + CONCAT_WS() 将字符串用分隔符连接，第一个参数为分隔符

      ```mysql
      mysql> select concat_ws("+",post,salary) from employee where salary > 10000;
      +----------------------------+
      | concat_ws("+",post,salary) |
      +----------------------------+
      | teacher+1000000.31         |
      | teacher+30000.00           |
      | operation+10000.13         |
      | operation+20000.00         |
      | operation+19000.00         |
      | operation+18000.00         |
      | operation+17000.00         |
      +----------------------------+
      ```

    + 结合case语句

      ```mysql
      SELECT
             (
                 CASE
                 WHEN emp_name = 'jingliyang' THEN
                     emp_name
                 WHEN emp_name = 'alex' THEN
                     CONCAT(emp_name,'_BIGSB')
                 ELSE
                     concat(emp_name, 'SB')
                 END
             ) as new_name
         FROM
             employee;
      ```

  + where 条件约束

    + 比较运算符（不能与null比较）：>  <  =  <>/!=

      ```mysql
      mysql> select emp_name,age from employee where post="teacher" and age>30;
      +----------+-----+
      | emp_name | age |
      +----------+-----+
      | alex     |  78 |
      | wupeiqi  |  81 |
      | yuanhao  |  73 |
      | 成龙     |  48 |
      +----------+-----+
      ```

    + 逻辑运算符：and  or not(is not  null/not in) 

      ```mysql
      mysql> select * from employee where post_comment is not null;
      ```

    + 范围

      + 多选 in(值1,值2,值3)

        ```mysql
        mysql> select emp_name,salary from employee where salary in(9000,10000,30000);
        +------------+----------+
        | emp_name   | salary   |
        +------------+----------+
        | jingliyang |  9000.00 |
        | jinxin     | 30000.00 |
        | 成龙       | 10000.00 |
        +------------+----------+
        ```

      + 区间 between 值1 and 值2

        ```mysql
        mysql> select emp_name,age,salary from employee where salary between 9000 and 10000;
        +------------+-----+----------+
        | emp_name   | age | salary   |
        +------------+-----+----------+
        | jingliyang |  18 |  9000.00 |
        | 成龙       |  48 | 10000.00 |
        +------------+-----+----------+
        ```

    + 模糊查询

      ```mysql
      mysql> select emp_name,salary from employee where emp_name like "jin%" or emp_name regexp "^yu";
      +------------+----------+
      | emp_name   | salary   |
      +------------+----------+
      | yuanhao    |  3500.00 |
      | jingliyang |  9000.00 |
      | jinxin     | 30000.00 |
      +------------+----------+
      ```

      + like
        + `%`--任意长度的字符
        + `_`--任意一个字符
      + regexp  正则

  + 聚合函数--分组中统计用

    **聚合函数聚合的是组的内容，若是没有分组，则默认一组**

    + 计数 count(字段)
    + 求和 sum()
    + 均值 avg()
    + 最大值 max()
    + 最小值 min()

  + group by 分组

    **多条记录之间的某个字段值相同，该字段通常用来作为分组的依据**

    + 单独使用 `group by 字段`

      单独使用时只能用作查询该组，要获取组内其他信息需要使用函数

      ```mysql
      mysql> select post from employee group by post;
      +-----------------------------------------+
      | post                                    |
      +-----------------------------------------+
      | operation                               |
      | sale                                    |
      | teacher                                 |
      | 老男孩驻沙河办事处外交大使                  |
      +-----------------------------------------+
      ```

    + group by和group_concat()函数一起使用

      分组后查询组内某字段所有值（聚合）

      ```mysql
      mysql> select post,group_concat(emp_name) from employee group by post limit 2;
      +-----------+------------------------------------------------+
      | post      | group_concat(emp_name)                         |
      +-----------+------------------------------------------------+
      | operation | 程咬铁,程咬铜,程咬银,程咬金,张野                    |
      | sale      | 格格,星星,丁丁,丫丫,歪歪                           |
      +-----------+------------------------------------------------+
      ```

    + group by 与聚合函数结合使用

      ```mysql
      #按照岗位分组，并查看每个组有多少人
      mysql> select post,count(emp_name) from employee group by post;
      +-----------------------------------------+-----------------+
      | post                                    | count(emp_name) |
      +-----------------------------------------+-----------------+
      | operation                               |               5 |
      | sale                                    |               5 |
      | teacher                                 |               7 |
      | 老男孩驻沙河办事处外交大使                  |               1 |
      +-----------------------------------------+-----------------+
      ```

  + having 过滤

    + having与where的区别

      + 执行优先级从高到低：where > group by > having
      + Where 发生在分组group by之前，因而Where中可以有任意字段，但是绝对不能使用聚合函数。
      + Having发生在分组group by之后，因而Having中可以使用分组的字段，无法直接取到其他字段,可以使用聚合函数，可以使用select中的重命名结果

    + 举例

      ```mysql
      mysql> select post,group_concat(emp_name),count(id) as 数量 from employee group by post having 数量>2 limit 2;
      +-----------+------------------------------------------------+--------+
      | post      | group_concat(emp_name)                         | 数量   |
      +-----------+------------------------------------------------+--------+
      | operation | 程咬铁,程咬铜,程咬银,程咬金,张野                   |      5 |
      | sale      | 格格,星星,丁丁,丫丫,歪歪                          |      5 |
      +-----------+------------------------------------------------+--------+
      ```

      ```mysql
      mysql> select post,avg(salary) as 平均工资 from employee having 平均工资>10000;
      +-----------------------------------------+--------------+
      | post                                    | 平均工资     |
      +-----------------------------------------+--------------+
      | 老男孩驻沙河办事处外交大使              | 64844.568889 |
      +-----------------------------------------+--------------+
      ```

      ```mysql
      mysql> select post,avg(salary) as 平均工资 from employee having 平均工资 between 0 and 120000;
      ```

  + order by 排序查询

    + 按单列排序

      select * from 表 order by 字段;

      + 升序asc（默认）

        ```mysql
        select * from 表 order by 字段 asc;
        ```

      + 降序desc

        ```mysql
        select * from 表 order by 字段 desc;
        ```

    + 多列排序（按先后）

      ```mysql
      select * from 表 order by 字段1 desc,字段2 asc;
      #首先按照字段1从大到小排，字段1相同时按照字段2从小到大排
      ```

      ```mysql
      mysql> select id,age,salary from employee order by age,salary desc;
      +----+-----+------------+
      | id | age | salary     |
      +----+-----+------------+
      |  7 |  18 |   30000.00 |
      | 15 |  18 |   20000.00 |
      | 16 |  18 |   19000.00 |
      | 17 |  18 |   18000.00 |
      | 18 |  18 |   17000.00 |
      |  6 |  18 |    9000.00 |
      |  1 |  18 |    7300.33 |
      | 12 |  18 |    3000.29 |
      | 11 |  18 |    1000.37 |
      | 14 |  28 |   10000.13 |
      | 13 |  28 |    4000.33 |
      |  5 |  28 |    2100.00 |
      | 10 |  38 |    2000.35 |
      |  8 |  48 |   10000.00 |
      |  9 |  48 |    3000.13 |
      |  4 |  73 |    3500.00 |
      |  2 |  78 | 1000000.31 |
      |  3 |  81 |    8300.00 |
      +----+-----+------------+
      ```

  + limit 限制查询的记录数（用于分页）

    + limit n  从零开始查询n个
    + limit m,n 从m+1开始取n个

    ```mysql
    mysql> select id from employee limit 3,5;
    +----+
    | id |
    +----+
    |  4 |
    |  5 |
    |  6 |
    |  7 |
    |  8 |
    +----+
    ```

    
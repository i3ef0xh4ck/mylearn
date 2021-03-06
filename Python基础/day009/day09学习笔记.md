## 函数初识

### 函数的作用

+ 封装代码，大量的减少重复代码
+ 重用性高

### 函数的定义

+ 基本结构

  def --关键字，声明要定义一个函数
  my_len 函数名，遵循变量命名规则
  () 固定结构 ，用于传参
  : 表示语句结束
  缩进
函数体
  
  ```
  def 函数名():
      函数体
  ```
  
  ```
  def my_len():#函数下函数体是被封装内容，被调用时才执行
      count = 0
      for i in s:
          count += 1
      print(count)
  ```


### 函数的调用

+ 方法

  函数名+()   `func()`

  ​	基本功能

  + 调用函数
  + 接收返回值

+ 返回值   `return`

  + 存在意义：因为函数被调用后，函数体中开辟的空间会被自动销毁，外部无法直接使用函数内部的数据

    ```
    def func():
        a = 10
        b = 20
        return a,b
    a,b = func() #拆包，解包，平行赋值
    print(a,b)
    print(func())
    ```

  + return 可以返回任意数据类型(python中所有对象)

  + return 可以返回多个数据类型,以元组的形式存储

  + return 可以终止当前函数,并将返回值返回给调用者

  + return 下方的代码不执行

  + return 不写时返回None,写了不写返回值也是返回None

  + 函数体中可以写多个return，但是只执行一个

+ 变量查找顺序

  ```
  局部-->全局-->内置空间
  ```

### 函数的参数

+ 形参：在函数定义阶段的参数

+ 实参：在函数调用阶段的参数

+ 传参：将实参传给形参的过程

+ 使用规则

  + 形参角度

    + 可以单独使用位置参数，也可以单独使用默认参数，也可以混合使用
    + 位置传参，必须一一对应，不可多，不可少
    + 默认参数：可以不传参，可以传参，传参会覆盖默认值
    + 混合使用参数：位置参数 > 默认参数

    ```
    def userinfo(name,age,hobby,sex = "男"):# 参数的优先级：位置参数 > 默认参数
        print(f"姓名：{name}  年龄：{age}  性别：{sex}  爱好：{hobby} ")
    userinfo("11","22","33","女")
    userinfo("11","22","33")
    ```

  + 实参角度

    + 可以单独使用位置参数，也可以单独使用关键字参数，也可以混合使用
    + 位置传参，必须一一对应
    + 关键字参数：指定变量传参
    + 混合使用参数：位置参数 > 关键字参数

    ```
    def func(a,b,c,d):
        print(a,b,c,d)
    func(1,2,3,5)  #实参 位置参数传递
    func(b=2,a=3,d=4,c=3)  #实参 关键字传参
    func(1,2,3,d=3)  #位置参数 > 关键字参数
    ```

    
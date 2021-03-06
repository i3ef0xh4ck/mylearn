# 1.底层的数据结构
# 2.面试 概念
# 3.索引 数据库查询速度相关

# 数据结构：
    # 线性结构（查询效率低）：
        #列表：连续，占用空间大，删改不灵活，索引取值块list  基于数组
        #链表：根据指向，节点，占用空间和删改都灵活，通过索引取值非常慢  deque 链表
    # 树形结构tree--二叉树（一个节点最多有两个子节点）：
        # 根节点root（唯一）
        # 分支节点branch（多层）
        # 叶子节点（一层）leaf
        # 树的高度，从根节点到叶子节点的层数（树的高度越短，查询步数越少）


# 计算机的磁盘读取原理
    #cpu的计算速度：500million条指令/s 约1亿+python的计算指令
    #计算机的读取效率
        #7200r/min--120r/s--9ms/r
        #平均寻道（找到数据）时间 5ms
        #找到磁道的平均时间 5ms
        #读一次磁盘的时间 10ms（可执行1百万python指令）
        #磁盘预读性原理 每一次读取数据的单位是 block块（linux上默认4096字节）
        #能够有效避免重复读取文件消耗的IO时间
# import dis
# def fun():
#     a =1
#     b =2
#     return a + b
# dis.dis(fun)


# 实际的数据库中数据的存储方式
# ------平衡树 balance tree  b-tree
# 根节点区间，分支节点，存范围及对应内存地址（树的高度越低越健康）
# 根据算法自动调整根节点（维护数的平衡）
# ---------链式结构，分支、叶子节点互相指向b+树（仅在叶子节点存放数据）



# myisam/innodb 存储引擎：索引结构都是通过b+树实现的

# 概念：
# 回表索引
# 聚簇索引/聚集索引：数据和索引存在一棵树上
# 辅助索引/非聚集索引：数据和索引不存在一棵树上
# 先从辅助索引查索引，然后从聚簇索引查
# 每一个字段都可以创建索引
# 对于一个字段创建的索引在当前字段作为条件时可以起到加速查询的作用


# myisam都是辅助索引
# innodb中主键是聚集索引，其他都是辅助索引（不设置主键默认添加空的主键列）
# -*- coding: utf-8 -*-
"""
累加器变量 accumulators variable
累加器变量仅通过联合和交换操作"添加"到的变量,可以有效支持并行.
可以使用累计器进行求和或计数(MR)操作
spark自身支持数值类型的累加器,开发人员可以添加对其他类型的支持.

作为用户: 可以创建命名累加器和未命名累加器
命名累加器将显示在webUI中针对某个修改累加器的计算阶段
spark显示每次task修改累加器值的列表记录--"Tasks"

累加器创建时可以初始化一个v值. task节点上能够对累加器进行add和+=操作.
然而, task节点不能读取累加器的值. 只有driver program可以读取累加器的值

累加器更新仅在action动作时
spark保证每个任务对累加器的更新仅应用一次, 重启任务不会更新累加器
在转换transformation阶段, 用户应该意识到每个任务的更新可以执行多次如果任务或作业阶段被重复执行.

累加器不改变spark的惰性计算行为
如果累加器正在更新,说明RDD上执行了action
因此,累加器在转换阶段不会被更新,因为没有action动作导致map被计算.
"""
from pyspark import SparkContext

sc = SparkContext(master="spark://spark001:7077", appName="accumulator_demo")

# accum = sc.accumulator(10)
#
#
# def f(x):
#     global accum
#     accum += x
#
#
# rdd = sc.parallelize([20, 30, 40, 50])
# rdd.foreach(f)
#
# final = accum.value
# print("累加后,累加器的值:{}".format(final))

# accum = sc.accumulator(0)
#
# sc.parallelize([1, 2, 3, 4]).foreach(lambda x: accum.add(x))
#
# print("累加后,累加器的值:{}".format(accum.value))

accum = sc.accumulator(0)


def g(x):
    accum.add(x)
    return x + 1


rdd1 = sc.parallelize([1, 2, 3])

rdd2 = rdd1.map(g)

print("累加器当前值:{}".format(accum.value))  # 累加器的值并未被更新, 因为map后没有action动作.
print("当前RDD所有元素:{}".format(rdd2.collect()))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : Add
# @Time         : 2020/4/10 11:20 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 
import tensorflow as tf


# todo: 验证层结构

class Add(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self, input_shape):
        # Be sure to call this somewhere!
        super().build(input_shape)

    def call(self, inputs, **kwargs):
        if not isinstance(inputs, list):
            return inputs
        if len(inputs) == 1:
            return inputs[0]
        if len(inputs) == 0:
            return tf.constant([[0.0]])

        return tf.keras.layers.add(inputs)


class OurDense(tf.keras.layers.Layer):
    """原来是继承Layer类，现在继承OurLayer类
    """

    def __init__(self, hidden_dim, output_dim,
                 hidden_activation='linear',
                 output_activation='linear', **kwargs):
        super(OurDense, self).__init__(**kwargs)
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.hidden_activation = hidden_activation
        self.output_activation = output_activation

    def build(self, input_shape):
        """在build方法里边添加需要重用的层，
        当然也可以像标准写法一样条件可训练的权重。
        """
        super(OurDense, self).build(input_shape)
        self.h_dense = tf.keras.layers.Dense(self.hidden_dim,
                                             activation=self.hidden_activation)
        self.o_dense = tf.keras.layers.Dense(self.output_dim,
                                             activation=self.output_activation)

    def call(self, inputs, **kwargs):
        """直接reuse一下层，等价于o_dense(h_dense(inputs))
        :param **kwargs:
        """
        # self.o_dense(self.h_dense(inputs))
        h = self.reuse(self.h_dense, inputs)
        o = self.reuse(self.o_dense, h)
        return o

    def compute_output_shape(self, input_shape):
        return input_shape[:-1] + (self.output_dim,)

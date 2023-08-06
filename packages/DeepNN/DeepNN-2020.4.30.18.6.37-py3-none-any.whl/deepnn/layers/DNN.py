#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : Python.
# @File         : DNN
# @Time         : 2020-03-13 13:42
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 
import tensorflow as tf


class DNN(tf.keras.layers.Layer):

    def __init__(self,
                 hidden_units_list,
                 activation='relu',
                 kernel_regularizer=tf.keras.regularizers.l2(),
                 use_bn=False,
                 dropout_rate=0,
                 seed=666,
                 **kwargs):
        super().__init__(**kwargs)

        self.hidden_units_list = hidden_units_list
        self.activation = activation
        self.dropout_rate = dropout_rate
        self.kernel_regularizer = kernel_regularizer
        self.use_bn = use_bn
        self.seed = seed
        self.num_layer = len(self.hidden_units_list)

    def build(self, input_shape):
        super().build(input_shape)  # self.built = True

        # https://blog.csdn.net/macair123/article/details/79511221
        # 一个初始化器可以由字符串指定（必须是下面的预定义初始化器之一），或一个callable的函数
        # Dense(64, kernel_initializer='random_normal')
        # Dense(64, kernel_initializer=initializers.random_normal(stddev=0.01))
        self.dense_layers = []
        for index, units in enumerate(self.hidden_units_list):
            _ = tf.keras.layers.Dense(
                units,
                activation=self.activation,
                use_bias=True,
                kernel_initializer='glorot_uniform',
                bias_initializer='zeros',
                kernel_regularizer=self.kernel_regularizer,
                bias_regularizer=None,
                name=f"dense{index}"
            )
            self.dense_layers.append(_)

        # BN
        if self.use_bn:
            self.bn_layers = self.num_layer * [tf.keras.layers.BatchNormalization()]

        self.dropout_layers = self.num_layer * [tf.keras.layers.Dropout(self.dropout_rate)]  # seed

    def call(self, inputs, **kwargs):

        for i in range(self.num_layer):
            fc = self.dense_layers[i](inputs)
            fc = self.bn_layers[i](fc) if self.use_bn else fc
            fc = self.dropout_layers[i](fc)

        return fc

    def compute_output_shape(self, input_shape):
        return input_shape[:-1] + (self.hidden_units_list[-1],)

    def get_config(self):
        base_config = super().get_config()
        config = {
            'hidden_units': self.hidden_units_list,
            'activation': self.activation,
            'kernel_regularizer': self.kernel_regularizer,
            'use_bn': self.use_bn,
            'dropout_rate': self.dropout_rate,
            'seed': self.seed
        }
        return {**base_config, **config}

import pickle

import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp

from garage.tf.models import CategoricalLSTMModel
from tests.fixtures import TfGraphTestCase


class TestCategoricalLSTMModel(TfGraphTestCase):

    def setup_method(self):
        super().setup_method()
        self.batch_size = 1
        self.time_step = 1
        self.feature_shape = 2
        self.output_dim = 1

        self.obs_inputs = np.full(
            (self.batch_size, self.time_step, self.feature_shape), 1.)
        self.obs_input = np.full((self.batch_size, self.feature_shape), 1.)

        self._input_var = tf.compat.v1.placeholder(tf.float32,
                                                   shape=(None, None,
                                                          self.feature_shape),
                                                   name='input')
        self._step_input_var = tf.compat.v1.placeholder(
            tf.float32, shape=(None, self.feature_shape), name='input')

    def test_dist(self):
        model = CategoricalLSTMModel(output_dim=1, hidden_dim=1)
        step_hidden_var = tf.compat.v1.placeholder(shape=(self.batch_size, 1),
                                                   name='step_hidden',
                                                   dtype=tf.float32)
        step_cell_var = tf.compat.v1.placeholder(shape=(self.batch_size, 1),
                                                 name='step_cell',
                                                 dtype=tf.float32)
        model.build(self._input_var, self._step_input_var, step_hidden_var,
                    step_cell_var)
        assert isinstance(model.networks['default'].dist,
                          tfp.distributions.OneHotCategorical)

    def test_is_pickleable(self):
        model = CategoricalLSTMModel(output_dim=1, hidden_dim=1)
        step_hidden_var = tf.compat.v1.placeholder(shape=(self.batch_size, 1),
                                                   name='step_hidden',
                                                   dtype=tf.float32)
        step_cell_var = tf.compat.v1.placeholder(shape=(self.batch_size, 1),
                                                 name='step_cell',
                                                 dtype=tf.float32)
        model.build(self._input_var, self._step_input_var, step_hidden_var,
                    step_cell_var)

        # assign bias to all one
        with tf.compat.v1.variable_scope('CategoricalLSTMModel/lstm',
                                         reuse=True):
            init_hidden = tf.compat.v1.get_variable('initial_hidden')

        init_hidden.load(tf.ones_like(init_hidden).eval())

        hidden = np.zeros((self.batch_size, 1))
        cell = np.zeros((self.batch_size, 1))

        outputs1 = self.sess.run(model.networks['default'].dist.logits,
                                 feed_dict={self._input_var: self.obs_inputs})
        output1 = self.sess.run(
            [
                model.networks['default'].step_output,
                model.networks['default'].step_hidden,
                model.networks['default'].step_cell
            ],
            feed_dict={
                self._step_input_var: self.obs_input,
                step_hidden_var: hidden,
                step_cell_var: cell
            })

        h = pickle.dumps(model)
        with tf.compat.v1.Session(graph=tf.Graph()) as sess:
            model_pickled = pickle.loads(h)

            input_var = tf.compat.v1.placeholder(tf.float32,
                                                 shape=(None, None,
                                                        self.feature_shape),
                                                 name='input')
            step_input_var = tf.compat.v1.placeholder(
                tf.float32, shape=(None, self.feature_shape), name='input')
            step_hidden_var = tf.compat.v1.placeholder(shape=(self.batch_size,
                                                              1),
                                                       name='initial_hidden',
                                                       dtype=tf.float32)
            step_cell_var = tf.compat.v1.placeholder(shape=(self.batch_size,
                                                            1),
                                                     name='initial_cell',
                                                     dtype=tf.float32)

            model_pickled.build(input_var, step_input_var, step_hidden_var,
                                step_cell_var)
            outputs2 = sess.run(model_pickled.networks['default'].dist.logits,
                                feed_dict={input_var: self.obs_inputs})
            output2 = sess.run(
                [
                    model_pickled.networks['default'].step_output,
                    model_pickled.networks['default'].step_hidden,
                    model_pickled.networks['default'].step_cell
                ],
                feed_dict={
                    step_input_var: self.obs_input,
                    step_hidden_var: hidden,
                    step_cell_var: cell
                })
            assert np.array_equal(outputs1, outputs2)
            assert np.array_equal(output1, output2)

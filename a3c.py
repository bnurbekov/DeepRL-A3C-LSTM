import tensorflow as tf

class A3C_graph_ops:
    # Building graph
    def __init__(self):
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.saver = tf.train.Saver()

            #TODO: define graph
            self.variable = tf.Variable(42, name='foo')
            self.initialize = tf.initialize_all_variables()
            self.assign = self.variable.assign(13)


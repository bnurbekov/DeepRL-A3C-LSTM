import tensorflow as tf

from a3c import A3C_graph
from environment import Environment

SKIP_TRAINING = False

def train(g):
	with tf.Session(graph = g.graph) as session:
		# Define training

def evaluate(g):
	with tf.Session(graph = g.graph) as session:
		# Define evaluation

def main(_):
	# Building graph:
	graph_ops = A3C_graph_ops()

	if not SKIP_TRAINING:
		train(graph_ops)

	evaluate(graph_ops)
		

if __name__ == "__main__":
	tf.app.run()
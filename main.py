from model import build_graph
from environment import Environment

SKIP_TRAINING = True

def train(session, graph_ops, saver):
	with tf.Session() as session:

def evaluate(session, graph_ops, saver):

def main():
	graph_ops = build_graph()

	saver = tf.train.Saver()

	if not SKIP_TRAINING:
		train(session, graph_ops, saver)

	evaluate(session, graph_ops, saver)
		

if __name__ == "__main__":
	tf.app.run()
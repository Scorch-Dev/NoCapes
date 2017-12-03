FIRST_DEGREE_POS = 1
SECOND_DEGREE_POS = 0.1
FIRST_DEGREE_NEG = -1 
SECOND_DEGREE_NEG = -0.1
BAD_SCORE = -99999

class Node:
	'''class that represents a node in the map'''
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.is_positive = True
		self.pos_relations = []
		self.neg_relations = []

	def add_relation(self, Node):
		if (Node.is_positive):
			self.pos_relations.append(Node)

		else:
			self.neg_relations.append(Node)

	def villify(self):
		self.is_positive = False
		for relation in self.pos_relations:
			relation.compute_score()

	def compute_score(self):
		if (!self.is_positive):
			self.score = BAD_SCORE
			return 

		self.score = 0
		for relation in self.pos_relations:
			self.score = self.score + FIRST_DEGREE_POS / len(self.pos_relations)
			for contact in relation.pos_relations:
				self.score = self.score + SECOND_DEGREE_POS / len(self.pos_relations)

		for relation in self.neg_relations:
			self.score = self.score + FIRST_DEGREE_NEG 
			for contact in relation.pos_relations:
				self.score = self.score + SECOND_DEGREE_NEG
		





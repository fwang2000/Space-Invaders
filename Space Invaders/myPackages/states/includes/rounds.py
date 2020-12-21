from .enemy import *
import random

class Rounds:

	def __init__(self):

		self.round_enemies = 0
		self.ySpace = -32

	def one(self, width):

		SimpleEnemyNumber = random.randrange(40, 80, 4)
		xSpace = width / (SimpleEnemyNumber//4 + 1)
		self.round_enemies = SimpleEnemyNumber

		wave1 = [SimpleEnemy((i + 1) * xSpace, self.ySpace) for i in range(SimpleEnemyNumber//4)]
		wave2 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 2) for i in range(SimpleEnemyNumber//4)]
		wave3 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 3) for i in range(SimpleEnemyNumber//4)]
		wave4 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 4) for i in range(SimpleEnemyNumber//4)]

		return wave1 + wave2 + wave3 + wave4

	def two(self, width):

		SimpleEnemyNumber = random.randrange(40, 60, 4)
		xSpace = width / (SimpleEnemyNumber//4 + 1)
		RacingEnemyNumber = 4
		self.round_enemies = SimpleEnemyNumber + RacingEnemyNumber

		wave1 = [SimpleEnemy((i + 1) * xSpace, self.ySpace) for i in range(SimpleEnemyNumber//4)]
		wave2 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 2) for i in range(SimpleEnemyNumber//4)]
		wave3 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 3) for i in range(SimpleEnemyNumber//4)]
		wave4 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 4) for i in range(SimpleEnemyNumber//4)]
		wave5 = [RacingEnemy(random.randint(0, width-64), self.ySpace), RacingEnemy(random.randint(0, width-64), self.ySpace), 
			     RacingEnemy(random.randint(0, width-64), self.ySpace * 2), RacingEnemy(random.randint(0, width-64), self.ySpace * 2)]

		return wave1 + wave2 + wave3 + wave4 + wave5

	def three(self, width):

		SimpleEnemyNumber = random.randrange(40, 60, 5)
		xSpace = width / (SimpleEnemyNumber//5 + 1)
		RacingEnemyNumber = 8
		self.round_enemies = SimpleEnemyNumber + RacingEnemyNumber

		wave1 = [RacingEnemy(random.randint(0, width-64), self.ySpace),
				 RacingEnemy(random.randint(0, width-64), self.ySpace),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 2),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 2)]

		wave2 = [SimpleEnemy((i + 1) * xSpace, self.ySpace * 2) for i in range(SimpleEnemyNumber//5)]
		wave3 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 3) for i in range(SimpleEnemyNumber//5)]
		wave4 = [SimpleEnemy((i + 1) * xSpace, self.ySpace * 4) for i in range(SimpleEnemyNumber//5)]
		wave5 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 5) for i in range(SimpleEnemyNumber//5)]
		wave6 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 6) for i in range(SimpleEnemyNumber//5)]

		wave7 = [RacingEnemy(random.randint(0, width-64), self.ySpace * 9),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 9),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 10),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 10)]


		return wave1 + wave2 + wave3 + wave4 + wave5 + wave6 + wave7

	def four(self, width):

		self.round_enemies = 20

		wave = [RacingEnemy(random.randint(0, width-64), self.ySpace), RacingEnemy(random.randint(0, width-64), self.ySpace),
				RacingEnemy(random.randint(0, width-64), self.ySpace * 2), RacingEnemy(random.randint(0, width-64), self.ySpace * 2),
				RacingEnemy(random.randint(0, width-64), self.ySpace * 4), RacingEnemy(random.randint(0, width-64), self.ySpace * 4),
				RacingEnemy(random.randint(0, width-64), self.ySpace * 6), RacingEnemy(random.randint(0, width-64), self.ySpace * 6),
				RacingEnemy(random.randint(0, width-64), self.ySpace * 8), RacingEnemy(random.randint(0, width-64), self.ySpace * 8),
				RacingEnemy(random.randint(0, width-64), self.ySpace * 10), RacingEnemy(random.randint(0, width-64), self.ySpace * 10),
				RacingEnemy(random.randint(0, width-64), self.ySpace * 12), RacingEnemy(random.randint(0, width-64), self.ySpace * 12),
				RacingEnemy(random.randint(0, width-64), self.ySpace * 14), RacingEnemy(random.randint(0, width-64), self.ySpace * 14),
				RacingEnemy(random.randint(0, width-64), self.ySpace * 16), RacingEnemy(random.randint(0, width-64), self.ySpace * 16),
				RacingEnemy(random.randint(0, width-64), self.ySpace * 18), RacingEnemy(random.randint(0, width-64), self.ySpace * 18)]

		return wave

	def five(self, width):

		MediumEnemyNumber = 10
		SimpleEnemyNumber = 25
		RacingEnemyNumber = 2
		xSpace = width / (MediumEnemyNumber//2 + 1)
		self.round_enemies = MediumEnemyNumber + SimpleEnemyNumber + RacingEnemyNumber


		wave1 = [MediumEnemy((i + 1) * xSpace, self.ySpace * 2) for i in range(MediumEnemyNumber//2)]
		wave2 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 3) for i in range(SimpleEnemyNumber//5)]
		wave3 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 4) for i in range(SimpleEnemyNumber//5)]
		wave4 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 5) for i in range(SimpleEnemyNumber//5)]
		wave5 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 6) for i in range(SimpleEnemyNumber//5)]
		wave6 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 7) for i in range(SimpleEnemyNumber//5)]
		wave7 =	[RacingEnemy(random.randint(0, width-64), self.ySpace * 7), RacingEnemy(random.randint(0, width-64), self.ySpace * 7)]
		wave8 =	[MediumEnemy((i + 1) * xSpace, self.ySpace * 9) for i in range(MediumEnemyNumber//2)]

		return wave1 + wave2 + wave3 + wave4 + wave5 + wave6 + wave7 + wave8
	
	def six(self, width):


		MediumEnemyNumber = 30
		RacingEnemyNumber = 8
		xSpace = width / 16
		self.round_enemies = MediumEnemyNumber + RacingEnemyNumber

		wave1 = [MediumEnemy(xSpace, self.ySpace * 2), MediumEnemy(15 * xSpace, self.ySpace * 2),
				 MediumEnemy(xSpace * 3, self.ySpace * 4), MediumEnemy(13 * xSpace, self.ySpace * 4),
				 MediumEnemy(xSpace * 5, self.ySpace * 6), MediumEnemy(11 * xSpace, self.ySpace * 6),
				 MediumEnemy(xSpace * 7, self.ySpace * 8), MediumEnemy(9 * xSpace, self.ySpace * 8),
				 MediumEnemy(xSpace * 7, self.ySpace * 10), MediumEnemy(9 * xSpace, self.ySpace * 10),
				 MediumEnemy(xSpace * 5, self.ySpace * 12), MediumEnemy(11 * xSpace, self.ySpace * 12),
				 MediumEnemy(xSpace * 3, self.ySpace * 14), MediumEnemy(13 * xSpace, self.ySpace * 14),
				 MediumEnemy(xSpace, self.ySpace * 16), MediumEnemy(15 * xSpace, self.ySpace * 16),
				 MediumEnemy(xSpace * 3, self.ySpace * 18), MediumEnemy(13 * xSpace, self.ySpace * 18),
				 MediumEnemy(xSpace * 5, self.ySpace * 20), MediumEnemy(11 * xSpace, self.ySpace * 20),
				 MediumEnemy(xSpace * 7, self.ySpace * 22), MediumEnemy(9 * xSpace, self.ySpace * 22),
				 MediumEnemy(xSpace * 7, self.ySpace * 24), MediumEnemy(9 * xSpace, self.ySpace * 24),
				 MediumEnemy(xSpace * 5, self.ySpace * 26), MediumEnemy(11 * xSpace, self.ySpace * 26),
				 MediumEnemy(xSpace * 3, self.ySpace * 28), MediumEnemy(13 * xSpace, self.ySpace * 28),
				 MediumEnemy(xSpace, self.ySpace * 30), MediumEnemy(15 * xSpace, self.ySpace * 30)]
		wave2 =	[RacingEnemy(random.randint(0, width-64), self.ySpace * 11), RacingEnemy(random.randint(0, width-64), self.ySpace * 11),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 11), RacingEnemy(random.randint(0, width-64), self.ySpace * 11),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 27), RacingEnemy(random.randint(0, width-64), self.ySpace * 27),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 27), RacingEnemy(random.randint(0, width-64), self.ySpace * 27)]

		return wave1 + wave2

	def seven(self, width):

		SimpleEnemyNumber = 28
		MediumEnemyNumber = 28
		RacingEnemyNumber = 4
		self.round_enemies = SimpleEnemyNumber + MediumEnemyNumber + RacingEnemyNumber
		xSpace = width / 10

		wave1 = [SimpleEnemy((i + 1) * xSpace, self.ySpace) for i in range(0, 8, 2)]
		wave2 =	[MediumEnemy((i + 1) * xSpace, self.ySpace * 2) for i in range(1, 9, 2)]
		wave3 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 3) for i in range(1, 9, 2)]
		wave4 =	[MediumEnemy((i + 1) * xSpace, self.ySpace * 4) for i in range(0, 8, 2)]
		wave5 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 5) for i in range(0, 8, 2)]
		wave6 = [MediumEnemy((i + 1) * xSpace, self.ySpace * 6) for i in range(1, 9, 2)]
		wave7 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 7) for i in range(1, 9, 2)]
		wave8 =	[MediumEnemy((i + 1) * xSpace, self.ySpace * 8) for i in range(0, 8, 2)]
		wave9 =	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 9) for i in range(0, 8, 2)]
		wave10=	[MediumEnemy((i + 1) * xSpace, self.ySpace * 10) for i in range(1, 9, 2)]
		wave11=	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 11) for i in range(1, 9, 2)]
		wave12=	[MediumEnemy((i + 1) * xSpace, self.ySpace * 12) for i in range(0, 8, 2)]
		wave13=	[SimpleEnemy((i + 1) * xSpace, self.ySpace * 13) for i in range(0, 8, 2)]
		wave14=	[MediumEnemy((i + 1) * xSpace, self.ySpace * 14) for i in range(1, 9, 2)]
		wave15=	[RacingEnemy(random.randint(0, width-64), self.ySpace * 24), RacingEnemy(random.randint(0, width-64), self.ySpace * 24),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 26), RacingEnemy(random.randint(0, width-64), self.ySpace * 26)]

		return wave1 + wave2 + wave3 + wave4 + wave5 + wave6 + wave7 + wave8 + wave9 + wave10 + wave11 + wave12 + wave13 + wave14 + wave15

	def eight(self, width):

		SimpleEnemyNumber = random.randrange(40, 60, 4)
		MediumEnemyNumber = random.randrange(12, 22, 2)
		RacingEnemyNumber = 8
		HeavyEnemyNumber = 2
		self.round_enemies = SimpleEnemyNumber + MediumEnemyNumber + RacingEnemyNumber + HeavyEnemyNumber
		simpleXSpace = width / (SimpleEnemyNumber//4 + 1)
		mediumXSpace = width / (MediumEnemyNumber//2 + 1)
		heavyXSpace = width / (HeavyEnemyNumber + 1)

		wave1 = [SimpleEnemy((i + 1) * simpleXSpace, self.ySpace) for i in range(SimpleEnemyNumber//4)]
		wave2 =	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 2) for i in range(SimpleEnemyNumber//4)]
		wave3 = [SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 3) for i in range(SimpleEnemyNumber//4)]
		wave4 =	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 4) for i in range(SimpleEnemyNumber//4)]
		wave5 =	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 8) for i in range(MediumEnemyNumber//2)]
		wave6 =	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 12) for i in range(MediumEnemyNumber//2)] 
		wave7 =	[HeavyEnemy((i + 1) * heavyXSpace, self.ySpace * 20) for i in range(HeavyEnemyNumber)]
		wave8 =	[RacingEnemy(random.randint(0, width-64), self.ySpace * 8), RacingEnemy(random.randint(0, width-64), self.ySpace * 6),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 12), RacingEnemy(random.randint(0, width-64), self.ySpace * 8),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 16), RacingEnemy(random.randint(0, width-64), self.ySpace * 14),
				 RacingEnemy(random.randint(0, width-64), self.ySpace * 20), RacingEnemy(random.randint(0, width-64), self.ySpace * 16)]

		return wave1 + wave2 + wave3 + wave4 + wave5 + wave6 + wave7 + wave8

	def nine(self, width):

		HeavyEnemyNumber = 10
		MediumEnemyNumber = 14
		SimpleEnemyNumber = 35
		RacingEnemyNumber = 8

		simpleXSpace = width / (SimpleEnemyNumber//7 + 1)
		mediumXSpace = width / (MediumEnemyNumber//2 + 1)
		heavyXSpace = width / (HeavyEnemyNumber//2 + 1)

		self.round_enemies = SimpleEnemyNumber + MediumEnemyNumber + HeavyEnemyNumber + RacingEnemyNumber

		wave1 = [HeavyEnemy(3 * heavyXSpace, self.ySpace * 4), MediumEnemy(4 * mediumXSpace, self.ySpace * 6),
				 SimpleEnemy(3 * simpleXSpace, self.ySpace * 8), MediumEnemy(4 * mediumXSpace, self.ySpace * 22),
				 HeavyEnemy(3 * heavyXSpace, self.ySpace * 32), RacingEnemy(300, self.ySpace * 8), 
				 RacingEnemy(600, self.ySpace * 8), RacingEnemy(400, self.ySpace * 12), 
				 RacingEnemy(500, self.ySpace * 12), RacingEnemy(500, self.ySpace * 18),
				 RacingEnemy(300, self.ySpace * 16), RacingEnemy(600, self.ySpace * 16),
				 RacingEnemy(400, self.ySpace * 18)]
		wave2 =	[HeavyEnemy((i + 1) * heavyXSpace, self.ySpace * 6) for i in range(1, HeavyEnemyNumber//2 - 1, 2)]
		wave3 =	[HeavyEnemy((i + 1) * heavyXSpace, self.ySpace * 8) for i in range(0, HeavyEnemyNumber//2, 4)]
		wave4 =	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 8) for i in range(2, MediumEnemyNumber//2 - 2, 2)]
		wave5 =	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 10) for i in range(1, MediumEnemyNumber//2 - 1, 4)]
		wave6 =	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 12) for i in range(0, MediumEnemyNumber//2, 6)]
		wave7 =	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 10) for i in range(1, SimpleEnemyNumber//7 - 1)]
		wave8 =	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 12) for i in range(0, SimpleEnemyNumber//7)]
		wave9 =	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 14) for i in range(0, SimpleEnemyNumber//7)]
		wave10=	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 16) for i in range(0, SimpleEnemyNumber//7)]
		wave11=	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 18) for i in range(0, SimpleEnemyNumber//7)]
		wave12=	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 20) for i in range(0, SimpleEnemyNumber//7)]
		wave13=	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 22) for i in range(0, 2)]
		wave14=	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 22) for i in range(3, SimpleEnemyNumber//7)]
		wave15=	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 24) for i in range(0, SimpleEnemyNumber//7, 4)]
		wave16=	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 24) for i in range(2, MediumEnemyNumber//2 - 2, 2)]
		wave17=	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 26) for i in range(1, MediumEnemyNumber//2 - 1, 4)]
		wave18=	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 28) for i in range(0, MediumEnemyNumber//2, 6)]
		wave19=	[HeavyEnemy((i + 1) * heavyXSpace, self.ySpace * 34) for i in range(1, HeavyEnemyNumber//2 - 1, 2)]
		wave20=	[HeavyEnemy((i + 1) * heavyXSpace, self.ySpace * 36) for i in range(0, HeavyEnemyNumber//2, 4)]
				

		return wave1 + wave2 + wave3 + wave4 + wave5 + wave6 + wave7 + wave8 + wave9 + wave10 + wave11 + wave12 + wave13 + wave14 + wave15 + wave16 + wave17 + wave18 + wave19 + wave20

	def ten(self, width):

		RacingEnemyNumber = 4
		MediumEnemyNumber = 49
		SimpleEnemyNumber = 66
		HeavyEnemyNumber = 13

		self.round_enemies = 1#RacingEnemyNumber + HeavyEnemyNumber + MediumEnemyNumber + SimpleEnemyNumber
		mediumXSpace = width / 14
		heavyXSpace = width / 6
		simpleXSpace = width / 14

		wave1 = [MediumEnemy((i + 1) * mediumXSpace, self.ySpace) for i in range(0, 13, 3)]
		wave2 =	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 3) for i in range(0, 13, 3)]
		wave3 =	[HeavyEnemy((i + 1) * mediumXSpace + 32, self.ySpace * 3) for i in range(1, 13, 3)]
		wave4 =	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 9) for i in range(13)]
		wave5 =	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 11) for i in range(13)]
		wave6 =	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 13) for i in range(13)]
		wave7 =	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 15) for i in range(13)]
		wave8 =	[SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 17) for i in range(13)]
		wave9 = [SimpleEnemy((i + 1) * simpleXSpace, self.ySpace * 19) for i in range(13)]
		wave10= [MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 30) for i in range(13)]
		wave11=	[MediumEnemy((i + 1) * mediumXSpace, self.ySpace * 32) for i in range(13)]
		wave12=	[HeavyEnemy((i + 1) * heavyXSpace * (6/5), self.ySpace * 40) for i in range(4)]
		wave13=	[HeavyEnemy((i + 1) * heavyXSpace, self.ySpace * 44) for i in range(5)]
		wave14=	[RacingEnemy(300, self.ySpace * 27), RacingEnemy(600, self.ySpace * 27),
				 RacingEnemy(400, self.ySpace * 31), RacingEnemy(500, self.ySpace * 31), 
				 SimpleEnemy(width//2, self.ySpace * 57)]

		return wave1 + wave2 + wave3 + wave4 + wave5 + wave6 + wave7 + wave8 + wave9 + wave10 + wave11 + wave12 + wave13 + wave14

	def eleven(self, width):

		return []

	def selection(self, index, width):
		
		switcher = {

			1: self.one,
			2: self.two,
			3: self.three,
			4: self.four,
			5: self.five,
			6: self.six,
			7: self.seven,
			8: self.eight,
			9: self.nine,
			10: self.ten,
			11: self.eleven
		}

		return switcher[index](width)

	def getEnemyCount(self):

		return self.round_enemies
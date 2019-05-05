from matplotlib import pyplot as plt
import scipy.stats as stats
import numpy as np
import math

class simulation:
    def __init__(self,t,l,n):
        self.t = t
        self.l = l
        self.SampleCount = n

    def runit(self):
        def needle_drop_simulation(self):
            #rand x and theta generation
            x = np.random.uniform(0, self.t/2)
            theta = np.random.uniform(0, np.pi/2)
            #chyecking for line cross
            if x < (self.l/2)*np.sin(theta):
                #print ("true")
                return True
            else:
                #print("flase")
                return False


        np.random.seed(0)
        lovert = []
        # initializing for storage
        results = np.zeros(self.SampleCount)
        for i in range(self.SampleCount):
            #storing results
            results[i] = needle_drop_simulation(self)
            # ***FOR PROBLEM 3 AND 4 TO ALLOW PLOTTING OF DIFFERENT L/T RATIOS ***
            #l +=1
            lovert.append(self.l/self.t)  #L Changes so that l/t ratio changes
        #print (results)
        #print (lovert)

        estimated_mean = [np.average(results[0:i]) for i in range(self.SampleCount)]

        #print final  mean P

        print("Final mean P estimate is", estimated_mean[-1])

        if self.t < self.l:  #1 + (2/math.pi)*((self.l/self.t)*(1 - math.sqrt(1-((self.t**2)/(self.l**2)))))- (math.asin(self.t/self.l))))
            varA= (self.l/self.t)*(1 - math.sqrt(1-((self.t**2)/(self.l**2))))
            varB= (math.asin(self.t/self.l)*math.pi/180)
            #pie = 2/(((estimated_mean[-1])-1+(math.asin(self.t/self.l)))/((self.l/self.t)*(1 - math.sqrt(1-((self.t**2)/(self.l**2))))))
            pie2 = (2*varA)/(estimated_mean[-1]-1+varB)
            #print(pie)
            print("pie2: ", pie2)
        else:
            print("Estimated pi value is", -2 * self.l / (estimated_mean[-1] * self.t))
        #ploting
        plt.figure()
        plt.plot(np.arange(self.SampleCount) + 1, estimated_mean, label="Mean estimate of P")
        plt.xlabel('Number of Throws')
        plt.ylabel('Probability of Needle Crossing Line')
        plt.title('Mean estimate of P with increasing number of needles thrown')
        plt.legend(loc='best')
        plt.show()


        # plt.figure()
        # plt.plot(lovert, estimated_mean, label = "Mean estimate of P")
        # plt.xlabel('l/t')
        # plt.ylabel('E(X): Probability of Needle Crossing Line')
        # #
        # plt.legend(loc='best')
        # plt.show()
class changingLOverT:
    def __init__(self, t, l, n):
        self.t = t
        self.l = l
        self.SampleCount = n
    def Ana(self):
        def needle_drop_simulation(self):
            # rand x and theta generation
            x = np.random.uniform(0, self.t / 2)
            theta = np.random.uniform(0, np.pi / 2)
            # chyecking for line cross
            if x < (self.l / 2) * np.sin(theta):
                return True
            else:
                return False

        np.random.seed(0)

        num_samples = 1000
        lovert =[]
        #initializing for storage
        results = np.zeros(num_samples)
        for i in range(num_samples):
            #storing results
            results[i] = needle_drop_simulation(self)
            # ***FOR PROBLEM 3 AND 4 TO ALLOW PLOTTING OF DIFFERENT L/T RATIOS ***
            self.l +=1
            lovert.append(self.l/self.t)  #L Changes so that l/t ratio changes
        estimated_mean = [np.average(results[0:i]) for i in range(num_samples)]

        # print final  mean P
        print("Final mean P estimate is", estimated_mean[-1])

        plt.figure()
        plt.plot(lovert, estimated_mean, label="Mean estimate of P with changing L/T")
        plt.xlabel('l/t')
        plt.ylabel('Probability of Needle Crossing Line')

        plt.legend(loc='best')
        plt.show()
class Analytical:
    def RunAnal(self):
        SmallLOverBigT = np.linspace(0, 1, 300)
        LargeLOverSmallT = np.linspace(1, 2, 300)
        ProbSmallL = []
        lessThanT = []
        MoreThanT = []
        ProbBigL = []
        sec = (2 / 3.14159) + 1
        for i, SmallLOverBigT in enumerate(SmallLOverBigT):
            ProbSmallL.append((2 * SmallLOverBigT / math.pi))
            lessThanT.append(SmallLOverBigT)

        for i, LargeLOverSmallT in enumerate(LargeLOverSmallT):
            ProbBigL.append((1.66)-(sec * (LargeLOverSmallT * (1 - math.sqrt(1 - (1 / LargeLOverSmallT) ** 2))) - ((np.arcsin(1 / LargeLOverSmallT)) * math.pi / 180)))
            MoreThanT.append(LargeLOverSmallT)

        plt.figure()
        plt.plot(lessThanT + MoreThanT, ProbSmallL + ProbBigL)
        plt.xlabel("l / t")
        plt.ylabel("Probability")
        plt.title("Probability (Analytical)")
        plt.show()


''' ***************** ANSWERS ********************
THE FOLLOWING OBJECT ORIENTED COMMANDS PROVIDE SOLUTIONS FROM EACH PROBLEM '''

''' *** PROBLEM 2 ***'''
T_bigger_than_L = simulation(3,2,1000)
T_bigger_than_L.runit()


''' *** PROBLEM 3 ***'''

T_less_than_L = simulation(1,2,1000)
T_less_than_L.runit()

''' *** PROBELEM 4 ***'''

h = changingLOverT(100,0,1000)
h.Ana()

''' *** PROBLEM 5 ***'''

anal = Analytical()
anal.RunAnal()


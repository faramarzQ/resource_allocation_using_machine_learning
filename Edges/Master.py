import Cloudlet
from joblib import load
from workers import Worker1
from workers import Worker2
from workers import Worker3
import numpy as np

class Master():
    def __init__(self):
        """ initialize Master class
        """

        self.numberOfCloudlets = 30;
        self.cloudlets = []

    def createCloudlets(self):
        """ creates cloudlets

        """

        for i in range(self.numberOfCloudlets):
            self.cloudlets.append(Cloudlet.Cloudlet())

    def findBestWorkersForCloudletsByML(self):
        """ finds best worker for each cloudlet using trained model
        """

        # load model
        model = load('Cloud/storage/model.joblib')

        for i in range(self.numberOfCloudlets):
            classLabel = model.predict([self.cloudlets[i].getCategorizedAsList()])
            self.cloudlets[i].classLabel = classLabel

    def allocateCloudletsToWorkers(self):
        """ allocates each task to each worker
        """

        # declare workers
        worker1 = Worker1.Worker1().overrideAttrs()
        worker2 = Worker2.Worker2().overrideAttrs()
        worker3 = Worker3.Worker3().overrideAttrs()

        # attach cloudlet to the given worker
        for i in range(self.numberOfCloudlets):
            if self.cloudlets[i].classLabel == 1:
                worker1.attachCloudlet(self.cloudlets[i])

            elif self.cloudlets[i].classLabel == 2:
                worker2.attachCloudlet(self.cloudlets[i])

            elif self.cloudlets[i].classLabel == 3:
                worker3.attachCloudlet(self.cloudlets[i])

        # run workers
        worker1.run()
        worker2.run()
        worker3.run()

        # print logs
        print('****************************ML******************************')
        print('************************************************************')
        worker1.log()
        worker2.log()
        worker3.log()

    def allocateCloudletsToWorkersGreedely(self):
        """ allocate each cloudlet to each worker using Greedy
        """

        # declare workers
        worker1 = Worker1.Worker1().overrideAttrs()
        worker2 = Worker2.Worker2().overrideAttrs()
        worker3 = Worker3.Worker3().overrideAttrs()

        # find attach best worker for each worker
        for i in range(self.numberOfCloudlets):

            #find best worker
            execTimeFor1 = worker1.execute(self.cloudlets[i])
            execTimeFor2 = worker2.execute(self.cloudlets[i])
            execTimeFor3 = worker3.execute(self.cloudlets[i])
            bestWorker = np.argmin([execTimeFor1, execTimeFor2, execTimeFor3])+1

            # attach est worker
            if bestWorker == 1:
                worker1.attachCloudlet(self.cloudlets[i])
            elif bestWorker == 2:
                worker2.attachCloudlet(self.cloudlets[i])
            elif bestWorker == 3:
                worker3.attachCloudlet(self.cloudlets[i])

            # clear cloudlet and worker history
            self.cloudlets[i].clearHistory()
            worker1.clearHistory()
            worker2.clearHistory()
            worker3.clearHistory()

        # run workers
        worker1.run()
        worker2.run()
        worker3.run()

        # print logs
        print('**************************Greedy****************************')
        print('************************************************************')
        worker1.log()
        worker2.log()
        worker3.log()

if __name__ == '__main__':
    """ start point of the Master Node
    """

    master = Master()

    master.createCloudlets()

    # allocate resources using Machine learning model
    master.findBestWorkersForCloudletsByML()
    master.allocateCloudletsToWorkers()

    # allocate resources using Greedy algorithm
    master.allocateCloudletsToWorkersGreedely()
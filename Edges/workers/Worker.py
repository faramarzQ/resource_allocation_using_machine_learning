
class Worker():
    def __init__(self):
        """ initialize Worker class
        """

        self.cloudlets = []
        self.bandwidth = {}
        self.mips = int
        self.position = int
        self.timer = 0

    def attachCloudlet(self, cloudlet):
        """ attach cloudlet to worker

        Args:
            cloudlet (Cloudlet()): cludlet object
        """
        self.cloudlets.append(cloudlet)

    def run(self):
        """ run the cloudlets on workers,
            cloudlets with high_priority=1 have more priority
        """
        for cloudlet in self.cloudlets:
            if cloudlet.high_priority == 1:
                self.execute(cloudlet)

        for cloudlet in self.cloudlets:
            if cloudlet.high_priority == 0:
                self.execute(cloudlet)

    def execute(self, cloudlet):
        """ execute cloudlet on worker

        Args:
            cloudlet (Cloudlet()): Cloudlet to execute on Worker

        Returns:
            [int]: timer of the worker
        """
        # calculate transfer time
        if cloudlet.position == self.position:
            cloudlet.transferTime = 0
        else:
            cloudlet.transferTime = cloudlet.size / self.bandwidth[cloudlet.position]

        # calculate execution time
        cloudlet.executionTime = cloudlet.instructions / self.mips

        self.timer += cloudlet.executionTime + cloudlet.transferTime

        return self.timer

    def log(self):
        """ print details of the transaction
        """
        print('------------------WORKER--------------------')
        print('position '+  str(self.position))
        print('MIPS: '+     str(self.mips))
        print('Duration: '+ str(self.timer))

        for c in self.cloudlets:
            # if c.position != 1:
            #     continue
            print(
                'From: '+               str(c.position)+
                '  |  High priority: '+   str(c.high_priority)+
                '  |  Instructions: '+    str(c.instructions)+' MI'
                '  |  Size: '+            str(c.size)+' MB'
                '  |  ExecutionTime: '+   str(round(c.executionTime))+' s'
                '  |  TransferTime: '+    str(round(c.transferTime))+' s'
                )

    def clearHistory(self):
        """ clear worker's timer
        """
        self.timer = 0
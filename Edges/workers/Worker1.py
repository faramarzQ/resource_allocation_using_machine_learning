from workers import Worker

class Worker1(Worker.Worker):

    def overrideAttrs(self):
        """ override some attributes

        Returns:
            [Worker1]: returns self object
        """

        self.mips = 2.3
        self.bandwidth = {
            1: 0,
            2: 1.6,
            3: 0.7
        }
        self.position = 1
        self.timer = 0

        return self

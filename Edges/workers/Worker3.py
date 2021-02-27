from workers import Worker

class Worker3(Worker.Worker):

    def overrideAttrs(self):
        """ override some attributes

        Returns:
            [Worker3]: returns self object
        """

        self.mips = 3
        self.bandwidth = {
            1: 0.7,
            2: 2,
            3: 0
        }
        self.position = 3
        self.timer = 0

        return self

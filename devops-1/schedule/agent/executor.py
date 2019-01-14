import subprocess




class Executor:
    def __init__(self, script):
        self.script = script

    def run(self):
        p = subprocess.Popen(self.script, shell=True)
        p.wait()


if __name__ == '__main__':
    executor = Executor('touch /tmp/test.txt')
    executor.run()





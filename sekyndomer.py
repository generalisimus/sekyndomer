import time
class Sec():
    def __enter__(self):
        return self
    def __exit__(*args):
        pass
    def __call__(self, num_runs):
        def timer(func):
            def for_one(num_runs=None):
                avg_time=0
                for i in range(num_runs):
                    t0 = time.time()
                    result = func()
                    t1 = time.time()
                    avg_time += (t1-t0)
                avg_time /= num_runs
                print("Количество запусков: {}".format(num_runs))
                print("Среднее время выполнения: %.5f" % avg_time + " секунды")
                return result
            return for_one
        return timer
with Sec() as sc:
    @sc(num_runs=None)
    def f():
        for j in range(1000000):
            pass
        
f(45)
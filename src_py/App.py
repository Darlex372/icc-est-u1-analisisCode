import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


from src_py.benchmarking import BenchMarking


if __name__ == "__main__":
    print("funciona")
    mO = BenchMarking()
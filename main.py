import numpy as np
import matplotlib as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import pymc as pm
import watermark


def main():
    print("Hello from bayesbookpy!")
    print(watermark.watermark(packages="numpy,scipy,pandas,matplotlib,seaborn,pymc,statsmodels"))


if __name__ == "__main__":
    main()

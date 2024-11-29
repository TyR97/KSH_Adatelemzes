import matplotlib.pyplot as plt
import numpy as np


def get_xy(data_frame):
    """
        A beolvasot adatokból kiválasztjuk mit szeretnék ábrázolni.

        :param data_frame: pandas.DataFrame
        :return:
    """

    print("Melyik értékekeket szeretnéd ábrázolni?")

    #Végig iterálunk a data_frame oszlopain és a nevűket sorszámmal együt kiírjuk
    for i in range(len(data_frame.columns)):
        print(i, data_frame.columns[i])

    X = int(input())
    Y = int(input())

    #A kiválasztott
    x = data_frame[data_frame.columns[X]].values
    y = data_frame[data_frame.columns[Y]].values

    return x, y
def linear_regression(x, y):
    """
        A két kiválasztott adatsorral lineáris regressziót számolunk.

        :param x: list
        :param y: list
        :return slope: float
        :return intercept: float
    """

    coefficients = np.polyfit(x, y, 1)
    slope, intercept = coefficients

    return slope, intercept


def plot_heat(mx):
    """
            Beolvasott adatokból számolt korrelációs mátrix ábrázolása hőtérképen

            :param mx: correlation matrix
            :return
        """

    plt.suptitle("Hőtérkép")
    plt.imshow(mx, cmap="coolwarm", interpolation="nearest")


def plot_fig(slope, intercept, x, y):
    """
        Adatok ábrázolása

        :param x: list
        :param y: list
        :return slope: float
        :return intercept: float
    """

    #Lineáris regresszió vonal kíszámítása
    line = slope * x + intercept

    fig, axs = plt.subplots(2)

    # Szorásdiagram és regresszió ábrázolása
    axs[0].scatter(x, y, marker = "^", color = "C4")
    axs[0].plot(x, line, color="C2")
    axs[0].grid()
    axs[0].set_title("Lineáris regresszió")

    #Vonal diagram ábrázolása
    axs[1].plot(x, y, "-.")
    axs[1].grid()
    axs[1].set_title("Vonal diagram")

    fig.tight_layout(pad = 2)

    # Ábrák megjelenítése
    plt.show()

import kshdata as kshd
import data_plotting as dp


data = kshd.read_data("adat.csv")

x, y = dp.get_xy(data)

slope, intercept = dp.linear_regression(x, y)

dp.plot_heat(data.corr())

dp.plot_fig(slope, intercept, x, y)

from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage = 0, xlbl = 't, c', ylbl = 'U, В', ttl = 'График зависимости U(t)'):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.title(ttl)
    plt.grid()
    plt.show()

def plot_sampling_period_hist(time, xlbl = 't, c', ylbl = 'Количество изерений', ttl = 'Распределение ...', xlim = 0.016):
    #s = set(time)
    #S = list(s).sort()
    #t = []
    #for x in S:
    #    t.append(S.count(x))
    #plot_voltage_vs_time(S, t)
    plt.figure(figsize=(10, 6))
    plt.hist(time)
    plt.xlim(0,xlim)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.title(ttl)
    plt.grid()
    plt.show()
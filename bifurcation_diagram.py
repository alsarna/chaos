import matplotlib.pyplot as plt
from logistic_map import logistic_map

def bifurcation_diagram(skipped_generations, data_generations):
    '''
    :param skipped_generations: generations that don't collect any data (optimized - 100)
    :param data_generations: generations that build a bifurcation diagram (optimized - 400)
    :return: plot bifurcation diagram
    '''

    r_container = []
    x1_container = []
    r = 0

    while r <= 4:
        x0 = 0.5
        for i in range(skipped_generations):
            x1 = logistic_map(r = r, x = x0)
            x0 = x1
        for i in range(data_generations):
            x1 = logistic_map(r=r, x=x0)
            x0 = x1
            r_container.append(r)
            x1_container.append(x1)
        r += 0.01
    plt.scatter(r_container, x1_container, s = 1, marker = ".")
    plt.xlabel("r")
    plt.ylabel("x")
    plt.title("Bifurcation diagram")
    plt.show()
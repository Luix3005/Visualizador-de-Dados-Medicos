import matplotlib.pyplot as plt
from medical_data_visualizer import draw_cat_plot, draw_heat_map, df


def main():
    fig1 = draw_cat_plot(df)
    fig1.savefig('catplot.png')

    fig2 = draw_heat_map(df)
    fig2.savefig('heatmap.png')

    plt.show()


if __name__ == '__main__':
    main()

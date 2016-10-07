import requests
import matplotlib.pyplot as plt


def main():
    # Please convert cson files into json first
    # Use requests to avoid boring Windows encoding problem
    data = requests.get('http://127.0.0.1/mapspot.json').json()

    for section_key, section in data.items():
        for map_key, map in section.items():
            labels = []
            xs = []
            ys = []
            for k, v in map.items():
                labels.append(k)
                xs.append(v[0])
                ys.append(-v[1])
            print(*zip(labels, xs, ys))
            plt.scatter(xs, ys, s=100)
            plt.xlim(0, 15000)
            plt.ylim(-8000, 0)
            for label, x, y in zip(labels, xs, ys):
                plt.annotate(label, xy=(x, y), xytext=(-int(label) * 2 - 10, -int(label) * 2 - 10),
                             textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
            plt.title("%s - %s" % (section_key, map_key))
            plt.savefig("%s.%s.png" % (section_key, map_key), dpi=150, format="png")
            plt.clf()


if __name__ == '__main__':
    main()

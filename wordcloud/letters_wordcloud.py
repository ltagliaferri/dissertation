from os import path
import matplotlib.pyplot as plt

from wordcloud import WordCloud


def main():
    d = path.dirname(__file__)

    # Catherine's Letters file
    text = open(path.join(d, 'all_the_letters.txt')).read()

    # Stopwords file
    stopwords = open(path.join(d, 'stopwords.txt')).read()

    # Word Cloud attributes
    wc = WordCloud(
                background_color="white",
                max_words=2000,
                stopwords=stopwords,
                max_font_size=60,
                min_font_size=8,
                random_state=50)

    # Generate Word Cloud
    wc.generate(text)

    # Show Word Cloud
    plt.imshow(wc)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    main()

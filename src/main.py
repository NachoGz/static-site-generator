from textnode import TextNode, TextType

def main():
    text = "This is a text node"
    type = TextType.BOLD
    url = "https://www.boot.dev"
    tn = TextNode(text, type, url)
    print(tn)


if __name__ == '__main__':
    main()

import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list:
    new_nodes = []
    for node in old_nodes:
                
        # If no delimiter is present, keep the node as is
        if delimiter not in node.text:
            new_nodes.append(node)
            continue
        
        split_nodes = node.text.split(delimiter)
        
        new_nodes.append(TextNode(split_nodes[0].strip(), TextType.TEXT))
        new_nodes.append(TextNode(split_nodes[1].strip(), text_type))
        new_nodes.append(TextNode(split_nodes[2].strip(), TextType.TEXT))
    
    return new_nodes


def extract_markdown_images(text) -> list:
    # Regular expression to match ![alt text](URL)
    pattern = r"!\[([^\]]+)\]\((https?://[^\)]+)\)"

    return re.findall(pattern, text)


def extract_markdown_links(text) -> list:
    # Regular expression to match [alt text](URL)
    pattern = r"(?<!!)\[(.*?)\]\((https?://[^\)]+)\)"
    
    return re.findall(pattern, text)


def split_nodes_image(old_nodes) -> list:
    result_nodes = []

    for node in old_nodes:
        text = node.text
        # Pattern to match image links and the surrounding text
        pattern = r"([^\[]*)(!\[[^\]]+\]\(https?://[^\)]+\))([^\[]*)"

        # We will break the text into nodes until there are no more matches
        remaining_text = text
        
        while True:
            match = re.search(pattern, remaining_text)
            if not match:
                break  # No more image links, break the loop

            before_image, image, after_image = match.groups()

            # Add the text before the image
            if before_image:
                result_nodes.append(TextNode(before_image.strip(), TextType.TEXT))

            # Extract alt text and URL from the image
            alt_text, url = re.match(r"!\[([^\]]+)\]\((https?://[^\)]+)\)", image).groups()
            result_nodes.append(TextNode(alt_text.strip(), TextType.IMAGE, url))

            # Update the remaining text to after the image
            remaining_text = after_image

        # Add any remaining text after the last image
        if remaining_text:
            result_nodes.append(TextNode(remaining_text.strip(), TextType.TEXT))

    return result_nodes


def split_nodes_link(old_nodes) -> list:
    result_nodes = []

    for node in old_nodes:
        text = node.text
        pattern = r"([^\[]*)(\[[^\]]+\]\(https?://[^\)]+\))([^\[]*)"

        matches = re.findall(pattern, text)

        remaining_text = text
        for before_link, link, after_link in matches:
            if before_link:
                result_nodes.append(TextNode(before_link.strip(), TextType.TEXT))
            alt_text, url = re.match(r"\[([^\]]+)\]\((https?://[^\)]+)\)", link).groups()
            result_nodes.append(TextNode(alt_text.strip(), TextType.LINK, url))
            remaining_text = after_link

        if remaining_text:
            result_nodes.append(TextNode(remaining_text.strip(), TextType.TEXT))

    return result_nodes

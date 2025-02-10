print("hello world")
import textnode

def main():
    test_node = textnode.TextNode("This is a text node", 
                                  textnode.TextType.Bold,
                                  "https://www.boot.dev")
    
    print(test_node)




if __name__ == "__main__":
    main()

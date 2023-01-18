text = input("请输入text的内容：")
words = input("请输入words的内容：").split( )

def find_word_positions(text, words): 
    positions = [] 
    for word in words:
        print(word) 
        start_position = 0 
        while True: 
            start_position = text.find(word, start_position) 
            print(start_position)
            if start_position == -1: 
                break 
            positions.append([start_position, start_position + len(word)-1]) 
            start_position += 1 
            positions.sort() 
    return positions

print(find_word_positions(text, words))
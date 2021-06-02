class SuffixTree(object):
    def __init__(self, word):
        self.word = word
        self.sorted_array = self.sort_suffix_array()

    def get_suffix_array(self):
        return [self.word[i:] for i in range(len(self.word))]

    def sort_suffix_array(self):
        return sorted(self.get_suffix_array())

    def find_shortest(self, prefix):
        for char in self.sorted_array: 
            if char.startswith(prefix):
                return char

        return None

    def find_longest(self, prefix):
        for i in range(len(self.sorted_array) - 1, 1, -1):
            if self.sorted_array[i].startswith(prefix):
                return self.sorted_array[i]

        return None

    def find_all(self, prefix):
        return [char for char in self.sorted_array if char.startswith(prefix)]
        
def main():
    word = SuffixTree('abracadabra')
    print(word.get_suffix_array())
    print(word.find_shortest('abra'))
    print(word.find_longest('abra'))
    print(word.find_all('abra'))

if __name__ == '__main__':
    main()

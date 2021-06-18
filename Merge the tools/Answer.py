from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    strlen = len(string)
    for i in range(0,strlen,k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    

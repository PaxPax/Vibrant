import os
"""
headers = ['Name','Address','Age','Phone Number']
data = [['Stan Licker', '2340 7th St.', 27, '309-431-3387'],['Shermane ZCoz', '3023 dfk', 34, '803-323-2343']]
style = default

"""
class Table:
    def __init__(self, headers, list_of_lists):
        self.longest_text = self.multi_list_len(list_of_lists)
        self.PADDING = 2
        self.width = self.PADDING
        self.height = self.PADDING
        # self.width, self.height = os.get_terminal_size()
    
    def displayData(self,headers,list_of_lists):
        pass

    def single_list_len(self, list):
        return len(max(list, key=len))

    def multi_list_len(self, multi_list):
        #expected a 2D list
        largest_word = 0
        for single_list in multi_list:
            test_length = self.single_list_len(single_list)
            if test_length > largest_word:
                largest_word = test_length
        return largest_word
    
    def set_headers(self, headers):
        #clear the screen
        print('\033[2J')
        for header in headers:

    def string_difference(self, a, b):
        return len(a) - len(b)
    # print('\033[2J')
    # print('\033[{0};{1}H{2}'.format(
    # self.title_posy, self.title_posx, title), end='')
    # print('\b')
    
data = [['Stan Licker', '2340 7th St.', '27', '309-431-33874'],['Shermane ZCoz', '3023 dfk', '34', '803-323-2343']]
headers = ['Name','Address','Age','Phone Number']
t = Table(headers, data)
print(f"This is the width {t.width}")
print(f"This is the height {t.height}")

# t.displayData(data)

""" Header 1  | Header 2  
   +----------+-----------+
   |slkfj     | dsklfjlskf|
   ------------------------
   |dalskf    |  dsaklfjds|
   ------------------------
"""

""" Name       | Age | Birthday
    ----------- ----- ---------
    Sammydfdf   23    10/14/1994
    James       10    12/13/1982
"""
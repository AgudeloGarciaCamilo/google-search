from googlesearch import search
import sys

from helpers.custom_input import CustomInput


class GoogleSearcher:
    
    def __init__(self):
        self.search_count = None
        self.keyword_to_search = None
        self.search_results = None
    
    def set_num_of_searches(self):
        print("Enter the number of search results you want to display for each Google search.")
        user_input = int(input())
        self.search_count = user_input
        print("\n")

    def enter_keyword(self):
        print("Enter the text for the Google Search: ")
        user_input = input()
        self.keyword_to_search = user_input
        print("\n")

    def perform_search(self):
        try:
            results = search(self.keyword_to_search, num_results=self.search_count)
            self.search_results = results
            print("Google Search performed successfully.")
        except Exception as e:
            print(e)
            print("Google Search faced an Exception.")
        finally:
            print("\n")
    
    def print_search_results(self):
        print( "The results for {} keywords are: ".format(self.keyword_to_search) )

        count = 1

        for search_result in self.search_results:
            print("Search No. {} -> {}".format(count, search_result))
            count = count + 1

        print("\n")


def main():  
    input_handler = CustomInput()
    google_search_handler =  GoogleSearcher()  

    user_input = input_handler.get_user_input()

    print('DA USER INPUT: ', user_input)
        
 
    
if __name__ == '__main__':  
    main()  
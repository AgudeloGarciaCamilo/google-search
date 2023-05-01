from googlesearch import search
import sys


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
        
    google_search_handler =  GoogleSearcher()  
        
    while(True):  
            
        # Available options
        print("\nSelect any of the operations listed below:")  
        print("1. Set the number of searches we need to display for each Google Search.")  
        print("2. Enter the keyword for the Google Search.")  
        print("3. Perform Google Search for the keyword.")  
        print("4. Print the Google search results obtained.")  
        print("5. Exit from the code execution.")  
            
        menu_choice = input()  
        menu_choice = int(menu_choice)  
    
        if menu_choice == 1:  
            google_search_handler.set_num_of_searches()  
        elif menu_choice == 2:  
            google_search_handler.enter_keyword()  
        elif menu_choice == 3:  
            google_search_handler.perform_search()  
        elif menu_choice == 4:  
            google_search_handler.print_search_results()  
        elif menu_choice == 5:  
            sys.exit()  
    
        print("Do you want to keep going? [y] or [n]")  
        continue_or_exit = input()  
    
        if continue_or_exit == 'y' or continue_or_exit == 'Y':  
            pass  
        elif continue_or_exit == 'n' or continue_or_exit == 'N':  
            sys.exit()  
    
if __name__ == '__main__':  
    main()  
from io import TextIOWrapper
from typing import Any, Generator
from googlesearch import search

from constants.app_config import FILE_TYPE_SEARCH_FORMAT, NUMBER_OF_RESULTS_PER_SEARCH, SITE_SEARCH_WEB, SLEEP_INTERVAL_SECONDS


class GoogleSearcher:
    def __init__(self):
        self.file_type_search_format: int = FILE_TYPE_SEARCH_FORMAT
        self.results_per_search: int = NUMBER_OF_RESULTS_PER_SEARCH
        self.site_search_web: str = SITE_SEARCH_WEB
        self.sleep_interval_seconds: int = SLEEP_INTERVAL_SECONDS    


    def perform_search(self, search_term: str) -> Generator[Any, None, None]:

        results: Generator[Any, None, None] = []

        try:
            results = search(search_term,
                            num_results=self.results_per_search,
                            sleep_interval=self.sleep_interval_seconds)
            print("Google Search performed successfully.")

        except Exception as e:
            print(e)
            print("Google Search faced an Exception.")

        finally:
            print("\n")
            return results
    

    def perform_double_quoted_search(self, search_term: str) -> Generator[Any, None, None]:        
        return self.perform_search(self._get_double_quoted_term(search_term))
    

    def perform_by_site_search(self, search_term: str) -> Generator[Any, None, None]:
        by_site_term: str = f'site:{self.site_search_web} {self._get_double_quoted_term(search_term)}'
        
        return self.perform_search(by_site_term)
    

    def perform_in_url_search(self, search_term: str) -> Generator[Any, None, None]:
        in_url_term: str = f'inurl:{self._get_double_quoted_term(search_term)}'
        
        return self.perform_search(in_url_term)


    def perform_in_title_search(self, search_term: str) -> Generator[Any, None, None]:
        in_title_term: str = f'intitle:{self._get_double_quoted_term(search_term)}'
        
        return self.perform_search(in_title_term)
    

    def perform_in_text_search(self, search_term: str) -> Generator[Any, None, None]:
        in_text_term: str = f'intext:{self._get_double_quoted_term(search_term)}'
        
        return self.perform_search(in_text_term)
    

    def perform_file_type_search(self, search_term: str) -> Generator[Any, None, None]:
        file_type_term: str = f'filetype:{self.file_type_search_format} {self._get_double_quoted_term(search_term)}'
        
        return self.perform_search(file_type_term)
    

    def _get_double_quoted_term(self, search_term: str) -> str:
        return '"' + search_term + '"'
    

    def write_to_file(self, file: TextIOWrapper, results: Generator[Any, None, None]):
        count = 1

        for search_result in results:
            file.write("Search No. {} -> {} \n".format(count, search_result))
            count = count + 1

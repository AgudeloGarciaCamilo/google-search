from core.google_searcher import GoogleSearcher
from helpers.custom_input import CustomInput

from constants.app_config import NUMBER_OF_RESULTS_PER_SEARCH, OUTPUT_FILE_FORMAT, OUTPUT_FILE_NAME_INPUT_MESSAGE, SEARCH_TERM_INPUT_MESSAGE


def main():  
    input_handler = CustomInput()
    google_search_handler =  GoogleSearcher()  

    user_input: str = input_handler.get_user_input(SEARCH_TERM_INPUT_MESSAGE)
    file_name_without_format: str = input_handler.get_user_input(OUTPUT_FILE_NAME_INPUT_MESSAGE)
    output_file_name: str = f'{file_name_without_format}.{OUTPUT_FILE_FORMAT}'

    search_results_1 = google_search_handler.perform_search(user_input)
    search_results_2 = google_search_handler.perform_double_quoted_search(user_input)
    search_results_3 = google_search_handler.perform_by_site_search(user_input)
    search_results_4 = google_search_handler.perform_in_url_search(user_input)
    search_results_5 = google_search_handler.perform_in_title_search(user_input)
    search_results_6 = google_search_handler.perform_in_text_search(user_input)
    search_results_7 = google_search_handler.perform_file_type_search(user_input)

    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        output_file.write(f'DA SEARCH TERM: {user_input}\n')
        output_file.write(f'Number of results per search: {NUMBER_OF_RESULTS_PER_SEARCH}\n')
        output_file.write('\n' * 2)

        output_file.write('### 1. Simple search ###\n')
        google_search_handler.write_to_file(output_file, search_results_1)
        output_file.write('\n' * 2)

        output_file.write('### 2. Double quoted search ###\n')
        google_search_handler.write_to_file(output_file, search_results_2)
        output_file.write('\n' * 2)

        output_file.write('### 3. Double quoted search + search by site ###\n')
        google_search_handler.write_to_file(output_file, search_results_3)
        output_file.write('\n' * 2)

        output_file.write('### 4. Double quoted search + search in URL ###\n')
        google_search_handler.write_to_file(output_file, search_results_4)
        output_file.write('\n' * 2)

        output_file.write('### 5. Double quoted search + search in title ###\n')
        google_search_handler.write_to_file(output_file, search_results_5)
        output_file.write('\n' * 2)

        output_file.write('### 6. Double quoted search + search in text ###\n')
        google_search_handler.write_to_file(output_file, search_results_6)
        output_file.write('\n' * 2)

        output_file.write('### 7. Double quoted search + search by file type ###\n')
        google_search_handler.write_to_file(output_file, search_results_7)
        output_file.write('\n' * 2)
 
    
if __name__ == '__main__':  
    main()  
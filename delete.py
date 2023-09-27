class class DownloadTask(luigi.Task):
# …
    def run(self):
        """Process data from API or Email exports."""
        # read mail text file
        date = self.date  # datetime.datetime.today().strftime('%Y-%m-%d')
        downloaded_from_api = True

        try:
            path_downloads = PATH_TO_API_DOWNLOADS
            folder_list = os.listdir(path_downloads)
            todays_folder = [folder for folder in folder_list if folder.endswith(self.date)]

            if not todays_folder:
                logging.warning(f"There was no data from API available from date: {self.date}. Checking for Email ex-port.")
                downloaded_from_api = False
                path = os.path.join(PATH_TO_MAILS, f"mails_until_{self.date}.CSV")
            else:
                lookup_folder_names = [folder[:-11] for folder in todays_folder]

        except FileNotFoundError:
            logging.error(f"Specified path does not exist: {path_downloads}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

        # process emails...
        try:
        # Implement the logic for email processing
        # ...
        except EmailProcessingError as epe:
            logging.error(f"An error Email Processing Error occurred: {epe}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")






    def move_file_to_archive(file_path):
        file_name = re.match('.*\/(.*$)', file_path)[1]
        file_folder = re.match('(.*\/).*', file_path)[1]
        new_folder = pathlib.Path(file_folder, '..', 'ARCHIVE', self.ed_id + '_' + self.timestamp.strftime("%Y%m%d-%H%M%S"))
        new_file = pathlib.Path(new_folder, file_name)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        os.rename(file_path, new_file)

    def write_output(message):
        with open(self.output_path, "w") as file:
            file.write(message)


from enum import Enum

class SourceType(Enum):
    REMOTE = 'remote'
    LOCAL = 'local'

def get_date_list(start_date, end_date, date_list_remote):
# ...

def get_date_range_list(date_list, start_date, end_date, ex_state, folders_pipeline, check_availability_function):
# ...

def generate_execution_param(date_range, source, local_db_name):
# ...

def get_execution_param(start_date, end_date, source, date_list_remote, ex_state, folders_pipeline):
    if source not in SourceType:
        raise ValueError("ERROR: the source name is not valid")

    if source == SourceType.REMOTE:
        date_list = get_date_list(start_date, end_date, date_list_remote)
        date_range_list = get_date_range_list(date_list, start_date, end_date, ex_state, folders_pipeline,
                                              check_folder_availability_remote)
    else:
        date_range_list = [(start_date, end_date)]

    local_db_name = get_local_db_name(source)

    param_list = [generate_execution_param(date_range, source, local_db_name) for date_range in date_range_list]

    return param_list





df.to_csv(f"{path}{file_name}{query_name}_{name}.csv", index=False, sep=';')





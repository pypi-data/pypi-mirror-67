#-----------------------------------------------------------------------------------------------------------------------------------------------------------
import os
import datetime
import urllib.request


root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
dat_fldr = root_fldr + os.sep + 'data'
mobile_user_agents_path = dat_fldr + os.sep + 'mobile_user_agents.txt'
desktop_user_agents_path = dat_fldr + os.sep + 'desktop_user_agents.txt'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

class CommonActions():

    def __init__(self):
        pass

    def file_to_list(self, path_to_file, encryption = 'utf-8', duplicates = True):
        handle = open(path_to_file, "r", encoding = encryption)
        if duplicates:
            data = [line.replace("\n", "") for line in handle.readlines()]
        else:
            data = list(dict.fromkeys([line.replace("\n", "") for line in handle.readlines()]))
        handle.close()
        return data

    def divide_list(self, lst, parts):
        medium_number = int(len(lst)) // parts
        divided_list = list()
        for i in range(0, parts):
            divided_list.append(lst[(medium_number * i):(medium_number * (i + 1))])
        if int(len(lst)) % parts != 0:
            divided_list[-1].extend(lst[(medium_number * parts):])
        return divided_list

    def write_list_as_line(self, path_to_file, info, delimiter = ',', encryption = 'utf-8', headers = False):
        if headers:
            mode = 'w'
        else:
            mode = 'a'
        handle = open(path_to_file, mode = mode, encoding = encryption)
        handle.write(delimiter.join(info) + '\n')
        handle.close()

    def create_dates_list(self, start_date, end_date, input_format = "%m/%d/%Y", output_format = "%m/%d/%Y"):
        sdate = datetime.datetime.strptime(start_date, input_format)
        edate = datetime.datetime.strptime(end_date, input_format)
        date_list = list(reversed([(edate - datetime.timedelta(days=x)).strftime(output_format) for x in range((edate - sdate).days + 1)]))
        return date_list

    def download_file_by_link(self, link, file_name, folder = '/'):
        if folder == '/':
            urllib.request.urlretrieve(link, file_name)
        elif (folder != '/') and (folder[-1] == '/'):
            path = folder + file_name
            urllib.request.urlretrieve(link, path)
        elif (folder != '/') and (folder[-1] != '/'):
            path = folder + '/' + file_name
            urllib.request.urlretrieve(link, path)

    def get_user_agents(self, type_, number):
        if type_ == 'mobile':
            mobile_user_agents = self.file_to_list(mobile_user_agents_path)
            return random.sample(mobile_user_agents, number)

        elif type_ == 'desktop':
            desktop_user_agents = self.file_to_list(desktop_user_agents_path)
            return random.sample(desktop_user_agents, number)

        elif type_ == 'mix':
            mobile_user_agents = self.file_to_list(mobile_user_agents_path)
            desktop_user_agents = self.file_to_list(desktop_user_agents_path)
            user_agents = mobile_user_agents + desktop_user_agents
            return random.sample(user_agents, number)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

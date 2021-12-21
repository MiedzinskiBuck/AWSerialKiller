import json
import os
import sys
from pathlib import Path

class Parser:

    def session_select(self):
        session_name = ""
        available_sessions = os.listdir("./results/")
        if available_sessions:
            print("================================================================================================")
            print("[+] Select Session:\n")
            print("0 - New Session")
            option = 1
            session_options = {}
            for stored_session in available_sessions:
                stored_session = stored_session.split("_")[0]
                session_options[str(option)] = stored_session
                print("{} - {}".format(str(option), stored_session))
                option += 1
            selected_option = input("\nSession: ")
            if not selected_option:
                print("\n[-] No session selected...exiting...")
                sys.exit()
            selected_option = int(selected_option)
            if selected_option == 0:
                selected_session = input("[+] Please name your session: ")
                os.mkdir("results/{}_session_data".format(selected_session))
                session_name = selected_session
            else:
                session_name = session_options[str(selected_option)]
        else:
            print("================================================================================================")
            selected_session = input("[+] Please name your session: ")
            session_name = selected_session
            os.mkdir("results/{}_session_data".format(selected_session))

        return session_name
    
    def parse_module_results(self, executed_command, module_results):
        executed_module = executed_command.split("/")[1]
        data_category = executed_module.split("_")[0]

        parsed_data = {}
        parsed_data[data_category] = []
        parsed_data[data_category].append(module_results)

        return parsed_data

    def store_parsed_results(self, selected_session, executed_module, parsed_results):
        category = list(parsed_results)[0]
        category_path = "./results/{}_session_data/{}".format(selected_session, category)
        executed_module = executed_module.split("/")[1]

        if not os.path.exists(category_path):
            os.mkdir(category_path)
        
        results_file_path = "{}/{}_results.json".format(category_path, executed_module)

        results_file = open(results_file_path, "w")
        json.dump(parsed_results, results_file, default=str)
        results_file.close()
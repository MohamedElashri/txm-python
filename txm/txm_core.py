import json
import os
import subprocess

class AliasManager:
    @staticmethod
    def handle_set(alias_name, tmux_command):
        alias_file = os.path.expanduser("~/.txm-aliases.json")
        if os.path.exists(alias_file):
            with open(alias_file, 'r') as f:
                aliases = json.load(f)
        else:
            aliases = {}
        
        aliases[alias_name] = tmux_command
        with open(alias_file, 'w') as f:
            json.dump(aliases, f)
            print(f"Alias {alias_name} set.")

    @staticmethod
    def handle_get(alias_name):
        alias_file = os.path.expanduser("~/.txm-aliases.json")
        if os.path.exists(alias_file):
            with open(alias_file, 'r') as f:
                aliases = json.load(f)
                if alias_name in aliases:
                    print(f"Alias {alias_name}: {aliases[alias_name]}")
                else:
                    print("Alias does not exist.")
        else:
            print("No aliases set.")

    @staticmethod
    def handle_remove(alias_name):
        alias_file = os.path.expanduser("~/.txm-aliases.json")
        if os.path.exists(alias_file):
            with open(alias_file, 'r') as f:
                aliases = json.load(f)
                if alias_name in aliases:
                    del aliases[alias_name]
                    with open(alias_file, 'w') as f:
                        json.dump(aliases, f)
                        print(f"Alias {alias_name} removed.")
                else:
                    print("Alias does not exist.")
        else:
            print("No aliases set.")

    @staticmethod
    def handle_list():
        alias_file = os.path.expanduser("~/.txm-aliases.json")
        if os.path.exists(alias_file):
            with open(alias_file, 'r') as f:
                aliases = json.load(f)
                for alias_name, tmux_command in aliases.items():
                    print(f"{alias_name} -> {tmux_command}")
        else:
            print("No aliases set.")



class PresetManager:
    @staticmethod
    def handle_save(preset_name):
        # Get the current tmux session details
        session_info = subprocess.check_output("tmux list-windows", shell=True).decode("utf-8")
        
        # Save it to the .txm-presets.json
        with open(".txm-presets.json", "r+") as f:
            presets = json.load(f)
            presets[preset_name] = session_info
            json.dump(presets, f)

    @staticmethod
    def handle_load(preset_name):
        # Load tmux session from saved preset
        with open(".txm-presets.json", "r") as f:
            presets = json.load(f)
            session_info = presets.get(preset_name)
            if session_info:
                # Implement session loading logic here
                pass

    @staticmethod
    def handle_remove(preset_name):
        # Remove saved preset
        with open(".txm-presets.json", "r+") as f:
            presets = json.load(f)
            presets.pop(preset_name, None)
            json.dump(presets, f)

    @staticmethod
    def handle_list():
        # List all saved presets
        with open(".txm-presets.json", "r") as f:
            presets = json.load(f)
            return list(presets.keys())



class LogManager:
    @staticmethod
    def handle_start(pane_id):
        # Start logging
        subprocess.run(f"tmux pipe-pane -o -t {pane_id} 'cat >>~/.txm_{pane_id}.log'", shell=True)

    @staticmethod
    def handle_stop(pane_id):
        # Stop logging
        subprocess.run(f"tmux pipe-pane -o -t {pane_id}", shell=True)

    @staticmethod
    def handle_show(pane_id):
        # Show logs
        log_file = f"~/.txm_{pane_id}.log"
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                return f.read()


class SyncManager:
    @staticmethod
    def handle_sync(operation):
        # Synchronize panes
        if operation == "on":
            subprocess.run("tmux setw synchronize-panes on", shell=True)
        elif operation == "off":
            subprocess.run("tmux setw synchronize-panes off", shell=True)

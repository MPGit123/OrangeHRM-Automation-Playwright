import os

def load_env_file(file_path=".env.sample"):
    try:
        with open(file_path) as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()

    except Exception as e:
        print(f"The file with the name {file_path} is not found")
        raise e
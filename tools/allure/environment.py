import platform
import sys

from config import settings



def create_allure_environment_file():
    os_info = f'os_info={platform.system()}, {platform.release()}'
    python_version = f'python_version={sys.version}'

    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    items.append(os_info)
    items.append(python_version)
    properties = "\n".join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
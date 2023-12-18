import config
import json
from dataclasses import asdict


# print(config.load())
# config.Config
# with open(config.CONFIG_FILE_PATH, "w") as config_file:
#     out = config.Config().__dict__
#     out.update({"browser": "all"})
#     json.dump(out, config_file, indent=4)
print(type(config.load))
print(type(config.Config))

import yaml
from dataclasses import dataclass
import marshmallow_dataclass

@dataclass
class RedditUserConfig:
  user_agent: str
  client_id: str
  client_secret: str
  username: str
  password: str

class RedditUserConfigLoader:
  yml_filename:str # yml file name to load reddit user config
  def __init__(self, yml_filename:str):
    self.yml_filename = yml_filename
  def get_user_config(self) -> RedditUserConfig:
    # reddit client
    with open(self.yml_filename, 'r') as stream:
        try:
          reddit_user_config_json = yaml.safe_load(stream)
          schema = marshmallow_dataclass.class_schema(RedditUserConfig)()
          return schema.load(reddit_user_config_json)
        except yaml.YAMLError as exc:
            print(exc)
            raise RuntimeError()

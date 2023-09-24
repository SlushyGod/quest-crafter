# Just load the config file into this, will be able to just pull from database or config file and have a basic interface to talk to
class GameboardSettings():
  def __init__(self):
    self.settings = {
      "job_types": [
        "Slayer",
        "Gaurd",
        "Fetch",
        "Crawler"
      ]
    }

  def get_job_types(self):
    return self.settings['job_types']

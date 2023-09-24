from random import randrange
from utils.gameboard_settings import GameboardSettings
from utils.name_generator import generate_name

gameboard = GameboardSettings()
class Job():
  def __init__(self, difficulty, job_type):
    self.difficulty = difficulty
    self.type = job_type
    self.contact = generate_name()

  # Game board determines difficulty, after that it should by up to the job
  def generate(difficulty):
    job_types = gameboard.get_job_types()
    job_type_int = randrange(0, len(gameboard.get_job_types()))
    job_type = job_types[job_type_int]

    return Job(difficulty, job_type)

  def deserialize(self):
    data = {
      "difficulty": self.difficulty,
      "job_type": self.type,
      "contact": self.contact,
    }
    return data
    

  # For the type of job generates encounters, people, and anything else the quest might need
  #def self.generate_game_state():
  
  # Has a generic template based on how the game_state is generated
  #def self.generate_description():
    
  # Based on the game state that was rolled, will try to determine actual difficulty, if there is no way then ignore it
  #def self.generate_real_difficulty():

def test():
  new_job = Job.generate(1)
  print(new_job.deserialize())

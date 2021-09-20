from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import time

class Form1(Form1Template):

  def __init__(self, **properties):
    self.init_components(**properties)
    self.user_algo_input.items = ['top-k sampling','generic sampling','greedy']
    self.time_since_last_submit = 0

  def submit_button_click(self, **event_args):
    text_input = self.user_text.text
    algo_input = self.user_algo_input.selected_value
    current_time = time.time()
    
    if current_time - self.time_since_last_submit > 10:
      self.time_since_last_submit = current_time
      
      if text_input != '':
        try:
          result = anvil.server.call("generate_text", text_input, algo_input)
          self.output_text.text = text_input + result
          self.error_text.text = ''
        except BaseException as e:
          print('Error: ',e)
          self.error_text.text = 'Error generating text'
      else:
        self.error_text.text = 'Please enter a prompt'
    else:
      self.error_text.text = 'Please wait before submitting'
    
    





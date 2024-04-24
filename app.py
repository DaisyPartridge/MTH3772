from vetiver import VetiverModel, VetiverAPI
from dotenv import load_dotenv, find_dotenv
import pins

load_dotenv(find_dotenv())

b = pins.board_folder('data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model', version = '20240306T123850Z-a6f9b')

app = VetiverAPI(v, check_prototype=True)
app.run(port = 8080)

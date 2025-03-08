from TwitterAccount import  TwitterAccount
import os
import dotenv
dotenv.load_dotenv()
USERNAME=os.getenv("USERNAME")
PASSWORD=os.getenv("PASSWORD")
account = TwitterAccount()
account.login(USERNAME, PASSWORD)

target_account="pokemonofficial.sg"
account.find_user(target_account)

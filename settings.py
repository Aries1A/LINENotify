# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

AT= os.environ.get("ACCESS_TOKEN") # 環境変数の値をAPに代入

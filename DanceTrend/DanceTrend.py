"""
	@name AlbumReview.py
	@date 2023 09 27
	@version 0.1.0
	@author jackjackjack® c/o W3BBIE
	@description Class model to generate dance trends
	             Uses openai API calls. 
	             Built for AI Label project.
"""

""" Module Imports """
from dotenv import dotenv_values
import datetime
import os
import openai
import random
import sys

""" API Key Configuration """
CONFIG = dotenv_values( "../.env" )
API = CONFIG[ "API_KEY" ]
openai.api_key = API
# openai.Model.list() # to list models available.

""" Class Model: AlbumReview """
class DanceTrend:
	pass
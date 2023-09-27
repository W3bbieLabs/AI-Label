"""
	@name AlbumReview.py
	@date 2023 09 26
	@version 0.1.0
	@author jackjackjack® c/o W3BBIE
	@description Class model to generate an album review. 
	             Uses openai API calls. 
	             Built for AI Label project.
"""

""" Script Imports """
from dotenv import dotenv_values
import datetime
import os
import openai
import random
import sys

""" API Key Configuration """
CONFIG = dotenv_values("../.env")
API = CONFIG["API_KEY"]
openai.api_key = API
openai.Model.list() # to list models available.

""" Class Model: AlbumReview """
class AlbumReview:
	reviewLengths = [ 256, 420, 1024 ]
	reviewSentiments = set( { "positive", "negative", "scathing", "rave", "neutral", "political", "atheist" } )
	authorLikenesses = set( { "chuck klosterman", "octavia e. butler", "james baldwin", "stephen king", "ta-nehisi coates", "" } )
	def __init__( self, artistName:str, titleOfAlbumOrProject:str ):
		self.artistName = artistName
		self.authorToImitate = random.choice( list( self.authorLikenesses ) )
		self.currentReview = None
		self.gptModel = "gpt-3.5-turbo"
		self.lengthOfReview = random.choice( self.reviewLengths )
		self.reviewSentiment = random.choice( list( self.reviewSentiments ) )
		self.titleOfAlbumOrProject = titleOfAlbumOrProject
		self.promptContext = self.establishPromptContext()
		self.promptExpert = self.establishPromptExpert()
	""" Getters/Setters """
	def getAuthorToImitate(self): return self.authorToImitate
	def setAuthorToImitate(self, newAuthor): self.authorToImitate = newAuthor
	def getCurrentReview( self ): return self.currentReview
	def getPromptContext( self ): return self.promptContext
	def getPromptExpert( self ): return self.promptExpert
	def getReviewLength( self ): return self.lengthOfReview
	def getReviewSentiment( self ): return self.reviewSentiment
	def setCurrentReview( self, someReview:str ): self.currentReview = someReview
	def setPromptContext( self, newPromptContext:str ): self.promptContext = newPromptContext
	def setPromptExpert( self, newPromptExpert ): self.promptExpert = newPromptExpert
	def setReviewLength( self, newReviewLength:int): self.lengthOfReview = newReviewLength
	def setReviewSentiment( self, newReviewSentiment ): self.reviewSentiment = newReviewSentiment
	
	""" Class Methods """
	def create( self, authorOfReview:str ):
		"""
			@method create()
			@param self
			@param authorOfReivew:str, the author likeness being used to write the review.
			@description generates the album review. 
			@usage self.create( authorOfReview )
		"""
		self.setAuthorToImitate( authorOfReview )
		self.setReviewLength( random.choice( self.reviewLengths ) )
		self.setReviewSentiment( random.choice( list( self.reviewSentiments ) ) )
		self.setPromptContext( self.establishPromptContext() )
		createdReview:str = openai.ChatCompletion.create( 
			model=self.gptModel, 
			messages=[
			    { "role":"system", "content": self.getPromptExpert() },
			    { "role": "user", "content": self.getPromptContext() }    
			],
			temperature=round( random.uniform( 1.0, 2.0 ), 1 ),
			max_tokens=256,
			top_p=round( random.uniform( 0.5, 1.0 ), 1 ),
			frequency_penalty=round( random.uniform( 0.1, 2.0 ), 1 ),
			presence_penalty=round( random.uniform( 0.1, 2.0 ), 1 ) )
		self.setCurrentReview( createdReview )
	def displayStats(self):
		"""
			@method displayStats()
			@param self
			@description prints information relative to the content.
			@usage self.displayStats()
		"""
		print(f"""
		Review Stats
		----------------------------------------
		Author: { self.authorToImitate }
		Character Count: { self.lengthOfReview }
		Sentiment: { self.getReviewSentiment() }
		Model: { self.gptModel }
		""")
	def displayReview(self):
		"""
			@method displayReview()
			@param self
			@description displays the generated review.
			@usage self.displayReview()
		"""
		print( self.getCurrentReview()[ "choices" ][ 0 ][ "message" ][ "content" ] )
	def establishPromptContext( self ):
		"""
			@method establishPromptContext()
			@param self
			@description returns a prompt context.
			@usage self.establishPromptContext()
		"""
		promptContext = f"Create a review of { self.artistName }'s latest project, { self.titleOfAlbumOrProject }. This review should be from the { self.getReviewSentiment() } point of view. This review could be up to { self.getReviewLength() } characters in length. The review should include perceived weaknesses, strengths of the project. It should also speak to { self.artistName }'s state of mind during the project's creation. Also, consider the aesthetic quality of the project; and speak to its cultural value. And imagine the best (and worst) environments to consume the project in. Because this is a review, also visualize they type of listener who would be most interested in { self.artistName }'s { self.titleOfAlbumOrProject }."
		return promptContext
	def establishPromptExpert( self ):
		"""
			@method establishPromptExpert()
			@param self
			@description returns persona for ai agent.
			@usage self.establishPromptExpert()
		"""
		promptExpert = f"You are { self.getAuthorToImitate() }. You are a pop-culture music journalist. "
		return promptExpert
	def write( self ):
		"""
			@method write()
			@param self
			@description writes the generated content to a .txt file.
			@usage self.write()
		"""
		timestamp = datetime.datetime.now().strftime( "%Y%m%d-%H%M%S" )
		with open( f"./outputs/album-reviews/{ timestamp }_review.txt", "w" ) as source:
			source.write( self.getCurrentReview()[ "choices" ][ 0 ][ "message" ][ "content" ] )

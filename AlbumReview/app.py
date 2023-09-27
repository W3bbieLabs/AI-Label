"""
	@name app.py
	@date 2023 09 26
	@version 0.1.0
	@author jackjackjack® c/o W3BBIE
	@description Class model to generate an album review. 
	             Uses openai API calls. 
	             Built for AI Label project.
"""
""" Module Imports """
import AlbumReview
import random
import sys

""" Arguement Config """
arguments = { "artistName": str(sys.argv[ 1 ]), 
              "titleOfAlbumOrProject": str(sys.argv[ 2 ]), 
              "reviewsToGenerate": int(sys.argv[ 3 ]) }

def checkArgumentLength():
	print( "Checking if neccessary arguments have been provided." ); displayArgs()
	if len(sys.argv) != 4: 
		help(); exit()
def displayArgs():
	print( "Arguments:" )
	for key,value in arguments.items():
		print( f"\t\t{ key } -------- { value }" )
def help():
	print("""
*** This script expects 4 command-line arguments. ***

Arguments
-----------------
[0] <script-name>            string    .py file
[1] <artist-name>            string    name of artist to generate review for.
[2] <title-of-album>         string    album or project associated with artist's review.
[3] <reviews-to-generate>    integer   number of reviews to generate.

Usage
-----------------
Anatomy      ----  <script-name> <artist-name> <title-of-album> <reviews-to-generate>
Live Example ----  app.py "frank ocean" "nostalgia ultra" "4"
\n""")

""" When script is executed. """
if __name__ == "__main__":
	checkArgumentLength()
	artistName = arguments[ "artistName" ]
	titleOfAlbumOrProject = arguments[ "titleOfAlbumOrProject" ]
	reviewsToGenerate = arguments[ "reviewsToGenerate" ]
	reviewsLeftToGenerate = int( reviewsToGenerate )
	reviewIndex = 0
	AlbumReview = AlbumReview.AlbumReview( artistName, titleOfAlbumOrProject )
	while reviewsLeftToGenerate > 0:
		randomAuthor = random.choice( list(AlbumReview.authorLikenesses ) )
		AlbumReview.setAuthorToImitate( randomAuthor )
		print( f"Review { reviewIndex + 1 } of { reviewsToGenerate } ")
		print( f"Creating a { AlbumReview.getReviewLength() } character review by { AlbumReview.getAuthorToImitate() }." )
		AlbumReview.create( randomAuthor )
		AlbumReview.displayStats()
		AlbumReview.displayReview()
		AlbumReview.write()
		reviewsLeftToGenerate -= 1
		reviewIndex += 1

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

def checkArgumentLength( arguments:dict ):
	EXPECTED_ARG_LENGTH = 3
	try:
		print( "Checking if neccessary arguments have been provided." ); displayArgs()
		if len( arguments ) != EXPECTED_ARG_LENGTH or len( sys.argv ) is None: 
			help(); exit()
	except IndexError:
		print("Too few or no arguments provided."); help()
	except ValueError:
		print("The passed in arguments need to be a dict.");help()
	except Exception:
		print("A really unexpected exception has occured.");help()
def displayArgs():
	print( "Arguments:" )
	for key, value in arguments.items():
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
	try:
		""" Arguement Config """
		arguments = { 
		    "artistName": str( sys.argv[ 1 ] ), 
		    "titleOfAlbumOrProject": str(sys.argv[ 2 ]), 
		    "reviewsToGenerate": int(sys.argv[ 3 ]) 
		}
		checkArgumentLength( arguments )
		artistName = arguments[ "artistName" ]
		titleOfAlbumOrProject = arguments[ "titleOfAlbumOrProject" ]
		reviewsToGenerate = arguments[ "reviewsToGenerate" ]
		reviewsLeftToGenerate = int( reviewsToGenerate )
		reviewIndex = 0
		while reviewsLeftToGenerate > 0:
			AR = AlbumReview.AlbumReview( artistName, titleOfAlbumOrProject )
			randomAuthor = random.choice( list( AR.authorLikenesses ) )
			AR.setAuthorToImitate( randomAuthor )
			print( f"Review { reviewIndex + 1 } of { reviewsToGenerate } ")
			print( f"Creating a { AR.getReviewLength() } character review by { AR.getAuthorToImitate() }." )
			AR.create( randomAuthor )
			AR.displayStats()
			AR.displayReview()
			AR.write()
			reviewsLeftToGenerate -= 1
			reviewIndex += 1
	except Exception as err:
		print(err)
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

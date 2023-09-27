"""
	@name app.py
	@date 2023 09 26
	@version 0.1.0
	@author jackjackjack® c/o W3BBIE
	@description Class model to generate an album review. 
	             Uses openai API calls. 
	             Built for AI Label project.
"""
import AlbumReview
import sys
arguments = { "artistName": str(sys.argv[1]), 
              "titleOfAlbumOrProject": str(sys.argv[2]), 
              "authorToImitate": str(sys.argv[3]),
              "reviewsToGenerate": int(sys.argv[4]) }
def checkArgumentLength():
	print( "Checking if neccessary arguments have been provided." ); displayArgs()
	if len(sys.argv) <= 1: 
		help(); exit()
def displayArgs():
	print( "Arguments:" )
	for key,value in arguments.items():
		print( f"\t\t{ key } -------- { value }" )
def help():
	print("""
*** This script expects 5 command-line arguments. ***

Arguments
-----------------
[0] <script-name>            string    .py file
[1] <artist-name>            string    name of artist to generate review for.
[2] <title-of-album>         string    album or project associated with artist's review.
[3] <author-to-imitate>      string    name of a writer to reference.
[4] <reviews-to-generate>    integer   number of reviews to generate.

Usage
-----------------
Anatomy      ----  <script-name> <artist-name> <title-of-album> <author-to-imitate> <reviews-to-generate>
Live Example ----  app.py "frank ocean" "nostalgia ultra" "chuck klosterman" "4"
\n""")
	
if __name__ == "__main__":
	checkArgumentLength()
	artistName = arguments[ "artistName" ]
	titleOfAlbumOrProject = arguments[ "titleOfAlbumOrProject" ]
	authorToImitate = arguments[ "authorToImitate" ]
	reviewsToGenerate = arguments[ "reviewsToGenerate" ]
	reviewsLeftToGenerate = int( reviewsToGenerate )
	reviewIndex = 0
	AlbumReview = AlbumReview.AlbumReview( artistName, authorToImitate, titleOfAlbumOrProject )
	print( f"Attempting to create { reviewsToGenerate } reviews by { authorToImitate }." )
	while reviewsLeftToGenerate > 0:
		print( f"Review { reviewIndex + 1 } of { reviewsToGenerate } ")
		reviewsLeftToGenerate -= 1
		reviewIndex += 1
		AlbumReview.create()
		AlbumReview.displayStats()
		AlbumReview.displayReview()
		AlbumReview.write()
import mediafile
import fresh_tomatoes


toy_story = mediafile.Media("Toy Story","1h 21m","friendship between toys and humans","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = mediafile.Media("Avatar","2h 42m","A marine stranded on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
avengers = mediafile.Media("Avengers Infinity Wars","2h 36m","Superheroes prevent World","https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg","https://www.youtube.com/watch?v=6ZfuNTqbHE8")
deadpool = mediafile.Media("Deadpool 2" ,"Trailer : 2 mins", "Deadpool and his team saves the world","https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg","https://www.youtube.com/watch?v=D86RtevtfrA")
breaking = mediafile.TV("Breaking Bad","S1-S5","A nice tv series","https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png","https://www.youtube.com/watch?v=ceqOTZnhgY8")
altered = mediafile.TV("Altered Carbon" ,"S1-S2", "A nice scifi tv series","https://upload.wikimedia.org/wikipedia/en/a/a0/Altered_Carbon_title.jpg","https://www.youtube.com/watch?v=dhFM8akm9a4")


movies = [toy_story,avatar,avengers,deadpool,breaking , altered]


fresh_tomatoes.open_movies_page(movies)

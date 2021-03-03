-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
--	If a show doesn’t have a genre, display NULL in the genre column
--	Each record should display: tv_shows.title - tv_genres.name
--	Results must be sorted in ascending order by the show title and genre name
--	You can use only one SELECT statement
SELECT tv_genres.name FROM tv_genres
       WHERE tv_genres.id  NOT IN (SELECT genre_id FROM tv_show_genres
       RIGHT JOIN tv_shows ON show_id = id 
       WHERE title = "Dexter") ORDER BY tv_genres.name ASC;

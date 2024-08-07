$(document).ready(function() {
  // Define the URL to fetch data from
  var url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Use jQuery's $.get method to perform the AJAX request
  $.get(url, function(data) {
      // Extract the list of movies from the response data
      var movies = data.results;

      // Select the ul#list_movies element
      var $listMovies = $('#list_movies');

      // Iterate over each movie and create a list item for each
      $.each(movies, function(index, movie) {
          // Create a new list item with the movie title
          var $listItem = $('<li>').text(movie.title);
          // Append the list item to the ul#list_movies element
          $listMovies.append($listItem);
      });
  });
});

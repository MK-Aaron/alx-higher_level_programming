$(document).ready(function() {
    // The URL to fetch data from
    var url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

    // Use jQuery's $.get method to perform the AJAX request
    $.get(url, function(data) {
        // Extract the character name from the response data
        var characterName = data.name;

        // Use jQuery to update the content of the div#character element
        $('#character').text(characterName);
    });
});

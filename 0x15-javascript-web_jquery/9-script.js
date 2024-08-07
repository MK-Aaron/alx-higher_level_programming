$(document).ready(function() {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function(response) {
      // Extract the 'hello' value from the response
      const helloText = response.hello;

      // Update the content of the DIV#hello
      $('#hello').text(helloText);
    },
    error: function() {
      // Handle any errors here
      $('#hello').text('Error fetching data');
    }
  });
});

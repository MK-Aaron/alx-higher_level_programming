$(document).ready(function() {
    $('#toggle_header').click(function() {
      // Select the <header> element
      var $header = $('header');
      
      // Check the current class and toggle
      if ($header.hasClass('red')) {
        $header.removeClass('red').addClass('green');
      } else {
        $header.removeClass('green').addClass('red');
      }
    });
  });

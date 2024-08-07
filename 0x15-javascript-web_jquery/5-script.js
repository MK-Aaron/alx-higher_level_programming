$(document).ready(function() {
  $('#add_item').click(function() {
    // Create a new row with the text "Item"
    var newItem = $('<li>Item</li>');
    
    // Append the new row element to the <ul> with the class "my_list"
    $('.my_list').append(newItem);
  });
});


$(document).ready(function () {
    $('#userForm').submit(function (event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/show_user',
            dataType: 'json',
            success: function (data) {
                // Assuming 'data' is the JSON response from the backend
                // You can update the following line based on the structure of your JSON data
                $('#successMessage').text(JSON.stringify(data));
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });
    });
});

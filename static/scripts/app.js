$(document).ready(function () {
        $('#userForm').submit(function (event) {
            event.preventDefault();

            var formData = {
                'first_name': $('#first_name').val(),
                'last_name': $('#last_name').val()
            };

            $.ajax({
                type: 'POST',
                url: '/add_user',
                data: formData,
                dataType: 'json',
                success: function (data) {
                    var successMessage = formData.first_name + ' ' + formData.last_name + ' added to DB successfully';

                    // Display success message on the webpage
                    $('#successMessage').text(successMessage);

                    // Clear the input fields
                    $('#first_name').val('');
                    $('#last_name').val('');
                },
                error: function (error) {
                    console.log('Error:', error);
                }
            });
        });
    });


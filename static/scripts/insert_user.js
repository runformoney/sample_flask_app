$(document).ready(function () {
    $('#insertUserForm').submit(function (event) {
        event.preventDefault();
        var userName = $('#userName').val();

        // Check if the name is empty
        if (!userName.trim()) {
            alert('Please enter a name.');
            return;
        }

        // Check if the name contains both first name and last name
        if (userName.split(' ').length < 2) {
            alert('Please enter both first name and last name.');
            return;
        }

        console.log("User name:", userName);

        $.ajax({
            type: 'POST',
            url: '/insert_user',
            data: { name: userName },
            dataType: 'json',
            success: function (data) {
                $('#insertResult').text(data.message);

                // Clear the input field after success
                $('#userName').val('');
            },
            error: function (error) {
                console.log('Error:', error);
                $('#insertResult').text('Backend Error: ' + error);
            }
        });
    });
});

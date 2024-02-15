$(document).ready(function () {
    $('#showUserBtn').click(function () {
        $.ajax({
            type: 'GET',
            url: '/show_user',
            dataType: 'json',
            success: function (data) {
                displayUserData(data);
            },
            error: function (error) {
                console.log('Error:', error);
                $('#userDataContainer').text('Backend Error: ' + error);
            }
        });
    });

    function displayUserData(data) {
        try {
            console.log(data)
            var userDataHtml = '<h2>User Data</h2>';

            userDataHtml += '<table border="1"><tr><th>Roll Number</th><th>Name</th></tr>';
            for (var i = 0; i < data.data.length; i++) {
                userDataHtml += '<tr><td>' + data.data[i].roll_number + '</td><td>' + data.data[i].name + '</td></tr>';
            }
            userDataHtml += '</table>';

            $('#userDataContainer').html(userDataHtml);
        } catch (error) {
            var errorMessage = '<p style="color: red;">Error: ' + error.message + '</p>';
            var dataMessage = '<p style="color: green;">Data from Backend: ' + data + '</p>';
            $('#userDataContainer').html(errorMessage + dataMessage);
        }
    }
});

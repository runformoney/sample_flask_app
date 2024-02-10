$(document).ready(function () {
    $('#userForm').submit(function (event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/show_user',
            dataType: 'json',
            success: function (data) {
                // Assuming 'data' is the JSON response from the backend
                displayTable(data);
            },
            error: function (error) {
                console.log('Error:', error);
                $('#tableContainer').text('Backend Error: ' + error);
            }
        });
    });

    function displayTable(data) {
    try {
        // Assuming 'data' is the JSON response from the backend
        var tableHtml = '<table border="1"><tr><th>Name</th><th>Roll Number</th></tr>';

        for (var i = 0; i < data.data.length; i++) {
            tableHtml += '<tr><td>' + data.data[i].name + '</td><td>' + data.data[i].roll_number + '</td></tr>';
        }

        tableHtml += '</table>';
        $('#tableContainer').html(tableHtml);
    } catch (error) {
        // Handle error and display in #tableContainer
        var errorMessage = '<p style="color: red;">Error: ' + error.message + '</p>';
        var data_message = '<p style="green: red;">Data from Backend: ' + data + '</p>';
        $('#tableContainer').html(errorMessage + data_message);
    }
}

});

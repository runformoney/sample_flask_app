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
            }
        });
    });

    function displayTable(data) {
        // Assuming 'data' is the JSON response from the backend
        var tableHtml = '<table border="1"><tr><th>Name</th><th>Roll Number</th></tr>';

        for (var i = 0; i < data.data.length; i++) {
            tableHtml += '<tr><td>' + data.data[i].name + '</td><td>' + data.data[i].roll_number + '</td></tr>';
        }

        tableHtml += '</table>';
        $('#tableContainer').html(tableHtml);
    }
});

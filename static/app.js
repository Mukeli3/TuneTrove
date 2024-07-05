$(document).ready(function() {
    // Fetch and display songs
    $.get('/songs', function(data) {
        var songsDiv = $('#songs');
        data.forEach(function(song) {
            songsDiv.append(
                '<div>' +
                '<h3>' + song.title + '</h3>' +
                '<p>Artist: ' + song.artist + '</p>' +
                '<p>Album: ' + song.album + '</p>' +
                '</div>'
            );
        });
    });

    // Fetch and display recommendations
    $.get('/recommendations', function(data) {
        var recommendationsDiv = $('#recommendations');
        data.forEach(function(song) {
            recommendationsDiv.append(
                '<div>' +
                '<h3>' + song.title + '</h3>' +
                '<p>Artist: ' + song.artist + '</p>' +
                '<p>Album: ' + song.album + '</p>' +
                '</div>'
            );
        });
    });
});

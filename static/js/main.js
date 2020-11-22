
$(".like").click(function (e) {
    e.preventDefault();

    const movie_id = $(this).attr("value");
    let likes = $(".movie_like_count" + movie_id).text();
    const movie_title = $("#movie_title").text();
    const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;


    $.ajax({
        type: 'POST',
        url: "/ajax/like/",
        data: {
            'likes': likes,
            'movie_id': movie_id,
            'movie_title': movie_title,
            'csrfmiddlewaretoken': csrf,
        },
        success: function (response) {
            if(response) {
                $( '#like' + movie_id ).removeClass('btn-primary btn-primary');
                $( '#like' + movie_id ).addClass('btn-primary btn-success');
                $(".movie_like_count" + movie_id).text(response);
            }
        }
    });
})


$(".dislike").click(function (e) {
    e.preventDefault();

    const movie_id = $(this).attr("value");
    let dislikes = $(".movie_dislike_count" + movie_id).text();
    const movie_title = $("#movie_title").text();
    const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;


    $.ajax({
        type: 'POST',
        url: "/ajax/dislike/",
        data: {
            'dislikes': dislikes,
            'movie_id': movie_id,
            'movie_title': movie_title,
            'csrfmiddlewaretoken': csrf,
        },
        success: function (response) {
            if(response) {
                $( '#dislike' + movie_id ).toggleClass('btn-primary btn-success');
                $(".movie_dislike_count" + movie_id).text(response);
            }
        }
    });
})




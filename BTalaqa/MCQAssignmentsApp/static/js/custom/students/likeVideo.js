$(document).ready(function() {

    $(".like-btn").click(function() {
        videoLikedId = $(this).attr('unique_id');
                $.ajax({
            type: "POST",
            url: "like_video/",
            context:$(this),
            data: {
                "id": videoLikedId
            },
            success: function(data) {
                if (data['success'])

                {
                    this.toggleClass('liked');
                }
            }
        });

    });



});
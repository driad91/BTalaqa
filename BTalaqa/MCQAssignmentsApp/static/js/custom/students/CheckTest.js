$(document).ready(function() {
    Array.prototype.unique = function() {
        return this.filter(function(value, index, self) {
            return self.indexOf(value) === index;
        });
    }
    $("#submit_test").click(function() {
        var questionIDs = [];
        $("[question_id]").each(function(i, el) {
            questionID = el.getAttribute("question_id");
            questionIDs.push(questionID);
        });
        questionIDs = questionIDs.unique();
        questionAnswersDict = {};
        var counter = 0;
        while (counter < questionIDs.length) {
            var answerID = $("input[name='" + questionIDs[counter] + "']:checked").val();
            if (answerID != null) {
                questionAnswersDict[questionIDs[counter]] = answerID;
            } else {
                alert("Please make sure you answer all questions before you submit!");
                return;
            }
            counter++;
        }

        var testId = $('#test_form').attr("test_id");

        $.ajax({
            type: "POST",
            url: " submit_test/",
            data: {
                "values": JSON.stringify({
                    "student_answers": questionAnswersDict,
                    "test_id": testId
                })
            },
            success: function(data) {
                execute(data);
            }
        });
    });
});

function execute(data, show_alert=true){
    var percentage = data['percentage'] + ' %';
    var corrections = data['corrections_dict'];
    var is_video_added = data['is_video_added'];
    if (show_alert) {
        alert('You scored ' + percentage + ' on this test');
    }
    $("input[type=radio]").attr('disabled', true);
    $('#submit_test').prop("disabled", true);
    for (var index in corrections) {
        //var correctionsArray = corrections[index].split(',');
        var chosenAnswer = corrections[index][0];
        var correctAnswers = [];
        counter = 1
        while (counter < corrections[index].length)
        {
            correctAnswers.push(corrections[index][counter]);
            counter++;
        }
        console.debug(correctAnswers);
    if (correctAnswers[0].includes(chosenAnswer)) {
            $('#correction_div_' + index.toString() + '_' + chosenAnswer.toString()).append("<i class ='fas fa-check'> </i>");
        } else {
            var correctAnswerDiv = "<div class='correct-answer'> <b> Correct Answer </b> </div>"

            $('#correction_div_' + index.toString() + '_' + chosenAnswer.toString()).append("<i class ='fas fa-times-circle'> </i>");
            $('#correction_div_' + index.toString() + '_' + correctAnswers[0].toString()).append(correctAnswerDiv);
        }
    }

    if (is_video_added)
    {

      $("#video_msg").removeClass("ghost");

    }
}

$( document ).ready(function() {
    if (student_answers!=0){
        execute(student_answers, show_alert=false);
        $('#retake_test_btn').prop('hidden',false);

    };

    $("#retake_test_btn").click(function() {

$('#retake_test_btn').prop('hidden',true);
$('.correction').each(function (index, value){

$(this).html('');
   $("input[type=radio]").attr('disabled', false);
 $('#submit_test').prop("disabled", false);

});

}
);
});


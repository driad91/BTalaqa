$(document).ready(function() {
Array.prototype.unique = function() {
  return this.filter(function (value, index, self) {
    return self.indexOf(value) === index;
  });
}
$("#submit_test").click(function() {
var questionIDs =[];
$("[question_id]").each(function(i,el){
questionID = el.getAttribute("question_id");
questionIDs.push(questionID);
});
questionIDs = questionIDs.unique();
questionAnswersDict={};
var counter = 0;
while (counter < questionIDs.length){
var answerID = $("input[name='" + questionIDs[counter]+ "']:checked").val();
if (answerID!=null)
{
questionAnswersDict[questionIDs[counter]] = answerID;
}
else
{
alert("Please make sure you answer all questions before you submit!");
return;

}
counter++;
}

var testId = $('#test_form').attr("test_id");

$.ajax({         type:"POST",
                 url:"submit_test/",
                 data: {"values":JSON.stringify({"student_answers":questionAnswersDict,"test_id": testId})},
                 success: function(data){
                 alert(data);
                 }
            });


});
 });
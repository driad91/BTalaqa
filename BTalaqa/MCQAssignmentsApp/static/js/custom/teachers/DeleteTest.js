$(document).ready(function(){

$("#delete-test-link").click(function() {

var check = confirm("Are you sure you want to delete this test?");
        if (check == true) {
            return true;
        }
        else{

        return false;
        }


});
});
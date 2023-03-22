$(document).ready(function(){

    var searchbtn = $('#search-btn')
    var searchform = $('#search-form')

    $(searchbtn).on('click', function(){
        searchform.submit();
    });

});
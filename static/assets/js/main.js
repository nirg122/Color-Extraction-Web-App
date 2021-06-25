function copyToClipboard(element) {
  var $temp = $("<input>");
  $("body").append($temp);
  $temp.val($(element).text()).select();
  document.execCommand("copy");
  $temp.remove();
}
$('#js-upload-files').bind('change', function() { var fileName = ''; fileName = $(this).val(); $('#file-selected').html(fileName); })
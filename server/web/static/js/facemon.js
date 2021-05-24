var host = ""
function sethost(h)
{
    host =  h
}
function gethost()
{
    return host
}
function getProtocol()
{
   return location.protocol;
}

function ajaxUpload(method, host ,request_data, successCB, failedCB)
{
    $.ajax({
        type:       method,
        url:        getProtocol() + "//" + host,
        data:       request_data, 
        processData: false, 
        contentType: false,
        success:    successCB,
        error:      failedCB
        }); 
}

function ajaxRequest(method, host ,request_data, successCB, failedCB)
{
    $.ajax({
        type:       method,
        url:        getProtocol() + "//" + host,
        data:       request_data, 
        success:    successCB,
        error:      failedCB
        }); 
}

function redirectTo(host)
{
    window.location.replace(getProtocol() + "//" + host);
}

function showError(msg)
{
    $("#errorMsg").text(msg)
    $("#errorModal").modal()
}
function showNotice(msg)
{
    $("#noticeMsg").text(msg)
    $("#noticeModal").modal()
}

function timeConverter(timestamp){
    var a = new Date(timestamp);
    var months = ['1','2','3','4','5','6','7','8','9','10','11','12'];
    var year = a.getFullYear();
    var month = months[a.getMonth()];
    var date = a.getDate();
    var hour = a.getHours();
    var min = a.getMinutes();
    var sec = a.getSeconds();
    var time = date + '' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
    return time;
}
function dateConverter(timestamp){
    var a = new Date(timestamp);
    var months = ['1','2','3','4','5','6','7','8','9','10','11','12'];
    var year = a.getFullYear();
    var month = months[a.getMonth()];
    var date = a.getDate();
    var time = date + '/' + month + '/' + year;
    return time;
}


function datetimeConverter(timestamp){    
    var a = new Date(timestamp);
    var months = ['1','2','3','4','5','6','7','8','9','10','11','12'];
    var year = a.getFullYear();
    var month = ("0" + months[a.getMonth()]).slice(-2);
    var day = ("0" + a.getDate()).slice(-2);
    var hour = ("0" + a.getHours()).slice(-2);
    var min = ("0" + a.getMinutes()).slice(-2);
    var sec = a.getSeconds();
    var time = day + '/' + month + '/' + year + ' ' + hour + ':' + min;    
    return time;
}

function decodeStream(stream)
{
    data = atob(stream)
    var bytes = new Array(data.length);
    for (var i = 0; i < data.length; i++) {
        bytes[i] = data.charCodeAt(i);
    }
    data = new Uint8Array(bytes);
    return data
}
function saveExcel(data)
{
    var blob = new Blob([data], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' }); 
    var elem = document.createElement('a');
    var url = window.URL.createObjectURL(blob)
    elem.download = 'report.xlsx'
    elem.href = url
    elem.click()
    window.URL.revokeObjectURL(url)
}
function genericFailCB(res)
{
    showError(res["responseJSON"]["Error"])
}

function genericSuccessCB(res)
{
    showNotice(res["Success"])
}

// string formatting
if (!String.prototype.format) {
    String.prototype.format = function() {
      var args = arguments;
      return this.replace(/{(\d+)}/g, function(match, number) { 
        return typeof args[number] != 'undefined'
          ? args[number]
          : match
        ;
      });
    };
  }
//slideshow
var slideIndex = 1;
// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }

  slides[slideIndex-1].style.display = "block"; 
  dots[slideIndex-1].className += " active";
}

function SetDate(input_date)
{
    var now = new Date();
    var day = ("0" + now.getDate()).slice(-2);
    var month = ("0" + (now.getMonth() + 1)).slice(-2);

    var today = now.getFullYear() + "-"+ (month) + "-"+(day) ;
    input_date.val(today);
}

function SetDateFromString(txt_date, timestamp)
{
    var date = new Date(timestamp * 1);
    var day = ("0" + date.getDate()).slice(-2);
    var month = ("0" + (date.getMonth() + 1)).slice(-2);

    var today = date.getFullYear() + "-"+ (month) + "-"+(day) ;
    txt_date.val(today);
}

function FormatHours(date)
{
    return ("0" + date.getHours()).slice(-2) + ':' + ("0" + date.getMinutes()).slice(-2)
}

function AllowNumberOnly(evt) {
    var theEvent = evt || window.event;
  
    // Handle paste
    if (theEvent.type === 'paste') {
        key = event.clipboardData.getData('text/plain');
    } else {
    // Handle key press
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode(key);
    }
    var regex = /[0-9]|\./;
    if( !regex.test(key) ) {
      theEvent.returnValue = false;
      if(theEvent.preventDefault) theEvent.preventDefault();
    }
  }

function ValidateEmail(email)
{
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    return re.test(email);
}
function IsStringEmpty(str)
{
    var empty = (str.trim().length === 0)
    return empty
}

function findGETParameter(parameterName) {
    var result = null,
        tmp = [];
    var items = location.search.substr(1).split("&");
    for (var index = 0; index < items.length; index++) {
        tmp = items[index].split("=");
        if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    }
    return result;
}

function VerifyToken(onSuccess, onFailed)
{
    jwt = parseJwt(Cookies.get('token'))
    onSuccess(jwt)
}

function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
};

//http://bootstrap-notify.remabledesigns.com/

function ShowToast(_message)
{
    $.notify({
        // options
        message: _message,
    },{
        // settings
        element: 'body',
        position: null,
        type: "info",
        allow_dismiss: false,
        newest_on_top: false,
        showProgressbar: false,
        placement: {
            from: "top",
            align: "right"
        },
        delay: 1000,
        offset: 20,
        spacing: 10,
        z_index: 1031,
        delay: 2000,
        mouse_over: null,
        template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
                    '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
                    '<span data-notify="icon"></span> ' +
                    '<span data-notify="title">{1}</span> ' +
                    '<span data-notify="message">{2}</span>' +
                    '<div class="progress" data-notify="progressbar">' +
                        '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
                    '</div>' +
                    '<a href="{3}" target="{4}" data-notify="url"></a>' +
                '</div>' 
    });
}

// UI utils

function removeClass(element, removeClass) {
    var newClassName = "";
    var i;
    var classes = element.className.split(" ");
    for (i = 0; i < classes.length; i++) {
        if (classes[i] !== removeClass) {
            newClassName += classes[i] + " ";
        }
    }
    if (i > 0) {
        newClassName = newClassName.substr(0, newClassName.length - 1);
    }
    element.className = newClassName;
}

function addClass(element, newClass) {
    element.className += " " + newClass;
}

function displayIfJsElements() {
    var elements = document.getElementsByClassName("display-if-js");
    [].forEach.call(elements, function (el) {
        el.style.display = 'block';
    });

    elements = document.getElementsByClassName("remove-if-js");
    [].forEach.call(elements, function (el) {
        el.style.display = 'none';
    });
}

// CSRF middleware

/**
 * @param {FormData} data
 * @param {XMLHttpRequest} request
 */
function getCSRFTokenThenSend(data, request) {
    var csrfRequest = new XMLHttpRequest();
    csrfRequest.open("GET", "/api/csrf");
    csrfRequest.onload = function () {
        if (csrfRequest.status === 200) {
            data.append("csrfmiddlewaretoken", csrfRequest.responseText);
            request.send(data);
        } else {
            console.error("CSRF request failed.")
        }
    };
    csrfRequest.send();
}

// Decideur form handling

function showDecideurForm() {
    decideurForm.style.display = "block";
}

/**
 * @param {XMLHttpRequest} request
 */
function processCallOutResult(request) {
    document.getElementById("decideur-container").style.display = "none";

    if (request.status === 200) {
        document.getElementById("decideur-success").style.display = "block";
    } else {
        document.getElementById("decideur-error").style.display = "block";
        console.error('Process call out result', request.status, request.responseText);
    }
}

/**
 * @param {string} content
 * @param {string} tagId
 * @param {string} data
 */
function addTag(content, tagId, data) {
    var x = document.createElement("span");
    x.innerText = "x";
    x.className = "close";
    x.onclick = function () {
        closeTag(tagId)
    };

    var newTag = document.createElement("span");
    newTag.id = tagId;
    newTag.innerText = content;
    newTag.className = "mail-to-tag depute-tag";
    newTag.setAttribute("data-circonscription", data);

    var parent = document.getElementById("decideur-recipients");
    parent.appendChild(newTag);
    newTag.appendChild(x);
}

function changeTags(deputes) {
    // Remove all existing tags
    var tags = document.getElementsByClassName("depute-tag");
    while (tags.length > 0) tags[0].parentNode.removeChild(tags[0]);

    // Add new tags
    for (var i = 0; i < deputes.length; i++) {
        var num_circo = deputes[i][4];
        var depute_name = deputes[i][0];
        addTag(depute_name + " (" + num_circo + ")", "recipient-" + num_circo, num_circo);
    }
}

function onPostalCodeInput(event) {
    var code = event.target.value;
    if (code.length === 5) {
        getDepute(code);
    }
}

/**
 * @param {string} postal_code
 */
function getDepute(postal_code) {
    var formData = new FormData();
    formData.append("postal_code", postal_code);

    var request = new XMLHttpRequest();
    request.open('POST', "/api/search-depute");
    request.onload = function () {
        if (request.status === 200) {
            changeTags(JSON.parse(request.responseText));
        } else {
            console.error("Error loading depute ", request.status, request.responseText)
        }
    };

    getCSRFTokenThenSend(formData, request);
}

function getRecipients() {
    var result = [];
    var tags = document.getElementsByClassName("depute-tag");
    for (var i = 0; i < tags.length; i++) {
        result.push(tags[i].getAttribute("data-circonscription"))
    }

    return result;
}

function sendMail() {
    var formData = new FormData(document.getElementById("decideur-form"));
    formData.append('send_to_government', isSendToGovernment ? '1' : '0');
    formData.append('circonscription_number', getRecipients()[0]);

    var request = new XMLHttpRequest();
    request.open("POST", "/api/call-out-ajax");
    request.onload = function () {
        processCallOutResult(request)
    };

    getCSRFTokenThenSend(formData, request);
}

// TODO we should be able to re-add a tag
function closeTag(tagId) {
    document.getElementById(tagId).style.display = 'none';
    if (tagId === 'government-tag') {
        isSendToGovernment = false;
    }
    if (tagId === 'depute-tag') {
        isSendToDepute = false;
    }

    var otherTag;
    // make sure at least one tag is selected
    if (!isSendToDepute && !isSendToGovernment) {
        if (tagId === 'government-tag') {
            otherTag = 'depute-tag';
            isSendToDepute = true;
        } else {
            otherTag = 'government-tag';
            isSendToGovernment = true;
        }
        document.getElementById(otherTag).style.display = 'initial';
    }
}

// Signature form handling

function sendSignature(ev) {
    ev.preventDefault();

    if (!isFormValid()) {
        return;
    }
    var formData = new FormData(ev.target);

    var request = new XMLHttpRequest();
    request.open("POST", "/api/sign-ajax");
    request.onload = function () {
        processSignResult(request)
    };

    getCSRFTokenThenSend(formData, request);
}

/**
 * @param {XMLHttpRequest} request
 */
function processSignResult(request) {
    document.getElementById("sign-form").style.display = "none";

    if (request.status === 200) {
        document.getElementById("signature-result").style.display = "initial";
    } else if (request.status === 400) {
        document.getElementById("signature-error").style.display = "initial";
        document.getElementById("signature-error-text").innerText = request.responseText;
    } else {
        console.error("Invalid signature form submission", request.status, request.responseText);
        document.getElementById("signature-error").style.display = "initial";
    }
}

function retrySignature() {
    document.getElementById("sign-form").style.display = "initial";
    document.getElementById("signature-error").style.display = "none";
}

function isFormValid() {
    return firstname.value && surname.value && email.value;
}

function onFormInput() {
    if (isFormValid()) {
        removeClass(submitBtn, "is-disabled");
    } else {
        addClass(submitBtn, "is-disabled");
    }
}

// Binding elements and functions

// TODO change these variables
var isSendToGovernment = true;
var isSendToDepute = true;

var firstname = document.getElementById("firstname");
var surname = document.getElementById("surname");
var email = document.getElementById("email");
var postalCode = document.getElementById("decideur-postal_code");
var submitBtn = document.getElementById("submit-btn");
var decideurForm = document.getElementById("decideur-form-container");

firstname.oninput = onFormInput;
surname.oninput = onFormInput;
email.oninput = onFormInput;
postalCode.oninput = onPostalCodeInput;

document.getElementById("sign-form").onsubmit = sendSignature;

displayIfJsElements();

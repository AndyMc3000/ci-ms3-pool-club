/* 
BDataTables.net Table sorting function
*/

$(document).ready(function() {
    $('#myTable').DataTable();
} );

/* 
Bootstrap validation
*/

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()

/*
 * EmailJS code for sending a user query from the contact form on index.html by email
 */
$(document).ready(function () {
    const btn = document.getElementById('contact-us-submit-btn');

    document.getElementById('contact-us-form')
        .addEventListener('submit', function (event) {
            event.preventDefault();

            btn.value = 'Sending...';
        
            if (event.target.checkValidity() === false) {
                event.target.classList.add('was-validated');
                return;
            }

            // This assigns form field id's to EmailJS email template parameters
            let templateParams = {
                from_name: document.getElementById('from_name').value,
                surname: document.getElementById('surname').value,
                tel_number: document.getElementById('tel_number').value,
                from_email: document.getElementById('from_email').value,
                message: document.getElementById('message').value,
            };

            emailjs.send('gmail', 'template_mee2ja9', templateParams)
                .then(function (response) {
                    // This code resets the form and stops the form from validating again on submit
                    // The jQuery code below used to achieve this was copied from Cina Saffary's GitHub issue thread relating to Bootstrap validation
                    var form = $('#contact-us-form')[0];
                    $(form).removeClass('was-validated');
                    form.reset();
                    console.log('SUCCESS!', response.status, response.text);
                    alert('Message Sent Successfully. Thank you for contacting us!');
                }, function (error) {
                    console.log('FAILED...', error);
                });
        });
});

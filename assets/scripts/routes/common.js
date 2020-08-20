// Common js
import appState from '../util/appState';

// Shared vars
let $window = $(window),
    $body = $('body'),
    $document = $(document);

export default {
  // JavaScript to be fired on all pages
  init() {

    function _displayVisitedModal() {
      let modal = '<div class="modal"><div><h2>Hello:</h2><p>You can only take the survey once. Please disregard this if you have not taken it yet. Thank you!</p></div><div><h2>Hola:</h2><p>Se puede contestar la encuesta una vez. Por favor ignore este mensaje si aún no la ha contestado. ¡Gracias!</p></div><button class="close button"><span class="sr-only">Close</span></button></div>';

      $body.addClass('modal-open');
      $body.append(modal);
      appState.modalOpen = true;
    }

    function _closeVisitedModal() {
      $('.modal').remove();
      $body.removeClass('modal-open');
      appState.modalOpen = false;
    }

    // Close the modal
    $document.on('click', '.close', _closeVisitedModal);
    $document.on('click', 'body.modal-open', function(e) {
      let $target = $(e.target);
      if (!$target.is('.modal') && !$target.parents('.modal').length) {
        _closeVisitedModal();
      }
    });


    // Check to see if the cookie is there
    if (document.cookie.split(';').some(function(item) {
        return item.trim().indexOf('pageVisited=') == 0
    })) {
      _displayVisitedModal();
    }

    // Set the page visited cookie
    document.cookie = "pageVisited=true";
  },
  finalize() {
    // JavaScript to be fired on all pages, after page specific JS is fired
  },
};

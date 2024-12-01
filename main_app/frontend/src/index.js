import 'select2/dist/css/select2.min.css';
import './style.css';

import $ from 'jquery';
import 'select2';

$(document).ready(function() {
    $('#id_authors').select2();
});
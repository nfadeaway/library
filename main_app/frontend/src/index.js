import 'select2/dist/css/select2.min.css';
import './style.scss';

import $ from 'jquery';
import 'select2';

$(document).ready(function() {
    $('#id_authors').select2();
});
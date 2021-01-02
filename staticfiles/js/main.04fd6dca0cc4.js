$(document).ready(function() {
    const COLORS = ['#FFFFFF', '#AEE5D7', '#FFD180', '#CFD8DC', '#FF8A80', '#CCFF90', '#FFFF8D', '#80D8FF'];
    COLORS.forEach((item, id) => {
        let element = `
            <li class="color_picker" 
            id="color-item-${id}"
            style="background-color: ${item}; "><input value="${COLORS[id]}" id="color-item-input-${id}" style="display: none" /></li>
        `;
        $('#color').append(element);
    });
    let global_color = {};
    let global_delete = {id: 0};
    let first_color = $('#color-item-input-0');
    $('#color-item-0').addClass('selected_color');
    global_color.elem = $('#color-item-0');
    first_color.attr('name', 'color');
    first_color.attr('id', 'color');

    $('.color_picker').click(function (e) {
        $(global_color.elem).removeClass('selected_color');
        $(e.currentTarget).addClass('selected_color');
        let prev_input = $(global_color.elem).children();
        prev_input.removeAttr('name');
        prev_input.removeAttr('id');
        let next_input = $(e.currentTarget).children();
        next_input.attr('name', 'color');
        next_input.attr('id', 'color');
        global_color.elem = e.currentTarget;
    });

    $(".delete-icon").click(function (e) {
        let default_url = $("#accept-delete").attr('href');
        let url = default_url.replace(global_delete.id, e.currentTarget.getAttribute('data'));
        global_delete.id = e.currentTarget.getAttribute('data');
        $("#accept-delete").attr('href', url);
    });
    $(".edit-icon").click(function (e) {
        let id = $(e.currentTarget).attr('data');
        let header = $(`#card-${id}`).find('.header-strong').text();
        let text = $(`#card-${id}`).find('.card-body-text').text();
        $('#title').val(header);
        $('#text').val(text);
        $('#create-edit-form').attr('action', `edit/${id}/`);
    });
});

// $("#accept-delete").click(function (e) {
//     $.ajax({
//         url: `card/delete/?delete_item=${e.currentTarget.getAttribute('data')}`,
//         dataType: 'json',
//         success: function (response) {
//             $('.main-cards-container').html(data);
//         }
//     });
// });

$(document).ready(function () {
    $('.btnEliminar').click(function () {
        var id = $(this).attr('data-id');
        $('#idModalEliminar').on('show.bs.modal', function(e) {
            alert('hll');
        }).modal('show');;
    });
});

$(document).ready(function(){
    $('.btnEliminarR').click(function(){
        var id = $(this).attr('data-id');
        if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {

            $.ajax({     
                headers: { "X-CSRFToken": token },   
                type: 'GET',
                url: "{% url 'eliminar' %}",
                data: {     
                    "csrfmiddlewaretoken": "{{ csrf_token }}",               
                    "id": id                    
                },       
           })
        }
    });
});